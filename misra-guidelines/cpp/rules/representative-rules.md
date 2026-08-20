# MISRA C++:2023 — Rules (representative set, grouped by C++ area)

> **Status:** This file is a **well-established, representative subset** of the
> C++:2023 rules, organized under the C++ standard areas they belong to. Every
> entry is marked `⚑verify` — the guidance reflects long-standing MISRA C++ /
> AUTOSAR C++14 practice, but the **exact rule IDs, categories, and wording of
> MISRA C++:2023 must be confirmed against the official document**. See
> `../overview.md` for how to complete this to the full 175-rule index.

Format: `<paraphrased rule> — (likely Category)` ⚑verify.

## Lexical conventions (identifiers, literals, comments)

- Identifiers must not be reused across scopes in a way that shadows/hides. *(Required)* ⚑verify
- The `/*` and `//` sequences must not appear inside a comment. *(Required)* ⚑verify
- Literal suffixes must use uppercase (`L`, `U`), never lowercase `l`. *(Required)* ⚑verify
- Numeric and character escape sequences must be well-formed and terminated. *(Required)* ⚑verify

## Basic concepts (declarations, scope, ODR, storage duration)

- An object/function must have exactly one definition (ODR). *(Required)* ⚑verify
- Objects must be initialized before their value is read. *(Mandatory)* ⚑verify
- An object should be declared in the smallest scope practical. *(Advisory)* ⚑verify
- `static` storage-duration objects must be initialized without ordering hazards
  (avoid the static initialization order fiasco). *(Required)* ⚑verify

## Standard conversions

- Implicit narrowing conversions that may lose value must not occur. *(Required)* ⚑verify
- A conversion must not remove `const`/`volatile` qualification. *(Required)* ⚑verify
- Pointer-to-integer and integer-to-pointer conversions should be avoided. *(Advisory)* ⚑verify

## Expressions

- Operator precedence should be made explicit with parentheses. *(Advisory)* ⚑verify
- The comma operator should not be used. *(Advisory)* ⚑verify
- Evaluation must not depend on unspecified order of evaluation / side-effect
  ordering. *(Required)* ⚑verify
- C-style casts must not be used; use named casts (`static_cast`, etc.). *(Required)* ⚑verify
- `reinterpret_cast` and `const_cast` should be avoided. *(Advisory/Required)* ⚑verify
- `sizeof` must not be applied to an expression with side effects. *(Mandatory)* ⚑verify

## Statements (control flow)

- The body of an iteration/selection statement must be a compound statement `{ }`. *(Required)* ⚑verify
- `if ... else if` chains must end with an `else`. *(Required)* ⚑verify
- Every `switch` must have a `default`, and each clause must end with `break`. *(Required)* ⚑verify
- `goto` should not be used. *(Advisory)* ⚑verify
- A loop counter must not be of floating type. *(Required)* ⚑verify

## Declarations

- Prefer `const` / `constexpr` for values that do not change. *(Advisory)* ⚑verify
- `auto` must not obscure the type where it harms readability/safety. *(Advisory)* ⚑verify
- A variable must not be declared with an implicit type. *(Required)* ⚑verify

## Declarators (pointers, references, functions)

- A function with non-`void` return type must return a value on all paths. *(Mandatory)* ⚑verify
- Pointer arithmetic must stay within the bounds of the same array. *(Required)* ⚑verify
- The address of an automatic object must not outlive that object. *(Required)* ⚑verify
- Functions should not be recursive. *(Required)* ⚑verify

## Classes & special member functions

- A class that manages a resource must define/`delete` the special member
  functions consistently (rule of 0/3/5). *(Required)* ⚑verify
- A base class intended for polymorphic use must have a `virtual` or protected
  non-virtual destructor. *(Required)* ⚑verify
- Data members should be `private`. *(Advisory)* ⚑verify
- Constructors that can take one argument should be `explicit` unless implicit
  conversion is intended. *(Required)* ⚑verify

## Derived classes & inheritance

- Virtual overrides must be marked `override`. *(Required)* ⚑verify
- Multiple inheritance from non-interface base classes should be avoided. *(Advisory)* ⚑verify
- A virtual function's default arguments must not be redefined in overrides. *(Required)* ⚑verify

## Overloading

- Overloaded operators must preserve their conventional semantics. *(Required)* ⚑verify
- `operator new`/`operator delete` must be provided/used consistently. *(Required)* ⚑verify

## Templates

- Template definitions must not depend on ill-formed constructs for any valid
  instantiation. *(Required)* ⚑verify
- Explicit specializations must be declared before first use. *(Required)* ⚑verify

## Exception handling

- Exceptions thrown must be caught by an appropriate handler; unhandled
  propagation across defined boundaries must be prevented. *(Required)* ⚑verify
- Destructors and functions marked `noexcept` must not allow exceptions to
  escape. *(Required)* ⚑verify
- Exceptions should be caught by reference (usually `const &`). *(Required)* ⚑verify
- An empty `throw;` (rethrow) must occur only within a `catch` block. *(Required)* ⚑verify

## Dynamic memory & resources

- Dynamic memory allocation should be constrained/avoided in favour of
  deterministic allocation; when used, ownership must be clear (RAII / smart
  pointers). *(Required)* ⚑verify
- Raw owning pointers should be avoided; use `std::unique_ptr`/`std::shared_ptr`. *(Advisory)* ⚑verify

## Preprocessor

- Function-like macros should be replaced by inline/`constexpr` functions where
  interchangeable. *(Advisory)* ⚑verify
- `#include` operands must be well-formed; no `'`, `"`, `\`, `/*`, `//` in the
  header name. *(Required)* ⚑verify
- Macro parameters in the replacement list must be parenthesised. *(Required)* ⚑verify

## Standard library usage

- Deprecated/removed C++ library features must not be used. *(Required)* ⚑verify
- C standard library facilities superseded by C++ equivalents should not be used. *(Advisory)* ⚑verify
- Library functions must be called with valid arguments (bounds, ranges). *(Required)* ⚑verify
