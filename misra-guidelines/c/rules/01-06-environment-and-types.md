# MISRA C:2023 — Rules §1–§6 (in depth)

Each entry: **ID — Category · Decidability · Scope**, paraphrased guideline,
rationale, and (where useful) non-compliant vs compliant C. Summaries are
paraphrased; verify `⚑verify` entries against the official standard.

---

## §1 — A standard C environment

### Rule 1.1 — Required · Decidable · System
**Guideline:** The program must contain no violations of standard C syntax and
constraints, and must not exceed the implementation's translation limits.
**Rationale:** Code relying on non-standard syntax or exceeding documented limits
(nesting depth, identifier length, etc.) may be rejected or silently mistranslated
by a conforming compiler.
```c
/* Non-compliant: constraint violation — assigning to array name */
int a[4]; a = other;        /* not an lvalue */
/* Compliant */
int a[4]; (void)memcpy(a, other, sizeof a);
```

### Rule 1.2 — Advisory · Undecidable · System
**Guideline:** Language extensions should not be used.
**Rationale:** Extensions (`__attribute__`, `#pragma`, inline asm keywords) are not
portable and change meaning between compilers.
```c
int x __attribute__((aligned(16)));   /* Non-compliant: GCC extension */
```
**Exception:** Extensions needed for the target may be used if isolated and
documented (see Dir 4.3 / Dir 1.2).

### Rule 1.3 — Required · Undecidable · System
**Guideline:** There must be no occurrence of undefined or critical unspecified
behaviour.
**Rationale:** UB (signed overflow, out-of-bounds access, use-after-free, data
races) makes program behaviour unpredictable across compilers/optimisation levels.
```c
int i = INT_MAX; i = i + 1;   /* Non-compliant: signed overflow is UB */
```

### Rule 1.4 — Required · Decidable · Single TU ⚑verify *(AMD2, C11/C18)*
**Guideline:** Emergent (newer) language features must not be used.
**Rationale:** Features such as `_Generic`, `_Atomic`, `_Noreturn`, `<threads.h>`
carry portability and analysis risks; restrict them unless explicitly adopted.

### Rule 1.5 — Required ⚑verify *(AMD3)*
**Guideline:** Obsolescent language features must not be used.
**Rationale:** Features flagged obsolescent by the C standard (e.g. certain
`gets`-style usages) may be removed and are error-prone.

---

## §2 — Unused code

### Rule 2.1 — Required · Undecidable · System
**Guideline:** A project must not contain unreachable code.
**Rationale:** Unreachable code cannot execute; its presence signals a logic error
and bloats the binary.
```c
return x;
y = 1;          /* Non-compliant: unreachable */
```

### Rule 2.2 — Required · Undecidable · System
**Guideline:** There must be no dead code (operations whose removal cannot affect
behaviour).
**Rationale:** Dead code wastes effort, confuses reviewers, and often hides a bug.
```c
(void)(a + b);  /* Non-compliant: result unused, no side effect */
```

### Rule 2.3 — Advisory · Decidable · System
**Guideline:** A project should not contain unused type declarations.
**Rationale:** Stale `typedef`s/tags clutter the code and mislead maintainers.

### Rule 2.4 — Advisory · Decidable · System
**Guideline:** A project should not contain unused tag declarations.

### Rule 2.5 — Advisory · Decidable · System
**Guideline:** A project should not contain unused macro declarations.

### Rule 2.6 — Advisory · Decidable · Single TU
**Guideline:** A function should not contain unused label declarations.

### Rule 2.7 — Advisory · Decidable · Single TU
**Guideline:** There should be no unused parameters in functions.
```c
void f(int used, int unused) { g(used); }   /* Non-compliant */
void f(int used, int x)      { (void)x; g(used); }  /* Compliant: explicitly consumed */
```

### Rule 2.8 — Advisory · Decidable · System ⚑verify *(AMD)*
**Guideline:** A project should not contain unused object definitions.

---

## §3 — Comments

### Rule 3.1 — Required · Decidable · Single TU
**Guideline:** The sequences `/*` and `//` must not appear within a comment.
**Rationale:** Nested comment markers cause code to be unexpectedly commented out.
```c
/* opening /* nested */ x = 1;   /* Non-compliant: x=1 is NOT commented out as intended */
```

### Rule 3.2 — Required · Decidable · Single TU
**Guideline:** Line-splicing (`\` at end of line) must not be used in `//` comments.
**Rationale:** A trailing backslash silently extends a `//` comment onto the next
line, swallowing code.
```c
// comment ending in backslash \
next_statement();   /* Non-compliant: this line is part of the comment */
```

---

## §4 — Character sets and lexical conventions

### Rule 4.1 — Required · Decidable · Single TU
**Guideline:** Octal and hexadecimal escape sequences must be terminated.
**Rationale:** `"\x1f2"` is one 3-digit hex escape, not `\x1f` + `2` — terminate to
avoid ambiguity.
```c
char s[] = "\x1B[0m";        /* Non-compliant: \x1B0 ambiguous */
char s[] = "\x1B" "[0m";     /* Compliant: adjacent literals terminate the escape */
```

### Rule 4.2 — Advisory · Decidable · Single TU
**Guideline:** Trigraphs should not be used.
**Rationale:** `??=` etc. are replaced during translation and cause surprising edits
to string contents.

---

## §5 — Identifiers

### Rule 5.1 — Required · Decidable · System
**Guideline:** External identifiers must be distinct (within the significant-
character limit).
**Rationale:** Two externals identical in the first N characters clash at link time
on limited toolchains.

### Rule 5.2 — Required · Decidable · Single TU
**Guideline:** Identifiers in the same scope and name space must be distinct.

### Rule 5.3 — Required · Decidable · Single TU
**Guideline:** An identifier in an inner scope must not hide one in an outer scope.
```c
int count;
void f(void){ int count = 0; }   /* Non-compliant: shadows file-scope count */
```

### Rule 5.4 — Required · Decidable · Single TU
**Guideline:** Macro identifiers must be distinct.

### Rule 5.5 — Required · Decidable · Single TU
**Guideline:** Identifiers must be distinct from macro names.

### Rule 5.6 — Required · Decidable · System
**Guideline:** A `typedef` name must be a unique identifier.

### Rule 5.7 — Required · Decidable · System
**Guideline:** A tag name must be a unique identifier.

### Rule 5.8 — Required · Decidable · System
**Guideline:** Identifiers with external linkage that define objects/functions must
be unique.

### Rule 5.9 — Advisory · Decidable · System
**Guideline:** Identifiers with internal linkage that define objects/functions
should be unique.

---

## §6 — Types

### Rule 6.1 — Required · Decidable · Single TU
**Guideline:** Bit-fields must only be declared with an appropriate type.
**Rationale:** The set of permitted bit-field types is implementation-defined for
types other than `int`/`unsigned int`/`_Bool`; use only portable ones.
```c
struct S { char b : 2; };        /* Non-compliant: char bit-field not portable */
struct S { unsigned int b : 2; };/* Compliant */
```

### Rule 6.2 — Required · Decidable · Single TU
**Guideline:** Single-bit named bit-fields must not be of a signed type.
**Rationale:** A 1-bit signed field holds only 0 and −1, almost never what's meant.
```c
struct S { signed int flag : 1; };   /* Non-compliant */
struct S { unsigned int flag : 1; }; /* Compliant */
```

### Rule 6.3 — Required · Decidable · Single TU ⚑verify *(AMD)*
**Guideline:** A bit-field must not be declared as a member of a union.
