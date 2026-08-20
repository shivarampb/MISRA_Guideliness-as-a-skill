# MISRA C:2023 — Rules §17–§19

Format: `Rule S.N — (Category, Decidability)`. Summaries are paraphrased.

## §17 — Functions

- **Rule 17.1** — *(Required, Decidable, Single TU)* — The features of
  `<stdarg.h>` (`va_list` etc.) must not be used.
- **Rule 17.2** — *(Required, Undecidable, System)* — Functions must not call
  themselves, directly or indirectly (no recursion).
- **Rule 17.3** — *(Mandatory, Decidable, Single TU)* — A function must not be
  declared implicitly.
- **Rule 17.4** — *(Mandatory, Decidable, Single TU)* — All exit paths from a
  function with non-`void` return type must have an explicit `return` with an
  expression.
- **Rule 17.5** — *(Advisory, Undecidable, Single TU)* — The argument for a
  parameter declared with an array type must have an appropriate number of
  elements.
- **Rule 17.6** — *(Mandatory, Decidable, Single TU)* — An array parameter
  declaration must not contain `static` between the `[ ]`.
- **Rule 17.7** — *(Required, Decidable, Single TU)* — The value returned by a
  non-`void` function must be used.
- **Rule 17.8** — *(Advisory, Decidable, Single TU)* — A function parameter should
  not be modified.
- **Rule 17.9** — *(Mandatory)* ⚑verify — A function declared `_Noreturn` must not
  return to its caller. *(AMD2, C11)*
- **Rule 17.10** — *(Required)* ⚑verify — A function declared `_Noreturn` must
  have `void` return type. *(AMD2)*
- **Rule 17.11** — *(Advisory)* ⚑verify — A function that never returns should be
  declared `_Noreturn`. *(AMD2)*
- **Rule 17.12** — *(Advisory)* ⚑verify — A function identifier should only be
  used with a preceding `&` or a parenthesised parameter list. *(AMD3)*
- **Rule 17.13** — *(Required)* ⚑verify — A function type must not be type
  qualified. *(AMD3)*

## §18 — Pointers and arrays

- **Rule 18.1** — *(Required, Undecidable, Single TU)* — A pointer resulting from
  arithmetic on a pointer operand must address an element of the same array.
- **Rule 18.2** — *(Required, Undecidable, Single TU)* — Subtraction between
  pointers must only apply to pointers addressing elements of the same array.
- **Rule 18.3** — *(Required, Undecidable, Single TU)* — Relational operators `>`,
  `>=`, `<`, `<=` must not be applied to pointers unless they point into the same
  object.
- **Rule 18.4** — *(Advisory, Decidable, Single TU)* — The `+`, `-`, `+=`, `-=`
  operators should not be applied to an expression of pointer type.
- **Rule 18.5** — *(Advisory, Decidable, Single TU)* — Declarations should contain
  no more than two levels of pointer nesting.
- **Rule 18.6** — *(Required, Undecidable, System)* — The address of an object
  with automatic storage must not be copied to another object that persists after
  the first object ceases to exist.
- **Rule 18.7** — *(Required, Decidable, Single TU)* — Flexible array members must
  not be declared.
- **Rule 18.8** — *(Required, Decidable, Single TU)* — Variable-length array types
  must not be used.
- **Rule 18.9** — *(Required)* ⚑verify — An object with temporary lifetime's
  address must not be assigned to an object that outlives it (compound literals).
  *(AMD3)*
- **Rule 18.10** — *(Mandatory)* ⚑verify — Pointers to variably-modified array
  types must not be used. *(AMD3)*

## §19 — Overlapping storage

- **Rule 19.1** — *(Mandatory, Undecidable, System)* — An object must not be
  assigned or copied to an overlapping object.
- **Rule 19.2** — *(Advisory, Decidable, Single TU)* — The `union` keyword should
  not be used.
