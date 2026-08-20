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

### Rule 21.22 — Mandatory · Undecidable · Single TU ⚑verify *(AMD3)*
**Guideline:** All operand arguments to any type-generic macros in `<tgmath.h>`
must have an appropriate essential type.

### Rule 21.23 — Required · Undecidable · Single TU ⚑verify *(AMD3)*
**Guideline:** All operand arguments to any multi-argument type-generic macros in
`<tgmath.h>` must have the same standard type.

### Rule 21.24 — Required · Decidable · Single TU ⚑verify *(AMD3)*
**Guideline:** The random-number generator functions of `<stdlib.h>` (`rand`,
`srand`) must not be used.

### Rule 21.25 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** All memory-synchronization operations must be executed in
sequentially-consistent order (`memory_order_seq_cst`).

### Rule 21.26 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** The Standard Library function `mtx_timedlock()` must only be invoked
on mutex objects of an appropriate (timed) mutex type.

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

### Rule 22.11 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** A thread previously joined or detached must not be joined or
detached again.

### Rule 22.12 — Mandatory · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** Thread objects, thread synchronization objects, and thread-specific
storage pointers must only be accessed by the appropriate Standard Library
functions.

### Rule 22.13 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** Thread objects, thread synchronization objects, and thread-specific
storage pointers must have appropriate storage duration.

### Rule 22.14 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** Thread synchronization objects (mutexes, condition variables) must
be initialized before being accessed.

### Rule 22.15 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** Thread synchronization objects and thread-specific storage pointers
must not be destroyed until after all threads accessing them have terminated.

### Rule 22.16 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** All mutex objects locked by a thread must be explicitly unlocked by
the same thread.

### Rule 22.17 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** No thread must unlock a mutex, or call `cnd_wait`/`cnd_timedwait` on
a mutex, that it has not previously locked.

### Rule 22.18 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** Non-recursive mutexes must not be recursively locked.

### Rule 22.19 — Required · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** A condition variable must be associated with at most one mutex
object.

### Rule 22.20 — Mandatory · Undecidable · System ⚑verify *(AMD3, C11)*
**Guideline:** Thread-specific storage pointers must be created (via `tss_create`)
before being accessed.
