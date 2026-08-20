# MISRA C:2023 — Rules §21–§22 (in depth)

Each entry: **ID — Category · Decidability · Scope**, paraphrased guideline,
rationale, and examples. Sections 21–22 were heavily extended by Amendments 1–3
(security, C11). Amendment-added entries are marked `⚑verify`.

---

## §21 — Standard libraries

### Rule 21.1 — Required · Decidable · Single TU
**Guideline:** `#define`/`#undef` must not be used on a reserved identifier/macro.
```c
#define _MYGUARD   /* Non-compliant: leading underscore reserved */
```

### Rule 21.2 — Required · Decidable · Single TU
**Guideline:** A reserved identifier or reserved macro name must not be declared.

### Rule 21.3 — Required · Decidable · Single TU
**Guideline:** The memory allocation/deallocation functions of `<stdlib.h>`
(`malloc`, `calloc`, `realloc`, `free`) must not be used.
**Rationale:** Dynamic allocation risks fragmentation, leaks, and non-determinism
(see Dir 4.12).

### Rule 21.4 — Required · Decidable · Single TU
**Guideline:** `<setjmp.h>` must not be used.

### Rule 21.5 — Required · Decidable · Single TU
**Guideline:** `<signal.h>` must not be used.

### Rule 21.6 — Required · Decidable · Single TU
**Guideline:** The Standard Library I/O functions (`<stdio.h>`, wide I/O) must not
be used.

### Rule 21.7 — Required · Decidable · Single TU
**Guideline:** `atof`, `atoi`, `atol`, `atoll` must not be used.
**Rationale:** No error reporting on malformed input; use `strtol` family.

### Rule 21.8 — Required · Decidable · Single TU
**Guideline:** `abort`, `exit`, `getenv` (and `system`) of `<stdlib.h>` must not be
used. *(scope adjusted by AMD; `system` split to 21.21)*

### Rule 21.9 — Required · Decidable · Single TU
**Guideline:** `bsearch` and `qsort` of `<stdlib.h>` must not be used.

### Rule 21.10 — Required · Decidable · Single TU
**Guideline:** The date/time functions of `<time.h>` (and `wcsftime`) must not be
used.

### Rule 21.11 — Required · Decidable · Single TU
**Guideline:** `<tgmath.h>` must not be used. *(⚑verify — some editions relax to
Advisory)*

### Rule 21.12 — Advisory · Decidable · Single TU
**Guideline:** The exception-handling features of `<fenv.h>` should not be used.
*(⚑verify — AMD3 may widen)*

### Rule 21.13 — Mandatory · Decidable · Single TU ⚑verify *(AMD1)*
**Guideline:** Any value passed to a `<ctype.h>` function must be representable as
`unsigned char` or equal `EOF`. **No deviation.**
```c
char c = fgetc_result; isdigit(c);      /* Non-compliant if char is signed & negative */
isdigit((unsigned char)c);              /* Compliant */
```

### Rule 21.14 — Required · Decidable · Single TU ⚑verify *(AMD1)*
**Guideline:** `memcmp` must not be used to compare null-terminated strings.

### Rule 21.15 — Required · Decidable · Single TU ⚑verify *(AMD1)*
**Guideline:** The pointer arguments to `memcpy`, `memmove`, `memcmp` must be
pointers to compatible types.

### Rule 21.16 — Required · Decidable · Single TU ⚑verify *(AMD1)*
**Guideline:** The pointer arguments to `memcmp` must point to appropriate essential
types (not e.g. floating or struct with padding).

### Rule 21.17 — Mandatory · Undecidable · Single TU ⚑verify *(AMD1)*
**Guideline:** Use of `<string.h>` functions must not access beyond the bounds of
the referenced objects. **No deviation.**

### Rule 21.18 — Mandatory · Undecidable · Single TU ⚑verify *(AMD1)*
**Guideline:** The `size_t` argument to a `<string.h>` function must have an
appropriate value. **No deviation.**

### Rule 21.19 — Mandatory · Decidable · Single TU ⚑verify *(AMD1)*
**Guideline:** Pointers returned by `localeconv`, `getenv`, `setlocale`, `strerror`
must be treated as pointer to const.

### Rule 21.20 — Mandatory · Decidable · Single TU ⚑verify *(AMD1)*
**Guideline:** The pointer returned by certain library functions must not be used
after a subsequent call to the same function.

### Rule 21.21 — Required · Decidable · Single TU ⚑verify *(AMD3)*
**Guideline:** `system` of `<stdlib.h>` must not be used.

### Rule 21.22–21.26 — ⚑verify *(AMD3)*
**Guideline:** Type-generic math (`<tgmath.h>`) and C11 atomics/memory-ordering/
thread-local constraints.

---

## §22 — Resources

### Rule 22.1 — Required · Undecidable · System
**Guideline:** All resources obtained via Standard Library functions must be
explicitly released.
```c
FILE *f = fopen("x","r"); /* ... */    /* Non-compliant if never fclose(f) */
```

### Rule 22.2 — Mandatory · Undecidable · System
**Guideline:** A block of memory must only be freed if it was allocated by a
Standard Library function. **No deviation.**
```c
int a[4]; free(a);   /* Non-compliant: a not heap-allocated */
```

### Rule 22.3 — Required · Undecidable · System
**Guideline:** The same file must not be open for read and write on different
streams at the same time.

### Rule 22.4 — Mandatory · Undecidable · System
**Guideline:** There must be no attempt to write to a stream opened read-only.
**No deviation.**

### Rule 22.5 — Mandatory · Undecidable · Single TU
**Guideline:** A pointer to a `FILE` must not be dereferenced. **No deviation.**

### Rule 22.6 — Mandatory · Undecidable · System
**Guideline:** A `FILE` pointer must not be used after the stream is closed.
**No deviation.**
```c
fclose(f); fprintf(f,"x");   /* Non-compliant: use after close */
```

### Rule 22.7 — Required · Decidable · Single TU ⚑verify *(AMD1)*
**Guideline:** `EOF` must only be compared with the unmodified return value of a
library function capable of returning `EOF`.

### Rule 22.8 — Required · Undecidable · System ⚑verify *(AMD1)*
**Guideline:** `errno` must be set to zero before a call to an errno-setting
function.

### Rule 22.9 — Required · Undecidable · System ⚑verify *(AMD1)*
**Guideline:** `errno` must be tested after calling an errno-setting function.
```c
errno = 0; v = strtol(s,&e,10); if (errno != 0) { /* handle */ }   /* Compliant */
```

### Rule 22.10 — Required · Undecidable · System ⚑verify *(AMD1)*
**Guideline:** `errno` must only be tested when the last function called was an
errno-setting function.

### Rule 22.11–22.20 — ⚑verify *(AMD3)*
**Guideline:** C11 threads/concurrency (`<threads.h>`): mutexes, condition
variables, and thread-specific storage — creation, ownership, and release
constraints.
