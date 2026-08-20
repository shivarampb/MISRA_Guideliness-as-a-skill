# MISRA C++:2023 — Rules (in depth, representative set)

> **Status:** a **well-established, representative subset** of the C++:2023 rules,
> grouped under the C++ standard areas they belong to, each with rationale and
> compliant/non-compliant C++. Every entry is `⚑verify` — the guidance reflects
> long-standing MISRA C++ / AUTOSAR C++14 practice, but the **exact rule IDs,
> categories, and wording of MISRA C++:2023 must be confirmed against the
> official document**. See `../overview.md` for how to complete this to all 175.

---

## Lexical conventions

### Comments must not nest — *(Required)* ⚑verify
```cpp
/* a /* b */ c;   // Non-compliant: 'c;' is live code, not a comment
```

### Literal suffixes must be uppercase — *(Required)* ⚑verify
```cpp
auto n = 100l;    // Non-compliant: looks like 1001
auto n = 100L;    // Compliant
```

---

## Basic concepts (declarations, scope, ODR, lifetime)

### One Definition Rule — *(Required)* ⚑verify
Every entity must have exactly one definition across the program.

### Objects must be initialized before use — *(Mandatory)* ⚑verify
```cpp
int x; use(x);        // Non-compliant: indeterminate
int x{0}; use(x);     // Compliant
```

### Declare in the narrowest scope — *(Advisory)* ⚑verify
Declare variables close to first use; prefer initialization at declaration.

### Avoid the static init-order fiasco — *(Required)* ⚑verify
Cross-TU dependencies between namespace-scope objects with dynamic initialization
must be avoided (use function-local statics / Meyers singleton).

---

## Standard conversions

### No implicit narrowing — *(Required)* ⚑verify
```cpp
int i = 300; char c = i;    // Non-compliant: narrowing
char c{ static_cast<char>(i) };  // Compliant: explicit + braces catch constants
```

### Do not cast away const/volatile — *(Required)* ⚑verify
```cpp
const int a = 1; int& r = const_cast<int&>(a);  // Non-compliant
```

---

## Expressions

### Make precedence explicit — *(Advisory)* ⚑verify
```cpp
x = a + b << c;      // Non-compliant
x = (a + b) << c;    // Compliant
```

### Do not use the comma operator — *(Advisory)* ⚑verify

### Use named casts, never C-style casts — *(Required)* ⚑verify
```cpp
double d = (double)i;                 // Non-compliant
double d = static_cast<double>(i);    // Compliant
```

### Avoid `reinterpret_cast` / `const_cast` — *(Required/Advisory)* ⚑verify

### `sizeof` operand must have no side effects — *(Mandatory)* ⚑verify
```cpp
n = sizeof(a[i++]);   // Non-compliant: i++ not evaluated
```

---

## Statements (control flow)

### Bodies must be compound statements — *(Required)* ⚑verify
```cpp
if (x) y = 1;         // Non-compliant
if (x) { y = 1; }     // Compliant
```

### `if...else if` must end with `else` — *(Required)* ⚑verify

### `switch` must have `default`; clauses end with `break` — *(Required)* ⚑verify
```cpp
switch (k) {
  case 1: v = 1; break;
  default: v = 0; break;   // Compliant
}
```

### `goto` should not be used — *(Advisory)* ⚑verify

### Loop counter must not be floating — *(Required)* ⚑verify

---

## Declarations

### Prefer `const`/`constexpr` — *(Advisory)* ⚑verify
```cpp
constexpr int kMax = 100;   // Compliant
```

### `auto` must not obscure type/safety — *(Advisory)* ⚑verify

---

## Declarators (pointers, references, functions)

### Non-void function must return on all paths — *(Mandatory)* ⚑verify
```cpp
int f(int x){ if (x) return 1; }   // Non-compliant: falls off end
```

### Pointer arithmetic stays within one array — *(Required)* ⚑verify

### Address of automatic object must not escape — *(Required)* ⚑verify
```cpp
int* g;
void f(){ int local{0}; g = &local; }   // Non-compliant: dangling
```

### Functions should not be recursive — *(Required)* ⚑verify

---

## Classes & special member functions

### Rule of 0/3/5 — *(Required)* ⚑verify
A class managing a resource must define (or `= delete`) destructor, copy, and move
operations consistently; otherwise default them all.
```cpp
struct Bad { int* p; ~Bad(){ delete p; } };   // Non-compliant: copy = double free
```

### Polymorphic base needs virtual/protected destructor — *(Required)* ⚑verify
```cpp
struct Base { virtual ~Base() = default; };   // Compliant
```

### Data members should be private — *(Advisory)* ⚑verify

### Single-argument constructors should be `explicit` — *(Required)* ⚑verify
```cpp
struct S { explicit S(int); };   // Compliant: no implicit conversions
```

---

## Derived classes & inheritance

### Mark overrides `override` — *(Required)* ⚑verify
```cpp
struct D : Base { void f() override; };   // Compliant
```

### Do not redefine a virtual's default arguments — *(Required)* ⚑verify

### Avoid multiple inheritance of non-interface bases — *(Advisory)* ⚑verify

---

## Overloading

### Overloaded operators keep conventional semantics — *(Required)* ⚑verify
(e.g. `operator==` is symmetric and side-effect-free.)

### Provide/replace `new`/`delete` consistently — *(Required)* ⚑verify

---

## Templates

### A template must be valid for every allowed instantiation — *(Required)* ⚑verify

### Explicit specializations declared before first use — *(Required)* ⚑verify

---

## Exception handling

### Do not let exceptions escape `noexcept`/destructors — *(Required)* ⚑verify
```cpp
~Widget() noexcept { /* must not throw */ }
```

### Catch exceptions by (const) reference — *(Required)* ⚑verify
```cpp
try { /*...*/ } catch (const std::exception& e) { /*...*/ }   // Compliant
try { /*...*/ } catch (std::exception e) { }                  // Non-compliant: slicing
```

### `throw;` (rethrow) only inside a `catch` — *(Required)* ⚑verify

---

## Dynamic memory & resources

### Constrain dynamic allocation; use RAII — *(Required)* ⚑verify
```cpp
auto p = std::make_unique<Widget>();   // Compliant: ownership is clear
Widget* p = new Widget();              // Non-compliant: manual delete required
```

### Avoid raw owning pointers — *(Advisory)* ⚑verify

---

## Preprocessor

### Prefer inline/`constexpr` over function-like macros — *(Advisory)* ⚑verify
```cpp
#define SQ(x) ((x)*(x))                        // Non-compliant (advisory)
constexpr int sq(int x){ return x * x; }       // Compliant
```

### Parenthesise macro parameters — *(Required)* ⚑verify

### Well-formed `#include` operands — *(Required)* ⚑verify

---

## Standard library usage

### Do not use deprecated/removed library features — *(Required)* ⚑verify

### Prefer C++ facilities over superseded C ones — *(Advisory)* ⚑verify
```cpp
std::array<int,4> a{};    // Compliant, over C array + <cstring>
```

### Call library functions with valid arguments — *(Required)* ⚑verify
