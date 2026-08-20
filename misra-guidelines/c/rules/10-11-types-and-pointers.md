# MISRA C:2023 — Rules §10–§11

Format: `Rule S.N — (Category, Decidability)`. Summaries are paraphrased.
See `../overview.md` for the essential type model that §10 relies on.

## §10 — The essential type model

- **Rule 10.1** — *(Required, Decidable, Single TU)* — Operands must not be of an
  inappropriate essential type for the operator.
- **Rule 10.2** — *(Required, Decidable, Single TU)* — Expressions of essentially
  character type must not be used inappropriately in `+` and `-` operations.
- **Rule 10.3** — *(Required, Decidable, Single TU)* — The value of an expression
  must not be assigned to an object with a narrower essential type or a different
  essential type category.
- **Rule 10.4** — *(Required, Decidable, Single TU)* — Both operands of an
  operator using the usual arithmetic conversions must have the same essential
  type category.
- **Rule 10.5** — *(Advisory, Decidable, Single TU)* — The value of an expression
  should not be cast to an inappropriate essential type.
- **Rule 10.6** — *(Required, Decidable, Single TU)* — The value of a composite
  expression must not be assigned to an object with wider essential type.
- **Rule 10.7** — *(Required, Decidable, Single TU)* — If a composite expression
  is one operand of an operator using the usual arithmetic conversions, the other
  operand must not have wider essential type.
- **Rule 10.8** — *(Required, Decidable, Single TU)* — The value of a composite
  expression must not be cast to a different essential type category or a wider
  essential type.

## §11 — Pointer type conversions

- **Rule 11.1** — *(Required, Decidable, Single TU)* — Conversions must not be
  performed between a pointer to a function and any other type.
- **Rule 11.2** — *(Required, Decidable, Single TU)* — Conversions must not be
  performed between a pointer to an incomplete type and any other type.
- **Rule 11.3** — *(Required, Decidable, Single TU)* — A cast must not be
  performed between a pointer to object type and a pointer to a different object
  type.
- **Rule 11.4** — *(Advisory, Decidable, Single TU)* — A conversion should not be
  performed between a pointer to object and an integer type.
- **Rule 11.5** — *(Advisory, Decidable, Single TU)* — A conversion should not be
  performed from pointer to `void` into pointer to object.
- **Rule 11.6** — *(Required, Decidable, Single TU)* — A cast must not be
  performed between pointer to `void` and an arithmetic type.
- **Rule 11.7** — *(Required, Decidable, Single TU)* — A cast must not be
  performed between pointer to object and a non-integer arithmetic type.
- **Rule 11.8** — *(Required, Decidable, Single TU)* — A cast must not remove any
  `const` or `volatile` qualification from the type pointed to by a pointer.
- **Rule 11.9** — *(Required, Decidable, Single TU)* — The macro `NULL` must be
  the only permitted form of integer null pointer constant.
- **Rule 11.10** — *(Required)* ⚑verify — The `_Atomic` qualifier must not be
  applied to the incomplete type `void`. *(AMD3, C11)*
