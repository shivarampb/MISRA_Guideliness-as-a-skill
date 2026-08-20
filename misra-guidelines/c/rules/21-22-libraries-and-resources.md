# MISRA C:2023 — Rules §21–§22

Format: `Rule S.N — (Category, Decidability)`. Summaries are paraphrased.
Sections 21 and 22 were heavily extended by Amendments 1–3 (security, C11).
Amendment-added entries are marked `⚑verify`.

## §21 — Standard libraries

- **Rule 21.1** — *(Required, Decidable, Single TU)* — `#define`/`#undef` must not
  be used on a reserved identifier or reserved macro name.
- **Rule 21.2** — *(Required, Decidable, Single TU)* — A reserved identifier or
  reserved macro name must not be declared.
- **Rule 21.3** — *(Required, Decidable, Single TU)* — The memory allocation/
  deallocation functions of `<stdlib.h>` must not be used.
- **Rule 21.4** — *(Required, Decidable, Single TU)* — `<setjmp.h>` must not be
  used.
- **Rule 21.5** — *(Required, Decidable, Single TU)* — `<signal.h>` must not be
  used.
- **Rule 21.6** — *(Required, Decidable, Single TU)* — The Standard Library I/O
  functions (`<stdio.h>`, and `<wchar.h>` I/O) must not be used.
- **Rule 21.7** — *(Required, Decidable, Single TU)* — `atof`, `atoi`, `atol`,
  `atoll` of `<stdlib.h>` must not be used.
- **Rule 21.8** — *(Required, Decidable, Single TU)* — `abort`, `exit`, `getenv`
  (and `system`) of `<stdlib.h>` must not be used. *(scope adjusted by AMD; see
  Rule 21.21)*
- **Rule 21.9** — *(Required, Decidable, Single TU)* — `bsearch` and `qsort` of
  `<stdlib.h>` must not be used.
- **Rule 21.10** — *(Required, Decidable, Single TU)* — The date/time functions of
  `<time.h>` (and `wcsftime`) must not be used.
- **Rule 21.11** — *(Required, Decidable, Single TU)* — `<tgmath.h>` must not be
  used. *(AMD: relaxed to Advisory in some editions — ⚑verify)*
- **Rule 21.12** — *(Advisory, Decidable, Single TU)* — The exception-handling
  features of `<fenv.h>` should not be used. *(AMD3 may widen this — ⚑verify)*
- **Rule 21.13** — *(Mandatory, Decidable, Single TU)* ⚑verify — Any value passed
  to a `<ctype.h>` function must be representable as `unsigned char` or equal
  `EOF`. *(AMD1)*
- **Rule 21.14** — *(Required, Decidable, Single TU)* ⚑verify — `memcmp` must not
  be used to compare null-terminated strings. *(AMD1)*
- **Rule 21.15** — *(Required, Decidable, Single TU)* ⚑verify — The pointer
  arguments to `memcpy`, `memmove`, `memcmp` must be pointers to compatible types.
  *(AMD1)*
- **Rule 21.16** — *(Required, Decidable, Single TU)* ⚑verify — The pointer
  arguments to `memcmp` must point to appropriate essential types. *(AMD1)*
- **Rule 21.17** — *(Mandatory, Undecidable, Single TU)* ⚑verify — Use of
  `<string.h>` functions must not access beyond the bounds of referenced objects.
  *(AMD1)*
- **Rule 21.18** — *(Mandatory, Undecidable, Single TU)* ⚑verify — The `size_t`
  argument to a `<string.h>` function must have an appropriate value. *(AMD1)*
- **Rule 21.19** — *(Mandatory, Decidable, Single TU)* ⚑verify — Pointers returned
  by `localeconv`, `getenv`, `setlocale`, `strerror` must be treated as pointer to
  const. *(AMD1)*
- **Rule 21.20** — *(Mandatory, Decidable, Single TU)* ⚑verify — The pointer
  returned by certain library functions must not be used after a subsequent call
  to the same function. *(AMD1)*
- **Rule 21.21** — *(Required, Decidable, Single TU)* ⚑verify — `system` of
  `<stdlib.h>` must not be used. *(AMD3)*
- **Rule 21.22–21.26** ⚑verify — Type-generic math (`<tgmath.h>`), and C11
  additions (`<stdatomic.h>`, memory-ordering, thread-local) constraints. *(AMD3)*

## §22 — Resources

- **Rule 22.1** — *(Required, Undecidable, System)* — All resources obtained via
  Standard Library functions must be explicitly released.
- **Rule 22.2** — *(Mandatory, Undecidable, System)* — A block of memory must only
  be freed if it was allocated by a Standard Library function.
- **Rule 22.3** — *(Required, Undecidable, System)* — The same file must not be
  open for read and write on different streams at the same time.
- **Rule 22.4** — *(Mandatory, Undecidable, System)* — There must be no attempt to
  write to a stream opened read-only.
- **Rule 22.5** — *(Mandatory, Undecidable, Single TU)* — A pointer to a `FILE`
  must not be dereferenced.
- **Rule 22.6** — *(Mandatory, Undecidable, System)* — The value of a `FILE`
  pointer must not be used after the associated stream is closed.
- **Rule 22.7** — *(Required, Decidable, Single TU)* ⚑verify — `EOF` must only be
  compared with the unmodified return value of a library function capable of
  returning `EOF`. *(AMD1)*
- **Rule 22.8** — *(Required, Undecidable, System)* ⚑verify — `errno` must be set
  to zero before a call to an errno-setting function. *(AMD1)*
- **Rule 22.9** — *(Required, Undecidable, System)* ⚑verify — `errno` must be
  tested after calling an errno-setting function. *(AMD1)*
- **Rule 22.10** — *(Required, Undecidable, System)* ⚑verify — `errno` must only
  be tested when the last function called was an errno-setting function. *(AMD1)*
- **Rule 22.11–22.20** ⚑verify — C11 threads/concurrency (`<threads.h>`):
  mutexes, condition variables, thread-specific storage — creation, ownership,
  and release constraints. *(AMD3)*
