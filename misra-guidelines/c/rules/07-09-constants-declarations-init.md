# MISRA C:2023 — Rules §7–§9

Format: `Rule S.N — (Category, Decidability)`. Summaries are paraphrased.

## §7 — Literals and constants

- **Rule 7.1** — *(Required, Decidable, Single TU)* — Octal constants must not be
  used.
- **Rule 7.2** — *(Required, Decidable, Single TU)* — A `u`/`U` suffix must be
  applied to all integer constants represented in an unsigned type.
- **Rule 7.3** — *(Required, Decidable, Single TU)* — The lowercase `l` must not
  be used in a literal suffix (use `L`).
- **Rule 7.4** — *(Required, Decidable, Single TU)* — A string literal must not be
  assigned to an object unless its type is pointer to const-qualified `char`.
- **Rule 7.5** — *(Required)* ⚑verify — An integer constant macro argument used in
  a way requiring a specific type must have that type. *(AMD3, `<stdint.h>`)*
- **Rule 7.6** — *(Required)* ⚑verify — The small integer variants of the minimum-
  width integer constant macros must not be used. *(AMD3)*

## §8 — Declarations and definitions

- **Rule 8.1** — *(Required, Decidable, Single TU)* — Types must be explicitly
  specified (no implicit `int`).
- **Rule 8.2** — *(Required, Decidable, Single TU)* — Function types must be in
  prototype form with named parameters.
- **Rule 8.3** — *(Required, Decidable, System)* — All declarations of an object
  or function must use the same names and type qualifiers.
- **Rule 8.4** — *(Required, Decidable, System)* — A compatible declaration must
  be visible when an object/function with external linkage is defined.
- **Rule 8.5** — *(Required, Decidable, System)* — An external object/function
  must be declared once in one and only one file.
- **Rule 8.6** — *(Required, Decidable, System)* — An identifier with external
  linkage must have exactly one external definition.
- **Rule 8.7** — *(Advisory, Decidable, System)* — Functions/objects should not
  have external linkage if referenced in only one TU.
- **Rule 8.8** — *(Required, Decidable, Single TU)* — `static` must be used in all
  declarations of objects/functions with internal linkage.
- **Rule 8.9** — *(Advisory, Decidable, System)* — An object should be defined at
  block scope if its identifier only appears in a single function.
- **Rule 8.10** — *(Required, Decidable, Single TU)* — An inline function must be
  declared `static`.
- **Rule 8.11** — *(Advisory, Decidable, Single TU)* — When an array with external
  linkage is declared, its size should be explicitly specified.
- **Rule 8.12** — *(Required, Decidable, Single TU)* — Within an enumerator list,
  implicitly-specified enumeration constant values must be unique.
- **Rule 8.13** — *(Advisory, Undecidable, System)* — A pointer should point to a
  const-qualified type whenever possible.
- **Rule 8.14** — *(Required, Decidable, Single TU)* — The `restrict` type
  qualifier must not be used.
- **Rule 8.15–8.17** ⚑verify — Alignment specifier rules (`_Alignas`, `_Alignof`,
  over-aligned types). *(AMD2, C11/C18)*

## §9 — Initialization

- **Rule 9.1** — *(Mandatory, Undecidable, System)* — The value of an object with
  automatic storage must not be read before it has been set.
- **Rule 9.2** — *(Required, Decidable, Single TU)* — The initializer for an
  aggregate or union must be enclosed in braces.
- **Rule 9.3** — *(Required, Decidable, Single TU)* — Arrays must not be partially
  initialized.
- **Rule 9.4** — *(Required, Decidable, Single TU)* — An element of an object must
  not be initialized more than once.
- **Rule 9.5** — *(Required, Decidable, Single TU)* — Where designated
  initializers initialize an array, the array size must be specified explicitly.
- **Rule 9.6** — *(Required)* ⚑verify — An initializer using chained designators
  must not contain initializers without designators. *(AMD3)*
- **Rule 9.7** — *(Mandatory)* ⚑verify — Atomic objects must be appropriately
  initialized before being accessed. *(AMD2/AMD3, C11)*
