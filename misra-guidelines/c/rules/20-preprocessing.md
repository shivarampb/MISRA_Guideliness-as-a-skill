# MISRA C:2023 — Rules §20 (Preprocessing directives)

Format: `Rule S.N — (Category, Decidability)`. Summaries are paraphrased.

- **Rule 20.1** — *(Advisory, Decidable, Single TU)* — `#include` directives
  should only be preceded by preprocessor directives or comments.
- **Rule 20.2** — *(Required, Decidable, Single TU)* — The `'`, `"`, `\`
  characters and the `/*`, `//` sequences must not occur in a header file name.
- **Rule 20.3** — *(Required, Decidable, Single TU)* — `#include` must be followed
  by either a `<filename>` or `"filename"` sequence.
- **Rule 20.4** — *(Required, Decidable, Single TU)* — A macro must not be defined
  with the same name as a keyword.
- **Rule 20.5** — *(Advisory, Decidable, Single TU)* — `#undef` should not be used.
- **Rule 20.6** — *(Required, Decidable, Single TU)* — Tokens that look like a
  preprocessing directive must not occur within a macro argument.
- **Rule 20.7** — *(Required, Decidable, Single TU)* — Expressions resulting from
  the expansion of macro parameters must be enclosed in parentheses.
- **Rule 20.8** — *(Required, Decidable, Single TU)* — The controlling expression
  of a `#if`/`#elif` must evaluate to 0 or 1.
- **Rule 20.9** — *(Required, Decidable, Single TU)* — All identifiers in a
  `#if`/`#elif` controlling expression must be `#define`d before evaluation.
- **Rule 20.10** — *(Advisory, Decidable, Single TU)* — The `#` and `##`
  preprocessor operators should not be used.
- **Rule 20.11** — *(Required, Decidable, Single TU)* — A macro parameter
  immediately following a `#` operator must not immediately be followed by a `##`
  operator.
- **Rule 20.12** — *(Required, Decidable, Single TU)* — A macro parameter used as
  an operand to `#` or `##`, and itself subject to further macro replacement, must
  only be used as an operand to these operators.
- **Rule 20.13** — *(Required, Decidable, Single TU)* — A line whose first token
  is `#` must be a valid preprocessing directive.
- **Rule 20.14** — *(Required, Decidable, Single TU)* — All `#else`, `#elif` and
  `#endif` must reside in the same file as the `#if`/`#ifdef`/`#ifndef` they relate
  to.
