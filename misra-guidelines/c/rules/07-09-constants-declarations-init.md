# MISRA C:2023 — Rules §7–§9 (in depth)

Each entry: **ID — Category · Decidability · Scope**, paraphrased guideline,
rationale, and examples. `⚑verify` = confirm against the official standard.

---

## §7 — Literals and constants

### Rule 7.1 — Required · Decidable · Single TU
**Guideline:** Octal constants must not be used.
**Rationale:** A leading `0` silently makes a constant octal — a classic bug.
```c
int mask = 011;   /* Non-compliant: octal 011 == decimal 9, not 11 */
int mask = 9;     /* Compliant */
```
**Exception:** The single digit `0` is not an octal constant.

### Rule 7.2 — Required · Decidable · Single TU
**Guideline:** A `u`/`U` suffix must be applied to all integer constants
represented in an unsigned type.
**Rationale:** Makes the constant's signedness explicit and avoids surprising
signed/unsigned conversions.
```c
uint32_t x = 0xFFFFFFFF;    /* Non-compliant: value needs unsigned type */
uint32_t x = 0xFFFFFFFFU;   /* Compliant */
```

### Rule 7.3 — Required · Decidable · Single TU
**Guideline:** The lowercase `l` must not be used in a literal suffix.
**Rationale:** `l` is easily confused with `1`. Use `L`.
```c
long n = 100l;   /* Non-compliant: looks like 1001 */
long n = 100L;   /* Compliant */
```

### Rule 7.4 — Required · Decidable · Single TU
**Guideline:** A string literal must not be assigned to an object unless its type
is pointer to const-qualified `char`.
**Rationale:** String literals are non-modifiable; writing through a non-const
pointer is UB.
```c
char *p = "hello";        /* Non-compliant */
const char *p = "hello";  /* Compliant */
```

### Rule 7.5 — Required ⚑verify *(AMD3)*
**Guideline:** An integer constant macro argument must have the type its macro
requires.

### Rule 7.6 — Required ⚑verify *(AMD3)*
**Guideline:** The small-integer variants of the minimum-width integer constant
macros must not be used.

---

## §8 — Declarations and definitions

### Rule 8.1 — Required · Decidable · Single TU
**Guideline:** Types must be explicitly specified (no implicit `int`).
```c
static x;         /* Non-compliant: implicit int */
static int x;     /* Compliant */
```

### Rule 8.2 — Required · Decidable · Single TU
**Guideline:** Function types must be in prototype form with named parameters.
```c
int f();              /* Non-compliant: not a prototype */
int f(int a, int b);  /* Compliant */
```

### Rule 8.3 — Required · Decidable · System
**Guideline:** All declarations of an object/function must use the same names and
type qualifiers.
**Rationale:** Divergent declarations across TUs cause silent type mismatches.

### Rule 8.4 — Required · Decidable · System
**Guideline:** A compatible declaration must be visible when an object/function
with external linkage is defined.
**Rationale:** Forces the definition to be checked against the header prototype.
```c
/* foo.c — Non-compliant: no visible prototype for exported symbol */
int foo(void){ return 1; }
/* Compliant: include the header that declares foo */
#include "foo.h"
int foo(void){ return 1; }
```

### Rule 8.5 — Required · Decidable · System
**Guideline:** An external object/function must be declared once, in one file
(typically a header).

### Rule 8.6 — Required · Decidable · System
**Guideline:** An identifier with external linkage must have exactly one external
definition.

### Rule 8.7 — Advisory · Decidable · System
**Guideline:** Functions/objects should not have external linkage if referenced in
only one TU (make them `static`).

### Rule 8.8 — Required · Decidable · Single TU
**Guideline:** `static` must be used in all declarations of objects/functions with
internal linkage.

### Rule 8.9 — Advisory · Decidable · System
**Guideline:** An object should be defined at block scope if used in only one
function.

### Rule 8.10 — Required · Decidable · Single TU
**Guideline:** An inline function must be declared `static`.
**Rationale:** Avoids the subtle external-inline linkage rules of C99+.

### Rule 8.11 — Advisory · Decidable · Single TU
**Guideline:** When an array with external linkage is declared, its size should be
specified explicitly.
```c
extern int table[];    /* Non-compliant */
extern int table[10];  /* Compliant */
```

### Rule 8.12 — Required · Decidable · Single TU
**Guideline:** Within an enumerator list, implicitly-specified enum constant values
must be unique.
```c
enum E { A = 1, B, C = 2 };   /* Non-compliant: B and C both == 2 */
```

### Rule 8.13 — Advisory · Undecidable · System
**Guideline:** A pointer should point to a const-qualified type whenever possible.

### Rule 8.14 — Required · Decidable · Single TU
**Guideline:** The `restrict` type qualifier must not be used.
**Rationale:** Misuse silently introduces UB via wrong aliasing assumptions.

### Rule 8.15–8.17 — ⚑verify *(AMD2, C11/C18)*
**Guideline:** Constraints on alignment specifiers (`_Alignas`, `_Alignof`) and
over-aligned types.

---

## §9 — Initialization

### Rule 9.1 — Mandatory · Undecidable · System
**Guideline:** The value of an automatic object must not be read before it is set.
**Rationale:** Reading an indeterminate value is UB. **No deviation permitted.**
```c
int x; use(x);        /* Non-compliant */
int x = 0; use(x);    /* Compliant */
```

### Rule 9.2 — Required · Decidable · Single TU
**Guideline:** The initializer for an aggregate or union must be enclosed in braces.
```c
int m[2][2] = {1,2,3,4};        /* Non-compliant */
int m[2][2] = {{1,2},{3,4}};    /* Compliant */
```

### Rule 9.3 — Required · Decidable · Single TU
**Guideline:** Arrays must not be partially initialized.
```c
int a[3] = {1};        /* Non-compliant: a[1],a[2] implicitly 0 — state intent */
int a[3] = {1, 0, 0};  /* Compliant */
```
**Exception:** `= {0}` to zero the whole array is permitted.

### Rule 9.4 — Required · Decidable · Single TU
**Guideline:** An element of an object must not be initialized more than once.
```c
int a[3] = {[0]=1, [0]=2};   /* Non-compliant */
```

### Rule 9.5 — Required · Decidable · Single TU
**Guideline:** Where designated initializers initialize an array, the array size
must be specified explicitly.
```c
int a[]  = {[2]=1};    /* Non-compliant: size implicit */
int a[3] = {[2]=1};    /* Compliant */
```

### Rule 9.6 — Required ⚑verify *(AMD3)*
**Guideline:** An initializer using chained designators must not mix in
initializers without designators.

### Rule 9.7 — Mandatory ⚑verify *(AMD2/AMD3, C11)*
**Guideline:** Atomic objects must be appropriately initialized before access.
