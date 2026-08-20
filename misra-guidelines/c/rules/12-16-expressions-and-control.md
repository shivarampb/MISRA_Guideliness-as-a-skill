# MISRA C:2023 — Rules §12–§16 (in depth)

Each entry: **ID — Category · Decidability · Scope**, paraphrased guideline,
rationale, and examples.

---

## §12 — Expressions

### Rule 12.1 — Advisory · Decidable · Single TU
**Guideline:** Operator precedence within expressions should be made explicit.
```c
x = a + b << c;         /* Non-compliant: is it (a+b)<<c ? */
x = (a + b) << c;       /* Compliant */
```

### Rule 12.2 — Required · Decidable · Single TU
**Guideline:** The right operand of a shift must lie in 0 .. (bit-width of left − 1).
```c
uint16_t v; v = v << 20;    /* Non-compliant: shift >= width is UB */
```

### Rule 12.3 — Advisory · Decidable · Single TU
**Guideline:** The comma operator should not be used.
```c
for (i=0, j=n; i<j; i++, j--)   /* Non-compliant */
```

### Rule 12.4 — Advisory · Decidable · Single TU
**Guideline:** Evaluation of constant expressions should not lead to unsigned
integer wrap-around.
```c
uint16_t x = 0xFFFFu + 1u;   /* Non-compliant: wraps to 0 */
```

### Rule 12.5 — Mandatory · Decidable · Single TU *(AMD1)*
**Guideline:** `sizeof` must not have an operand that is a function parameter
declared as "array of type". **No deviation permitted.**
```c
void f(int a[10]){ size_t n = sizeof(a); }  /* Non-compliant: a is a pointer, sizeof==ptr size */
```

---

## §13 — Side effects

### Rule 13.1 — Required · Undecidable · Single TU
**Guideline:** Initializer lists must not contain persistent side effects.
```c
int a[2] = { i++, i++ };   /* Non-compliant */
```

### Rule 13.2 — Required · Undecidable · System
**Guideline:** An expression's value and side effects must be identical under all
permitted evaluation orders.
```c
y = f() + g();   /* Non-compliant if f and g share/modify state */
```

### Rule 13.3 — Advisory · Decidable · Single TU
**Guideline:** A full expression with `++`/`--` should have no other potential side
effects.
```c
x = a++ + b--;   /* Non-compliant */
```

### Rule 13.4 — Advisory · Decidable · Single TU
**Guideline:** The result of an assignment operator should not be used.
```c
if ((x = get()) != 0) {}   /* Non-compliant */
x = get(); if (x != 0) {}  /* Compliant */
```

### Rule 13.5 — Required · Undecidable · Single TU
**Guideline:** The right operand of `&&`/`||` must not contain persistent side
effects.
```c
if (ok && (count++ > 0)) {}   /* Non-compliant: count++ may not run */
```

### Rule 13.6 — Mandatory · Decidable · Single TU
**Guideline:** The operand of `sizeof` must not contain any expression with
potential side effects. **No deviation permitted.**
```c
n = sizeof(a[i++]);   /* Non-compliant: i++ not evaluated */
```

---

## §14 — Control statement expressions

### Rule 14.1 — Required · Undecidable · Single TU
**Guideline:** A loop counter must not have essentially floating type.
```c
for (float f=0.0f; f!=1.0f; f+=0.1f) {}   /* Non-compliant: never exactly 1.0 */
```

### Rule 14.2 — Required · Undecidable · Single TU
**Guideline:** A `for` loop must be well-formed (single counter, clear init/cond/
step, counter not modified in body).

### Rule 14.3 — Required · Undecidable · System
**Guideline:** Controlling expressions must not be invariant.
```c
if (sizeof(int) > 0) {}   /* Non-compliant: always true */
```

### Rule 14.4 — Required · Decidable · Single TU
**Guideline:** The controlling expression of `if`/iteration must have essentially
Boolean type.
```c
int p; if (p) {}          /* Non-compliant */
int p; if (p != 0) {}     /* Compliant */
```

---

## §15 — Control flow

### Rule 15.1 — Advisory · Decidable · Single TU
**Guideline:** `goto` should not be used.

### Rule 15.2 — Required · Decidable · Single TU
**Guideline:** `goto` must jump to a label later in the same function.
```c
loop: ... goto loop;   /* Non-compliant: backward jump */
```

### Rule 15.3 — Required · Decidable · Single TU
**Guideline:** A label referenced by `goto` must be in the same or an enclosing
block of the `goto`.

### Rule 15.4 — Advisory · Decidable · Single TU
**Guideline:** No more than one `break`/`goto` should terminate any iteration
statement.

### Rule 15.5 — Advisory · Decidable · Single TU
**Guideline:** A function should have a single point of exit at the end.
```c
int f(int x){ if(x) return 1; return 0; }   /* Non-compliant: two returns */
```

### Rule 15.6 — Required · Decidable · Single TU
**Guideline:** The body of an iteration/selection statement must be a compound
statement `{ }`.
```c
if (x) y = 1;              /* Non-compliant */
if (x) { y = 1; }         /* Compliant */
```

### Rule 15.7 — Required · Decidable · Single TU
**Guideline:** All `if ... else if` chains must terminate with an `else`.
```c
if (a) {} else if (b) {}              /* Non-compliant */
if (a) {} else if (b) {} else {}     /* Compliant */
```

---

## §16 — Switch statements

### Rule 16.1 — Required · Decidable · Single TU
**Guideline:** All `switch` statements must be well-formed (per rules 16.2–16.7).

### Rule 16.2 — Required · Decidable · Single TU
**Guideline:** A switch label must only appear when the enclosing compound
statement is the switch body (no Duff's-device-style labels).

### Rule 16.3 — Required · Decidable · Single TU
**Guideline:** An unconditional `break` must terminate every switch-clause.
```c
case 1: x=1;            /* Non-compliant: falls through */
case 1: x=1; break;     /* Compliant */
```

### Rule 16.4 — Required · Decidable · Single TU
**Guideline:** Every `switch` must have a `default` label.

### Rule 16.5 — Required · Decidable · Single TU
**Guideline:** A `default` label must be the first or last switch label.

### Rule 16.6 — Required · Decidable · Single TU
**Guideline:** Every `switch` must have at least two switch-clauses.
**Rationale:** A one-clause switch should be an `if`.

### Rule 16.7 — Required · Decidable · Single TU
**Guideline:** A switch-expression must not have essentially Boolean type (use
`if`/`else`).
