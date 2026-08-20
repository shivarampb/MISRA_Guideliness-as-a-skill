# MISRA C:2023 — Rules §12–§16

Format: `Rule S.N — (Category, Decidability)`. Summaries are paraphrased.

## §12 — Expressions

- **Rule 12.1** — *(Advisory, Decidable, Single TU)* — The precedence of
  operators within expressions should be made explicit with parentheses.
- **Rule 12.2** — *(Required, Decidable, Single TU)* — The right-hand operand of a
  shift must lie in range 0 to (width in bits of the left operand − 1).
- **Rule 12.3** — *(Advisory, Decidable, Single TU)* — The comma operator should
  not be used.
- **Rule 12.4** — *(Advisory, Decidable, Single TU)* — Evaluation of constant
  expressions should not lead to unsigned integer wrap-around.
- **Rule 12.5** — *(Mandatory, Decidable, Single TU)* — The `sizeof` operator must
  not have an operand that is a function parameter declared as "array of type".
  *(AMD1)*

## §13 — Side effects

- **Rule 13.1** — *(Required, Undecidable, Single TU)* — Initializer lists must
  not contain persistent side effects.
- **Rule 13.2** — *(Required, Undecidable, System)* — The value of an expression
  and its persistent side effects must be the same under all permitted evaluation
  orders.
- **Rule 13.3** — *(Advisory, Decidable, Single TU)* — A full expression with a
  `++`/`--` should have no other potential side effects.
- **Rule 13.4** — *(Advisory, Decidable, Single TU)* — The result of an assignment
  operator should not be used.
- **Rule 13.5** — *(Required, Undecidable, Single TU)* — The right-hand operand of
  a `&&` or `||` must not contain persistent side effects.
- **Rule 13.6** — *(Mandatory, Decidable, Single TU)* — The operand of `sizeof`
  must not contain any expression with potential side effects.

## §14 — Control statement expressions

- **Rule 14.1** — *(Required, Undecidable, Single TU)* — A loop counter must not
  have essentially floating type.
- **Rule 14.2** — *(Required, Undecidable, Single TU)* — A `for` loop must be
  well-formed.
- **Rule 14.3** — *(Required, Undecidable, System)* — Controlling expressions must
  not be invariant (always true/false).
- **Rule 14.4** — *(Required, Decidable, Single TU)* — The controlling expression
  of an `if` or iteration statement must have essentially Boolean type.

## §15 — Control flow

- **Rule 15.1** — *(Advisory, Decidable, Single TU)* — The `goto` statement should
  not be used.
- **Rule 15.2** — *(Required, Decidable, Single TU)* — `goto` must jump to a label
  declared later in the same function.
- **Rule 15.3** — *(Required, Decidable, Single TU)* — Any label referenced by a
  `goto` must be in the same block or an enclosing block of the `goto`.
- **Rule 15.4** — *(Advisory, Decidable, Single TU)* — There should be no more
  than one `break`/`goto` terminating any iteration statement.
- **Rule 15.5** — *(Advisory, Decidable, Single TU)* — A function should have a
  single point of exit at the end.
- **Rule 15.6** — *(Required, Decidable, Single TU)* — The body of an iteration or
  selection statement must be a compound statement (`{ }`).
- **Rule 15.7** — *(Required, Decidable, Single TU)* — All `if ... else if`
  constructs must be terminated with an `else` statement.

## §16 — Switch statements

- **Rule 16.1** — *(Required, Decidable, Single TU)* — All `switch` statements
  must be well-formed.
- **Rule 16.2** — *(Required, Decidable, Single TU)* — A switch label must only be
  used when the most closely-enclosing compound statement is the switch body.
- **Rule 16.3** — *(Required, Decidable, Single TU)* — An unconditional `break`
  must terminate every switch-clause.
- **Rule 16.4** — *(Required, Decidable, Single TU)* — Every `switch` must have a
  `default` label.
- **Rule 16.5** — *(Required, Decidable, Single TU)* — A `default` label must be
  the first or last switch label.
- **Rule 16.6** — *(Required, Decidable, Single TU)* — Every `switch` must have at
  least two switch-clauses.
- **Rule 16.7** — *(Required, Decidable, Single TU)* — A switch-expression must
  not have essentially Boolean type.
