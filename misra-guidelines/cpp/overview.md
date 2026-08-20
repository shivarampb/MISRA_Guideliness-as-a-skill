# MISRA C++:2023 — Overview

MISRA C++:2023 is a **complete rewrite** of the C++ guidelines, replacing MISRA
C++:2008. It targets **ISO C++17** and aligns closely with the AUTOSAR C++14
guidelines (which it effectively absorbs and supersedes).

- **179 guidelines total** = **4 directives** + **175 rules**.
- Each guideline has a **category** and a **decidability**, same scheme as C.
- The **section numbering mirrors the ISO C++ standard's clause structure**, so a
  rule ID like `Rule 6.7.2` sits under the C++ clause on the same topic.

## Categories

Same three-tier scheme as MISRA C:

| Category   | Deviations                          |
|------------|-------------------------------------|
| Mandatory  | Never permitted                     |
| Required   | Permitted only with a formal record |
| Advisory   | Permitted; recording recommended    |

C++:2023 also classifies each guideline's analysis as **Decidable** or
**Undecidable**, and by scope (**Single Translation Unit** or **System**), just
like MISRA C.

## Guideline ID scheme

MISRA C++:2023 rules use a **three-part number** derived from the C++ standard's
clause layout: `Rule <clause>.<subclause>.<index>` (e.g. `Rule 8.2.3`).
Directives use `Dir <n>.<n>.<n>`. This differs from MISRA C's two-part
`Rule S.N` scheme — do not assume a C rule number maps to the same C++ number.

## Section structure (mirrors ISO C++17 clauses)

The rules are grouped under sections corresponding to the C++ standard, broadly:

| Area                         | Typical clause topic                                |
|------------------------------|-----------------------------------------------------|
| General / language independent | Character sets, program structure                 |
| Lexical conventions          | Identifiers, literals, comments                      |
| Basic concepts               | Declarations, scope, storage duration, ODR          |
| Standard conversions         | Implicit conversions, integral/pointer conversions  |
| Expressions                  | Operators, casts, `sizeof`, order of evaluation      |
| Statements                   | Selection, iteration, jump, `switch`                 |
| Declarations                 | `const`/`constexpr`, `auto`, type specifiers         |
| Declarators                  | Pointers, references, function declarators           |
| Classes                      | Members, access, special member functions            |
| Derived classes              | Inheritance, virtual functions                       |
| Overloading                  | Operator/function overloading, conversions           |
| Templates                    | Template parameters, instantiation, specialization   |
| Exception handling           | `throw`, `catch`, `noexcept`, stack unwinding         |
| Preprocessor                 | Macros, `#include`, conditional compilation          |
| Library introduction / usage | Use of the C++ standard library                      |

> The exact clause names, per-clause rule counts, and every rule ID must be
> confirmed against the official MISRA C++:2023 document — see the note below.

## ⚠️ Enumeration status — important

Unlike the MISRA C bundle (whose rule list is stable and long-established via
C:2012), the **verbatim per-rule identifiers of MISRA C++:2023 could not be
grounded** in this build: the authoritative reference lists are blocked by the
environment's network policy, the standard is copyright-protected, and the
reachable community sources use the *old* MISRA C++:2008 hyphenated numbering
(`5-0-1`) rather than the 2023 dotted scheme (`8.2.3`), so they are unsafe to
copy.

The `cpp/rules/` files therefore provide **comprehensive thematic coverage** —
every ISO C++17 clause area, with rationale and compliant/non-compliant examples
per guideline — but with each entry marked `⚑verify`. Treat this as a complete
**engineering reference**; treat the official standard as the authority for the
exact IDs/categories needed in a **formal compliance matrix**.

To pin the exact `Rule x.y.z` identifiers, provide **any one** of:
- the official MISRA C++:2023 PDF (place it in the repo; I'll paraphrase it), or
- a plain-text/CSV list of the rule IDs + titles, or
- an unblocked reference page listing them.
