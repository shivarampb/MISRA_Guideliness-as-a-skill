# MISRA C++:2023 — Rules (comprehensive, in depth)

> **Coverage & accuracy.** This file gives **comprehensive thematic coverage** of
> MISRA C++:2023, organized under the **ISO C++17 clause areas** the standard's
> section numbering mirrors, with rationale and compliant/non-compliant C++ for
> each guideline. Every entry is marked `⚑verify`: the *guidance* reflects
> long-established MISRA C++ / AUTOSAR C++14 practice, but the **exact rule IDs,
> categories, and official wording of MISRA C++:2023 must be confirmed against the
> purchased standard** — its per-rule identifiers (dotted, e.g. `Rule 8.2.3`) could
> not be grounded in this build environment (authoritative lists are copyright-
> protected / network-blocked). Use this as an engineering reference; use the
> official document for a formal compliance matrix. See `../overview.md`.

Legend: category shown as *(Mandatory / Required / Advisory)*.

---

## 1. General & lexical conventions

- **Trigraphs and digraphs must not be used.** *(Required)* ⚑verify
- **The `/*` and `//` sequences must not appear within a comment.** *(Required)* ⚑verify
```cpp
/* a /* b */ c;   // Non-compliant: 'c;' is live code
```
- **Each expression statement / declaration should be on its own line.** *(Advisory)* ⚑verify
- **Literal suffixes must be uppercase (`L`, `U`, `LL`).** *(Required)* ⚑verify
```cpp
auto n = 100l;   // Non-compliant     auto n = 100L;  // Compliant
```
- **Octal constants (other than `0`) and octal escape sequences must not be used.** *(Required)* ⚑verify
- **User-defined literals should be used only where they improve clarity.** *(Advisory)* ⚑verify
- **A character/string literal must not be modified.** *(Required)* ⚑verify

## 2. Identifiers & naming

- **Identifiers must not be reused across scopes so as to shadow/hide.** *(Required)* ⚑verify
```cpp
int count;
void f(){ int count = 0; }   // Non-compliant: hides outer 'count'
```
- **An identifier must not be reused for different entities in different name spaces confusingly.** *(Required)* ⚑verify
- **Identifiers should be distinct in a typographically unambiguous way** (avoid `l`/`1`, `O`/`0`). *(Advisory)* ⚑verify
- **Macro names must be reserved-safe and distinct from other identifiers.** *(Required)* ⚑verify

## 3. Basic concepts (declarations, scope, ODR, storage duration, lifetime)

- **Every entity must have exactly one definition (ODR).** *(Required)* ⚑verify
- **An object must be initialized before its value is read.** *(Mandatory)* ⚑verify
```cpp
int x; use(x);        // Non-compliant
int x{0}; use(x);     // Compliant (brace-init also prevents narrowing)
```
- **Declare each variable in the narrowest practical scope, initialized at
  declaration.** *(Advisory)* ⚑verify
- **The static initialization-order fiasco must be avoided** (no cross-TU
  dependency between dynamically-initialized namespace-scope objects). *(Required)* ⚑verify
```cpp
// Compliant: function-local static, initialized on first use
Config& config(){ static Config c; return c; }
```
- **An object's address must not be used outside its lifetime** (no dangling). *(Required)* ⚑verify
- **`thread_local` storage must be used deliberately and documented.** *(Advisory)* ⚑verify

## 4. Standard conversions

- **Implicit conversions that lose value/precision (narrowing) must not occur.** *(Required)* ⚑verify
```cpp
int i = 300; char c = i;             // Non-compliant: narrowing
char c{ static_cast<char>(i) };      // Compliant: explicit
```
- **`const`/`volatile` qualification must not be cast away.** *(Required)* ⚑verify
- **Pointer↔integer conversions should be avoided.** *(Advisory)* ⚑verify
- **A null pointer must be written `nullptr`, never `0` or `NULL`.** *(Required)* ⚑verify
```cpp
int* p = NULL;      // Non-compliant
int* p = nullptr;   // Compliant
```
- **An array must not decay to a pointer where the size is needed** (prefer
  `std::array`/`std::span`). *(Advisory)* ⚑verify

## 5. Expressions

- **Operator precedence should be made explicit with parentheses.** *(Advisory)* ⚑verify
- **The comma operator must not be used.** *(Required)* ⚑verify
- **Evaluation must not depend on unspecified order of evaluation.** *(Required)* ⚑verify
```cpp
y = f() + g();   // Non-compliant if f/g share mutable state
```
- **C-style and functional-notation casts must not be used; use named casts.** *(Required)* ⚑verify
```cpp
double d = (double)i;                 // Non-compliant
double d = static_cast<double>(i);    // Compliant
```
- **`reinterpret_cast` must not be used** (save rare, documented low-level cases). *(Required)* ⚑verify
- **`const_cast` must not be used to modify a const object.** *(Required)* ⚑verify
- **`dynamic_cast` result must be checked before use.** *(Required)* ⚑verify
- **The operand of `sizeof` must not have side effects.** *(Mandatory)* ⚑verify
- **Bitwise operators must not be applied to signed/Boolean operands.** *(Required)* ⚑verify
- **Increment/decrement must not be mixed with other side effects in one
  expression.** *(Advisory)* ⚑verify
- **The result of an assignment must not be used as a sub-expression.** *(Advisory)* ⚑verify
```cpp
if ((x = get()) != 0) {}   // Non-compliant
```

## 6. Statements (control flow)

- **The body of an `if`/`else`/loop must be a compound statement `{ }`.** *(Required)* ⚑verify
- **An `if...else if` chain must end with an `else`.** *(Required)* ⚑verify
- **Every `switch` must have a `default`; each clause ends with `break`** (no
  unintended fall-through). *(Required)* ⚑verify
- **A `switch` must have at least two case-clauses.** *(Required)* ⚑verify
- **`goto` must not be used** (or only jump forward within the same function). *(Advisory/Required)* ⚑verify
- **A loop counter must not be of floating type.** *(Required)* ⚑verify
- **A `for` loop must be well-formed; range-based `for` is preferred.** *(Advisory)* ⚑verify
```cpp
for (const auto& item : items) { use(item); }   // Compliant
```
- **A function should have a single exit at the end (or use RAII to make multiple
  exits safe).** *(Advisory)* ⚑verify

## 7. Declarations (specifiers)

- **Types must be explicitly specified where `auto` would harm clarity/safety.** *(Advisory)* ⚑verify
- **Use `const`/`constexpr` for values that do not change.** *(Advisory)* ⚑verify
```cpp
constexpr int kMax = 100;   // Compliant
```
- **`volatile` must be used only for genuinely volatile access.** *(Required)* ⚑verify
- **A declaration must declare no more than one variable.** *(Advisory)* ⚑verify
- **`using` (type alias) is preferred over `typedef`.** *(Advisory)* ⚑verify
- **An enumeration should be scoped (`enum class`).** *(Required)* ⚑verify
```cpp
enum Color { Red };          // Non-compliant: unscoped
enum class Color { Red };    // Compliant
```
- **`[[nodiscard]]` should mark functions whose result must be used.** *(Advisory)* ⚑verify

## 8. Declarators (pointers, references, functions, arrays)

- **A non-`void` function must return a value on every path.** *(Mandatory)* ⚑verify
- **Variable-length arrays must not be used.** *(Required)* ⚑verify
- **Pointer arithmetic must remain within one array; prefer `std::span`/iterators.** *(Required)* ⚑verify
- **The address of an automatic object must not outlive it.** *(Required)* ⚑verify
- **Functions must not be recursive (bounded stack).** *(Required)* ⚑verify
- **A function must not have an unbounded variadic (`...`) parameter list;** use
  variadic templates instead. *(Required)* ⚑verify
- **Function parameters should be `const` references for non-trivial types.** *(Advisory)* ⚑verify
- **Default arguments must not be repeated/contradicted across declarations.** *(Required)* ⚑verify
- **A parameter should not be modified within the function.** *(Advisory)* ⚑verify

## 9. Classes & special member functions

- **A class managing a resource must obey the Rule of 0/3/5.** *(Required)* ⚑verify
```cpp
struct Bad { int* p; ~Bad(){ delete p; } };   // Non-compliant: copy => double free
```
- **A polymorphic base class must have a `virtual` (or protected non-virtual)
  destructor.** *(Required)* ⚑verify
- **Data members should be `private`.** *(Advisory)* ⚑verify
- **Single-argument constructors should be `explicit`.** *(Required)* ⚑verify
- **Members must be initialized in declaration order (member-init list).** *(Required)* ⚑verify
- **A constructor must not call a virtual function that expects a fully
  constructed object.** *(Required)* ⚑verify
- **`= default` / `= delete` should express intent for special members.** *(Advisory)* ⚑verify
- **A class with virtual functions should mark them `override`/`final` in
  derived classes.** *(Required)* ⚑verify

## 10. Derived classes & inheritance

- **Every override must be marked `override`.** *(Required)* ⚑verify
```cpp
struct D : Base { void f() override; };   // Compliant
```
- **A virtual function's default arguments must not be changed in an override.** *(Required)* ⚑verify
- **Multiple inheritance from non-interface (stateful) bases should be avoided.** *(Advisory)* ⚑verify
- **Virtual inheritance should be used only where a diamond truly requires it.** *(Advisory)* ⚑verify
- **A base class subobject must not be sliced by value copy.** *(Required)* ⚑verify

## 11. Overloading

- **Overloaded operators must preserve conventional semantics** (`==` symmetric,
  side-effect-free, etc.). *(Required)* ⚑verify
- **Overload sets must not be ambiguous or rely on surprising conversions.** *(Required)* ⚑verify
- **`operator new`/`operator delete` must be provided and used in matching pairs.** *(Required)* ⚑verify
- **User-defined conversion operators should be `explicit` unless implicit
  conversion is intended.** *(Advisory)* ⚑verify

## 12. Templates & generic programming

- **A template must be well-formed for every permitted instantiation.** *(Required)* ⚑verify
- **Explicit specializations must be declared before first use.** *(Required)* ⚑verify
- **Template parameters should be constrained (concepts / `static_assert`).** *(Advisory)* ⚑verify
```cpp
static_assert(std::is_integral_v<T>, "T must be integral");   // Compliant
```
- **SFINAE / overload resolution must not silently select an unintended
  specialization.** *(Required)* ⚑verify
- **Non-type template parameters must have appropriate types.** *(Required)* ⚑verify

## 13. Exception handling

- **Exceptions must not escape a `noexcept` function or a destructor.** *(Required)* ⚑verify
```cpp
~Widget() noexcept { /* must not throw */ }
```
- **Exceptions must be caught by (const) reference, not by value.** *(Required)* ⚑verify
```cpp
catch (const std::exception& e) { }   // Compliant
catch (std::exception e) { }          // Non-compliant: slicing
```
- **Only objects derived from a common exception base should be thrown.** *(Required)* ⚑verify
- **An empty `throw;` (rethrow) must appear only inside a `catch`.** *(Required)* ⚑verify
- **Every exception thrown must have a matching handler on all paths.** *(Required)* ⚑verify
- **`catch(...)` should be used only as a last-resort/boundary handler.** *(Advisory)* ⚑verify
- **Resources must be released on the exceptional path (RAII, not manual cleanup).** *(Required)* ⚑verify

## 14. Dynamic memory & resource management

- **Dynamic allocation must be constrained/avoided; when used, ownership must be
  explicit via RAII (smart pointers).** *(Required)* ⚑verify
```cpp
auto p = std::make_unique<Widget>();   // Compliant
Widget* p = new Widget();              // Non-compliant: manual delete
```
- **Raw owning pointers must not be used.** *(Required)* ⚑verify
- **`new`/`delete` (and `new[]`/`delete[]`) must be correctly paired.** *(Required)* ⚑verify
- **A pointer must not be used after the object is freed / moved-from.** *(Mandatory)* ⚑verify
- **`std::move` must not be used on a `const` object or a value used afterwards.** *(Required)* ⚑verify

## 15. Concurrency

- **Shared data accessed by multiple threads must be protected (mutex/atomic).** *(Required)* ⚑verify
- **A mutex must be released on all paths (`std::lock_guard`/`scoped_lock`).** *(Required)* ⚑verify
```cpp
std::lock_guard<std::mutex> lk(m);   // Compliant: RAII unlock
```
- **Deadlock must be avoided (consistent lock ordering / `std::scoped_lock`).** *(Required)* ⚑verify
- **A thread must be joined or detached before its handle is destroyed.** *(Required)* ⚑verify
- **Data races (unsynchronized concurrent access) are undefined and must not
  occur.** *(Mandatory)* ⚑verify

## 16. Preprocessor

- **Function-like macros should be replaced by inline / `constexpr` functions.** *(Advisory)* ⚑verify
```cpp
#define SQ(x) ((x)*(x))                    // Non-compliant (advisory)
constexpr int sq(int x){ return x * x; }   // Compliant
```
- **Object-like macros for constants should be `constexpr` / `enum` instead.** *(Advisory)* ⚑verify
- **Macro parameters in the replacement list must be parenthesised.** *(Required)* ⚑verify
- **`#include` operands must be well-formed** (no `'`, `"`, `\`, `/*`, `//`). *(Required)* ⚑verify
- **Headers must have include guards or `#pragma once`.** *(Required)* ⚑verify
- **`#undef` should not be used.** *(Advisory)* ⚑verify
- **`#` / `##` operators should not be used.** *(Advisory)* ⚑verify

## 17. Standard library usage

- **Deprecated or removed library features must not be used.** *(Required)* ⚑verify
- **C standard-library facilities superseded by C++ equivalents should not be
  used** (`<cstring>` raw ops → `std::string`/`std::array`/algorithms). *(Advisory)* ⚑verify
```cpp
std::array<int,4> a{};   // Compliant, over C array + memset
```
- **Library functions must be called with valid arguments (ranges, bounds).** *(Required)* ⚑verify
- **Iterators must not be used after invalidation.** *(Mandatory)* ⚑verify
- **`std::vector<bool>` and other surprising specializations should be avoided.** *(Advisory)* ⚑verify
- **C++ I/O / locale features with heavy runtime cost should be used
  deliberately.** *(Advisory)* ⚑verify
- **`<csetjmp>`, `<csignal>`, `<cstdarg>` facilities must not be used.** *(Required)* ⚑verify

---

### Directives
See [`directives.md`](directives.md) for the four MISRA C++:2023 directives.
