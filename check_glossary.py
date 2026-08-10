#!/usr/bin/env python3
"""Boundary check for the EGD document set.

Asserts the bidirectional contract stated in GLOSSARY.md:
  * every philosophy headword has a glossary row
  * every enforcement entry has a glossary row
  * every glossary row names a real headword and a real entry
  * the section recorded in the glossary matches the philosophy section
  * the enforcement entry sits under the same section as its principle

Exits nonzero on any violation. Run before commit.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXEMPT = {"Traceability of Reported Results"}  # governing; no direct entry by design


def sectioned(text, pattern):
    """Yield (section, headword) for each match, tracking the enclosing ## heading."""
    section = None
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        m = re.match(pattern, line)
        if m:
            yield section, m.group(1).strip()


def glossary_rows(text):
    rows = {}
    for line in text.splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 4 or cells[0] in ("Headword", "Marker"):
            continue
        if cells[3] not in ("Active", "Superseded"):
            continue
        rows[cells[0]] = (cells[1], cells[2])
    return rows


def main():
    phil = (HERE / "PHILOSOPHY.md").read_text()
    enf = (HERE / "ENFORCEMENT.md").read_text()
    glos = (HERE / "GLOSSARY.md").read_text()

    ph = dict((h, s) for s, h in sectioned(phil, r"^\*\*(.+?):\*\*"))
    en = dict((h, s) for s, h in sectioned(enf, r"^\*\*(.+?)\*\*$"))
    gl = glossary_rows(glos)

    fail = []

    for h in sorted(set(ph) - set(gl)):
        fail.append(f"philosophy headword missing from glossary: {h}")
    for h in sorted(set(en) - set(gl)):
        fail.append(f"enforcement entry missing from glossary: {h}")
    for h in sorted(set(gl) - set(ph)):
        fail.append(f"glossary row names no philosophy headword: {h}")
    for h in sorted(set(ph) - set(en) - EXEMPT):
        fail.append(f"philosophy headword has no enforcement entry: {h}")

    for h, (gsec, gentry) in sorted(gl.items()):
        if h in ph and ph[h] != gsec:
            fail.append(
                f"section mismatch for {h}: philosophy={ph[h]!r} glossary={gsec!r}")
        if h in ph and h in en and ph[h] != en[h]:
            fail.append(
                f"section mismatch for {h}: philosophy={ph[h]!r} enforcement={en[h]!r}")

    print(f"philosophy headwords: {len(ph)}")
    print(f"enforcement entries:  {len(en)}")
    print(f"glossary rows:        {len(gl)}")

    if fail:
        print("\nFAIL")
        for f in fail:
            print("  " + f)
        return 1
    print("\nPASS: bidirectional contract holds, sections aligned")
    return 0


if __name__ == "__main__":
    sys.exit(main())
