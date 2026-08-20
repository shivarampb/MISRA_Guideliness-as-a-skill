# MISRA C:2023 — Rules §1–§6

Format: `Rule S.N — (Category, Decidability)`. Summaries are paraphrased.

## §1 — A standard C environment

- **Rule 1.1** — *(Required, Decidable, System)* — The program must contain no
  violations of the standard C syntax and constraints, and must not exceed the
  implementation's translation limits.
- **Rule 1.2** — *(Advisory, Undecidable, System)* — Language extensions should
  not be used.
- **Rule 1.3** — *(Required, Undecidable, System)* — There must be no occurrence
  of undefined or critical unspecified behaviour.
- **Rule 1.4** — *(Required, Decidable, Single TU)* ⚑verify — Emergent language
  features (e.g. `_Generic`, `_Atomic`, `_Noreturn`, `<threads.h>`) must not be
  used. *(AMD2, C11/C18)*
- **Rule 1.5** — *(Required)* ⚑verify — Obsolescent language features must not be
  used. *(AMD3)*

## §2 — Unused code

- **Rule 2.1** — *(Required, Undecidable, System)* — A project must not contain
  unreachable code.
- **Rule 2.2** — *(Required, Undecidable, System)* — There must be no dead code
  (operations whose removal cannot affect program behaviour).
- **Rule 2.3** — *(Advisory, Decidable, System)* — A project should not contain
  unused type declarations.
- **Rule 2.4** — *(Advisory, Decidable, System)* — A project should not contain
  unused tag declarations.
- **Rule 2.5** — *(Advisory, Decidable, System)* — A project should not contain
  unused macro declarations.
- **Rule 2.6** — *(Advisory, Decidable, Single TU)* — A function should not
  contain unused label declarations.
- **Rule 2.7** — *(Advisory, Decidable, Single TU)* — There should be no unused
  parameters in functions.
- **Rule 2.8** — *(Advisory, Decidable, System)* ⚑verify — A project should not
  contain unused object definitions. *(AMD)*

## §3 — Comments

- **Rule 3.1** — *(Required, Decidable, Single TU)* — The character sequences
  `/*` and `//` must not be used within a comment.
- **Rule 3.2** — *(Required, Decidable, Single TU)* — Line-splicing (`\` at end
  of line) must not be used in `//` comments.

## §4 — Character sets and lexical conventions

- **Rule 4.1** — *(Required, Decidable, Single TU)* — Octal and hexadecimal
  escape sequences must be terminated.
- **Rule 4.2** — *(Advisory, Decidable, Single TU)* — Trigraphs should not be
  used.

## §5 — Identifiers

- **Rule 5.1** — *(Required, Decidable, System)* — External identifiers must be
  distinct (within the implementation's significant-character limit).
- **Rule 5.2** — *(Required, Decidable, Single TU)* — Identifiers declared in the
  same scope and name space must be distinct.
- **Rule 5.3** — *(Required, Decidable, Single TU)* — An identifier in an inner
  scope must not hide one in an outer scope.
- **Rule 5.4** — *(Required, Decidable, Single TU)* — Macro identifiers must be
  distinct.
- **Rule 5.5** — *(Required, Decidable, Single TU)* — Identifiers must be distinct
  from macro names.
- **Rule 5.6** — *(Required, Decidable, System)* — A `typedef` name must be a
  unique identifier.
- **Rule 5.7** — *(Required, Decidable, System)* — A tag name must be a unique
  identifier.
- **Rule 5.8** — *(Required, Decidable, System)* — Identifiers with external
  linkage that define objects/functions must be unique.
- **Rule 5.9** — *(Advisory, Decidable, System)* — Identifiers with internal
  linkage that define objects/functions should be unique.

## §6 — Types

- **Rule 6.1** — *(Required, Decidable, Single TU)* — Bit-fields must only be
  declared with an appropriate type.
- **Rule 6.2** — *(Required, Decidable, Single TU)* — Single-bit named bit-fields
  must not be of a signed type.
- **Rule 6.3** — *(Required, Decidable, Single TU)* ⚑verify — A bit-field must not
  be declared as a member of a union. *(AMD)*
