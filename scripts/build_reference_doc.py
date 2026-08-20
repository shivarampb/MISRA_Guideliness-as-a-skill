#!/usr/bin/env python3
"""Build a single styled HTML reference document from the skill's markdown files.

Reads the MISRA C and C++ guideline markdown, converts a focused subset of
Markdown to HTML, and emits a self-contained, print-ready reference document.
Run from the repo root:  python3 scripts/build_reference_doc.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "misra-guidelines"

# (section title, source file) in reading order
SOURCES = [
    ("MISRA C:2023 — Overview",              SKILL / "c/overview.md"),
    ("MISRA C:2023 — Directives",            SKILL / "c/directives.md"),
    ("MISRA C:2023 — Rules §1–§6",           SKILL / "c/rules/01-06-environment-and-types.md"),
    ("MISRA C:2023 — Rules §7–§9",           SKILL / "c/rules/07-09-constants-declarations-init.md"),
    ("MISRA C:2023 — Rules §10–§11",         SKILL / "c/rules/10-11-types-and-pointers.md"),
    ("MISRA C:2023 — Rules §12–§16",         SKILL / "c/rules/12-16-expressions-and-control.md"),
    ("MISRA C:2023 — Rules §17–§19",         SKILL / "c/rules/17-19-functions-pointers-storage.md"),
    ("MISRA C:2023 — Rules §20",             SKILL / "c/rules/20-preprocessing.md"),
    ("MISRA C:2023 — Rules §21–§22",         SKILL / "c/rules/21-22-libraries-and-resources.md"),
    ("MISRA C++:2023 — Overview",            SKILL / "cpp/overview.md"),
    ("MISRA C++:2023 — Directives",          SKILL / "cpp/rules/directives.md"),
    ("MISRA C++:2023 — Rules",               SKILL / "cpp/rules/representative-rules.md"),
]


def inline(text: str) -> str:
    """Convert inline markdown (escaping HTML first, then re-adding markup)."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        # inline code
        if ch == "`":
            j = text.find("`", i + 1)
            if j != -1:
                out.append("<code>" + html.escape(text[i + 1:j]) + "</code>")
                i = j + 1
                continue
        # links [t](u)
        m = re.match(r"\[([^\]]+)\]\(([^)]+)\)", text[i:])
        if m:
            out.append('<a href="%s">%s</a>' % (html.escape(m.group(2)), html.escape(m.group(1))))
            i += m.end()
            continue
        # bold **..**
        if text.startswith("**", i):
            j = text.find("**", i + 2)
            if j != -1:
                out.append("<strong>" + html.escape(text[i + 2:j]) + "</strong>")
                i = j + 2
                continue
        # italic *..*
        if ch == "*":
            j = text.find("*", i + 1)
            if j != -1 and j != i + 1:
                out.append("<em>" + html.escape(text[i + 1:j]) + "</em>")
                i = j + 1
                continue
        out.append(html.escape(ch))
        i += 1
    return "".join(out)


CODE_KW = {
    "c": r"\b(int|char|void|const|static|inline|struct|union|enum|unsigned|signed|"
         r"short|long|float|double|return|if|else|for|while|switch|case|default|"
         r"break|goto|sizeof|typedef|extern|volatile|restrict|_Atomic|_Noreturn)\b",
    "cpp": r"\b(int|char|void|const|constexpr|static|inline|struct|class|union|enum|"
           r"unsigned|signed|short|long|float|double|bool|auto|return|if|else|for|"
           r"while|switch|case|default|break|goto|sizeof|typedef|using|namespace|"
           r"template|typename|virtual|override|final|explicit|noexcept|throw|try|"
           r"catch|new|delete|nullptr|public|private|protected|this|std)\b",
}


def highlight(code: str, lang: str) -> str:
    esc = html.escape(code)
    # comments
    esc = re.sub(r"(//[^\n]*)", r'<span class="c">\1</span>', esc)
    esc = re.sub(r"(/\*.*?\*/)", r'<span class="c">\1</span>', esc, flags=re.S)
    if lang in CODE_KW:
        esc = re.sub(CODE_KW[lang], r'<span class="k">\1</span>', esc)
    return esc


def convert(md: str) -> str:
    lines = md.split("\n")
    html_out = []
    i = 0
    in_list = False

    def close_list():
        nonlocal in_list
        if in_list:
            html_out.append("</ul>")
            in_list = False

    while i < len(lines):
        line = lines[i]

        # fenced code
        if line.startswith("```"):
            lang = line[3:].strip()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            close_list()
            html_out.append('<pre class="code"><code>%s</code></pre>'
                            % highlight("\n".join(buf), lang))
            continue

        # tables
        if line.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            close_list()
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ['<div class="tablewrap"><table><thead><tr>']
            t += ["<th>%s</th>" % inline(h) for h in header]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            html_out.append("".join(t))
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_list()
            level = len(m.group(1))
            html_out.append("<h%d>%s</h%d>" % (level, inline(m.group(2)), level))
            i += 1
            continue

        # hr
        if re.match(r"^---+\s*$", line):
            close_list()
            html_out.append("<hr>")
            i += 1
            continue

        # blockquote
        if line.startswith(">"):
            close_list()
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").strip())
                i += 1
            html_out.append('<blockquote>%s</blockquote>' % inline(" ".join(buf)))
            continue

        # list item
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            if not in_list:
                html_out.append("<ul>")
                in_list = True
            html_out.append("<li>%s</li>" % inline(m.group(1)))
            i += 1
            continue

        # blank
        if not line.strip():
            close_list()
            i += 1
            continue

        # paragraph (gather until blank / structural)
        close_list()
        buf = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#{1,6}\s|```|>|\s*[-*]\s|\|)", lines[i]) and not re.match(r"^---+\s*$", lines[i]):
            buf.append(lines[i])
            i += 1
        html_out.append("<p>%s</p>" % inline(" ".join(buf)))

    close_list()
    return "\n".join(html_out)


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def main():
    body_parts = []
    toc = []
    for title, path in SOURCES:
        if not path.exists():
            continue
        sid = slug(title)
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, html.escape(title)))
        body_parts.append('<section id="%s" class="doc-section">' % sid)
        body_parts.append('<div class="section-eyebrow">%s</div>'
                          % ("MISRA C++" if "C++" in title else "MISRA C"))
        body_parts.append(convert(path.read_text()))
        body_parts.append("</section>")

    template = (ROOT / "scripts" / "doc_template.html").read_text()
    out = template.replace("<!--TOC-->", "\n".join(toc)).replace("<!--BODY-->", "\n".join(body_parts))
    dest = ROOT / "docs" / "misra-guidelines-reference.html"
    dest.write_text(out)
    print("Wrote", dest, "(%d bytes)" % len(out))


if __name__ == "__main__":
    main()
