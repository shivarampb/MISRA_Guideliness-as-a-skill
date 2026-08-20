# MISRA C:2023 — Rules §17–§19 (in depth)

Each entry: **ID — Category · Decidability · Scope**, paraphrased guideline,
rationale, and examples. `⚑verify` = confirm against the official standard.

---

## §17 — Functions

### Rule 17.1 — Required · Decidable · Single TU
**Guideline:** The features of `<stdarg.h>` (`va_list`, `va_start`, …) must not be
used.
**Rationale:** Variadic functions bypass type checking.

### Rule 17.2 — Required · Undecidable · System
**Guideline:** Functions must not call themselves, directly or indirectly.
**Rationale:** Recursion makes stack usage unbounded/unanalysable.
```c
int fact(int n){ return n?n*fact(n-1):1; }   /* Non-compliant */
```

### Rule 17.3 — Mandatory · Decidable · Single TU
**Guideline:** A function must not be declared implicitly. **No deviation.**
```c
y = foo();   /* Non-compliant if no prototype for foo is visible */
```

### Rule 17.4 — Mandatory · Decidable · Single TU
**Guideline:** All exit paths from a non-`void` function must have an explicit
`return` with an expression. **No deviation.**
```c
int f(int x){ if(x) return 1; }   /* Non-compliant: falls off the end */
```

### Rule 17.5 — Advisory · Undecidable · Single TU
**Guideline:** The argument for a parameter declared with an array type must have an
appropriate number of elements.

### Rule 17.6 — Mandatory · Decidable · Single TU
**Guideline:** An array parameter declaration must not contain `static` between the
`[ ]`. **No deviation.**
```c
void f(int a[static 10]);   /* Non-compliant */
```

### Rule 17.7 — Required · Decidable · Single TU
**Guideline:** The value returned by a non-`void` function must be used.
```c
foo();               /* Non-compliant if foo returns a value */
(void)foo();         /* Compliant: explicitly discarded */
```

### Rule 17.8 — Advisory · Decidable · Single TU
**Guideline:** A function parameter should not be modified.
```c
void f(int n){ n++; use(n); }        /* Non-compliant */
void f(int n){ int m=n+1; use(m); }  /* Compliant */
```

### Rule 17.9 — Mandatory ⚑verify *(AMD2, C11)*
**Guideline:** A `_Noreturn` function must not return to its caller.

### Rule 17.10 — Required ⚑verify *(AMD2)*
**Guideline:** A `_Noreturn` function must have `void` return type.

### Rule 17.11 — Advisory ⚑verify *(AMD2)*
**Guideline:** A function that never returns should be declared `_Noreturn`.

### Rule 17.12 — Advisory ⚑verify *(AMD3)*
**Guideline:** A function identifier should be used only with `&` or a parenthesised
argument list.

### Rule 17.13 — Required ⚑verify *(AMD3)*
**Guideline:** A function type must not be type qualified.

---

## §18 — Pointers and arrays

### Rule 18.1 — Required · Undecidable · Single TU
**Guideline:** A pointer from arithmetic on a pointer operand must address an
element of the same array.
```c
int a[10]; int *p = &a[0] + 11;   /* Non-compliant: out of bounds */
```

### Rule 18.2 — Required · Undecidable · Single TU
**Guideline:** Pointer subtraction must only apply to pointers into the same array.

### Rule 18.3 — Required · Undecidable · Single TU
**Guideline:** `>`, `>=`, `<`, `<=` must not be applied to pointers unless they
point into the same object.

### Rule 18.4 — Advisory · Decidable · Single TU
**Guideline:** `+`, `-`, `+=`, `-=` should not be applied to pointer expressions
(prefer array indexing).
```c
p += 1;      /* Non-compliant (advisory) */
x = p[1];    /* Compliant */
```

### Rule 18.5 — Advisory · Decidable · Single TU
**Guideline:** Declarations should contain no more than two levels of pointer
nesting.
```c
int ***p;    /* Non-compliant */
```

### Rule 18.6 — Required · Undecidable · System
**Guideline:** The address of an object with automatic storage must not be copied to
an object that persists after it ceases to exist.
```c
int *g;
void f(void){ int local; g = &local; }   /* Non-compliant: dangling after return */
```

### Rule 18.7 — Required · Decidable · Single TU
**Guideline:** Flexible array members must not be declared.
```c
struct S { int n; int data[]; };   /* Non-compliant */
```

### Rule 18.8 — Required · Decidable · Single TU
**Guideline:** Variable-length array types must not be used.
```c
void f(int n){ int a[n]; }   /* Non-compliant: VLA */
```

### Rule 18.9 — Required ⚑verify *(AMD3)*
**Guideline:** The address of an object with temporary lifetime must not outlive it.

### Rule 18.10 — Mandatory ⚑verify *(AMD3)*
**Guideline:** Pointers to variably-modified array types must not be used.

---

## §19 — Overlapping storage

### Rule 19.1 — Mandatory · Undecidable · System
**Guideline:** An object must not be assigned or copied to an overlapping object.
**No deviation.**
```c
memcpy(&buf[0], &buf[1], 4);   /* Non-compliant: overlapping */
```

### Rule 19.2 — Advisory · Decidable · Single TU
**Guideline:** The `union` keyword should not be used.
**Rationale:** Reading a member other than the last written is unspecified/UB.
