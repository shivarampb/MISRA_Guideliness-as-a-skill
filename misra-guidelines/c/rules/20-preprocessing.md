# MISRA C:2023 — Rules §20 (Preprocessing directives, in depth)

Each entry: **ID — Category · Decidability · Scope**, paraphrased guideline,
rationale, and examples.

---

### Rule 20.1 — Advisory · Decidable · Single TU
**Guideline:** `#include` directives should only be preceded by preprocessor
directives or comments.
**Rationale:** Keeps include order predictable and header effects at the top.

### Rule 20.2 — Required · Decidable · Single TU
**Guideline:** The `'`, `"`, `\` characters and the `/*`, `//` sequences must not
occur in a header file name.
```c
#include "sub\dir\h.h"   /* Non-compliant: \ is UB in header name */
#include "sub/dir/h.h"   /* Compliant */
```

### Rule 20.3 — Required · Decidable · Single TU
**Guideline:** `#include` must be followed by `<filename>` or `"filename"`.

### Rule 20.4 — Required · Decidable · Single TU
**Guideline:** A macro must not be defined with the same name as a keyword.
```c
#define const   /* Non-compliant */
```

### Rule 20.5 — Advisory · Decidable · Single TU
**Guideline:** `#undef` should not be used.
**Rationale:** `#undef` obscures which definition of a macro is in force.

### Rule 20.6 — Required · Decidable · Single TU
**Guideline:** Tokens that look like a preprocessing directive must not occur within
a macro argument.
```c
FN(
#include "x.h"   /* Non-compliant */
)
```

### Rule 20.7 — Required · Decidable · Single TU
**Guideline:** Expressions resulting from expansion of macro parameters must be
enclosed in parentheses.
```c
#define SQ(x) x*x            /* Non-compliant: SQ(a+b) -> a+b*a+b */
#define SQ(x) ((x)*(x))      /* Compliant */
```

### Rule 20.8 — Required · Decidable · Single TU
**Guideline:** The controlling expression of `#if`/`#elif` must evaluate to 0 or 1.

### Rule 20.9 — Required · Decidable · Single TU
**Guideline:** All identifiers in a `#if`/`#elif` controlling expression must be
`#define`d before evaluation.
```c
#if FEATURE_X            /* Non-compliant if FEATURE_X may be undefined */
#if defined(FEATURE_X) && (FEATURE_X == 1)   /* Compliant */
```

### Rule 20.10 — Advisory · Decidable · Single TU
**Guideline:** The `#` and `##` preprocessor operators should not be used.
**Rationale:** Stringisation/token-pasting are hard to read and error-prone.

### Rule 20.11 — Required · Decidable · Single TU
**Guideline:** A macro parameter immediately after `#` must not be immediately
followed by `##`.

### Rule 20.12 — Required · Decidable · Single TU
**Guideline:** A macro parameter used with `#`/`##`, and itself subject to further
replacement, must only be used as an operand to these operators.

### Rule 20.13 — Required · Decidable · Single TU
**Guideline:** A line whose first token is `#` must be a valid preprocessing
directive.

### Rule 20.14 — Required · Decidable · Single TU
**Guideline:** All `#else`, `#elif`, `#endif` must reside in the same file as the
`#if`/`#ifdef`/`#ifndef` they relate to.
