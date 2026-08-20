# MISRA Guidelines as a Skill

A Claude Code / Agent skill that provides a **reference index** of the
**MISRA C:2023** and **MISRA C++:2023** coding guidelines, kept in separate
bundles.

The skill lives in [`misra-guidelines/`](misra-guidelines/). Its entry point is
[`misra-guidelines/SKILL.md`](misra-guidelines/SKILL.md).

**Installation:** see the step-by-step guide at
[`docs/how-to-add-the-skill.html`](docs/how-to-add-the-skill.html) (open in a
browser). In short: copy the `misra-guidelines/` folder into `~/.claude/skills/`
(personal) or `.claude/skills/` (per-project), start a fresh session, and Claude
loads it automatically when you ask about MISRA / C / C++ compliance.

**Consolidated reference document:** every directive and rule (C and C++) in one
document, with rationale and examples:
- [`docs/misra-guidelines-reference.html`](docs/misra-guidelines-reference.html) — styled, theme-aware, print-ready
- [`docs/misra-guidelines-reference.pdf`](docs/misra-guidelines-reference.pdf) — portable/printable

Regenerate it from the source markdown any time with:

```
python3 scripts/build_reference_doc.py
```

## What it covers

| Standard        | Total | Directives | Rules | Base language        |
|-----------------|-------|-----------|-------|----------------------|
| MISRA C:2023    | ~221  | ~21       | ~200  | C90 / C99 / C11 / C18|
| MISRA C++:2023  | 179   | 4         | 175   | C++17                |

Every entry records the guideline's **ID**, **category** (Mandatory / Required /
Advisory), **decidability**, and a **paraphrased summary** of its intent.

## Layout

```
misra-guidelines/
├── SKILL.md                 # router + how to use
├── c/
│   ├── overview.md          # categories, essential type model, deviations
│   ├── directives.md        # Dir 1.x – 4.x (+ later additions)
│   └── rules/               # rules grouped by section (§1–§22)
└── cpp/
    ├── overview.md          # categories, ID scheme, C++17 clause structure
    └── rules/
        ├── directives.md
        └── representative-rules.md
```

## Important notes

- **Copyright:** MISRA guideline text is © MISRA / HORIBA MIRA Ltd. This skill
  contains **paraphrased summaries only** — not the official wording — and is not
  a substitute for the purchased standard.
- **Accuracy:** The MISRA C index is grounded in the long-established MISRA
  C:2012 rule set plus its amendments; entries added/changed by amendments are
  flagged `⚑verify`. The MISRA C++:2023 rule list is provided as an accurate
  structural framework plus a representative rule set (also `⚑verify`), because
  the authoritative enumeration was not reachable in the build environment. See
  `cpp/overview.md` for how to complete it to all 175 rules.
- Always defer to the **official MISRA document** for certification/compliance
  work.
