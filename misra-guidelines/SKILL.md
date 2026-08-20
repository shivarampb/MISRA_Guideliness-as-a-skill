---
name: misra-guidelines
description: >-
  Reference index of MISRA C:2023 and MISRA C++:2023 coding guidelines. Use when
  reviewing, writing, or auditing C or C++ code for MISRA compliance; when the
  user mentions MISRA, a MISRA rule/directive ID (e.g. "Rule 8.4", "Dir 4.12"),
  or asks about safety-critical / automotive / embedded coding standards. Routes
  to a per-language, per-section index of every guideline with its ID, category
  (Mandatory/Required/Advisory), decidability, and a paraphrased summary.
---

# MISRA Guidelines (C:2023 & C++:2023)

This skill is a **reference index** of the MISRA coding guidelines. It lets you
look up any guideline by ID, tell whether a piece of code complies, and explain
*why* a rule exists. The two standards are kept in **separate bundles** because
they have different numbering schemes, categories, and scope.

## ⚠️ Copyright & accuracy notice — read once

- The **verbatim text** of MISRA guidelines is copyright © MISRA / HORIBA MIRA
  Ltd. This skill contains **paraphrased summaries only**, plus factual
  reference data (IDs, categories, decidability). It is **not** a substitute for
  the official standard, and it does not reproduce the official wording.
- Amendment-added rules (security AMD1, C11/C18 AMD2, AMD3, AMD4) and their
  categories should be **verified against the official document** before being
  cited in a formal compliance matrix. Entries that need such verification are
  marked `⚑verify`.
- Always defer to the **purchased official standard** for certification work.

## How to use this skill

1. **Identify the language.** C → load `c/`. C++ → load `cpp/`.
2. **Read the overview once** (`c/overview.md` or `cpp/overview.md`) to learn the
   category system, decidability, and the deviation process.
3. **Jump to the right section file** — don't load everything. Guidelines are
   grouped by section number, matching the official standard's chapters.
4. When asked "does this code comply with Rule X.Y?", look up X's **section
   file**, read the entry, then assess the code against the paraphrased intent.

## Quick facts

| Standard        | Year | Total | Directives | Rules | Language base        |
|-----------------|------|-------|-----------|-------|----------------------|
| MISRA C:2023    | 2023 | ~221  | ~21       | ~200  | C90 / C99 / C11 / C18|
| MISRA C++:2023  | 2023 | 179   | 4         | 175   | C++17                |

> Counts are the published 2023 totals. C:2023 consolidates MISRA C:2012 plus
> Amendments 1–4 and Technical Corrigenda into one document; C++:2023 is a full
> rewrite replacing MISRA C++:2008.

## Bundle map

### MISRA C:2023 → `c/`
- `c/overview.md` — categories, decidability, essential type model, deviations
- `c/directives.md` — all directives (Dir 1.x – Dir 4.x, plus later additions)
- `c/rules/` — rules grouped by section:
  - `01-06-environment-and-types.md` — §1 environment, §2 unused code, §3
    comments, §4 lexical, §5 identifiers, §6 types
  - `07-09-constants-declarations-init.md` — §7 literals, §8 declarations, §9
    initialization
  - `10-11-types-and-pointers.md` — §10 essential type model, §11 pointer
    conversions
  - `12-16-expressions-and-control.md` — §12 expressions, §13 side effects, §14
    control expressions, §15 control flow, §16 switch
  - `17-19-functions-pointers-storage.md` — §17 functions, §18 pointers/arrays,
    §19 overlapping storage
  - `20-preprocessing.md` — §20 preprocessing directives
  - `21-22-libraries-and-resources.md` — §21 standard libraries, §22 resources

### MISRA C++:2023 → `cpp/`
- `cpp/overview.md` — categories, decidability, section structure, C++17 scope
- `cpp/rules/` — guidelines grouped by section (numbering mirrors the ISO C++
  standard clauses)

## Category legend (both standards)

| Category   | Meaning                                                        |
|------------|---------------------------------------------------------------|
| Mandatory  | Must always be followed. **No deviations permitted.**         |
| Required   | Must be followed. Deviations allowed only with formal record. |
| Advisory   | Recommended. Deviations allowed; should still be recorded.    |

## Decidability legend

| Term        | Meaning                                                             |
|-------------|--------------------------------------------------------------------|
| Decidable   | A static analyser can always determine compliance.                 |
| Undecidable | Cannot be determined in all cases by analysis; needs review/testing.|
| Single TU / System | Scope the check needs: one translation unit, or whole program.|
