#!/usr/bin/env python3
"""
Genera PDFs por capítulo para los Módulos 3 al 12 del libro
"Ingeniería de IA desde los Fundamentos".

Fuente:  ModuloX/v1.0/
Salida:  ModuloX/pdf/
"""

import os
import re
import subprocess
import tempfile
from pathlib import Path
import markdown as md_lib

BASE = Path("/home/notebian/Documentos/capacitacion-ia/Libro-IIngenieria-de-IA-desde-los-Fundamentos")

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

p {
    margin: 0 0 0.9em 0;
    text-align: justify;
    hyphens: auto;
}

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

ul, ol {
    margin: 0.4em 0 0.9em 0;
    padding-left: 1.6em;
}

li {
    margin-bottom: 0.3em;
    line-height: 1.65;
}

li > ul, li > ol { margin: 0.2em 0 0.3em 0; }

hr {
    border: none;
    border-top: 1px solid #c5d0de;
    margin: 2em 0;
}

strong { color: #0d2240; }
em     { color: #333; }

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


def get_chapters(v10_dir: Path) -> dict:
    """Auto-descubre capítulos y sus secciones desde el directorio v1.0."""
    chapters = {}
    pattern = re.compile(r"Capitulo-(\d+)-Seccion-(\d+)-v1\.0\.md")
    for f in sorted(v10_dir.glob("Capitulo-*-Seccion-*-v1.0.md")):
        m = pattern.match(f.name)
        if m:
            cap = m.group(1)   # "01", "02", etc.
            sec = int(m.group(2))
            if cap not in chapters:
                chapters[cap] = []
            chapters[cap].append(sec)
    for cap in chapters:
        chapters[cap].sort()
    return dict(sorted(chapters.items()))


def build_html(module_num: int, cap: str, sections: list, v10_dir: Path) -> str:
    parts = []
    for sec in sections:
        fn = v10_dir / f"Capitulo-{cap}-Seccion-{str(sec).zfill(2)}-v1.0.md"
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
  <title>Capítulo {int(cap)} — Módulo {module_num}</title>
  <style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""


def html_to_pdf(html_path: Path, pdf_path: Path) -> bool:
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


def process_module(module_num: int):
    v10_dir = BASE / f"Modulo{module_num}/v1.0"
    pdf_dir = BASE / f"Modulo{module_num}/pdf"

    if not v10_dir.exists():
        print(f"  ✗  Módulo {module_num}: no existe v1.0/")
        return

    chapters = get_chapters(v10_dir)
    if not chapters:
        print(f"  ✗  Módulo {module_num}: no se encontraron archivos en v1.0/")
        return

    pdf_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n{'='*50}")
    print(f"  MÓDULO {module_num}  ({len(chapters)} capítulos)")
    print(f"{'='*50}")

    for cap, sections in chapters.items():
        print(f"\n  ── Capítulo {cap} ({len(sections)} secciones) ──")

        html_content = build_html(module_num, cap, sections, v10_dir)

        tmp_html = pdf_dir / f"_tmp_mod{module_num}_cap{cap}.html"
        tmp_html.write_text(html_content, encoding="utf-8")

        pdf_out = pdf_dir / f"Capitulo-{cap}.pdf"
        ok = html_to_pdf(tmp_html, pdf_out)
        tmp_html.unlink(missing_ok=True)

        if ok:
            size = pdf_out.stat().st_size
            print(f"  ✓  {pdf_out.name}  ({size:,} bytes)")
        else:
            print(f"  ✗  Error generando {pdf_out.name}")


def main():
    for module_num in range(3, 13):
        process_module(module_num)

    print("\n\n✓ Proceso terminado.")
    print("PDFs generados en ModuloX/pdf/ para módulos 3 al 12.")


if __name__ == "__main__":
    main()
