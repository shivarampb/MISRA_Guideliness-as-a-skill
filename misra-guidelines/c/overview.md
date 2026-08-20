# MISRA C:2023 — Overview

MISRA C:2023 is the third edition of the MISRA C guidelines. It consolidates
**MISRA C:2012** with **Amendments 1–4** and the **Technical Corrigenda** into a
single document, and covers the **C90, C99, C11 and C18** language editions.

- **~221 guidelines total** ≈ **~21 directives** + **~200 rules**.
- Each guideline has a **category** and a **decidability**.
- Rules are numbered `Rule <section>.<index>`; directives `Dir <section>.<index>`.

## Categories

| Category   | Deviations                | Notes                                    |
|------------|---------------------------|------------------------------------------|
| Mandatory  | **Never** permitted       | Introduced in C:2012; violation = defect |
| Required   | Permitted, formally recorded | The bulk of the ruleset               |
| Advisory   | Permitted, recording recommended | Good practice                     |

## Rules vs. Directives

- **Rules** — compliance can be checked purely from the **source code**. Most are
  amenable to static analysis.
- **Directives** — compliance also depends on information **outside the code**
  (requirements, documentation, process). A tool alone cannot fully check them.

## Decidability

- **Decidable** — an analyser can always give a correct yes/no.
- **Undecidable** — cannot be resolved in every case; needs review, testing, or
  runtime checks.
- Analysis scope is either **Single Translation Unit** or **System** (whole
  program / all TUs linked together).

## The Essential Type Model (key concept for §10)

MISRA defines an "essential type" for every expression, independent of the C
type used to store it. The essential type categories are:

- essentially **Boolean**
- essentially **character**
- essentially **signed** integer
- essentially **unsigned** integer
- essentially **enum** (named, non-anonymous)
- essentially **floating**

Section 10 rules constrain mixing these categories and prevent implicit
conversions that silently change value or category. This model is the single
most important concept to understand when applying MISRA C.

## Deviation process (for Required/Advisory only)

A compliant project may deviate from a **Required** or **Advisory** guideline if
it records a **deviation**: the guideline ID, the rationale, the scope, and sign
-off. **Mandatory** guidelines can never be deviated. A **Guideline Compliance
Summary (GCS)** documents, for every guideline, whether the project complies,
deviates, or the guideline is disapplied.

## Section map (rules)

| §   | Topic                          | Index file                              |
|-----|--------------------------------|-----------------------------------------|
| 1   | A standard C environment       | rules/01-06-environment-and-types.md    |
| 2   | Unused code                    | rules/01-06-environment-and-types.md    |
| 3   | Comments                       | rules/01-06-environment-and-types.md    |
| 4   | Character sets & lexical        | rules/01-06-environment-and-types.md    |
| 5   | Identifiers                    | rules/01-06-environment-and-types.md    |
| 6   | Types                          | rules/01-06-environment-and-types.md    |
| 7   | Literals and constants         | rules/07-09-constants-declarations-init.md |
| 8   | Declarations and definitions   | rules/07-09-constants-declarations-init.md |
| 9   | Initialization                 | rules/07-09-constants-declarations-init.md |
| 10  | The essential type model       | rules/10-11-types-and-pointers.md       |
| 11  | Pointer type conversions       | rules/10-11-types-and-pointers.md       |
| 12  | Expressions                    | rules/12-16-expressions-and-control.md  |
| 13  | Side effects                   | rules/12-16-expressions-and-control.md  |
| 14  | Control statement expressions  | rules/12-16-expressions-and-control.md  |
| 15  | Control flow                   | rules/12-16-expressions-and-control.md  |
| 16  | Switch statements              | rules/12-16-expressions-and-control.md  |
| 17  | Functions                      | rules/17-19-functions-pointers-storage.md |
| 18  | Pointers and arrays            | rules/17-19-functions-pointers-storage.md |
| 19  | Overlapping storage            | rules/17-19-functions-pointers-storage.md |
| 20  | Preprocessing directives       | rules/20-preprocessing.md               |
| 21  | Standard libraries             | rules/21-22-libraries-and-resources.md  |
| 22  | Resources                      | rules/21-22-libraries-and-resources.md  |

Directives live in `directives.md`.

> `⚑verify` on an entry means: check the ID/category against the official
> standard before using it in a formal compliance record — it was added or
> changed by an amendment and public reconstructions vary.
