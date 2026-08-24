# Doxygen Function Header Formatting Rules

**Applies to:** C, C++, Qt C++ — All `.c`, `.cpp`, `.h`, `.hpp` files  
**Standards:** DO-178C | MISRA C:2023 | Data Patterns Coding Guidelines  
**Tag style:** `@` prefix mandatory — backslash prefix (`\`) is prohibited

---

## Rule 1 — Block Style

Every function must be preceded by a `/** ... */` block comment.  
No blank line between the closing `*/` and the function declaration.

```
/**
 * @brief  ...
 */
return_type FunctionName(params);
```

- Use `/** ... */` — never `/* ... */` (MISRA C:2023 Rule 3.1)
- Interior lines must begin with ` * ` (space-asterisk-space)
- Use `/*!` only in Qt C++ projects where the team has agreed on that style
- Do **not** mix `/**` and `/*!` in the same file

---

## Rule 2 — Mandatory Tags (every function, no exceptions)

Every function documentation block **must** contain these tags in this order:

```
@brief
@details        (if behaviour is non-trivial)
@param[in/out]  (one per parameter)
@return / @retval
@pre            (if preconditions exist)
@post           (if postconditions exist)
@note           (if constraints exist)
@warning        (if safety-relevant)
@see            (if related functions exist)
```

---

## Rule 3 — @brief

- **One line only.** Never wrap to a second line.
- Must be the **first tag** in the block.
- Must describe **what** the function does, not how.
- Must end without a full stop (period).
- Must be descriptive enough to identify the function without reading the rest.

```
/** @brief  Converts raw ADC count to calibrated voltage in millivolts */
```

---

## Rule 4 — @details

- Write **what** the function does, its algorithm at a high level, and any non-obvious behaviour.
- Do **not** repeat what `@brief` already states.
- Do **not** describe implementation internals (those go in the `.c`/`.cpp` source block).
- Use `@par Title` to split long `@details` into named sub-sections.
- Do **not** embed `/* */` anywhere inside the block (MISRA C:2023 Rule 3.1); use `//` for any inline notes.

---

## Rule 5 — @param direction (mandatory)

Bare `@param` without direction is **prohibited** in Data Patterns projects.  
Every parameter must use one of:

| Tag | When to use |
|---|---|
| `@param[in]  name  desc` | Function reads the value; does not write to pointed-to memory |
| `@param[out] name  desc` | Function writes to pointed-to memory; incoming value is ignored |
| `@param[in,out] name desc` | Function both reads and overwrites the pointed-to value |

**Rules:**
- One `@param` tag per parameter — no grouping multiple params on one line
- Parameter name in the tag must exactly match the declaration spelling
- Description must state: units, valid range, and NULL behaviour for pointers
- `const` pointer parameters → `@param[in]`
- Non-`const` pointer parameters written by the function → `@param[out]`
- Non-`const` pointer parameters read and written → `@param[in,out]`
- Pointer parameters must state whether NULL is permitted or causes undefined behaviour

---

## Rule 6 — @tparam (C++ templates only)

- One `@tparam` per template type parameter
- Must appear **before** all `@param` tags
- Must state type constraints or required interface (e.g. must be POD, must have `toBytes()`)

---

## Rule 7 — @return and @retval

**@return** — general description of what is returned  
**@retval** — one entry per discrete return code or enumerated value

Rules:
- Every non-`void` function **must** have `@return` or at least one `@retval`
- When the function returns a status/error enum, use **both** `@return` (type) and one `@retval` per possible code
- State units for numeric returns (e.g. "in milliseconds", "in dBm")
- State what is returned on error paths
- Do **not** use `@returns` (alias) and `@return` in the same project — pick one
- Do **not** use `@result` — use `@return`

---

## Rule 8 — @throw / @throws / @exception (C++ only)

- One tag per exception type the function can propagate
- Use the fully-qualified exception class name
- State the condition that triggers the throw
- Pick one alias (`@throw` preferred) and use it consistently — do **not** mix

---

## Rule 9 — @pre (Preconditions)

Use `@pre` to state every condition that **must be true before** the function is called.  
The function is not required to check these at runtime (that is a separate coding rule).

Mandatory preconditions to document:
- Hardware or subsystem must be initialised
- Calling context restrictions (ISR, task, thread)
- Non-NULL pointer assumptions
- Value range requirements on inputs
- Required prior function calls (e.g. `Init()` must have been called)
- Mutex or lock must be held / not held

---

## Rule 10 — @post (Postconditions)

Use `@post` to state every condition **guaranteed to be true after the function returns normally**.

Mandatory postconditions to document:
- Output parameter validity (e.g. valid only when return is `true`)
- State changes in hardware or module-level state
- Resources allocated or released
- Buffers modified or cleared
- Error integrators or accumulators reset

---

## Rule 11 — @note

Use for important **usage constraints** that are not safety hazards.  
Examples: thread-safety status, ISR calling context, re-entrancy, platform limitations,  
one-shot vs repeatable calls, performance characteristics.

- Do **not** use `@note` for safety-critical hazards — use `@warning`
- Do **not** overuse — reserve for genuinely important constraints

---

## Rule 12 — @warning

Use for any condition that:
- Accesses hardware registers directly
- Disables or modifies interrupt state
- Energises actuators, motors, or RF transmitters
- Writes to non-volatile memory (EEPROM, Flash)
- Performs an irreversible operation
- Produces physical output (RF, voltage, motion)

`@warning` is **mandatory** whenever any of the above applies.

---

## Rule 13 — @see

Use to cross-reference:
- Companion functions (e.g. Init → DeInit, Open → Close)
- Functions that must be called before or after
- Structs or enums used by this function
- Related module group

Multiple `@see` entries are allowed on separate lines.

---

## Rule 14 — @deprecated (when applicable)

When a function is deprecated:
- State **why** it is deprecated
- State the **replacement** function name
- State the **version** from which the replacement is available
- State the **version** at which this function will be removed

---

## Rule 15 — @todo and @bug (development only)

- `@todo` — flags an incomplete implementation; must include sprint or ticket reference
- `@bug` — documents a known defect; must include issue tracker ID (e.g. JIRA)
- **Neither `@todo` nor `@bug` may remain in a released software baseline**
- CI/CD pipeline must check for and reject these in release builds

---

## Rule 16 — DO-178C Mandatory Tags

For all functions subject to DO-178C, these additional tags are mandatory:

| Tag | Requirement |
|---|---|
| `@requirement{REQ-ID} desc` | Traces to SRS requirement. One tag per requirement satisfied |
| `@testreq{TC-ID: desc}` | Traces to Software Test Specification test case ID |
| `@reviewed` | Applied after formal peer code review; add reviewer name + date in `@note` |
| `@safetyreq{SAF-ID} desc` | Traces to safety requirement (FTA/FMEA/HAZOP); safety-critical functions only |

---

## Rule 17 — MISRA C:2023 Deviations

When a MISRA C:2023 deviation permit is granted for a function, the `@note` tag in the function block **must** state:

1. MISRA rule number and title
2. Deviation permit reference identifier
3. Rationale for the deviation
4. Conditions under which the deviation is valid (e.g. `#ifdef DEBUG_BUILD`)

The LDRA TBManager suppression comment must appear **after** the closing `*/` of the doc block, never inside it.

---

## Rule 18 — Tag Order

Tags must appear in this order within every function documentation block:

```
1.  @brief
2.  @details
3.  @par         (if used)
4.  @tparam      (C++ templates only)
5.  @param[in]
6.  @param[out]
7.  @param[in,out]
8.  @return
9.  @retval      (one per code)
10. @throw       (C++ only)
11. @pre
12. @post
13. @note
14. @warning
15. @attention
16. @deprecated  (if applicable)
17. @todo        (if applicable)
18. @bug         (if applicable)
19. @see
20. @since       (if applicable)
21. @requirement (DO-178C)
22. @testreq     (DO-178C)
23. @safetyreq   (safety-critical)
24. @reviewed    (post code review)
25. @internal    (if internal-only)
```

---

## Rule 19 — Header vs Source File Split

| Location | What to document |
|---|---|
| `.h` / `.hpp` | API contract: `@brief`, `@details`, all `@param`, `@return`/`@retval`, `@pre`, `@post`, `@note`, `@warning`, `@see`, `@throw`, DO-178C tags |
| `.c` / `.cpp` | Implementation notes, algorithm details, MISRA deviation rationale, internal `@note` — use `@internal` to prevent these appearing in public output |

Never duplicate the full doc block in both files.  
If a source file doc block is needed, use `@copydoc FunctionName` to reference the header block, then add source-only content with `@internal`.

---

## Rule 20 — Inline Member Documentation (structs / enums passed to functions)

When a function takes a struct or enum parameter, the struct/enum members must be documented using trailing inline comments:

- Use `/**< description */` for full inline block annotation
- Use `///<  description` for compact single-line annotation
- Align all `*/` or end-of-comment markers in a column for readability
- The `<` modifier is mandatory — without it, the comment documents the next field, not the current one

---

## Prohibited Patterns

| Pattern | Rule violated |
|---|---|
| `/* */` inside a Doxygen block | MISRA C:2023 Rule 3.1 |
| Blank line between doc block and declaration | Severs Doxygen association |
| `@param` without `[in]`/`[out]`/`[in,out]` | DO-178C parameter direction requirement |
| `@return` missing on non-void function | DO-178C interface documentation requirement |
| `@section` inside a function block | Only valid inside `@page` / `@mainpage` |
| Mixing `///` and `//!` in the same file | Consistency rule |
| Mixing `@return` and `@returns` in a project | Consistency rule |
| `@todo` or `@bug` in a release baseline | Quality gate rule |
| Duplicate doc block in both `.h` and `.cpp` | Produces duplicate output; use `@copydoc` |
| `\brief` or `\param` (backslash style) | LDRA/toolchain consistency rule |

---

## Quick Checklist — Before Committing a Function Header

- [ ] Block starts with `/**` — not `/*`
- [ ] No blank line between `*/` and the declaration
- [ ] `@brief` is present and is one line only
- [ ] Every parameter has `@param[in]`, `@param[out]`, or `@param[in,out]`
- [ ] Parameter name matches the declaration exactly
- [ ] `@return` or `@retval` present for every non-void function
- [ ] All `@retval` codes covered for enum return types
- [ ] `@pre` states all init / state / range preconditions
- [ ] `@post` states all output validity and state-change guarantees
- [ ] `@warning` present if function accesses hardware or produces physical output
- [ ] `@see` lists all companion functions
- [ ] `@requirement` and `@testreq` present (DO-178C projects)
- [ ] No `/* */` inside the block (MISRA C:2023 Rule 3.1)
- [ ] No `\param` or `\brief` backslash-style tags
- [ ] MISRA deviation (if any) documented in `@note` with permit reference
- [ ] `@todo` / `@bug` absent if this is a release build
