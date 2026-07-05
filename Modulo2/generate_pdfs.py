#!/usr/bin/env python3
"""
Genera PDFs por capítulo para el Módulo 2 del libro
"Ingeniería de IA desde los Fundamentos".

Fuente: Modulo2/v1.0/
Salida: Modulo2/pdf/
"""

import os
import re
import subprocess
import tempfile
from pathlib import Path
import markdown as md_lib

BASE = Path("/home/notebian/Documentos/capacitacion-ia/Libro-IIngenieria-de-IA-desde-los-Fundamentos")
V10  = BASE / "Modulo2/v1.0"
PDF  = BASE / "Modulo2/pdf"

CHAPTERS = {
    16: list(range(1, 11)),   # 10 secciones
    17: list(range(1, 10)),   # 9 secciones
    18: list(range(1, 10)),   # 9 secciones
    19: list(range(1, 10)),   # 9 secciones
    20: list(range(1, 8)),    # 7 secciones
    21: list(range(1, 8)),    # 7 secciones
    22: list(range(1, 8)),    # 7 secciones
}

CSS = """
@page {
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2.5cm;
}

* { box-sizing: border-box; }

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.75;
    color: #1a1a1a;
}

/* ── Títulos ── */
h1 {
    font-family: 'Arial', 'Helvetica', sans-serif;
    font-size: 20pt;
    color: #0d2240;
    margin-top: 2.5em;
    margin-bottom: 0.4em;
    padding-bottom: 0.3em;
    border-bottom: 3px solid #0d2240;
    page-break-before: always;
}
h1:first-child { page-break-before: avoid; }

h2 {
    font-family: 'Arial', 'Helvetica', sans-serif;
    font-size: 15pt;
    color: #1a3a5c;
    margin-top: 1.8em;
    margin-bottom: 0.3em;
    border-left: 4px solid #1a3a5c;
    padding-left: 0.6em;
}

h3 {
    font-family: 'Arial', 'Helvetica', sans-serif;
    font-size: 12pt;
    color: #2a4f78;
    margin-top: 1.4em;
    margin-bottom: 0.2em;
}

h4 {
    font-family: 'Arial', 'Helvetica', sans-serif;
    font-size: 11pt;
    color: #3a6494;
    margin-top: 1em;
    margin-bottom: 0.15em;
    font-style: italic;
}

/* ── Párrafos ── */
p {
    margin: 0 0 0.9em 0;
    text-align: justify;
    hyphens: auto;
}

/* ── Citas ── */
blockquote {
    border-left: 4px solid #0d2240;
    margin: 1.2em 0;
    padding: 0.7em 1.4em;
    background: #f0f4f8;
    border-radius: 0 5px 5px 0;
    font-style: italic;
    color: #333;
}
blockquote p { margin: 0; }

/* ── Código ── */
code {
    font-family: 'Courier New', Courier, monospace;
    font-size: 9pt;
    background: #f0f0f0;
    padding: 0.1em 0.35em;
    border-radius: 3px;
    color: #c0392b;
}

pre {
    background: #1e1e2e;
    border-radius: 6px;
    padding: 1em 1.2em;
    margin: 1em 0;
    overflow-x: auto;
    page-break-inside: avoid;
}

pre code {
    font-size: 8.5pt;
    line-height: 1.55;
    color: #cdd6f4;
    background: none;
    padding: 0;
}

/* ── Tablas ── */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.2em 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

thead th {
    background: #0d2240;
    color: #ffffff;
    padding: 0.55em 0.8em;
    text-align: left;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
    font-size: 9pt;
}

tbody td {
    border: 1px solid #c5d0de;
    padding: 0.45em 0.8em;
    vertical-align: top;
}

tbody tr:nth-child(even) td { background: #f5f8fc; }

/* ── Listas ── */
ul, ol {
    margin: 0.4em 0 0.9em 0;
    padding-left: 1.6em;
}

li {
    margin-bottom: 0.3em;
    line-height: 1.65;
}

li > ul, li > ol { margin: 0.2em 0 0.3em 0; }

/* ── Separadores ── */
hr {
    border: none;
    border-top: 1px solid #c5d0de;
    margin: 2em 0;
}

/* ── Énfasis ── */
strong { color: #0d2240; }
em     { color: #333; }

/* ── Diagramas Mermaid ── */
.mermaid-box {
    text-align: center;
    margin: 1.5em 0;
    page-break-inside: avoid;
}

.mermaid-box svg {
    max-width: 100%;
    height: auto;
}

.mermaid-fallback {
    font-family: 'Courier New', monospace;
    font-size: 8pt;
    background: #f8f8f8;
    border: 1px dashed #aaa;
    padding: 0.8em;
    border-radius: 4px;
    overflow-x: auto;
    color: #555;
}
"""


def render_mermaid(code: str, idx: int, tmp: Path) -> str:
    """Convierte un bloque mermaid a SVG inline. Fallback a pre si falla."""
    mmd = tmp / f"d{idx}.mmd"
    svg = tmp / f"d{idx}.svg"
    mmd.write_text(code, encoding="utf-8")

    try:
        result = subprocess.run(
            ["mmdc", "-i", str(mmd), "-o", str(svg),
             "-b", "transparent", "--width", "850"],
            capture_output=True, text=True, timeout=30
        )
        if svg.exists():
            content = svg.read_text(encoding="utf-8")
            content = re.sub(r"<\?xml[^>]+\?>\s*", "", content)
            return f'<div class="mermaid-box">{content}</div>'
    except Exception:
        pass

    safe = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<pre class="mermaid-fallback">{safe}</pre>'


def md_to_html_body(combined: str, tmp: Path) -> str:
    """Convierte markdown combinado a HTML body, pre-renderizando mermaid."""
    mermaid_re = re.compile(r"```mermaid\n(.*?)\n```", re.DOTALL)
    counter = [0]
    placeholders: dict[str, str] = {}

    def replacer(m):
        key = f"MMSVG{counter[0]}END"
        placeholders[key] = render_mermaid(m.group(1), counter[0], tmp)
        counter[0] += 1
        return key

    md_processed = mermaid_re.sub(replacer, combined)

    body = md_lib.markdown(
        md_processed,
        extensions=["tables", "fenced_code", "nl2br"],
        output_format="html"
    )

    for key, svg in placeholders.items():
        body = body.replace(key, svg)

    return body


def build_html(chapter_num: int, sections: list[int]) -> str:
    """Lee secciones, las combina y devuelve HTML completo."""
    parts = []
    for sec in sections:
        fn = V10 / f"Capitulo-{chapter_num}-Seccion-{str(sec).zfill(2)}-v1.0.md"
        if fn.exists():
            if parts:
                parts.append("\n\n---\n\n")
            parts.append(fn.read_text(encoding="utf-8"))
        else:
            print(f"  ⚠  No encontrado: {fn.name}")

    combined = "".join(parts)

    with tempfile.TemporaryDirectory() as tmp_str:
        tmp = Path(tmp_str)
        body = md_to_html_body(combined, tmp)

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Capítulo {chapter_num} — Módulo 2</title>
  <style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""


def html_to_pdf(html_path: Path, pdf_path: Path) -> bool:
    """Usa Chrome headless para convertir HTML a PDF."""
    result = subprocess.run(
        [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-software-rasterizer",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={pdf_path}",
            "--print-to-pdf-no-header",
            str(html_path),
        ],
        capture_output=True, text=True, timeout=120
    )
    return pdf_path.exists()


def main():
    PDF.mkdir(parents=True, exist_ok=True)

    for chapter_num, sections in CHAPTERS.items():
        print(f"\n── Capítulo {chapter_num} ──")

        html_content = build_html(chapter_num, sections)

        # Escribir HTML en archivo temporal
        tmp_html = PDF / f"_tmp_cap{chapter_num}.html"
        tmp_html.write_text(html_content, encoding="utf-8")

        pdf_out = PDF / f"Capitulo-{chapter_num}.pdf"

        ok = html_to_pdf(tmp_html, pdf_out)
        tmp_html.unlink(missing_ok=True)

        if ok:
            size = pdf_out.stat().st_size
            print(f"  ✓  {pdf_out.name}  ({size:,} bytes)")
        else:
            print(f"  ✗  Error generando {pdf_out.name}")

    print("\n✓ Proceso terminado. PDFs en:", PDF)


if __name__ == "__main__":
    main()
