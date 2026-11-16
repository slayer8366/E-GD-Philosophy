# Recount of 2026-11-16: the counting rules, fixed before any count

Filed by the curator under RECORD.md 2026-11-16-01. This is the recount session's Phase 1 report, on Fable, as received. It is committed before the session is told to count (PROTOCOL rule 10). The only change is removing the two-space indent the delivery harness puts on every line of a returned report. Everything below the line is the session's text, unedited.

---

# Recounter, Phase 1: counting rules (no figures computed)

Read-only throughout: every read was `git show <commit>:<path>` or `git ls-tree`/`git log` piped to grep/python3 -I; nothing written anywhere. One item was not read: nothing I read referred to the Restricted Object, so nothing was skipped under that rule.

## What I read to define the rules (format discovery only)

- E-GD at 7e227d0: `trials/forager-2026-10-16.md`, `trials/forager-2026-11-05.md` in full; `PROTOCOL.md` lines 103-125 (rules 9 and 10, the `committed:<sha256>` form); `RECORDING.md` field list for intent (line 34: `Prediction (outcome — planner)`, `Prediction (mechanism — coder)`, `Finish line`, `Abort conditions`, `Baseline`). I did not read readers' reports or verification notes.
- Forager RECORD.md at 97f26098 and 0b3075182: the header, the first entry of each Kind, two mid-record entries (-1115, -1200), two late ones (-1590, -2150), the set of distinct `**Kind:**` labels and of distinct field names (listed, not tallied), the shapes of all `**Closes:**`, `**Continues:**`, `**Timestamp:**` values, and a delimiter regularity check.
- Forager at 0b3075182: filenames under `prompts/preserved/` with dates 2026-10-17..24 and 2026-10-22..2026-11-01 (listed as the input set; not tallied), and the first `verdict` line of each `*-report.md` in 2026-10-17..24 (to learn the line's forms).
- pre-main 6e24b22c4: `git ls-tree prompts/preserved/` for 2026-10-22..11-01 — the diff against the records branch shows those files are absent on pre-main, so figure 10's input is the records branch.
- forager-forecast RECORD.md at 98d4b33a6: header (lines 1-40), distinct Kind labels, first and last ID line, delimiter check.
- RECORD.md commit history to 0b3075182: newest/oldest three commits, presence of merge commits (yes, e.g. bebeb5736), renames (none), distinct author offsets (+0000, -0700, -0800), author≠committer dates (exist, minutes apart).

Format facts the rules rest on (checked at both Forager commits and the forecast commit): every `**Kind:**` line is immediately preceded by a line that is exactly `---` (ignoring blank lines) and immediately followed by an `**ID:**` line; every ID matches `2026-MM-DD-<digits>` (Forager prefixes: 2026-09-22, -23, -26, -27, -28; forecast: 2026-09-28 only); every Timestamp value matches `YYYY-MM-DDTHH:MM:SSZ`; only `dispatch-note` entries lack a Timestamp; one empty block (`---` then `---`) exists after -53 in Forager's record. Closes/Continues values are free text: several IDs, parentheticals naming preserved-prompt IDs (`(preserved 2026-10-01-02)`, `(preserved -57)`), short forms (`with -191`), ranges (`-722 to -727`), and `dispatch 2026-10-22-02`. Prediction appears under these field names: `Prediction`, `Prediction (outcome — planner)`, `Prediction (outcome, planner)`, `Prediction (mechanism — coder)`, `Prediction (mechanism, coder)`, `Prediction (mechanism — auditor)`, `Prediction (mechanism — coder), Hazel's, verbatim in substance`, plus `Planner prediction (stated in the dispatch, not withheld)`, `Prediction check`, `Predictions against the result`. Verdict lines take the forms `**Verdict: Pass with items.**`, `**Verdict for the whole promotion: Pass with items.**`, `## Verdict: PASS WITH ITEMS`, `**Verdict: Pass with items (promote with conditions).**`; in four files the first line containing "verdict" is a "Yardstick:" line, so the rule must anchor on a line that starts with "Verdict".

## Common definitions

- **D1 Entry.** Text of `git show <commit>:RECORD.md`, split on `\n---\n`. A block is an entry iff its first non-blank line starts with `**Kind:**`. Header (before the first separator) and empty blocks are not entries. Kind = `\*\*Kind:\*\*\s*(\S+)`; ID = first `\*\*ID:\*\*\s*(\S+)`; Timestamp = first `^\*\*Timestamp:\*\*\s*(\S+)` (multiline). Body = block text stripped.
- **D2 Field line.** A line matching `^\*\*(.+?):\*\*`; the field name is group 1, stripped. Variant D2b also admits bulleted/indented fields: `^\s*(?:[-*]\s+)?\*\*(.+?):\*\*`. Primary is D2; D2b reported only where it changes a figure.
- **D3 ID token.** ID X appears as a token in text T iff `re.search(r'(?<!\d)' + re.escape(X) + r'(?!\d)', T)`. Full form only.
- **D4 Short-form expansion (variant only).** In a Closes/Continues value, remove parentheticals beginning `(preserved`; then each `(?<![\w-])-(\d{1,4})(?!\d)` becomes `2026-09-28-\1`; `A to B` (full or short forms) expands to every integer between.
- **D5 Sequence.** For prefix `2026-09-28-`, seq = int of the remainder. "After -1106" = seq > 1106 (primary). Variant: entries after the first entry whose ID is 2026-09-28-1106, in file order.
- **D6 Commit date.** Author date as recorded, `git log --format=%ad --date=iso`, first 10 characters (calendar date in the commit's own recorded offset). Variant: committer date in UTC. Variant reported only where it changes a figure; commits on either side of the boundary that move between conventions will be listed.
- **D7 Commit set.** `git rev-list --no-merges 0b3075182 -- RECORD.md` (default history simplification). Variant: add `--full-history`. Parent P = `C^`. A commit whose parent lacks RECORD.md is skipped and reported.

## Rules per figure

**F1.** Forager 97f26098b05f5535924505b7d6b8f496a5f47b03, RECORD.md: count of D1 entries. Claim: 1,275.

**F2.** F1 grouped by Kind (exact label). Claim: 330 continuation, 243 intent, 224 decision, 166 terminal, 128 dispatch-note, 91 merge, 40 outcome, 21 observation, 13 correction, 11 device-note, 5 handoff, 3 finding.

**F3.** Same commit, entries with Kind `intent`. Group "before" = Timestamp < `2026-09-30T00:00:00Z` (string compare; all values are Z); group "from then on" = the rest; intents with no Timestamp reported. "Carries a Prediction field" (primary) = has ≥1 D2 field whose name matches `^Prediction\b(?! check)` — this admits every `Prediction…` form above and excludes `Planner prediction (…)`, `Prediction check`, `Predictions against the result`; the value (even `not authored`) is not examined. Variant P-b: any D2 field name containing `prediction` case-insensitively. Variant P-c: primary, and at least one such field's value is not empty and not `not authored`/`none`/`n/a` (case-insensitive, trailing period ignored). "Finish line" = D2 field name exactly `Finish line`. Report Prediction for both groups, Finish line for the from-then-on group (also Abort conditions and Baseline, as context). Claim: 99 of 100 before; 0 of 143 from then on; Finish line 31 of 143.

**F4.** `git show 97f26098:RECORD.md`: occurrences of `committed:\s*[0-9a-fA-F]{64}` (primary); as context, the literal `committed:<sha256>` and bare `committed:`. Claim: 0.

**F5.** Same commit, intents. "Closed" = ∃ entry with Kind `terminal` having a D2 `Closes` field whose value contains the intent's ID as a D3 token. Count intents not closed. "Has a continuation" = ∃ entry with Kind `continuation` having a D2 `Continues` field whose value contains the intent's ID as a D3 token; count among the unclosed. Variants: (a) D4 expansion on Closes and Continues; (b) continuation by any Kind with a Continues field; (c) closing by Kind `terminal` or `outcome`. Claim: 63 unclosed; 49 of those continued.

**F6.** Forager 0b3075182cfefe98fc5cfa57e9ab456e3729f8d0: entries with seq > 1106 (D5), count and grouped by Kind. Variant: D5 file-position. Claim: 1,055; decision 564, outcome 109, observation 95, intent 93, terminal 70, merge 63, device-note 16, correction 13, dispatch 13, handoff 7, continuation 6, finding 2, dispatch-note 2, ruling 1, audit 1.

**F7.** Among F6 entries, Kind `intent`: count; with Prediction (F3 primary); with `Finish line`; with `Abort conditions` (exact field name); with all three; with `Baseline` (context). "Not closed" = no entry of Kind `terminal` or `outcome` anywhere in the record at 0b3075182 whose D2 `Closes` value contains the ID as a D3 token. Variant: D4 expansion. Context: how many unclosed have any entry with a Continues field naming them. Claim: 93; 66; 81; 80; 32 unclosed.

**F8.** Among F6 entries, Kind `correction`: count; the UTC date of each Timestamp; whether all lie in [2026-10-16, 2026-10-20]. Claim: 13, all in range.

**F9a (edits inside an existing entry).** For each C in D7 with parent P: parse D1 entries of P and C; for each ID, the list of bodies. C "edits inside an existing entry" iff ∃ ID present in both where (both lists length 1 and bodies differ) or (equal length > 1 and sorted lists differ). Header changes excluded; an ID whose count changes between P and C is an add/remove, not an edit, and is reported separately. Split by D6 date ≥ 2026-11-02 vs before. Also report, for the edit-commits: how many are whitespace-only; how many touch only the last entry of P (appending to the newest entry); and how many commits remove an entry (ID in P, absent in C). Claim: 61 from 2026-11-02; 4 before.

**F9b (deleted committed lines).** For each C in D7: deletions = second column of `git diff --numstat P C -- RECORD.md`. Count commits with deletions > 0, and totals, split by D6 date ≥ 2026-11-01 vs before. Report the `--full-history` variant's totals. Claim: 48 of 296 since 2026-11-01; 10 of 1,904 before.

**F10.** Dispatch IDs = group 1 of `^(\d{4}-\d{2}-\d{2}-\d{2})(?:-.*)?\.md$` over basenames of files directly under `prompts/preserved/` at 0b3075182 (so a `-report.md` shares its dispatch's ID; `planner-handoff`, `sorrel-*`, `sage-*` files carry no ID), kept when the date part is in [2026-10-22, 2026-11-01], as a set. "Named by an intent" = ∃ entry of Kind `intent` at 0b3075182 whose block text contains the ID as a D3 token. Count IDs with none. Variants: named by an entry of any Kind; named only via an intent's `Dispatch-file` field. Claim: 127.

**F11.** S_F = set of D1 IDs in Forager RECORD.md at 0b3075182; S_f = set of D1 IDs in forager-forecast RECORD.md at 98d4b33a6f34985732aecf9a6b35dae28545db44. Report |S_F ∩ S_f|, its members, whether it equals {2026-09-28-2001 … -2043}, and for each member whether the Forager and forecast entries differ in Kind or Title. Claim: 43.

**F12 (pattern counts, my own patterns).** Over F6 entries; T = block text; matching case-insensitive. Unless stated, the figure is "entries matching".
  a. verify-first / Phase 1 report: `verify[- ]?first|phase[ -]1 report`. Variant: `verify[- ]?first|phase[ -]1\b`. Claim 112.
  b. premise found wrong: on T with newlines as spaces, `premises?\b[^.]{0,150}?\b(wrong|false|fail(?:s|ed|ure)?|incorrect|not hold|no longer h[eo]ld|mistaken|untrue|disproved|corrected)\b|\b(wrong|false|incorrect|mistaken|disproved|corrected)\b[^.]{0,80}?\bpremises?\b`. Sub-count: the match span widened by 150 characters each side contains `planner|dispatch`. Claim 35; 21.
  c. revert: `\brevert`. Claim 160.
  d. `\(recommended\)`: occurrences and entries; case-sensitive `\(Recommended\)` as variant. Claim 814 across 442.
  e. against the recommendation: occurrences and entries of `(?:against|not|instead of|rather than|over|declined|rejected|overrode|overruled|overriding)\s+(?:the\s+|its\s+|my\s+|a\s+)?recommend(?:ed|ation)` or `recommend(?:ed|ation)[^.]{0,60}\b(?:not (?:taken|chosen|followed)|declined|rejected|overruled|set aside)`. Claim 4 in 3. This pattern is a guess at the wording; the figure's dependence on it will be stated.
  f. verbatim owner quote: on T with newlines kept, `\b(?:owner|operator)\b[^.\n]{0,80}\bverbatim\b|\bverbatim\b[^.\n]{0,80}\b(?:owner|operator)\b`. Variant: additionally requires `"`, `“` or `”` in the entry. Claim 585.

**F13.** Set = files directly under `prompts/preserved/` at 0b3075182 with basename matching `^2026-10-(1[7-9]|2[0-4])-.*-report\.md$` and containing `audit` or `promotion-recheck` (device checks and Phase 1 reports excluded). Verdict = first line matching `^\s*(?:#+\s*|\*\*)?Verdict\b[^:\n]{0,60}:\s*(.+)` (case-insensitive); value = group 1, trailing `**` stripped, cut at the first `.` or `(`, whitespace collapsed, lowercased. Count files, and files whose value is exactly `pass with items`; files with no verdict line reported. Variant: every `*-report.md` in the date range, each with its verdict or "none". Claim: 11 files, 11 "pass with items".

**F14.** (a) Presence of the line `**ID:** 2026-09-28-1342` in `4176f988:RECORD.md`, `8f8426e38^:RECORD.md`, `8f8426e38:RECORD.md`, `0b3075182:RECORD.md`; count of entries at 0b3075182 whose text contains `-1342` as a token `(?<![\d-])-?1342(?!\d)` preceded by `2026-09-28-` or a bare hyphen ("still cited"). (b) For N in 1963..1967: presence of `**ID:** 2026-09-28-N` in `8900e8843^:RECORD.md`, `8900e8843:RECORD.md`, `0b3075182:RECORD.md`; whether the Title/Kind at 8900e8843^ and at 0b3075182 differ (reused); the first commit writing each, by `git log --format=%h -S'**ID:** 2026-09-28-N' 8900e8843 -- RECORD.md`.

## Disclosures for Phase 1

- Confirmed: all format facts above were read at the named commits. Inferred: that readers' "Prediction field" meant the field forms admitted by F3's primary rule (RECORDING.md names two of them); that figure 10's "dispatch IDs" are preserved-prompt filename prefixes (the records branch holds them, pre-main does not).
- Could not determine before counting: which date convention the earlier counts used for figure 9 (D6 fixes mine); which file set figure 13 used (F13 fixes mine, and the brief's first and last filenames fall inside it).
- Premises in the brief checked: all six commits exist and are what the brief says (dates 2026-10-16/18, 2026-11-02 ×2, 2026-11-05 ×2). `prompts/preserved/` for 10-22..11-01 is absent on pre-main 6e24b22c4, so "pre-main" is not an input to any count here.
- Decided beyond scope: none. I computed no claimed figure; listing filenames and distinct Kind labels enumerated inputs without tallying them.
- Observed, not asked: the brief's own correct-count for figure 9b implies 2,200 non-merge commits in D7; the record header at 0b3075182 still says "Twelve entry types are in use" while fifteen labels appear.

Stopping here as instructed. Tell me to go on and I will run exactly these rules.
