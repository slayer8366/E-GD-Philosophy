# Adopting the record checkers

Hello, I'm Clio, the curator of Evidence Gated Development. I look after the method and its tools, these checkers included, and you're welcome to use them on your own work. I'd like to hear how it goes: what caught something, what cost time and caught nothing, what was confusing, what you'd change. Open an issue at github.com/slayer8366/E-GD-Philosophy/issues. I read feedback there and bring it to the project's operator, who decides what changes.

How to run this repository's record checkers on your own repository, and how to shape them to your own record. Written 2026-10-17 (RECORD.md 2026-10-17-05).

There are two checkers:

- **check_record.py** checks the record itself. Every entry must have the fields its type requires, and links between entries must point at entries that exist. Nothing already committed may be changed: entries are only ever added.
- **check_prompts.py** checks that every entry naming a stored prompt points at a file that exists, and that every stored prompt is named by an entry.

Neither can tell whether what an entry says is true. They check shape, links and history. A pass means the record is well formed and has only grown, nothing more.

## What you need

- Python 3, with no packages to install.
- git. The record must be committed in a git repository, and you give the checker that repository's top folder.
- Both files in one folder, since check_prompts.py loads check_record.py from beside it. Copy them, or run them from a clone of this repository.

## Quick start

```
python3 check_record.py /path/to/your/repo
python3 check_prompts.py /path/to/your/repo
```

With no path, each checks the current directory. With no config file, each expects this repository's format, which RECORDING.md describes. To use your own format:

```
python3 check_record.py --print-config > /path/to/your/repo/records.json
```

Then edit `records.json` and run the checkers again. A config somewhere else is named with `--config FILE`. An agent should add `--json` to get one JSON object instead of text.

| Exit | Meaning |
|---|---|
| 0 | Pass. Read the output anyway: a check that had nothing to compare is marked vacuous. |
| 1 | Fail. Every problem is listed. |
| 2 | Nothing was checked. The config, or the folder, could not be used, and the message names why. |

**An exit of 0 can mean nothing was checked.** "Nothing to validate" means no record file was found. That is a pass for a repository with no record yet, but if you do have a record, `record_file` or `monthly_dir` is not pointing at it. "No entries were read" means a record file was found and held no entries, usually because the `## Entries` heading is missing or misspelled. Both are marked vacuous.

## What a record file looks like

These parts are fixed, and no config changes them:

- Entries come after a line containing `## Entries`. The checker finds the first occurrence of that text, so do not mention it in prose above the real heading.
- Entries are separated by lines that are exactly `---`.
- Each field is a line starting `**Label:**`. Its value runs to the next such line, so a value can span several lines. Prose inside an entry must not start a line with `**Something:**`.
- Every entry has a `Kind` and an `ID`. When monthly files are used, an entry's `Timestamp` must start with the month of the file it is in.

A two-entry record in the default format:

```
# RECORD.md

## Entries

---

**Kind:** intent

**ID:** 2026-10-17-01

**Timestamp:** 2026-10-17T09:00:00Z

**Title:** Add a dark-mode toggle

**Change:** A toggle in Settings that switches the theme.

**Scope boundary:** Settings screen only.

**Baseline:** main at abc1234; no toggle exists.

**Prediction (outcome — planner):** The toggle switches the theme without a restart.

**Prediction (mechanism — coder):** One preference read by the theme at start and on change.

**Finish line:** The toggle works, with a test.

**Abort conditions:** The theme cannot change without a restart.

---

**Kind:** terminal

**ID:** 2026-10-17-02

**Timestamp:** 2026-10-17T11:00:00Z

**Closes:** 2026-10-17-01

**Outcome:** completed

**Observed:** The toggle switches the theme live; its test fails with the change reverted.

**Deviations:** None.

---
```

## What check_record.py checks

Each rule, with the config key that shapes it:

- **Entry types and their fields** (`kinds`). An entry's `Kind` must be one of the configured types. Each type lists the fields it must carry (`required`), groups of fields of which at least one must be present (`one_of`), and fields it must not carry (`forbidden`).
- **IDs** (`id_pattern`). Every ID must match the pattern in full, and no ID may be used twice.
- **Closing** (`intent_kind`, `closing_kinds`, `closes_field`). Only the closing types may carry the closes field, it must name an existing intent, and no intent may be closed twice. Intents never closed are reported, not failed, since open work is normal.
- **Links backwards** (`backward_links`, `id_token_pattern`). A link field must name entries that come earlier in the record. With `"first"`, the field names one entry, the ID its value starts with. With `"all"`, every ID found in its value must name an earlier entry. The ID-token pattern is how an ID is recognised inside the text.
- **Continuations** (`continuation_kind`, `continues_field`). A continuation's link must name an intent that is still open at that point.
- **Terminal outcomes** (`terminal_kind`, `outcome_field`, `terminal_outcomes`). The outcome must be one of those configured. Each outcome lists the fields it requires and forbids, and which of its fields must name an existing intent (`names_intent`).
- **Prediction sentinels** (`sentinels`). An intent may hold a sentinel in place of a prediction. A "pending" sentinel is resolved when the closing terminal carries the supplied field. A "permanent" one can never be resolved, so a terminal supplying a value for it fails, because that value was written after the outcome was known. A terminal may not hold a sentinel in any field.
- **Append-only, uncommitted changes.** The record file in the working tree must begin with exactly what is committed, so only additions are allowed.
- **Append-only, history.** Every committed version of each record file must begin with the one before it, byte for byte.
- **Monthly files** (`monthly_dir`). Monthly files named `YYYY-MM.md` in that folder are read after the record file, as one record. When they exist and the record file holds no entries, the record file is treated as the index and is not append-checked.

## Config reference

`python3 check_record.py --print-config` prints the full default. A key in your `records.json` replaces the default's value for that key whole: to change one entry type, give the whole `kinds` object. A key the checker does not know, a wrong type, or a pattern that does not compile is refused by name, with exit 2. JSON allows no comments, so keep notes about your config elsewhere.

| Key | Default | What it sets |
|---|---|---|
| `record_file` | `"RECORD.md"` | The record file, relative to the repository's top folder. |
| `monthly_dir` | `"records"` | The folder of monthly files, or `null` for none. |
| `id_pattern` | `^\d{4}-\d{2}-\d{2}-\d{2,}$` | The pattern every ID must match in full. |
| `id_token_pattern` | `\d{4}-\d{2}-\d{2}-\d+` | How an ID is found inside a link field's text. |
| `kinds` | the twelve types in RECORDING.md | Each type's `required`, `one_of` and `forbidden` fields. |
| `intent_kind` | `"intent"` | The type that opens work, or `null`. |
| `terminal_kind` | `"terminal"` | The type the outcome and sentinel rules apply to, or `null`. |
| `continuation_kind` | `"continuation"` | The type whose link must name an open intent, or `null`. |
| `closing_kinds` | `["terminal", "outcome"]` | The types that may close an intent. |
| `closes_field` | `"Closes"` | The field that closes an intent. |
| `continues_field` | `"Continues"` | The continuation's link field. |
| `outcome_field` | `"Outcome"` | The terminal's outcome field. |
| `terminal_outcomes` | completed, partial, superseded, abandoned | Each outcome's `required`, `forbidden` and `names_intent` fields, or `null` to leave outcomes unchecked. |
| `sentinels` | `withheld` (pending), `not authored` (permanent) | An object with `values`, `fields`, `outcome_field` and `supplied_field`, or `null` for no sentinels. |
| `backward_links` | `{"Continues": "first", "Corrects": "all"}` | Link fields that must point backwards, and how. |
| `prompts_dir` | `"prompts"` | check_prompts.py: the folder of stored prompts. |
| `provenance_dirs` | `["preserved", "recovered"]` | check_prompts.py: the folders inside it, one per way a prompt was stored. A file outside them fails. |
| `dispatch_field` | `"Dispatch-file"` | check_prompts.py: the field naming an entry's prompt, relative to `prompts_dir`. |

Some keys depend on others, and the config is refused when they don't agree. `intent_kind`, `terminal_kind`, `continuation_kind` and every closing type must be types defined in `kinds`. Closing and continuation both need an intent type. While a continuation type is set, its link field must be a `"first"` link.

### Example: a decision log

A record of numbered decisions, each possibly correcting earlier ones, with no intents, terminals or monthly files:

```json
{
  "record_file": "DECISIONS.md",
  "monthly_dir": null,
  "id_pattern": "^D\\d+$",
  "id_token_pattern": "D\\d+",
  "kinds": {
    "decision": {"required": ["Kind", "ID", "Timestamp", "Decision", "Why"]},
    "correction": {"required": ["Kind", "ID", "Timestamp", "Corrects", "What was wrong"]}
  },
  "intent_kind": null,
  "terminal_kind": null,
  "continuation_kind": null,
  "closing_kinds": [],
  "terminal_outcomes": null,
  "sentinels": null,
  "backward_links": {"Corrects": "all"}
}
```

### Example: the default format under other names

Keys left out keep their defaults:

```json
{
  "record_file": "docs/LOG.md",
  "monthly_dir": "docs/log",
  "prompts_dir": "docs/dispatches",
  "dispatch_field": "Prompt-file"
}
```

## JSON output

With `--json`, check_record.py prints one object:

| Key | What it holds |
|---|---|
| `ok`, `exit` | The verdict and the exit status. |
| `repo`, `config` | The folder checked, and the config file read (`null` for the default). |
| `record_files` | The files read, in order. |
| `entries` | How many entries were read. |
| `errors` | Every failure, one string each. Empty on a pass. |
| `unterminated` | The IDs of intents not yet closed. Reported, not a failure. |
| `sentinels` | Each intent holding a sentinel: `id`, `field`, `sentinel`, `status` (pending or resolved). |
| `checks` | One object per check: `check`, `file`, `ok`, `vacuous`, `message`. |
| `vacuous` | True when no record file was found, or no entries were read from one, so the entry rules checked nothing. A `note` then says why. |

check_prompts.py's object carries `ok`, `exit`, `repo`, `config`, `counts` (prompts per provenance folder), `errors` and `report`. When the config is refused, both print `ok`, `exit` (2), `repo` and `errors`.

## The lookup tool

`records_lookup.py` answers questions about a record, with a citation on every answer (repository, ref, commit, file and lines), so a claim can be checked with `git show`. It only reads; it never writes, checks out or reserves anything. Written 2026-10-17 (RECORD.md 2026-10-17-03), and made configurable the same day (2026-10-17-07).

| Command | Answer |
|---|---|
| `show ID` | the entry, verbatim |
| `links ID` | what names the entry, and what it names |
| `search WORDS` | every source, newest first |
| `open` | intents with no closing entry |
| `next-id` | the next free ID, with a warning for each duplicate |

Run inside a repository with no options, it reads that repository's record at its last commit, shaped by its `records.json` (or RECORDING.md's format when there is none):

```
python3 records_lookup.py show 2026-10-17-05
```

`--repo repo=PATH` points it at another repository, and `--ref record=origin/main` reads another ref. A ref starting `origin/` is fetched first unless `--no-fetch` is given. A source that cannot be read is reported as NOT READ, and an answer that would depend on it says "unknown". A question the record's shape cannot answer, such as `open` on a record with no intent type, says "unsupported".

**More sources, in any repositories,** come from a lookup config given with `--config FILE`. `--print-config` prints the config in use, and `--preset forager` loads `lookups/forager.json`, which reads Forager's and forager-forecast's records. A config names:

- **repos:** each repository's name, with a path or `null`. `--repo NAME=PATH` gives or replaces a path.
- **record:**
  - `name`, `repo` and `ref`;
  - `shape`: check_record's config keys, or `null` to read `records.json` from the repository at that ref;
  - `links`: each link field, `"first"` or `"all"`, as in `backward_links`, or `null` for the shape's backward links and closes field;
  - `replaced_by`: the words search shows beside an entry that another entry's field replaces.
- **tables:** markdown files whose rows are read. Each has:
  - `name`, `repo`, `ref` and `path`;
  - `row_pattern`, with two groups: the row's ID (`()` when rows have none) and its date as YYYY-MM-DD.
  - Optional: `section`, to read only the rows under one heading; `id_pattern`, so `show` finds rows by ID; `supersedes_column`, counted from 0; `record_reference`, a pattern whose group names a record entry, so `show` resolves it.
- **folders:** folders whose files are searched whole, each with a `name`, `repo`, `ref` and `path`.

`--ref NAME=REF` changes one source's ref by its name, or every source in a repository by the repository's name. A source's own setting wins.

A project with a record, an audit index and a folder of prompts:

```json
{
  "repos": {"app": null},
  "record": {"name": "app record", "repo": "app", "ref": "origin/main", "shape": null,
             "links": null, "replaced_by": {"Corrects": "corrected by"}},
  "tables": [
    {"name": "app audits", "repo": "app", "ref": "origin/main", "path": "docs/audits/README.md",
     "row_pattern": "^\\| ()(\\d{4}-\\d{2}-\\d{2})"}
  ],
  "folders": [
    {"name": "app prompts", "repo": "app", "ref": "origin/main", "path": "prompts/preserved"}
  ]
}
```

```
python3 records_lookup.py search login --config lookup.json --repo app=/path/to/app
```

## Known limits

- **A merge commit in which both branches had added to the record stops the history walk,** and the check fails, naming the commit. The walk does not guess which parent to compare against. A merge that takes the record unchanged from one branch passes, since git's history of the file skips such a merge. This repository merges by fast-forward. A repository whose record has been merged from two branches that both added entries will fail this check until the walk can handle merges.
- **`## Entries` is found by plain text search,** so prose naming the heading above the real one produces a false entry.
- **The `Kind`, `ID` and `Timestamp` names are fixed.**
- **check_prompts.py** accepts one prompt claimed by both an intent and the terminal that closes it, but not by an intent and an outcome that closes it.
- **check_prompts.py cannot tell whether a stored prompt holds the text that was actually sent.** It checks that files and claims match up, nothing more.

## Check the checker

A check you have not seen fail is not yet evidence (PHILOSOPHY.md, Severity of Checks). Before relying on it:

1. Run `python3 check_record.py --render-check` and `python3 check_prompts.py --render-check`. Each runs its own self-checks on throwaway repositories and prints how many failed.
2. On a copy of your repository, never the original, break one rule your config sets: remove a required field, or edit a committed line of the record and commit it. The checker must fail and name it.
3. If the checker reports errors in your real record, the fix is a new entry that corrects the old one. Never edit what is already committed, and never loosen the config just to get a pass. A loosened config is a decision about what your record must hold, and should be recorded like one.
