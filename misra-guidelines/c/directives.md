# MISRA C:2023 — Directives

Directives require information **beyond the source code** (requirements,
documentation, build process) to check. Format: `Dir S.N — (Category, Decidability)`.

## Dir 1 — The implementation

- **Dir 1.1** — *(Required, Undecidable, System)* — Any implementation-defined
  behaviour the program's output depends on must be documented and understood.
- **Dir 1.2** — *(Advisory)* ⚑verify — Language extensions should be documented
  and understood.

## Dir 2 — Compilation and build

- **Dir 2.1** — *(Required, Undecidable, System)* — All source files must compile
  without any compilation errors.

## Dir 3 — Requirements traceability

- **Dir 3.1** — *(Required, Undecidable, System)* — All code must be traceable to
  documented requirements.

## Dir 4 — Code design

- **Dir 4.1** — *(Required, Undecidable, System)* — Run-time failures must be
  minimized.
- **Dir 4.2** — *(Advisory, Undecidable, Single TU)* — All use of assembly
  language should be documented.
- **Dir 4.3** — *(Required, Decidable, Single TU)* — Assembly language must be
  encapsulated and isolated.
- **Dir 4.4** — *(Advisory, Undecidable, Single TU)* — Sections of code should
  not be "commented out".
- **Dir 4.5** — *(Advisory, Undecidable, System)* — Identifiers in the same name
  space with overlapping visibility should be typographically unambiguous.
- **Dir 4.6** — *(Advisory, Undecidable, Single TU)* — `typedef`s that indicate
  size and signedness should be used in place of the basic numerical types.
- **Dir 4.7** — *(Required, Undecidable, Single TU)* — If a function returns
  error information, that error information must be tested.
- **Dir 4.8** — *(Advisory, Undecidable, Single TU)* — If a pointer to a struct
  or union is never dereferenced within a TU, its implementation should be hidden.
- **Dir 4.9** — *(Advisory, Undecidable, Single TU)* — A function should be
  preferred over a function-like macro where they are interchangeable.
- **Dir 4.10** — *(Required, Decidable, Single TU)* — Precautions must be taken to
  prevent a header file's contents being included more than once (include guards).
- **Dir 4.11** — *(Required, Undecidable, Single TU)* — The validity of values
  passed to library functions must be checked.
- **Dir 4.12** — *(Required, Undecidable, Single TU)* — **Dynamic memory
  allocation must not be used.**
- **Dir 4.13** — *(Advisory, Undecidable, Single TU)* — Functions that operate on
  a resource should be called in an appropriate sequence.
- **Dir 4.14** — *(Required, Undecidable, Single TU)* — The validity of values
  received from external sources must be checked. *(added by AMD1 — security)*
- **Dir 4.15** — *(Required, Undecidable, Single TU)* ⚑verify — Evaluation of
  floating-point expressions must not lead to the undetected generation of
  infinities and NaNs. *(AMD3)*

## Later directive sections *(C:2023 amendments)* ⚑verify

Public reconstructions report additional directive sections in C:2023 (the
published total is ~21 directives across ~5 sections, versus 17 in the original
C:2012). Notably a **concurrency** directive area (e.g. `Dir 5.x`) is associated
with the C11 threading additions. **Confirm the exact IDs, titles, and
categories of any `Dir 5.x` guidelines against the official MISRA C:2023
document** before citing them.
