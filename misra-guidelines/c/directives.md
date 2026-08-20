# MISRA C:2023 — Directives (in depth)

Directives require information **beyond the source code** (requirements,
documentation, build process) to check. Each entry: **ID — Category ·
Decidability · Scope**, paraphrased guideline, rationale, and guidance.

---

## Dir 1 — The implementation

### Dir 1.1 — Required · Undecidable · System
**Guideline:** Any implementation-defined behaviour the program's output depends on
must be documented and understood.
**Rationale:** Type sizes, `char` signedness, right-shift of negatives, etc. vary
by compiler; relying on them undocumented breaks portability.

### Dir 1.2 — Advisory ⚑verify
**Guideline:** Language extensions should be documented and understood.

---

## Dir 2 — Compilation and build

### Dir 2.1 — Required · Undecidable · System
**Guideline:** All source files must compile without any compilation errors.
**Rationale:** Warnings/errors suppressed or ignored hide real defects; a clean
build at max diagnostic level is the baseline.

---

## Dir 3 — Requirements traceability

### Dir 3.1 — Required · Undecidable · System
**Guideline:** All code must be traceable to documented requirements.
**Rationale:** Untraceable code may be unnecessary or unverified — a safety concern.

---

## Dir 4 — Code design

### Dir 4.1 — Required · Undecidable · System
**Guideline:** Run-time failures must be minimized.
**Rationale:** Guard against division by zero, overflow, out-of-range indexing, null
dereference — by design, static proof, or run-time checks.

### Dir 4.2 — Advisory · Undecidable · Single TU
**Guideline:** All use of assembly language should be documented.

### Dir 4.3 — Required · Decidable · Single TU
**Guideline:** Assembly language must be encapsulated and isolated.
```c
/* Compliant: wrap asm in a documented inline function */
static inline void nop(void){ __asm("nop"); }
```

### Dir 4.4 — Advisory · Undecidable · Single TU
**Guideline:** Sections of code should not be "commented out".
**Rationale:** Use version control, not comments, to remove code. Commented-out
code rots and confuses.

### Dir 4.5 — Advisory · Undecidable · System
**Guideline:** Identifiers in the same name space with overlapping visibility should
be typographically unambiguous (avoid `l`/`1`, `O`/`0`, `rn`/`m`).

### Dir 4.6 — Advisory · Undecidable · Single TU
**Guideline:** `typedef`s that indicate size and signedness should be used in place
of the basic numerical types.
```c
int   count;     /* Non-compliant */
int32_t count;   /* Compliant */
```

### Dir 4.7 — Required · Undecidable · Single TU
**Guideline:** If a function returns error information, that error information must
be tested.
```c
(void)fclose(f);          /* Non-compliant if the result matters */
if (fclose(f) != 0) { /* handle */ }   /* Compliant */
```

### Dir 4.8 — Advisory · Undecidable · Single TU
**Guideline:** If a pointer to a struct/union is never dereferenced within a TU, its
implementation should be hidden (opaque type).

### Dir 4.9 — Advisory · Undecidable · Single TU
**Guideline:** A function should be preferred over a function-like macro where
interchangeable.
**Rationale:** Functions are type-checked and side-effect-safe; macros aren't.

### Dir 4.10 — Required · Decidable · Single TU
**Guideline:** Precautions must be taken to prevent a header being included more
than once (include guards / `#pragma once`).
```c
#ifndef FOO_H
#define FOO_H
/* ... */
#endif
```

### Dir 4.11 — Required · Undecidable · Single TU
**Guideline:** The validity of values passed to library functions must be checked.
```c
if (x >= 0.0) { r = sqrt(x); }   /* Compliant: domain checked */
```

### Dir 4.12 — Required · Undecidable · Single TU
**Guideline:** **Dynamic memory allocation must not be used.**
**Rationale:** Non-deterministic timing, fragmentation, and leak/UAF risk make it
unsuitable for many safety-critical systems.

### Dir 4.13 — Advisory · Undecidable · Single TU
**Guideline:** Functions operating on a resource should be called in an appropriate
sequence (e.g. open → use → close).

### Dir 4.14 — Required · Undecidable · Single TU *(AMD1 — security)*
**Guideline:** The validity of values received from external sources must be
checked (bounds, type, range) before use.

### Dir 4.15 — Required · Undecidable · Single TU ⚑verify *(AMD3)*
**Guideline:** Evaluation of floating-point expressions must not lead to the
undetected generation of infinities and NaNs.

---

## Dir 5 — Concurrency *(C:2023 / AMD3)* ⚑verify

The published C:2023 total is ~21 directives across ~5 sections (vs 17 in the
original C:2012). The **concurrency** section (`Dir 5.x`), tied to the C11
`<threads.h>` additions, contains:

### Dir 5.1 — Required · Undecidable · System ⚑verify
**Guideline:** There must be no data races between threads.
**Rationale:** Unsynchronized concurrent access to shared data (at least one a
write) is undefined behaviour.

### Dir 5.2 — Required · Undecidable · System ⚑verify
**Guideline:** There must be no deadlocks between threads.
**Rationale:** Circular lock-acquisition waits halt the program; use a consistent
global lock ordering.

### Dir 5.3 — Advisory · Undecidable · System ⚑verify
**Guideline:** There should be no dynamic thread creation (thread pools /
statically-created threads are preferred for determinism).

> **Confirm the exact IDs, titles, and categories of the `Dir 5.x` guidelines
> against the official MISRA C:2023 document** before citing them in a formal
> compliance matrix.
