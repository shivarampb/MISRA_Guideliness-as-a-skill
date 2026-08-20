# MISRA C:2023 — Rules §10–§11 (in depth)

Each entry: **ID — Category · Decidability · Scope**, paraphrased guideline,
rationale, and examples. See `../overview.md` for the essential type model.

---

## §10 — The essential type model

The "essential type" of an expression is its natural type before implicit
promotion. Categories: Boolean, character, signed, unsigned, enum, floating.
These rules stop implicit mixing that silently changes value or category.

### Rule 10.1 — Required · Decidable · Single TU
**Guideline:** Operands must not be of an inappropriate essential type for the
operator.
```c
char c; int x = c << 1;    /* Non-compliant: shift on essentially char */
```

### Rule 10.2 — Required · Decidable · Single TU
**Guideline:** Expressions of essentially character type must not be used
inappropriately in `+`/`-`.
```c
char c = '0' + '5';        /* Non-compliant: adding two chars */
char c = (char)('0' + 5);  /* Compliant: char + int(offset) */
```

### Rule 10.3 — Required · Decidable · Single TU
**Guideline:** A value must not be assigned to an object with narrower essential
type or a different essential type category.
```c
uint8_t b = 300;           /* Non-compliant: narrows, and 300 > 255 */
int16_t s = -1; uint16_t u = s;  /* Non-compliant: category change signed->unsigned */
```

### Rule 10.4 — Required · Decidable · Single TU
**Guideline:** Both operands of an operator using the usual arithmetic conversions
must have the same essential type category.
```c
uint32_t u; int32_t s; if (u > s) {}   /* Non-compliant: unsigned vs signed */
```

### Rule 10.5 — Advisory · Decidable · Single TU
**Guideline:** A value should not be cast to an inappropriate essential type.
```c
(bool)3.0f;    /* Non-compliant: floating cast to bool */
```

### Rule 10.6 — Required · Decidable · Single TU
**Guideline:** The value of a composite expression must not be assigned to an
object with wider essential type.
```c
uint16_t a,b; uint32_t r = a + b;   /* Non-compliant: a+b is 16-bit composite */
uint32_t r = (uint32_t)a + b;       /* Compliant */
```

### Rule 10.7 — Required · Decidable · Single TU
**Guideline:** If a composite expression is one operand where usual arithmetic
conversions apply, the other operand must not have wider essential type.

### Rule 10.8 — Required · Decidable · Single TU
**Guideline:** The value of a composite expression must not be cast to a different
essential type category or a wider essential type.

---

## §11 — Pointer type conversions

### Rule 11.1 — Required · Decidable · Single TU
**Guideline:** Conversions must not be performed between a function pointer and any
other type.
```c
void (*fp)(void) = (void(*)(void))0x8000;  /* Non-compliant */
```

### Rule 11.2 — Required · Decidable · Single TU
**Guideline:** Conversions must not be performed between a pointer to an incomplete
type and any other type.

### Rule 11.3 — Required · Decidable · Single TU
**Guideline:** A cast must not be performed between a pointer to object type and a
pointer to a different object type.
```c
uint8_t *p; uint32_t *q = (uint32_t*)p;   /* Non-compliant: alignment/aliasing risk */
```

### Rule 11.4 — Advisory · Decidable · Single TU
**Guideline:** A conversion should not be performed between a pointer to object and
an integer type.
```c
uintptr_t a = (uintptr_t)ptr;   /* Non-compliant (advisory): document if required */
```

### Rule 11.5 — Advisory · Decidable · Single TU
**Guideline:** A conversion should not be performed from pointer to `void` into
pointer to object.

### Rule 11.6 — Required · Decidable · Single TU
**Guideline:** A cast must not be performed between pointer to `void` and an
arithmetic type.

### Rule 11.7 — Required · Decidable · Single TU
**Guideline:** A cast must not be performed between pointer to object and a
non-integer arithmetic type.

### Rule 11.8 — Required · Decidable · Single TU
**Guideline:** A cast must not remove `const`/`volatile` qualification from the
pointed-to type.
```c
const int *cp; int *p = (int*)cp;   /* Non-compliant: casts away const */
```

### Rule 11.9 — Required · Decidable · Single TU
**Guideline:** The macro `NULL` must be the only permitted form of integer null
pointer constant.
```c
int *p = 0;      /* Non-compliant */
int *p = NULL;   /* Compliant */
```

### Rule 11.10 — Required ⚑verify *(AMD3, C11)*
**Guideline:** The `_Atomic` qualifier must not be applied to incomplete `void`.
