# MISRA C++:2023 — Directives

MISRA C++:2023 defines **4 directives** — guidance requiring information beyond
the source code (process, documentation, design). The exact IDs and wording
below should be confirmed against the official standard (`⚑verify`).

- **Dir (implementation behaviour)** — *(Required)* ⚑verify — Any use of
  implementation-defined behaviour on which the program's output depends must be
  documented and understood. *(analogue of MISRA C Dir 1.1)*
- **Dir (traceability)** — *(Required)* ⚑verify — Code should be traceable to
  documented requirements. *(analogue of MISRA C Dir 3.1)*
- **Dir (run-time failure)** — *(Required)* ⚑verify — Run-time failures should be
  minimized / handled. *(analogue of MISRA C Dir 4.1)*
- **Dir (documentation of design intent)** — *(Advisory)* ⚑verify — Design intent
  that cannot be expressed in code (e.g. rationale for permitted deviations,
  encapsulation choices) should be documented.

> These four map conceptually to the MISRA C directive families but the official
> C++:2023 numbering and precise text differ. Verify before formal use.
