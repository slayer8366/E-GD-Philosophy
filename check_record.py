"""check_record.py -- validator for this repository's RECORD.md.

RECONSTRUCTED, not recovered, and the distinction matters enough to
spell out where the line falls.

A version of this file existed at commit 5d7af96 in this repository.
That commit no longer exists on any branch or remote reachable from
here -- see DURABILITY.md for how. The only surviving fragment is
ledger_validator_core.py in a separate project (OSCam, ~/imx on the
machine this was rebuilt on), which vendored nine functions from
check_record.py at 5d7af96 (plus their real dependencies:
MergeCommitEncountered, the ID_RE/FIELD_RE/ENTRY_SPLIT_RE regexes,
SENTINELS, and _first_divergent_line) for its own LEDGER.md format.
That vendoring recorded, at the time, that the nine functions' bodies
were byte-identical to these originals, confirmed by direct diff
against 5d7af96. That diff cannot be re-run -- 5d7af96 is gone -- so
this file's core logic below is copied from the vendored copy on
trust in that prior verification, not on a comparison performed now.
Say that plainly rather than calling this a recovery.

Two module-level constants could not be restored to their original
values and are flagged rather than guessed at. The vendoring header
in ledger_validator_core.py directly quotes two field labels as
originals -- "Prediction (outcome — planner)" and "Prediction
(mechanism — coder)" -- and those are used exactly below. It also
claims TERMINAL_REQUIRED "differs in content from the original" but
never quotes what that content was; and SUPPLIED_FIELD is a real
dependency of validate_entries that was never named in the vendoring
header's own dependency list at all (the same shape of omission that
header itself flags for _first_divergent_line, except that one was
caught and this one wasn't, here, now). TERMINAL_REQUIRED's non-
prediction field names and SUPPLIED_FIELD are therefore carried
forward UNCHANGED from the LEDGER.md-adapted values, not restored --
if this repository's real RECORD.md ever used different text for
either, this file is wrong until someone who remembers or can find
the original corrects it.

The functions below (split_entries, parse_fields, validate_entries,
check_superseded_by, check_duplicate_terminals, check_append_only,
check_history_append_only, _commit_log_for, _show_bytes) plus
MergeCommitEncountered, the three regexes, SENTINELS, and
_first_divergent_line are otherwise unmodified from the vendored
copy: only RECORD_NAME and the two quoted field labels differ from
what ledger_validator_core.py carries, and that difference is
configuration, not logic.

Extended 2026-10-16 (RECORD.md 2026-10-16-07), so the "unmodified"
above no longer holds for two functions: validate_entries and
check_duplicate_terminals now implement RECORDING.md's twelve entry
types with minimal required fields (OTHER_REQUIRED and the constants
beside it), terminal outcomes completed/partial/superseded/abandoned,
and backward links for Continues and Corrects. An outcome carrying
Closes counts as its intent's closing entry. render_check gains checks
19 to 38 for these rules. The other vendored functions are unchanged.

Extended again 2026-10-17 (RECORD.md 2026-10-17-01): ID_RE accepts two
or more digits after the date; validate_entries takes labelled blocks
from several files and checks an entry's Timestamp month against its
monthly file; record_files, validate_repo, append_only_checks,
history_checks and main_monthly read RECORD.md and records/YYYY-MM.md as
one record. render_check gains checks 39 to 46.

Extended again 2026-10-17 (RECORD.md 2026-10-17-05) so any repository
can use it: main(argv) checks the repository it is given (default: the
current directory, never this file's own folder), shaped by that
repository's records.json or the file --config names. DEFAULT_CONFIG,
built from the constants below, is RECORDING.md's format; validate_entries
and the functions around it read the config instead of the constants,
and with the default every earlier result is unchanged. --json prints one
JSON object; --print-config prints the default to copy and edit.
main_monthly is folded into main. render_check gains checks 47 to 55.
ADOPTING.md explains the config to someone adopting this.

main() and render_check() below are NEW CONSTRUCTION, modeled on
OSCam's ledger_cli.py (itself new construction there, since the
original main()/render_check() were never vendored) but not a copy of
anything that survives. Their argument surface, output format, and
check ordering are this file's own design, not a recovery of what
check_record.py's CLI used to look like.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RECORD_NAME = "RECORD.md"

# See module docstring: the two prediction field labels are restored
# from a direct quotation in the vendoring header. TERMINAL_REQUIRED's
# other field names are NOT restored -- carried forward unchanged from
# the LEDGER.md-adapted list, flagged as unconfirmed.
INTENT_REQUIRED = [
    "Kind", "ID", "Timestamp", "Title", "Change", "Scope boundary",
    "Baseline", "Prediction (outcome — planner)",
    "Prediction (mechanism — coder)", "Finish line", "Abort conditions",
]
TERMINAL_REQUIRED = [
    "Kind", "ID", "Timestamp", "Closes", "Outcome", "Observed", "Deviations",
]

ID_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{2,}$")
FIELD_RE = re.compile(r"^\*\*(.+?):\*\*\s?(.*)$")
ENTRY_SPLIT_RE = re.compile(r"(?m)^---$")

# Sentinels: permitted only as the exact, complete value of a prediction
# field in an INTENT entry. 'withheld' is a timing state -- the value
# exists but has not been released to the executor yet, and is expected
# to be appended later as its own field. 'not authored' is permanent --
# the value was never written and appending one later would mean it was
# fabricated after the outcome, which is the specific act the store
# exists to prevent. Never collapse the two into one "missing" state.
SENTINELS = {"withheld", "not authored"}
SENTINEL_PREDICTION_FIELDS = {
    "Prediction (outcome — planner)",
    "Prediction (mechanism — coder)",
}
OUTCOME_FIELD = "Prediction (outcome — planner)"
# Not restored -- see module docstring. Carried forward unchanged from
# the LEDGER.md-adapted value; no quoted original exists to replace it.
SUPPLIED_FIELD = "Prediction-outcome-supplied"

# RECORDING.md's entry types, added 2026-10-16 (RECORD.md 2026-10-16-07).
# Minimal required fields, by the operator's ruling: Kind, ID, Timestamp,
# the who-wrote-it Notes line, and each type's link field. Everything else
# a type carries is checked by reading, not here.
OTHER_REQUIRED = {
    "continuation": ["Kind", "ID", "Timestamp", "Notes", "Continues"],
    "decision": ["Kind", "ID", "Timestamp", "Notes"],
    "outcome": ["Kind", "ID", "Timestamp", "Notes"],
    "observation": ["Kind", "ID", "Timestamp", "Notes"],
    "finding": ["Kind", "ID", "Timestamp", "Notes", "Continues"],
    "device-note": ["Kind", "ID", "Timestamp", "Notes"],
    "correction": ["Kind", "ID", "Timestamp", "Notes", "Corrects"],
    "merge": ["Kind", "ID", "Timestamp", "Notes", "Merge-commit", "Backup"],
    "dispatch-note": ["Kind", "ID", "Timestamp", "Notes"],
    "handoff": ["Kind", "ID", "Timestamp", "Notes"],
}
# Types whose link takes one of two fields; one of the pair is required.
ONE_OF_REQUIRED = {
    "outcome": ("Continues", "Closes"),
    "dispatch-note": ("Dispatch-file", "Dispatch"),
}
# Only these close an intent; an outcome closes one only when it carries Closes.
CLOSING_KINDS = ("terminal", "outcome")
# A continuation opens and closes nothing (Claude-kit v0.2's rule).
CONT_FORBIDDEN = ["Closes", "Outcome", "Superseded-by", "Finish line",
                  "Prediction (outcome — planner)",
                  "Prediction (mechanism — coder)"]
# The terminal outcomes (completed, partial, superseded, abandoned) and the
# fields each requires or forbids are in DEFAULT_CONFIG["terminal_outcomes"].
DEFERRED_FIELD = "Deferred"
ENTRY_ID_TOKEN_RE = re.compile(r"\d{4}-\d{2}-\d{2}-\d+")

# Monthly record files, added 2026-10-17 (RECORD.md 2026-10-17-01):
# records/YYYY-MM.md, read with RECORD.md as one record (RECORDING.md,
# "Layout: one file per month"). _month_file_re builds the pattern from
# the configured folder.
MONTHLY_DIR = "records"

# Config, added 2026-10-17 (RECORD.md 2026-10-17-05): any repository's
# record, shaped by an optional records.json. DEFAULT_CONFIG is built from
# the constants above, so with no config the checker applies RECORDING.md's
# format exactly as before. The functions below read the config, not the
# constants; a top-level key in a config replaces the default's value whole.
def _default_kinds():
    kinds = {"intent": {"required": list(INTENT_REQUIRED)},
             "terminal": {"required": list(TERMINAL_REQUIRED)}}
    for k, required in OTHER_REQUIRED.items():
        kinds[k] = {"required": list(required)}
        if k in ONE_OF_REQUIRED:
            kinds[k]["one_of"] = [list(ONE_OF_REQUIRED[k])]
        if k == "continuation":
            kinds[k]["forbidden"] = list(CONT_FORBIDDEN)
    return kinds


DEFAULT_CONFIG = {
    "record_file": RECORD_NAME,
    "monthly_dir": MONTHLY_DIR,
    "id_pattern": ID_RE.pattern,
    "id_token_pattern": ENTRY_ID_TOKEN_RE.pattern,
    "kinds": _default_kinds(),
    "intent_kind": "intent",
    "terminal_kind": "terminal",
    "continuation_kind": "continuation",
    "closing_kinds": list(CLOSING_KINDS),
    "closes_field": "Closes",
    "continues_field": "Continues",
    "outcome_field": "Outcome",
    "terminal_outcomes": {
        "completed": {"forbidden": [DEFERRED_FIELD]},
        "partial": {"required": [DEFERRED_FIELD]},
        "superseded": {"required": ["Superseded-by"], "names_intent": ["Superseded-by"]},
        "abandoned": {"required": ["Working-state"]},
    },
    "sentinels": {
        "values": {"withheld": "pending", "not authored": "permanent"},
        "fields": sorted(SENTINEL_PREDICTION_FIELDS),
        "outcome_field": OUTCOME_FIELD,
        "supplied_field": SUPPLIED_FIELD,
    },
    "backward_links": {"Continues": "first", "Corrects": "all"},
    "prompts_dir": "prompts",
    "provenance_dirs": ["preserved", "recovered"],
    "dispatch_field": "Dispatch-file",
}
CONFIG_NAME = "records.json"


class ConfigError(Exception):
    """A config that cannot be used: unreadable, not JSON, an unknown key,
    a wrong type, or a regex that does not compile. The message names the
    key. main() reports it and exits 2; nothing is checked with a config
    that was refused."""


def _need(cond, key, msg):
    if not cond:
        raise ConfigError(f"{key}: {msg}")


def _names(v):
    return isinstance(v, list) and all(isinstance(x, str) and x for x in v)


def _check_spec(spec, key, allowed):
    _need(isinstance(spec, dict), key, "must be an object")
    unknown = sorted(set(spec) - set(allowed))
    _need(not unknown, key, f"unknown key(s) {unknown}; allowed: {', '.join(allowed)}")
    for sub in allowed:
        if sub == "one_of" and sub in spec:
            _need(isinstance(spec[sub], list)
                  and all(_names(g) and len(g) >= 2 for g in spec[sub]),
                  f"{key}.one_of", "must be a list of lists of two or more field names")
        elif sub in spec:
            _need(_names(spec[sub]), f"{key}.{sub}", "must be a list of field names")


def validate_config(cfg):
    """Raises ConfigError naming the first key that is wrong; returns cfg."""
    unknown = sorted(set(cfg) - set(DEFAULT_CONFIG))
    _need(not unknown, "config", f"unknown key(s) {unknown}; known keys: "
          f"{', '.join(DEFAULT_CONFIG)}")
    for key in ("record_file", "id_pattern", "id_token_pattern", "closes_field",
                "continues_field", "outcome_field", "prompts_dir", "dispatch_field"):
        _need(isinstance(cfg[key], str) and cfg[key], key, "must be a non-empty string")
    _need(cfg["monthly_dir"] is None or (isinstance(cfg["monthly_dir"], str)
                                         and cfg["monthly_dir"]),
          "monthly_dir", "must be a folder name, or null for no monthly files")
    for key in ("id_pattern", "id_token_pattern"):
        try:
            re.compile(cfg[key])
        except re.error as e:
            raise ConfigError(f"{key}: does not compile as a regular "
                              f"expression ({e})") from e
    kinds = cfg["kinds"]
    _need(isinstance(kinds, dict) and kinds, "kinds", "must be a non-empty object")
    for name, spec in kinds.items():
        _check_spec(spec, f"kinds.{name}", ("required", "one_of", "forbidden"))
    for key in ("intent_kind", "terminal_kind", "continuation_kind"):
        v = cfg[key]
        _need(v is None or (isinstance(v, str) and v in kinds), key,
              f"must be null or one of the kinds ({', '.join(kinds)}); got {v!r}")
    _need(_names(cfg["closing_kinds"]) and all(k in kinds for k in cfg["closing_kinds"]),
          "closing_kinds", f"must be a list of kinds ({', '.join(kinds)})")
    _need(not (cfg["closing_kinds"] or cfg["continuation_kind"]) or cfg["intent_kind"],
          "intent_kind", "is null, but closing_kinds or continuation_kind is set, "
          "and both refer to intents")
    links = cfg["backward_links"]
    _need(isinstance(links, dict) and all(isinstance(k, str) and k and v in ("first", "all")
                                          for k, v in links.items()),
          "backward_links", 'must map field names to "first" or "all"')
    _need(not cfg["continuation_kind"] or links.get(cfg["continues_field"]) == "first",
          "backward_links", f"must map continues_field ({cfg['continues_field']!r}) "
          f'to "first" while continuation_kind is set')
    outcomes = cfg["terminal_outcomes"]
    _need(outcomes is None or (isinstance(outcomes, dict) and outcomes),
          "terminal_outcomes", "must be a non-empty object, or null for outcomes not checked")
    for name, spec in (outcomes or {}).items():
        _check_spec(spec, f"terminal_outcomes.{name}", ("required", "forbidden", "names_intent"))
    sent = cfg["sentinels"]
    if sent is not None:
        keys = ("values", "fields", "outcome_field", "supplied_field")
        _need(isinstance(sent, dict) and set(sent) == set(keys), "sentinels",
              f"must be null or an object with exactly the keys {', '.join(keys)}")
        _need(isinstance(sent["values"], dict) and all(
            isinstance(k, str) and k and v in ("pending", "permanent")
            for k, v in sent["values"].items()),
              "sentinels.values", 'must map sentinel text to "pending" or "permanent"')
        _need(_names(sent["fields"]), "sentinels.fields", "must be a list of field names")
        for sub in ("outcome_field", "supplied_field"):
            _need(sent[sub] is None or (isinstance(sent[sub], str) and sent[sub]),
                  f"sentinels.{sub}", "must be a field name or null")
    _need(_names(cfg["provenance_dirs"]) and cfg["provenance_dirs"], "provenance_dirs",
          "must be a non-empty list of folder names")
    return cfg


def load_config(repo_dir, path=None):
    """(config, source). source is the config file read, or None for the
    default. path, when given, is used and must exist; otherwise the
    repository's records.json is read if present. A config's top-level
    keys replace the default's whole; everything is validated before use."""
    import copy
    import json
    if path is not None:
        cfg_path = Path(path)
        _need(cfg_path.is_file(), "--config", f"{path} does not exist")
    else:
        cfg_path = Path(repo_dir) / CONFIG_NAME
        if not cfg_path.is_file():
            return copy.deepcopy(DEFAULT_CONFIG), None
    try:
        user = json.loads(cfg_path.read_text())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        raise ConfigError(f"{cfg_path}: not readable as JSON ({e})") from e
    _need(isinstance(user, dict), str(cfg_path), "must hold one JSON object")
    merged = copy.deepcopy(DEFAULT_CONFIG)
    merged.update(user)
    return validate_config(merged), str(cfg_path)


def _month_file_re(cfg):
    """records/YYYY-MM.md under the configured monthly folder, or None."""
    if cfg["monthly_dir"] is None:
        return None
    return re.compile(rf"^{re.escape(cfg['monthly_dir'])}/(\d{{4}}-\d{{2}})\.md$")


def split_entries(text):
    """Raw text blocks for each entry, found after the '## Entries'
    heading and separated by bare '---' lines. Header/format
    documentation above that heading is never entry content."""
    marker = "## Entries"
    idx = text.find(marker)
    if idx == -1:
        return []
    body = text[idx + len(marker):]
    parts = ENTRY_SPLIT_RE.split(body)
    return [p.strip() for p in parts if p.strip()]


def parse_fields(block):
    """One entry block -> ordered dict of label -> value text. A field's
    value runs from immediately after its '**Label:**' line to the next
    such line or the block's end; this is why a value may span multiple
    lines without any indentation convention."""
    fields = {}
    label = None
    value_lines = []
    for line in block.splitlines():
        m = FIELD_RE.match(line)
        if m:
            if label is not None:
                fields[label] = "\n".join(value_lines).strip()
            label = m.group(1).strip()
            rest = m.group(2)
            value_lines = [rest] if rest.strip() else []
        elif label is not None:
            value_lines.append(line)
    if label is not None:
        fields[label] = "\n".join(value_lines).strip()
    return fields


def validate_entries(text, labelled_blocks=None, config=None):
    """Returns (entries, errors, unterminated_ids, sentinel_reports).
    errors is a list of human-readable violation strings. unterminated_ids
    and sentinel_reports are both reported, never on their own a cause of
    failure -- except one specific combination folded into errors: a
    permanent 'not authored' sentinel paired with a later-supplied value,
    which means a prediction was fabricated after the outcome.

    sentinel_reports is a list of {id, field, sentinel, status} dicts,
    status one of 'pending' or 'resolved'.

    labelled_blocks, when given, is a list of (source file, block) pairs
    read from several record files (validate_repo); text is then unused.
    An entry with a Timestamp in a monthly file must carry its month.

    config (2026-10-17-05) sets the entry types, ID pattern, closing and
    link rules, outcomes and sentinels; None means DEFAULT_CONFIG, which
    is RECORDING.md's format. The rules below are those of the 2026-10-16
    and 2026-10-17-01 extensions, read from the config."""
    cfg = DEFAULT_CONFIG if config is None else config
    kinds = cfg["kinds"]
    id_re = re.compile(cfg["id_pattern"])
    token_re = re.compile(cfg["id_token_pattern"])
    month_re = _month_file_re(cfg)
    intent_kind = cfg["intent_kind"]
    terminal_kind = cfg["terminal_kind"]
    cont_kind = cfg["continuation_kind"]
    closing_kinds = cfg["closing_kinds"]
    closes_f = cfg["closes_field"]
    continues_f = cfg["continues_field"]
    outcome_f = cfg["outcome_field"]
    outcomes = cfg["terminal_outcomes"]
    sent = cfg["sentinels"] or {}
    sentinel_values = sent.get("values", {})
    sentinel_fields = set(sent.get("fields", []))
    pred_outcome_f = sent.get("outcome_field")
    supplied_f = sent.get("supplied_field")

    errors = []
    entries = []
    seen_ids = {}
    sentinel_reports = []

    if labelled_blocks is None:
        labelled_blocks = [(None, b) for b in split_entries(text)]
    for i, (source, block) in enumerate(labelled_blocks):
        fields = parse_fields(block)
        kind = fields.get("Kind", "").strip()
        entry_id = fields.get("ID", "").strip()
        label_for_errors = entry_id or f"entry #{i + 1} (no ID)"

        if kind not in kinds:
            errors.append(f"{label_for_errors}: missing or invalid Kind "
                          f"(got {kind!r})")
            continue
        spec = kinds[kind]

        if not entry_id:
            errors.append(f"{kind} {label_for_errors}: missing required "
                          f"field 'ID'")
        elif not id_re.fullmatch(entry_id):
            errors.append(f"{kind} {entry_id}: malformed ID (does not match "
                          f"the ID pattern {id_re.pattern})")

        month_match = month_re.match(source or "") if month_re else None
        timestamp = fields.get("Timestamp", "").strip()
        if month_match and timestamp and timestamp[:7] != month_match.group(1):
            errors.append(f"{kind} {label_for_errors}: Timestamp month "
                          f"{timestamp[:7]} but filed in {source}")

        for req_label in spec.get("required", []):
            value = fields.get(req_label, "").strip()
            if not value:
                errors.append(f"{kind} {label_for_errors}: missing required "
                              f"field {req_label!r}")
            elif (kind == intent_kind and req_label in sentinel_fields
                  and value in sentinel_values):
                sentinel_reports.append({
                    "id": entry_id, "field": req_label, "sentinel": value,
                    "status": "pending",
                })

        if kind == terminal_kind:
            for field_name, field_value in fields.items():
                if field_value.strip() in sentinel_values:
                    errors.append(
                        f"{kind} {label_for_errors}: field {field_name!r} "
                        f"carries sentinel {field_value.strip()!r} -- "
                        f"sentinels are not permitted in terminal entries, "
                        f"since nothing there can legitimately be "
                        f"outstanding or absent")
            outcome = fields.get(outcome_f, "").strip()
            if outcome and outcomes is not None:
                if outcome not in outcomes:
                    errors.append(f"{kind} {label_for_errors}: outcome "
                                  f"{outcome!r} is not one of "
                                  f"{sorted(outcomes)}")
                else:
                    for f in outcomes[outcome].get("required", []):
                        if not fields.get(f, "").strip():
                            errors.append(f"{kind} {label_for_errors}: outcome "
                                          f"{outcome!r} requires field {f!r}")
                    for f in outcomes[outcome].get("forbidden", []):
                        if f in fields:
                            errors.append(f"{kind} {label_for_errors}: outcome "
                                          f"{outcome!r} may not carry field {f!r}")

        for group in spec.get("one_of", []):
            if not any(fields.get(f, "").strip() for f in group):
                errors.append(f"{kind} {label_for_errors}: needs "
                              + " or ".join(f"field {f!r}" for f in group))

        if kind not in closing_kinds and closes_f in fields:
            closers = (" or ".join(closing_kinds) + " entries"
                       if closing_kinds else "no entry type")
            errors.append(f"{kind} {label_for_errors}: carries field "
                          f"{closes_f!r}, but only {closers} close an intent")

        for label in spec.get("forbidden", []):
            if label in fields:
                errors.append(f"{kind} {label_for_errors}: carries field "
                              f"{label!r}, which a {kind} entry may not carry")

        if entry_id:
            if entry_id in seen_ids:
                errors.append(f"duplicate ID {entry_id}: used by entry "
                              f"#{seen_ids[entry_id] + 1} and entry #{i + 1}")
            else:
                seen_ids[entry_id] = i

        entries.append({"kind": kind, "id": entry_id, "fields": fields})

    intent_ids = {e["id"] for e in entries
                  if intent_kind and e["kind"] == intent_kind and e["id"]}
    closed_ids = set()
    for e in entries:
        if e["kind"] not in closing_kinds:
            continue
        closes = e["fields"].get(closes_f, "").strip()
        if not closes:
            continue
        if closes not in intent_ids:
            errors.append(f"{e['kind']} {e['id']}: {closes_f} names no existing "
                          f"intent ID ({closes_f.lower()}={closes!r})")
        else:
            closed_ids.add(closes)

    # Backward links point at entries that exist earlier in the record. A
    # "first" link names one entry by the ID token its value starts with,
    # since Forager's practice sometimes follows it with a parenthesis; an
    # "all" link names every ID token in its value. A continuation's link
    # names an intent still open at that point (Claude-kit v0.2's rule).
    first_pos = {}
    for pos, e in enumerate(entries):
        if e["id"] and e["id"] not in first_pos:
            first_pos[e["id"]] = pos
    for pos, e in enumerate(entries):
        label = e["id"] or "(no ID)"
        for field, mode in cfg["backward_links"].items():
            target_text = e["fields"].get(field, "").strip()
            if not target_text:
                continue
            if mode == "first":
                m = token_re.match(target_text)
                target = m.group(0) if m else target_text
                tpos = first_pos.get(target)
                if tpos is None or tpos >= pos:
                    errors.append(f"{e['kind']} {label}: {field} {target!r} "
                                  f"names no earlier entry")
                elif e["kind"] == cont_kind and field == continues_f:
                    if entries[tpos]["kind"] != intent_kind:
                        errors.append(f"{e['kind']} {label}: {field} "
                                      f"{target!r} names a "
                                      f"{entries[tpos]['kind']}, not an intent")
                    else:
                        closers = [c["id"] for c in entries[:pos]
                                   if c["kind"] in closing_kinds
                                   and c["fields"].get(closes_f, "").strip() == target]
                        if closers:
                            errors.append(f"{e['kind']} {label}: {field} "
                                          f"{target!r}, an intent already closed "
                                          f"by {', '.join(closers)}")
            else:
                cids = token_re.findall(target_text)
                if not cids:
                    errors.append(f"{e['kind']} {label}: {field} names no "
                                  f"entry ID")
                for cid in cids:
                    cpos = first_pos.get(cid)
                    if cpos is None or cpos >= pos:
                        errors.append(f"{e['kind']} {label}: {field} {cid!r}, "
                                      f"which names no earlier entry")

    # A later-supplied outcome prediction cannot be written into the
    # sentinel's own intent entry -- that entry is already committed, and
    # append-only is enforced by byte-prefix, so nothing can be inserted
    # into an already-committed block; only new blocks may be appended.
    # The supplied field therefore lives in the TERMINAL entry that closes
    # the intent, cross-referenced via Closes, the same way Closes itself
    # already links a terminal entry back to an intent one.
    intents_by_id = {e["id"]: e for e in entries
                     if intent_kind and e["kind"] == intent_kind and e["id"]}
    for e in entries:
        if not (terminal_kind and supplied_f and pred_outcome_f):
            break
        if e["kind"] != terminal_kind:
            continue
        supplied_value = e["fields"].get(supplied_f, "").strip()
        if not supplied_value:
            continue
        closes = e["fields"].get(closes_f, "").strip()
        intent = intents_by_id.get(closes)
        if intent is None:
            continue  # already reported above as a bad Closes reference
        outcome_value = intent["fields"].get(pred_outcome_f, "").strip()
        state = sentinel_values.get(outcome_value)
        if state is None:
            continue  # nothing to resolve; not validated further, see report
        if state == "permanent":
            errors.append(
                f"{e['kind']} {e['id']}: closes intent {closes} whose "
                f"{pred_outcome_f!r} is {outcome_value!r} (permanent), but "
                f"carries a {supplied_f!r} field -- a permanent "
                f"sentinel is never resolved; that combination means the "
                f"prediction was fabricated after the outcome")
        else:  # a pending sentinel, legitimately resolved
            for report in sentinel_reports:
                if report["id"] == closes and report["field"] == pred_outcome_f:
                    report["status"] = "resolved"

    unterminated = sorted(intent_ids - closed_ids)
    return entries, errors, unterminated, sentinel_reports


def record_files(repo_dir, config=None):
    """Relative names of the record's files: the record file if present,
    then the monthly folder's YYYY-MM.md files in month order. Their
    entries form one record."""
    cfg = DEFAULT_CONFIG if config is None else config
    repo_dir = Path(repo_dir)
    record = cfg["record_file"]
    files = [record] if (repo_dir / record).is_file() else []
    month_re = _month_file_re(cfg)
    mdir = repo_dir / cfg["monthly_dir"] if month_re else None
    if mdir is not None and mdir.is_dir():
        files += sorted(f"{cfg['monthly_dir']}/{p.name}" for p in mdir.iterdir()
                        if month_re.match(f"{cfg['monthly_dir']}/{p.name}"))
    return files


def monthly_mode(repo_dir, config=None):
    cfg = DEFAULT_CONFIG if config is None else config
    month_re = _month_file_re(cfg)
    return bool(month_re) and any(month_re.match(f) for f in record_files(repo_dir, cfg))


def _is_index(repo_dir, rel, config=None):
    """The record file is the index when monthly files exist and it holds
    no entries of its own."""
    cfg = DEFAULT_CONFIG if config is None else config
    return (rel == cfg["record_file"] and monthly_mode(repo_dir, cfg)
            and not split_entries((Path(repo_dir) / rel).read_text()))


def _index_note(cfg):
    return (f"the index (no entries; they are in {cfg['monthly_dir']}/): "
            f"append-only checks not applied, since its rewrite into the index "
            f"at a split is the recorded one-time exception (RECORDING.md)")


INDEX_NOTE = _index_note(DEFAULT_CONFIG)


def validate_repo(repo_dir, config=None):
    """validate_entries over every record file, in order, as one record."""
    labelled = []
    for rel in record_files(repo_dir, config):
        text = (Path(repo_dir) / rel).read_text()
        labelled += [(rel, b) for b in split_entries(text)]
    return validate_entries("", labelled, config)


def append_only_checks(repo_dir, config=None):
    """The working-tree append-only check on each record file. Returns a
    list of {file, ok, msg, vacuous}; the index is reported, not checked."""
    cfg = DEFAULT_CONFIG if config is None else config
    results = []
    for rel in record_files(repo_dir, cfg):
        if _is_index(repo_dir, rel, cfg):
            results.append({"file": rel, "ok": True, "msg": _index_note(cfg),
                            "vacuous": True})
            continue
        ok, msg, vacuous = check_append_only(repo_dir, record_name=rel)
        results.append({"file": rel, "ok": ok, "msg": msg, "vacuous": vacuous})
    return results


def _has_commits(repo_dir):
    return subprocess.run(
        ["git", "-C", str(repo_dir), "rev-parse", "--verify", "-q", "HEAD"],
        capture_output=True).returncode == 0


def history_checks(repo_dir, config=None):
    """The history walk on each record file. Returns a list of {file, ok,
    msg, count, vacuous, violations}; the index is reported, not walked,
    and a repository with no commits yet has nothing to walk."""
    cfg = DEFAULT_CONFIG if config is None else config
    results = []
    has_commits = _has_commits(repo_dir)
    for rel in record_files(repo_dir, cfg):
        if _is_index(repo_dir, rel, cfg):
            results.append({"file": rel, "ok": True, "msg": _index_note(cfg),
                            "count": 0, "vacuous": True, "violations": []})
            continue
        if not has_commits:
            results.append({"file": rel, "ok": True,
                            "msg": "no commits yet; nothing to walk",
                            "count": 0, "vacuous": True, "violations": []})
            continue
        try:
            ok, violations, count, vacuous = check_history_append_only(
                repo_dir, record_name=rel)
            msg = (f"{count} commit(s) checked, each a byte-prefix extension "
                   f"of the one before it" if ok
                   else f"{len(violations)} violation(s)")
        except MergeCommitEncountered as e:
            ok, violations, count, vacuous, msg = False, [], 0, False, str(e)
        results.append({"file": rel, "ok": ok, "msg": msg, "count": count,
                        "vacuous": vacuous, "violations": violations})
    return results


def check_superseded_by(entries, config=None):
    """(ok, errors, vacuous). Cross-references every terminal entry's
    Superseded-by value (present when Outcome is 'superseded') against
    the set of existing intent entry IDs. Vacuous when no terminal entry
    in the store declares Outcome: superseded at all -- there is
    nothing to cross-reference, not a check that ran and found nothing
    wrong. Since 2026-10-17-05 the fields cross-referenced are each
    configured outcome's names_intent fields; by default, superseded's
    Superseded-by, as before."""
    cfg = DEFAULT_CONFIG if config is None else config
    intent_kind, terminal_kind = cfg["intent_kind"], cfg["terminal_kind"]
    outcomes = cfg["terminal_outcomes"] or {}
    intent_ids = {e["id"] for e in entries
                  if intent_kind and e["kind"] == intent_kind and e["id"]}
    declared = []
    for e in entries:
        if not terminal_kind or e["kind"] != terminal_kind:
            continue
        outcome = e["fields"].get(cfg["outcome_field"], "").strip()
        declared += [(e, f) for f in outcomes.get(outcome, {}).get("names_intent", [])]
    if not declared:
        return True, [], True

    errs = []
    for e, field in declared:
        sup = e["fields"].get(field, "").strip()
        if sup and sup not in intent_ids:
            errs.append(f"{e['kind']} {e['id']}: {field} names no "
                       f"existing intent ID ({field.lower()}={sup!r})")
    return not errs, errs, False


def check_duplicate_terminals(entries, config=None):
    """(ok, errors). More than one terminal entry closing the same
    intent ID is an error, not a report -- unlike unterminated (a
    normal in-progress state), multiply-terminated is not a state any
    correct process produces. Names every colliding entry ID, not just
    the second one, so an operator seeing a duplicate knows whether
    there are two or five."""
    cfg = DEFAULT_CONFIG if config is None else config
    by_closes = {}
    for e in entries:
        if e["kind"] not in cfg["closing_kinds"]:
            continue
        closes = e["fields"].get(cfg["closes_field"], "").strip()
        if not closes:
            continue
        by_closes.setdefault(closes, []).append((e["id"], e["kind"]))

    errs = []
    for closes, closers in sorted(by_closes.items()):
        if len(closers) > 1:
            ids = [i for i, _ in closers]
            noun = ("terminal entries"
                    if all(k == cfg["terminal_kind"] for _, k in closers)
                    else f"closing entries ({' or '.join(cfg['closing_kinds'])})")
            errs.append(f"intent {closes} is closed by {len(closers)} {noun}, "
                       f"not one: {', '.join(ids)}")
    return not errs, errs


def check_append_only(repo_dir, record_name=RECORD_NAME):
    """(ok, message, vacuous). Compares the current on-disk file against
    what is committed at HEAD; the current file must start with HEAD's
    content unchanged, with only additions permitted after it. vacuous is
    True only for the one case where no comparison was actually possible
    (the file is not present at HEAD yet, so there is nothing to
    violate) -- a real pass, with real prior content to compare against,
    is not vacuous even though it also has nothing to report."""
    repo_dir = Path(repo_dir)
    current_path = repo_dir / record_name
    if not current_path.is_file():
        return False, f"{record_name} does not exist in the working tree", False

    probe = subprocess.run(
        ["git", "-C", str(repo_dir), "cat-file", "-e", f"HEAD:{record_name}"],
        capture_output=True)
    if probe.returncode != 0:
        return (True, f"{record_name} not present at HEAD yet; nothing to "
               f"violate", True)

    head = subprocess.run(
        ["git", "-C", str(repo_dir), "show", f"HEAD:{record_name}"],
        capture_output=True, text=True, check=True)
    head_lines = head.stdout.splitlines()
    current_lines = current_path.read_text().splitlines()

    if len(current_lines) < len(head_lines):
        idx = len(current_lines)
        return (False, f"line {idx + 1} removed: {head_lines[idx]!r} is no "
               f"longer present in the working tree", False)

    for idx, head_line in enumerate(head_lines):
        if current_lines[idx] != head_line:
            return (False, f"line {idx + 1} changed: HEAD had "
                   f"{head_line!r}, working tree now has "
                   f"{current_lines[idx]!r}", False)

    return True, "current file starts with HEAD's content unchanged", False


class MergeCommitEncountered(Exception):
    """Raised by check_history_append_only when a commit touching
    RECORD.md has more than one parent. The walk stops rather than
    guessing which parent to diff against -- a merge commit changes
    that, and reconciling it is an operator decision, not an inference
    this module makes on its own."""


def _commit_log_for(repo_dir, record_name=RECORD_NAME):
    """Ordered list of {hash, subject, parents} for every commit that has
    touched record_name, oldest first. parents is a list of parent
    hashes; more than one means a merge commit."""
    repo_dir = Path(repo_dir)
    result = subprocess.run(
        ["git", "-C", str(repo_dir), "log", "--reverse",
         "--format=%H%x00%s%x00%P", "--", record_name],
        capture_output=True, text=True, check=True)
    commits = []
    for line in result.stdout.splitlines():
        if not line:
            continue
        h, subject, parents = line.split("\x00")
        commits.append({
            "hash": h, "subject": subject,
            "parents": parents.split() if parents else [],
        })
    return commits


def _show_bytes(repo_dir, commit_hash, record_name=RECORD_NAME):
    result = subprocess.run(
        ["git", "-C", str(repo_dir), "show", f"{commit_hash}:{record_name}"],
        capture_output=True, check=True)
    return result.stdout


def _first_divergent_line(older_bytes, newer_bytes):
    older_lines = older_bytes.decode("utf-8", errors="replace").splitlines()
    newer_lines = newer_bytes.decode("utf-8", errors="replace").splitlines()
    for idx, ol in enumerate(older_lines):
        if idx >= len(newer_lines) or newer_lines[idx] != ol:
            return idx + 1
    return len(older_lines) + 1


def check_history_append_only(repo_dir, record_name=RECORD_NAME):
    """(ok, violations, commit_count, vacuous). Walks every commit that
    touched record_name, oldest first, and asserts each version's full
    text (compared as raw bytes, not a line-diff heuristic) is a
    byte-prefix of the next. Reports every violating pair found, not
    just the first. vacuous is True when fewer than two commits exist to
    compare (zero or one), so zero prefix comparisons were actually
    performed. Raises MergeCommitEncountered, rather than returning a
    result, if any commit in the walk has more than one parent."""
    commits = _commit_log_for(repo_dir, record_name)

    merge = next((c for c in commits if len(c["parents"]) > 1), None)
    if merge is not None:
        raise MergeCommitEncountered(
            f"commit {merge['hash']} ({merge['subject']!r}) touching "
            f"{record_name} has {len(merge['parents'])} parents; merge "
            f"commits are out of scope for this walk")

    violations = []
    for i in range(1, len(commits)):
        older, newer = commits[i - 1], commits[i]
        older_bytes = _show_bytes(repo_dir, older["hash"], record_name)
        newer_bytes = _show_bytes(repo_dir, newer["hash"], record_name)
        if not newer_bytes.startswith(older_bytes):
            violations.append({
                "older": older["hash"], "older_subject": older["subject"],
                "newer": newer["hash"], "newer_subject": newer["subject"],
                "divergence_line": _first_divergent_line(older_bytes, newer_bytes),
            })

    return not violations, violations, len(commits), len(commits) <= 1


# --------------------------------------------------------------------------
# CLI wrapper. New construction -- see module docstring. Modeled on
# OSCam's ledger_cli.py (also new construction there), not a recovery of
# check_record.py's original main()/render_check(). Since 2026-10-17-05 it
# checks the repository it is given (default: the current directory), with
# that repository's records.json or the file --config names.
# --------------------------------------------------------------------------


def _git_top_error(repo):
    """None when repo is the top folder of a git work tree, else why not.
    The append-only checks read HEAD:<path>, which git resolves from the
    top folder, so a subfolder would silently compare the wrong file."""
    top = subprocess.run(["git", "-C", str(repo), "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True)
    if top.returncode != 0:
        return (f"{repo} is not inside a git repository; the append-only "
                f"checks read the record's committed history")
    top_path = Path(top.stdout.strip()).resolve()
    if top_path != repo:
        return (f"{repo} is inside the git repository {top_path}; give that "
                f"top folder, with record_file and monthly_dir set to paths "
                f"inside it")
    return None


def _parse_args(argv):
    import argparse
    parser = argparse.ArgumentParser(
        prog="check_record.py",
        description="Check a repository's append-only record against its "
                    "records.json (or RECORDING.md's format when it has none). "
                    "Exit 0 pass, 1 fail, 2 unusable config or repository.")
    parser.add_argument("repo", nargs="?", default=".",
                        help="the repository's top folder (default: the current directory)")
    parser.add_argument("--config", help="a config file to use instead of the "
                        "repository's records.json")
    parser.add_argument("--json", action="store_true",
                        help="print the results as one JSON object")
    parser.add_argument("--print-config", action="store_true",
                        help="print the default config, to copy into records.json and edit")
    parser.add_argument("--render-check", action="store_true",
                        help="run this file's own self-checks")
    return parser.parse_args(argv)


def main(argv=None):
    import json
    args = _parse_args(sys.argv[1:] if argv is None else argv)
    if args.render_check:
        return render_check()
    if args.print_config:
        print(json.dumps(DEFAULT_CONFIG, indent=2, ensure_ascii=False))
        return 0

    repo = Path(args.repo).resolve()
    result = {"ok": False, "exit": 2, "repo": str(repo), "config": None,
              "record_files": [], "entries": 0, "errors": [], "unterminated": [],
              "sentinels": [], "checks": [], "vacuous": False}

    def finish(code, lines):
        result["exit"], result["ok"] = code, code == 0
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print("\n".join(lines))
        return code

    try:
        if not repo.is_dir():
            raise ConfigError(f"repo: {repo} is not a folder")
        cfg, source = load_config(repo, args.config)
    except ConfigError as e:
        result["errors"] = [f"config error: {e}"]
        return finish(2, [f"config error: {e}", "Nothing was checked."])
    result["config"] = source
    git_error = _git_top_error(repo)
    if git_error:
        result["errors"] = [git_error]
        return finish(2, [git_error, "Nothing was checked."])

    lines = [f"repository: {repo}",
             f"config: {source or 'default (RECORDING.md format; no ' + CONFIG_NAME + ')'}"]
    files = record_files(repo, cfg)
    result["record_files"] = files
    if not files:
        result["vacuous"] = True
        msg = (f"{cfg['record_file']} does not exist yet in {repo}, and no "
               f"monthly files -- nothing to validate. This is not a failure: "
               f"the record store has no content until a first entry is "
               f"committed. If a record does exist, record_file or monthly_dir "
               f"in the config does not point at it.")
        result["note"] = msg
        return finish(0, lines + [msg])

    entries, errors, unterminated, sentinel_reports = validate_repo(repo, cfg)
    result.update(entries=len(entries), unterminated=unterminated,
                  sentinels=sentinel_reports)
    lines += [f"record files: {', '.join(files)}", f"entries: {len(entries)}"]
    if not entries:
        result["vacuous"] = True
        result["note"] = (f"no entries were read from {', '.join(files)}: the "
                          f"entry rules checked nothing. Entries follow a line "
                          f"containing '## Entries', separated by '---' lines.")
        lines.append(f"NOTE: {result['note']}")
    if unterminated:
        lines.append(f"unterminated intent entries (reported, not a failure): "
                     f"{', '.join(unterminated)}")
    if sentinel_reports:
        lines.append("intent entries with prediction sentinels (reported, not "
                     "a failure):")
        lines += [f"  {r['id']}: {r['field']} = {r['sentinel']!r} ({r['status']})"
                  for r in sentinel_reports]
    lines.append("")

    def add_check(name, label, r):
        result["checks"].append({"check": name, "file": r.get("file"), "ok": r["ok"],
                                 "vacuous": r["vacuous"], "message": r["msg"]})
        vac = " (vacuous)" if r["vacuous"] and r["ok"] else ""
        lines.append(f"[{label}] {'PASS' if r['ok'] else 'FAIL'}: {r['msg']}{vac}")

    for r in append_only_checks(repo, cfg):
        add_check("working-tree", f"working-tree check: {r['file']} -- changes "
                  f"since the last commit", r)
        if not r["ok"]:
            errors.append(f"working-tree append-only, {r['file']}: {r['msg']}")
    for r in history_checks(repo, cfg):
        add_check("history walk", f"history walk: {r['file']} -- every "
                  f"committed version", r)
        for v in r["violations"]:
            msg = (f"{v['older'][:10]} ({v['older_subject']!r}) -> "
                   f"{v['newer'][:10]} ({v['newer_subject']!r}): diverges at "
                   f"line {v['divergence_line']}")
            lines.append("    " + msg)
            errors.append(f"history walk, {r['file']}: {msg}")
        if not r["ok"] and not r["violations"]:
            errors.append(f"history walk, {r['file']}: {r['msg']}")

    sup_ok, sup_errors, sup_vacuous = check_superseded_by(entries, cfg)
    linked = sorted({f for o in (cfg["terminal_outcomes"] or {}).values()
                     for f in o.get("names_intent", [])})
    add_check("names-intent", f"{', '.join(linked) or 'outcome'} cross-reference "
              f"-- terminals whose outcome must name an intent",
              {"ok": sup_ok, "vacuous": sup_vacuous,
               "msg": ("no entry declares such an outcome" if sup_vacuous
                       else f"{len(sup_errors)} error(s)")})
    lines += ["    " + e for e in sup_errors]
    errors += [f"{', '.join(linked)}: {e}" for e in sup_errors]

    dup_ok, dup_errors = check_duplicate_terminals(entries, cfg)
    add_check("closed-once", "closed-once check -- no intent closed by more "
              "than one closing entry",
              {"ok": dup_ok, "vacuous": not cfg["closing_kinds"],
               "msg": f"{len(dup_errors)} intent(s) closed more than once"})
    lines += ["    " + e for e in dup_errors]
    errors += [f"duplicate terminal: {e}" for e in dup_errors]

    result["errors"] = errors
    if errors:
        return finish(1, lines + ["", "FAIL"] + ["  " + e for e in errors])
    return finish(0, lines + ["", f"PASS: entries structurally valid across "
                              f"{len(files)} record file(s); working-tree check, "
                              f"history walk, and cross-references all clean"])


# --------------------------------------------------------------------------
# Self-tests. Every fixture lives under tempfile.mkdtemp(). New suite --
# OSCam's six self-tests were written against LEDGER.md's renamed fields;
# this suite is written directly against this file's own RECORD.md field
# set and covers more categories, per this task's own scope.
# --------------------------------------------------------------------------

def _render_entry(fields):
    return "\n".join(f"**{label}:** {value}" for label, value in fields.items()
                     if value is not None)


def _minimal_intent(id_="2026-01-01-01", **overrides):
    fields = {
        "Kind": "intent", "ID": id_, "Timestamp": "2026-01-01T00:00:00Z",
        "Title": "t", "Change": "c", "Scope boundary": "s", "Baseline": "b",
        "Prediction (outcome — planner)": "po",
        "Prediction (mechanism — coder)": "pm",
        "Finish line": "f", "Abort conditions": "a",
    }
    fields.update(overrides)
    return _render_entry(fields)


def _minimal_terminal(id_="2026-01-01-02", closes="2026-01-01-01",
                      outcome="completed", **overrides):
    fields = {
        "Kind": "terminal", "ID": id_, "Timestamp": "2026-01-01T00:01:00Z",
        "Closes": closes, "Outcome": outcome, "Observed": "o", "Deviations": "d",
    }
    fields.update(overrides)
    return _render_entry(fields)


def _minimal_record(*entries):
    parts = ["# RECORD.md", "", "## Entries", "", "---", ""]
    for e in entries:
        parts.append(e)
        parts.append("")
        parts.append("---")
        parts.append("")
    return "\n".join(parts)


def _init_repo(tmp_dir):
    subprocess.run(["git", "-C", str(tmp_dir), "init", "-q"], check=True)


def _commit_record(tmp_dir, content, msg="record"):
    (Path(tmp_dir) / RECORD_NAME).write_text(content)
    subprocess.run(["git", "-C", str(tmp_dir), "add", RECORD_NAME], check=True)
    subprocess.run(["git", "-C", str(tmp_dir), "-c", "user.name=check_record_test",
                    "-c", "user.email=check_record_test@example.invalid",
                    "commit", "-q", "-m", msg], check=True)


def render_check():
    print("check_record.py --render-check")
    failures = []

    def check(name, expect_fail_msg, fn):
        print(f"\n[{name}] expected failure mode if broken: {expect_fail_msg}")
        try:
            fn()
            print(f"[{name}] PASS")
        except Exception as e:
            print(f"[{name}] FAIL: {e!r}")
            failures.append(name)

    # ---- Check 1: well-formed record passes (positive case) ---------------
    def check1():
        text = _minimal_record(_minimal_intent(), _minimal_terminal())
        entries, errors, unterminated, _ = validate_entries(text)
        assert not errors, f"well-formed record produced errors: {errors}"
        assert not unterminated
        assert len(entries) == 2

    check("check1_well_formed_record_passes",
          "N/A -- positive case, validated by the negative checks below "
          "catching sabotages of the same fixture",
          check1)

    # ---- Check 2: field presence -- missing required field is caught ------
    def check2():
        text = _minimal_record(_minimal_intent(Change=None))
        _, errors, _, _ = validate_entries(text)
        assert any("2026-01-01-01" in e and "'Change'" in e for e in errors), (
            f"missing 'Change' field not reported by ID and field name: {errors}")

    check("check2_missing_field_names_fault",
          "an entry missing a required field is accepted, or the error "
          "does not name both the entry and the missing field",
          check2)

    # ---- Check 3: field presence -- missing restored prediction label -----
    def check3():
        text = _minimal_record(_minimal_intent(**{"Prediction (outcome — planner)": None}))
        _, errors, _, _ = validate_entries(text)
        assert any("Prediction (outcome — planner)" in e for e in errors), (
            f"missing restored outcome-prediction field not reported: {errors}")

    check("check3_missing_restored_prediction_field_caught",
          "an intent entry missing the restored 'Prediction (outcome — "
          "planner)' field is accepted, or the error does not name it",
          check3)

    # ---- Check 4: Closes resolution ----------------------------------------
    def check4():
        text = _minimal_record(_minimal_intent(),
                                _minimal_terminal(closes="2026-01-01-99"))
        _, errors, _, _ = validate_entries(text)
        assert any("2026-01-01-99" in e and "Closes" in e for e in errors), (
            f"terminal closing a nonexistent intent ID not reported: {errors}")

    check("check4_closes_resolution_catches_dangling_reference",
          "a terminal entry's Closes field naming a nonexistent intent ID "
          "is accepted silently",
          check4)

    # ---- Check 5: duplicate IDs --------------------------------------------
    def check5():
        text = _minimal_record(_minimal_intent(id_="2026-01-01-01"),
                                _minimal_intent(id_="2026-01-01-01", Title="second"))
        _, errors, _, _ = validate_entries(text)
        assert any("duplicate ID 2026-01-01-01" in e for e in errors), (
            f"duplicate entry ID not reported: {errors}")

    check("check5_duplicate_id_caught",
          "two entries sharing the same ID are accepted, or the error "
          "does not name the colliding ID",
          check5)

    # ---- Check 6: duplicate terminals --------------------------------------
    def check6():
        text = _minimal_record(
            _minimal_intent(),
            _minimal_terminal(id_="2026-01-01-02"),
            _minimal_terminal(id_="2026-01-01-03"),
        )
        entries, _, _, _ = validate_entries(text)
        ok, errs = check_duplicate_terminals(entries)
        assert not ok, "duplicate terminal closing the same intent not reported"
        assert any("closed by 2 terminal entries" in e and
                   "2026-01-01-02" in e and "2026-01-01-03" in e
                   for e in errs), (
            f"duplicate-terminal error did not name both closing entries: {errs}")

    check("check6_duplicate_terminal_names_both_closers",
          "one intent closed by two terminal entries is accepted, or the "
          "error does not name both closing entries",
          check6)

    # ---- Check 7: sentinel 'withheld' reported pending, not an error ------
    def check7():
        text = _minimal_record(
            _minimal_intent(**{"Prediction (outcome — planner)": "withheld"}))
        _, errors, _, sentinel_reports = validate_entries(text)
        assert not errors, f"a pending 'withheld' sentinel was treated as an error: {errors}"
        assert any(r["sentinel"] == "withheld" and r["status"] == "pending"
                   for r in sentinel_reports), (
            f"'withheld' sentinel not reported pending: {sentinel_reports}")

    check("check7_withheld_sentinel_reported_pending",
          "a 'withheld' outcome-prediction sentinel is either treated as "
          "an error or not surfaced in sentinel_reports as pending",
          check7)

    # ---- Check 8: 'withheld' sentinel resolved by a later terminal --------
    def check8():
        text = _minimal_record(
            _minimal_intent(**{"Prediction (outcome — planner)": "withheld"}),
            _minimal_terminal(**{"Prediction-outcome-supplied": "it worked"}))
        _, errors, _, sentinel_reports = validate_entries(text)
        assert not errors, f"legitimate resolution of a withheld sentinel raised errors: {errors}"
        assert any(r["sentinel"] == "withheld" and r["status"] == "resolved"
                   for r in sentinel_reports), (
            f"withheld sentinel not marked resolved once supplied by the "
            f"closing terminal: {sentinel_reports}")

    check("check8_withheld_sentinel_resolved_by_terminal",
          "a terminal entry supplying the outcome for an intent whose "
          "prediction was legitimately 'withheld' is not recognized as a "
          "resolution",
          check8)

    # ---- Check 9: 'not authored' + later-supplied is fabrication ----------
    def check9():
        text = _minimal_record(
            _minimal_intent(**{"Prediction (outcome — planner)": "not authored"}),
            _minimal_terminal(**{"Prediction-outcome-supplied": "it worked"}))
        _, errors, _, _ = validate_entries(text)
        assert any("fabricated after the outcome" in e for e in errors), (
            f"a permanently 'not authored' sentinel paired with a later-"
            f"supplied value was not flagged as fabrication: {errors}")

    check("check9_not_authored_plus_supplied_is_fabrication",
          "an intent whose outcome prediction is permanently 'not "
          "authored' is not flagged when a terminal entry later supplies "
          "a value anyway",
          check9)

    # ---- Check 10: sentinels forbidden in terminal entries -----------------
    def check10():
        text = _minimal_record(
            _minimal_intent(),
            _minimal_terminal(Observed="withheld"))
        _, errors, _, _ = validate_entries(text)
        assert any("Observed" in e and "withheld" in e for e in errors), (
            f"a sentinel value in a terminal entry field was accepted: {errors}")

    check("check10_sentinel_forbidden_in_terminal_entry",
          "a terminal entry carrying a sentinel value in any field is "
          "accepted, or the error does not name the field and value",
          check10)

    # ---- Check 11: working-tree append-only catches a modified line -------
    def check11():
        tmp = Path(tempfile.mkdtemp(prefix="check_record_render_check_"))
        _init_repo(tmp)
        original = _minimal_record(_minimal_intent(), _minimal_terminal())
        _commit_record(tmp, original, "initial record")

        lines = original.splitlines()
        target_idx = next(i for i, l in enumerate(lines) if l.startswith("**Title:**"))
        lines[target_idx] = "**Title:** tampered"
        (tmp / RECORD_NAME).write_text("\n".join(lines))

        ok, msg, vacuous = check_append_only(tmp)
        assert not ok, "a modified existing line was not caught"
        assert not vacuous, "a real comparison was incorrectly reported vacuous"
        assert f"line {target_idx + 1}" in msg

    check("check11_working_tree_append_only_catches_modified_line",
          "modifying an existing, already-committed line in RECORD.md is "
          "not caught, or the failure does not name the changed line",
          check11)

    # ---- Check 12: working-tree append-only, vacuous case -----------------
    def check12():
        tmp = Path(tempfile.mkdtemp(prefix="check_record_render_check_"))
        _init_repo(tmp)
        (tmp / RECORD_NAME).write_text(_minimal_record(_minimal_intent()))
        ok, msg, vacuous = check_append_only(tmp)
        assert ok, f"RECORD.md absent from HEAD (nothing committed yet) was reported as a violation: {msg}"
        assert vacuous, "a check with nothing at HEAD to compare against was not reported vacuous"

    check("check12_working_tree_append_only_vacuous_before_first_commit",
          "a RECORD.md that exists in the working tree but has never been "
          "committed is reported as a violation, or the vacuous case is "
          "not flagged as vacuous",
          check12)

    # ---- Check 13: history walk on a real append-only repo ----------------
    def check13():
        tmp = Path(tempfile.mkdtemp(prefix="check_record_render_check_"))
        _init_repo(tmp)
        v1 = _minimal_record(_minimal_intent())
        v2 = _minimal_record(_minimal_intent(), _minimal_terminal())
        _commit_record(tmp, v1, "intent")
        _commit_record(tmp, v2, "terminal")
        ok, violations, count, vacuous = check_history_append_only(tmp)
        assert ok, f"a genuinely append-only history was reported violating: {violations}"
        assert count == 2
        assert not vacuous, "two real committed versions was incorrectly reported vacuous"

    check("check13_history_walk_real_repo",
          "a genuinely append-only two-commit history is reported as "
          "violating, or the wrong commit count is walked",
          check13)

    # ---- Check 14: history walk, vacuous case (one commit) ----------------
    def check14():
        tmp = Path(tempfile.mkdtemp(prefix="check_record_render_check_"))
        _init_repo(tmp)
        _commit_record(tmp, _minimal_record(_minimal_intent()), "only commit")
        ok, violations, count, vacuous = check_history_append_only(tmp)
        assert ok, f"a single-commit history was reported violating: {violations}"
        assert count == 1
        assert vacuous, "a history with fewer than two versions was not reported vacuous"

    check("check14_history_walk_vacuous_single_commit",
          "a RECORD.md history with only one committed version performs a "
          "comparison anyway, or is not reported vacuous",
          check14)

    # ---- Check 15: history walk catches a removed line ---------------------
    def check15():
        tmp = Path(tempfile.mkdtemp(prefix="check_record_render_check_"))
        _init_repo(tmp)
        v1 = "line1\nline2\nline3\n"
        v2 = "line1\nline3\n"  # line2 removed
        (tmp / RECORD_NAME).write_text(v1)
        subprocess.run(["git", "-C", str(tmp), "add", RECORD_NAME], check=True)
        subprocess.run(["git", "-C", str(tmp), "-c", "user.name=x", "-c",
                        "user.email=x@example.invalid", "commit", "-q", "-m", "v1"],
                       check=True)
        (tmp / RECORD_NAME).write_text(v2)
        subprocess.run(["git", "-C", str(tmp), "add", RECORD_NAME], check=True)
        subprocess.run(["git", "-C", str(tmp), "-c", "user.name=x", "-c",
                        "user.email=x@example.invalid", "commit", "-q", "-m", "v2 bad"],
                       check=True)
        ok, violations, count, _ = check_history_append_only(tmp)
        assert not ok, "a commit that removed a line from history was not caught"
        assert violations[0]["divergence_line"] == 2

    check("check15_history_walk_catches_removed_line",
          "a commit that removed an existing line from RECORD.md's "
          "history is accepted by the walk",
          check15)

    # ---- Check 16: merge commit stops the walk -----------------------------
    def check16():
        # A merge that changes an unrelated file (or fast-forwards cleanly)
        # gets pruned out of `git log -- RECORD.md`'s default history
        # simplification entirely -- confirmed by direct reproduction
        # while building this suite, not assumed. Only a merge that
        # genuinely reconciles divergent RECORD.md content on both sides
        # survives that simplification and reaches the walk at all, so
        # that is what this fixture has to construct.
        tmp = Path(tempfile.mkdtemp(prefix="check_record_render_check_"))
        _init_repo(tmp)
        _commit_record(tmp, _minimal_record(_minimal_intent(id_="2026-01-01-01")),
                       "on main")
        subprocess.run(["git", "-C", str(tmp), "checkout", "-q", "-b", "side"], check=True)
        _commit_record(tmp, _minimal_record(
            _minimal_intent(id_="2026-01-01-01"),
            _minimal_intent(id_="2026-01-01-02")), "on side")
        subprocess.run(["git", "-C", str(tmp), "checkout", "-q", "-"], check=True)
        _commit_record(tmp, _minimal_record(
            _minimal_intent(id_="2026-01-01-01"),
            _minimal_intent(id_="2026-01-01-03")), "on main further")
        subprocess.run(["git", "-C", str(tmp), "-c", "user.name=x", "-c",
                        "user.email=x@example.invalid", "merge", "-q",
                        "--no-ff", "side", "-m", "merge side"],
                       capture_output=True)  # expected to conflict; resolved below
        _commit_record(tmp, _minimal_record(
            _minimal_intent(id_="2026-01-01-01"),
            _minimal_intent(id_="2026-01-01-02"),
            _minimal_intent(id_="2026-01-01-03")), "merge side")
        try:
            check_history_append_only(tmp)
        except MergeCommitEncountered:
            pass
        else:
            raise AssertionError("a merge commit touching RECORD.md did not "
                                 "raise MergeCommitEncountered")

    check("check16_merge_commit_stops_the_walk",
          "a merge commit touching RECORD.md is silently walked (wrong "
          "parent guessed) instead of raising MergeCommitEncountered",
          check16)

    # ---- Check 17: Superseded-by cross-reference, vacuous case ------------
    def check17():
        entries, _, _, _ = validate_entries(
            _minimal_record(_minimal_intent(), _minimal_terminal()))
        ok, errs, vacuous = check_superseded_by(entries)
        assert ok and not errs, f"no superseded entries but check reported errors: {errs}"
        assert vacuous, "a store with no Outcome: superseded entries was not reported vacuous"

    check("check17_superseded_by_vacuous_when_none_declared",
          "a record with no terminal entry declaring Outcome: superseded "
          "is not reported vacuous, or is reported as a failure",
          check17)

    # ---- Check 18: Superseded-by cross-reference catches a bad reference --
    def check18():
        entries, _, _, _ = validate_entries(_minimal_record(
            _minimal_intent(),
            _minimal_terminal(outcome="superseded",
                              **{"Superseded-by": "2026-01-01-99"})))
        ok, errs, vacuous = check_superseded_by(entries)
        assert not ok, "a Superseded-by naming a nonexistent intent ID was accepted"
        assert not vacuous
        assert any("2026-01-01-99" in e for e in errs)

    check("check18_superseded_by_catches_dangling_reference",
          "a terminal entry's Superseded-by field naming a nonexistent "
          "intent ID is accepted",
          check18)

    # ---- Checks 19-36: RECORDING.md's twelve entry types (2026-10-16-07) --
    # Minimal required fields by the operator's ruling: Kind, ID, Timestamp,
    # Notes, and each type's link field. Written before the rules existed.

    def ent(kind, id_, **fields):
        base = {"Kind": kind, "ID": id_, "Timestamp": "2026-01-01T00:05:00Z",
                "Notes": "Written by the test."}
        base.update(fields)
        return _render_entry(base)

    def errs_of(*entries):
        _, errors, unterminated, _ = validate_entries(_minimal_record(*entries))
        return errors, unterminated

    def check19():
        errors, unterminated = errs_of(
            _minimal_intent("2026-01-01-01"),
            ent("continuation", "2026-01-01-02", Continues="2026-01-01-01"),
            ent("decision", "2026-01-01-03", Continues="2026-01-01-02"),
            ent("outcome", "2026-01-01-04", Continues="2026-01-01-01"),
            ent("observation", "2026-01-01-05"),
            ent("finding", "2026-01-01-06", Continues="2026-01-01-01"),
            ent("device-note", "2026-01-01-07"),
            ent("correction", "2026-01-01-08", Corrects="2026-01-01-03, its wording"),
            ent("merge", "2026-01-01-09", **{"Merge-commit": "a" * 40, "Backup": "2026-01-01-01"}),
            ent("dispatch-note", "2026-01-01-10", Dispatch="2026-01-01-01"),
            ent("handoff", "2026-01-01-11"),
            _minimal_terminal("2026-01-01-12", closes="2026-01-01-01"))
        assert not errors, f"a record using all twelve types produced errors: {errors}"
        assert not unterminated, f"unexpected unterminated: {unterminated}"

    check("check19_all_twelve_kinds_accepted",
          "a record using every RECORDING.md entry type with minimal fields is rejected",
          check19)

    def check20():
        errors, _ = errs_of(ent("memo", "2026-01-01-01"))
        assert any("invalid Kind" in e for e in errors), f"unknown kind accepted: {errors}"

    check("check20_unknown_kind_still_rejected",
          "a kind outside the twelve is accepted (guard: passes before and after the "
          "change by design, so it is not evidence for the change)",
          check20)

    def check21():
        errors, _ = errs_of(ent("decision", "2026-01-01-01", Notes=None))
        assert any("2026-01-01-01" in e and "'Notes'" in e for e in errors), (
            f"decision without Notes not reported by ID and field: {errors}")

    check("check21_new_kind_missing_notes_named",
          "an entry of a new type without its Notes line is accepted",
          check21)

    def check22():
        errors, _ = errs_of(ent("continuation", "2026-01-01-01"))
        assert any("2026-01-01-01" in e and "'Continues'" in e for e in errors), (
            f"continuation without Continues not reported: {errors}")

    check("check22_continuation_missing_continues_named",
          "a continuation with no Continues field is accepted",
          check22)

    def check23():
        errors, _ = errs_of(_minimal_intent("2026-01-01-01"),
                            _minimal_terminal("2026-01-01-02", closes="2026-01-01-01"),
                            ent("continuation", "2026-01-01-03", Continues="2026-01-01-01"))
        assert any("2026-01-01-03" in e and "closed" in e for e in errors), (
            f"continuation of a closed intent not caught: {errors}")

    check("check23_continuation_of_closed_intent_caught",
          "a continuation naming an intent already closed earlier in the file is accepted",
          check23)

    def check24():
        errors, _ = errs_of(ent("decision", "2026-01-01-01"),
                            ent("continuation", "2026-01-01-02", Continues="2026-01-01-01"))
        assert any("2026-01-01-02" in e and "not an intent" in e for e in errors), (
            f"continuation of a non-intent not caught: {errors}")

    check("check24_continuation_of_non_intent_caught",
          "a continuation naming an entry that is not an intent is accepted",
          check24)

    def check25():
        errors, _ = errs_of(_minimal_intent("2026-01-01-01"),
                            ent("continuation", "2026-01-01-02", Continues="2026-01-01-01",
                                Outcome="completed"))
        assert any("2026-01-01-02" in e and "'Outcome'" in e for e in errors), (
            f"continuation carrying Outcome not caught: {errors}")

    check("check25_continuation_forbidden_field_caught",
          "a continuation carrying a closing field (Outcome) is accepted",
          check25)

    def check26():
        errors, unterminated = errs_of(_minimal_intent("2026-01-01-01"),
                                       ent("outcome", "2026-01-01-02", Closes="2026-01-01-01"))
        assert not errors, f"outcome closing its intent produced errors: {errors}"
        assert not unterminated, f"outcome with Closes did not close: {unterminated}"

    check("check26_outcome_with_closes_closes_intent",
          "an outcome carrying Closes is rejected, or leaves its intent unterminated",
          check26)

    def check27():
        entries, _, _, _ = validate_entries(_minimal_record(
            _minimal_intent("2026-01-01-01"),
            _minimal_terminal("2026-01-01-02", closes="2026-01-01-01"),
            ent("outcome", "2026-01-01-03", Closes="2026-01-01-01")))
        ok, errs = check_duplicate_terminals(entries)
        assert not ok and any("2026-01-01-02" in e and "2026-01-01-03" in e for e in errs), (
            f"terminal and outcome both closing one intent not caught: {errs}")

    check("check27_terminal_and_outcome_double_close_caught",
          "an intent closed by both a terminal and an outcome passes the "
          "closed-once check",
          check27)

    def check28():
        errors, _ = errs_of(ent("outcome", "2026-01-01-01"))
        assert any("2026-01-01-01" in e and "Continues" in e and "Closes" in e
                   for e in errors), f"outcome with neither link not caught: {errors}"

    check("check28_outcome_needs_continues_or_closes",
          "an outcome with neither Continues nor Closes is accepted",
          check28)

    def check29():
        errors, _ = errs_of(ent("correction", "2026-01-01-01", Corrects="2026-01-01-99"))
        assert any("2026-01-01-01" in e and "2026-01-01-99" in e for e in errors), (
            f"correction naming a nonexistent entry not caught: {errors}")

    check("check29_correction_dangling_reference_caught",
          "a correction whose Corrects names no existing entry is accepted",
          check29)

    def check30():
        errors, _ = errs_of(_minimal_intent("2026-01-01-01"),
                            ent("decision", "2026-01-01-02", Closes="2026-01-01-01"))
        assert any("2026-01-01-02" in e and "'Closes'" in e for e in errors), (
            f"Closes on a decision not caught: {errors}")

    check("check30_closes_on_other_kind_caught",
          "a type other than terminal or outcome carrying Closes is accepted",
          check30)

    def check31():
        errors, _ = errs_of(_minimal_intent("2026-01-01-01"),
                            _minimal_terminal("2026-01-01-02", outcome="parked"))
        assert any("2026-01-01-02" in e and "parked" in e for e in errors), (
            f"terminal outcome outside the four not caught: {errors}")

    check("check31_unknown_terminal_outcome_caught",
          "a terminal Outcome outside completed, partial, superseded, abandoned is accepted",
          check31)

    def check32():
        errors, _ = errs_of(_minimal_intent("2026-01-01-01"),
                            _minimal_terminal("2026-01-01-02", outcome="partial"))
        assert any("2026-01-01-02" in e and "'Deferred'" in e for e in errors), (
            f"partial without Deferred not caught: {errors}")

    check("check32_partial_requires_deferred",
          "a partial terminal without a Deferred field is accepted",
          check32)

    def check33():
        errors, _ = errs_of(_minimal_intent("2026-01-01-01"),
                            _minimal_terminal("2026-01-01-02", Deferred="step 3"))
        assert any("2026-01-01-02" in e and "Deferred" in e for e in errors), (
            f"completed carrying Deferred not caught: {errors}")

    check("check33_completed_with_deferred_caught",
          "a completed terminal carrying Deferred is accepted",
          check33)

    def check34():
        errors, _ = errs_of(ent("merge", "2026-01-01-01", **{"Merge-commit": "a" * 40}))
        assert any("2026-01-01-01" in e and "'Backup'" in e for e in errors), (
            f"merge without Backup not caught: {errors}")

    check("check34_merge_requires_backup",
          "a merge entry that names no backup is accepted",
          check34)

    def check35():
        errors, _ = errs_of(ent("dispatch-note", "2026-01-01-01"))
        assert any("2026-01-01-01" in e and "Dispatch" in e for e in errors), (
            f"dispatch-note with no dispatch reference not caught: {errors}")

    check("check35_dispatch_note_requires_dispatch_reference",
          "a dispatch-note naming neither Dispatch-file nor Dispatch is accepted",
          check35)

    def check36():
        errors, _ = errs_of(ent("decision", "2026-01-01-01", Continues="2026-01-01-99"))
        assert any("2026-01-01-01" in e and "2026-01-01-99" in e for e in errors), (
            f"Continues naming a nonexistent entry not caught: {errors}")

    check("check36_continues_dangling_on_other_kind_caught",
          "a Continues on a decision naming no existing entry is accepted",
          check36)

    # Checks 37-38 were written after the rules (gaps found before the
    # revert runs); their evidence is the revert run, not a red before.
    def check37():
        missing = []
        for k in OTHER_REQUIRED:
            fields = {"Notes": None}
            if k == "merge":
                fields.update({"Merge-commit": "a" * 40, "Backup": "b"})
            errors, _ = errs_of(ent(k, "2026-01-01-01", **fields))
            if not any("2026-01-01-01" in e and "'Notes'" in e for e in errors):
                missing.append(k)
        assert not missing, f"types accepted without Notes: {missing}"

    check("check37_every_new_kind_requires_notes",
          "some new entry type is accepted without its who-wrote-it Notes line",
          check37)

    def check38():
        cases = [("finding", {}, "'Continues'"), ("correction", {}, "'Corrects'"),
                 ("merge", {"Backup": "b"}, "'Merge-commit'")]
        missing = []
        for k, fields, label in cases:
            errors, _ = errs_of(ent(k, "2026-01-01-01", **fields))
            if not any("2026-01-01-01" in e and label in e for e in errors):
                missing.append((k, label))
        assert not missing, f"link fields not required: {missing}"

    check("check38_link_fields_required",
          "a finding without Continues, a correction without Corrects, or a merge "
          "without Merge-commit is accepted",
          check38)

    # ---- Checks 39-46: monthly record files and longer IDs (2026-10-17-01) --
    # Written before the rules existed. Functions are looked up, not called
    # directly, so a missing rule fails as an assertion naming it rather
    # than as a NameError that never ran the test.

    def need(name):
        fn = globals().get(name)
        assert fn is not None, f"{name} does not exist: the monthly-file rule is missing"
        return fn

    def month_record(month, *entries):
        parts = [f"# Record, {month}", "", "## Entries", "", "---", ""]
        for e in entries:
            parts += [e, "", "---", ""]
        return "\n".join(parts)

    def write_monthly(tmp, months, index=True):
        tmp = Path(tmp)
        if index:
            (tmp / RECORD_NAME).write_text("# RECORD.md\n\nThe index; entries are in records/.\n")
        (tmp / "records").mkdir(exist_ok=True)
        for m, entries in months.items():
            (tmp / "records" / f"{m}.md").write_text(month_record(m, *entries))

    def check39():
        errors, _ = errs_of(_minimal_intent("2026-09-28-1106"))
        assert not any("malformed ID" in e for e in errors), (
            f"a four-digit ID number is rejected: {errors}")

    check("check39_four_digit_id_number_accepted",
          "an ID like 2026-09-28-1106 (Forager's running sequence) is rejected as malformed",
          check39)

    def check40():
        errors, _ = errs_of(_minimal_intent("2026-09-28-1"))
        assert any("malformed ID" in e for e in errors), (
            f"a one-digit ID number is accepted: {errors}")

    check("check40_one_digit_id_number_still_rejected",
          "a one-digit ID number is accepted (guard: passes before and after by design)",
          check40)

    def months_fixture(tmp, ts_intent="2026-09-30T00:00:00Z"):
        write_monthly(tmp, {
            "2026-09": [_minimal_intent("2026-09-28-01", Timestamp=ts_intent)],
            "2026-10": [ent("continuation", "2026-09-28-02", Continues="2026-09-28-01",
                            Timestamp="2026-10-02T00:00:00Z"),
                        _minimal_terminal("2026-09-28-03", closes="2026-09-28-01",
                                          Timestamp="2026-10-03T00:00:00Z")],
        })

    def check41():
        validate_repo = need("validate_repo")
        tmp = Path(tempfile.mkdtemp())
        months_fixture(tmp)
        entries, errors, unterminated, _ = validate_repo(tmp)
        assert not errors, f"a valid two-month record produced errors: {errors}"
        assert len(entries) == 3 and not unterminated, (
            f"monthly files not read as one record: {len(entries)} entries, "
            f"unterminated {unterminated}")

    check("check41_monthly_files_read_as_one_record",
          "records/YYYY-MM.md files are not read, or not read as one record across months",
          check41)

    def check42():
        validate_repo = need("validate_repo")
        tmp = Path(tempfile.mkdtemp())
        write_monthly(tmp, {
            "2026-09": [_minimal_intent("2026-09-28-01", Timestamp="2026-09-30T00:00:00Z")],
            "2026-10": [ent("decision", "2026-09-28-01", Timestamp="2026-10-01T00:00:00Z")],
        })
        _, errors, _, _ = validate_repo(tmp)
        assert any("duplicate ID 2026-09-28-01" in e for e in errors), (
            f"an ID used in two monthly files not caught: {errors}")

    check("check42_duplicate_id_across_months_caught",
          "the same ID in two monthly files is accepted",
          check42)

    def check43():
        validate_repo = need("validate_repo")
        tmp = Path(tempfile.mkdtemp())
        write_monthly(tmp, {
            "2026-09": [_minimal_intent("2026-09-28-01", Timestamp="2026-10-05T00:00:00Z")],
        })
        _, errors, _, _ = validate_repo(tmp)
        assert any("2026-09-28-01" in e and "records/2026-09.md" in e and "2026-10" in e
                   for e in errors), f"an entry filed in the wrong month not caught: {errors}"

    check("check43_entry_in_wrong_month_caught",
          "an entry whose Timestamp month differs from its monthly file's month is accepted",
          check43)

    def check44():
        append_only_checks = need("append_only_checks")
        tmp = Path(tempfile.mkdtemp())
        _init_repo(tmp)
        months_fixture(tmp)
        subprocess.run(["git", "-C", str(tmp), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(tmp), "-c", "user.name=t", "-c",
                        "user.email=t@example.invalid", "commit", "-q", "-m", "m"], check=True)
        p = tmp / "records" / "2026-09.md"
        p.write_text(p.read_text().replace("**Title:** t", "**Title:** edited"))
        results = append_only_checks(tmp)
        bad = [r for r in results if r["file"] == "records/2026-09.md" and not r["ok"]]
        assert bad, f"an edited committed line in a monthly file not caught: {results}"

    check("check44_monthly_file_append_only_checked",
          "an edit to a committed line of a monthly file passes the working-tree check",
          check44)

    def check45():
        append_only_checks = need("append_only_checks")
        tmp = Path(tempfile.mkdtemp())
        _init_repo(tmp)
        months_fixture(tmp)
        results = append_only_checks(tmp)
        idx = [r for r in results if r["file"] == RECORD_NAME]
        assert idx and idx[0]["ok"] and "index" in idx[0]["msg"], (
            f"RECORD.md as the index is not reported as such: {results}")

    check("check45_index_record_md_reported_not_checked",
          "with monthly files and an entry-less RECORD.md, RECORD.md is not reported as the index",
          check45)

    def check46():
        history_checks = need("history_checks")
        tmp = Path(tempfile.mkdtemp())
        _init_repo(tmp)
        months_fixture(tmp)
        def commit(msg):
            subprocess.run(["git", "-C", str(tmp), "add", "-A"], check=True)
            subprocess.run(["git", "-C", str(tmp), "-c", "user.name=t", "-c",
                            "user.email=t@example.invalid", "commit", "-q", "-m", msg], check=True)
        commit("one")
        p = tmp / "records" / "2026-10.md"
        p.write_text(p.read_text().replace("**Observed:** o\n", ""))
        commit("two")
        results = history_checks(tmp)
        bad = [r for r in results if r["file"] == "records/2026-10.md" and not r["ok"]]
        assert bad, f"a committed line removed from a monthly file not caught by the walk: {results}"

    check("check46_monthly_file_history_walked",
          "a line removed from a monthly file in a committed change passes the history walk",
          check46)

    # ---- Checks 47-55: any repository, shaped by a JSON config (2026-10-17-05)
    # Written before the behaviour existed; run through main(argv), the real
    # entry point. A main() that takes no arguments fails by assertion.

    import inspect, io, json
    from contextlib import redirect_stdout

    def run_main(argv):
        params = inspect.signature(main).parameters
        assert params, "main() takes no arguments: the repository argument is missing"
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(argv)
        return code, buf.getvalue()

    def repo_with(files):
        tmp = Path(tempfile.mkdtemp())
        _init_repo(tmp)
        for rel, text in files.items():
            p = tmp / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text if isinstance(text, str) else json.dumps(text))
        return tmp

    def note(id_, **fields):
        base = {"Kind": "note", "ID": id_}
        base.update(fields)
        return _render_entry(base)

    NOTE_CONFIG = {"record_file": "LOG.md", "kinds": {"note": {"required": ["Kind", "ID", "Body"]}},
                   "intent_kind": None, "terminal_kind": None, "continuation_kind": None,
                   "closing_kinds": []}

    def check47():
        bad = repo_with({RECORD_NAME: _minimal_record(_minimal_intent(Change=None))})
        code, out = run_main([str(bad)])
        assert code == 1 and "'Change'" in out, (
            f"the given repository was not the one checked (exit {code}): {out!r}")
        good = repo_with({RECORD_NAME: _minimal_record(_minimal_intent())})
        code, out = run_main([str(good)])
        assert code == 0, f"a valid record in the given repository failed (exit {code}): {out!r}"

    check("check47_repository_argument_is_the_one_checked",
          "the checker checks its own folder, not the repository it is given",
          check47)

    def check48():
        tmp = repo_with({"records.json": {"record_file": "LOG.md"},
                         "LOG.md": _minimal_record(_minimal_intent())})
        code, out = run_main([str(tmp)])
        assert code == 0 and "LOG.md" in out, (
            f"records.json in the repository was not read (exit {code}): {out!r}")

    check("check48_records_json_in_repository_is_read",
          "a records.json in the checked repository is ignored",
          check48)

    def check49():
        tmp = repo_with({"records.json": NOTE_CONFIG,
                         "LOG.md": _minimal_record(note("2026-01-01-01", Body="b"),
                                                   note("2026-01-01-02"),
                                                   _minimal_intent("2026-01-01-03"))})
        code, out = run_main([str(tmp)])
        assert code == 1, f"a config's entry types were not applied (exit {code}): {out!r}"
        assert "2026-01-01-02" in out and "'Body'" in out, f"missing Body not named: {out!r}"
        assert "invalid Kind" in out and "intent" in out, (
            f"a kind outside the config's types was accepted: {out!r}")

    check("check49_config_sets_the_entry_types",
          "a config's own entry types and required fields are not applied",
          check49)

    def check50():
        cfg = dict(NOTE_CONFIG, id_pattern="^N\\d+$", id_token_pattern="N\\d+")
        tmp = repo_with({"records.json": cfg,
                         "LOG.md": _minimal_record(note("N12", Body="b"), note("2026-01-01-02", Body="b"))})
        code, out = run_main([str(tmp)])
        assert "2026-01-01-02: malformed ID" in out and "N12: malformed ID" not in out, (
            f"a config's ID pattern was not applied: {out!r}")

    check("check50_config_sets_the_id_pattern",
          "a config's ID pattern is not applied",
          check50)

    def check51():
        tmp = repo_with({"records.json": {"recordfile": "X"}, RECORD_NAME: _minimal_record(_minimal_intent())})
        code, out = run_main([str(tmp)])
        assert code == 2 and "recordfile" in out, f"an unknown config key was not refused by name (exit {code}): {out!r}"
        tmp = repo_with({"records.json": {"id_pattern": "("}, RECORD_NAME: _minimal_record(_minimal_intent())})
        code, out = run_main([str(tmp)])
        assert code == 2 and "id_pattern" in out, f"a bad regex was not refused by name (exit {code}): {out!r}"

    check("check51_invalid_config_refused_by_name",
          "an unknown key or an uncompilable regex in the config is accepted or not named",
          check51)

    def check52():
        tmp = repo_with({RECORD_NAME: _minimal_record(_minimal_intent(Change=None))})
        code, out = run_main([str(tmp), "--json"])
        data = json.loads(out)
        assert data["ok"] is False and data["entries"] == 1 and any("'Change'" in e for e in data["errors"]), (
            f"--json output lacks ok, entries or errors: {data}")

    check("check52_json_output",
          "--json does not print one JSON object carrying ok, entries and errors",
          check52)

    def check53():
        default = globals().get("DEFAULT_CONFIG")
        assert default is not None, "DEFAULT_CONFIG does not exist: the config is missing"
        code, out = run_main(["--print-config"])
        printed = json.loads(out)
        assert printed == json.loads(json.dumps(default)), "--print-config does not print the default config"
        tmp = repo_with({"records.json": printed, RECORD_NAME: _minimal_record(_minimal_intent())})
        code, out = run_main([str(tmp)])
        assert code == 0, f"the printed default config, used as records.json, fails a valid record: {out!r}"

    check("check53_print_config_round_trips",
          "--print-config does not print the default, or the printed default is not a valid config",
          check53)

    def check54():
        rec = "# Record, 2026-10\n\n## Entries\n\n---\n\n" + _minimal_intent(Timestamp="2026-10-01T00:00:00Z") + "\n\n---\n"
        tmp = repo_with({"records.json": {"monthly_dir": "log"}, RECORD_NAME: "# RECORD.md\n\nThe index.\n",
                         "log/2026-10.md": rec})
        code, out = run_main([str(tmp), "--json"])
        assert json.loads(out)["entries"] == 1, f"a configured monthly folder was not read: {out!r}"
        tmp = repo_with({"records.json": {"monthly_dir": None}, RECORD_NAME: _minimal_record(_minimal_intent()),
                         "records/2026-10.md": rec.replace("2026-01-01-01", "2026-01-01-09")})
        code, out = run_main([str(tmp), "--json"])
        assert json.loads(out)["entries"] == 1, f"monthly_dir null did not turn monthly files off: {out!r}"

    check("check54_monthly_dir_configurable",
          "a configured monthly folder is not read, or null does not turn monthly files off",
          check54)

    def check55():
        tmp = repo_with({"records.json": {"terminal_outcomes": {"done": {}}},
                         RECORD_NAME: _minimal_record(_minimal_intent(),
                                                      _minimal_terminal(outcome="done"),
                                                      _minimal_intent("2026-01-01-03"),
                                                      _minimal_terminal("2026-01-01-04", closes="2026-01-01-03"))})
        code, out = run_main([str(tmp)])
        assert "'done' is not one of" not in out and "'completed' is not one of" in out, (
            f"configured terminal outcomes were not applied: {out!r}")

    check("check55_terminal_outcomes_configurable",
          "a config's terminal outcomes are not applied",
          check55)

    # Check 56 was written after 47-55, when verifying ADOPTING.md found that
    # a record file with no '## Entries' heading reads as zero entries and
    # passes with nothing marking it vacuous. Committed red before the fix.
    def check56():
        tmp = repo_with({RECORD_NAME: "# RECORD.md\n\n## entries\n\n---\n\n" + _minimal_intent() + "\n\n---\n"})
        code, out = run_main([str(tmp), "--json"])
        data = json.loads(out)
        assert data["entries"] == 0 and data["vacuous"] is True and "Entries" in data.get("note", ""), (
            f"a record read as zero entries is not marked vacuous with a note: {data}")
        code, out = run_main([str(tmp)])
        assert "no entries were read" in out, f"the text output does not say no entries were read: {out!r}"

    check("check56_zero_entries_marked_vacuous",
          "a record file that yields no entries passes without being marked vacuous",
          check56)

    # ---- Checks 57-62: the history walk across merges (2026-10-17-11) ----
    # Written before the walk handled merges. Each fixture holds a real
    # two-parent merge, and each check runs through main(argv). PROTOCOL rule
    # 13: "every row from both sides is kept"; "No record entry is written
    # inside a merge commit".
    MERGE_MSG = "each branch's additions"

    def git_in(tmp, *a):
        return subprocess.run(["git", "-C", str(tmp), "-c", "user.name=t", "-c",
                               "user.email=t@example.invalid", *a], capture_output=True, text=True)

    def block(id_):
        return "\n" + ent("observation", id_) + "\n\n---\n"

    BASE = _minimal_record(_minimal_intent("2026-01-01-01"))
    A, B, C = block("2026-01-01-02"), block("2026-01-01-03"), block("2026-01-01-04")

    def merge_repo(main_text, side_text, merged_text, side_first_edit=None):
        """base on main; side branch writes side_text (optionally first a
        commit with side_first_edit); main writes main_text (or an unrelated
        file); a real --no-ff merge of side into main, resolved to merged_text.
        Returns (repo, merge hash, side commit hashes)."""
        tmp = Path(tempfile.mkdtemp())
        git_in(tmp, "init", "-q", "-b", "main")
        (tmp / RECORD_NAME).write_text(BASE)
        git_in(tmp, "add", "-A"); git_in(tmp, "commit", "-qm", "base")
        git_in(tmp, "checkout", "-qb", "side")
        side_commits = []
        for text in ([side_first_edit] if side_first_edit else []) + [side_text]:
            (tmp / RECORD_NAME).write_text(text)
            git_in(tmp, "commit", "-qam", "side")
            side_commits.append(git_in(tmp, "rev-parse", "HEAD").stdout.strip())
        git_in(tmp, "checkout", "-q", "main")
        if main_text is not None:
            (tmp / RECORD_NAME).write_text(main_text)
            git_in(tmp, "commit", "-qam", "main adds")
        else:
            (tmp / "other.txt").write_text("o\n")
            git_in(tmp, "add", "-A"); git_in(tmp, "commit", "-qm", "main other")
        git_in(tmp, "merge", "-q", "--no-ff", "--no-commit", "side")
        (tmp / RECORD_NAME).write_text(merged_text)
        git_in(tmp, "add", "-A"); git_in(tmp, "commit", "-qm", "merge side")
        parents = git_in(tmp, "log", "-1", "--format=%P").stdout.split()
        assert len(parents) == 2, f"fixture is not a two-parent merge: {parents}"
        return tmp, git_in(tmp, "rev-parse", "HEAD").stdout.strip(), side_commits

    def walk_errors(tmp):
        code, out = run_main([str(tmp), "--json"])
        data = json.loads(out)
        return data["ok"], [e for e in data["errors"] if e.startswith("history walk")]

    def check57():
        for merged in (BASE + A + B, BASE + B + A):
            tmp, m, _ = merge_repo(BASE + A, BASE + B, merged)
            ok, errs = walk_errors(tmp)
            assert ok and not errs, f"a merge keeping both branches' entries whole failed the walk: {errs}"

    check("check57_merge_keeping_both_branches_passes",
          "a merge whose record is the base followed by each branch's additions, in either order, fails",
          check57)

    def check58():
        edited = B.replace("Written by the test.", "Written by someone else.")
        tmp, m, _ = merge_repo(BASE + A, BASE + B, BASE + A + edited)
        ok, errs = walk_errors(tmp)
        assert not ok and any(m[:10] in e and MERGE_MSG in e for e in errs), (
            f"a merge that edited a branch's entry was not reported against the merge: {errs}")

    check("check58_merge_editing_an_entry_fails",
          "a merge that changes a line one branch committed passes, or fails without naming the merge",
          check58)

    def check59():
        tmp, m, _ = merge_repo(BASE + A, BASE + B, BASE + A + B + C)
        ok, errs = walk_errors(tmp)
        assert not ok and any(m[:10] in e and MERGE_MSG in e for e in errs), (
            f"an entry written inside the merge was not reported (rule 13): {errs}")

    check("check59_entry_written_inside_a_merge_fails",
          "a merge that adds an entry of its own passes, against PROTOCOL rule 13",
          check59)

    def check60():
        tmp, m, _ = merge_repo(BASE + A, BASE + B, BASE + A)
        ok, errs = walk_errors(tmp)
        assert not ok and any(m[:10] in e and MERGE_MSG in e for e in errs), (
            f"a merge that kept one branch's record and dropped the other's entry was not reported: {errs}")

    check("check60_merge_dropping_a_branch_entry_fails",
          "a merge that discards an entry committed on the other branch passes (git's default "
          "history of the file hides such a merge)",
          check60)

    def check61():
        edit = BASE.replace("**Title:** t", "**Title:** edited on the side branch")
        tmp, m, side = merge_repo(BASE + A, edit + B, BASE + A + B, side_first_edit=edit)
        ok, errs = walk_errors(tmp)
        assert not ok and any(side[0][:10] in e and "diverges at line" in e for e in errs), (
            f"an edit committed on a side branch, then left out by the merge, was not reported: {errs}")

    check("check61_side_branch_edit_reported",
          "a committed edit on a merged-in branch goes unreported because the walk follows one parent",
          check61)

    def check62():
        tmp = repo_with({})
        (tmp / RECORD_NAME).write_text(BASE)
        git_in(tmp, "add", "-A"); git_in(tmp, "commit", "-qm", "one")
        (tmp / RECORD_NAME).write_text(BASE.replace("**Title:** t", "**Title:** edited") + A)
        git_in(tmp, "commit", "-qam", "two")
        two = git_in(tmp, "rev-parse", "HEAD").stdout.strip()
        ok, errs = walk_errors(tmp)
        assert not ok and any(two[:10] in e and "diverges at line" in e for e in errs), (
            f"a linear edit of a committed line was not reported: {errs}")

    check("check62_linear_edit_still_reported",
          "a committed line edited in linear history passes (guard: passes before and after by design)",
          check62)

    print(f"\n{'FAIL' if failures else 'PASS'}: {len(failures)} of "
          f"{62} checks failed{': ' + ', '.join(failures) if failures else ''}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
