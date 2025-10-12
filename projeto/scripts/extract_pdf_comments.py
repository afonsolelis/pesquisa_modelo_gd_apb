#!/usr/bin/env python3
import sys
import os
from typing import List

try:
    import fitz  # PyMuPDF
except Exception as e:
    print("Erro: PyMuPDF não está instalado (pacote 'pymupdf').")
    sys.exit(2)


def format_annot_entry(page_num: int, annot) -> List[str]:
    info = getattr(annot, "info", {}) or {}
    author = info.get("title") or info.get("author") or ""
    subject = info.get("subject") or ""
    content = info.get("content") or ""
    created = info.get("creationDate") or info.get("creationdate") or ""
    modified = info.get("modDate") or info.get("moddate") or ""

    try:
        atype = annot.type[1]  # (code, name)
    except Exception:
        atype = str(getattr(annot, "type", ""))

    lines = [f"Página {page_num} | Tipo: {atype} | Autor: {author or '—'}"]
    if subject:
        lines.append(f"Assunto: {subject}")
    if content:
        lines.append(f"Comentário: {content}")
    if created or modified:
        lines.append(
            f"Datas: criado={created or '—'} | modificado={modified or '—'}"
        )
    lines.append("-" * 60)
    return lines


def main() -> int:
    if len(sys.argv) < 2:
        print("Uso: extract_pdf_comments.py <caminho_para_pdf>")
        return 1

    pdf_path = sys.argv[1]
    if not os.path.isfile(pdf_path):
        print(f"Arquivo não encontrado: {pdf_path}")
        return 1

    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Falha ao abrir PDF: {e}")
        return 1

    output_lines: List[str] = []
    total_annots = 0

    for i in range(doc.page_count):
        page = doc.load_page(i)
        annot = page.first_annot
        while annot is not None:
            # Considerar como comentário apenas quando há conteúdo/subject, ou notas de texto
            info = getattr(annot, "info", {}) or {}
            has_content = bool((info.get("content") or info.get("subject") or "").strip())
            try:
                atype_name = annot.type[1]
            except Exception:
                atype_name = ""

            if has_content or atype_name.lower() in {"text"}:  # sticky notes normalmente têm conteúdo
                output_lines.extend(format_annot_entry(i + 1, annot))
                total_annots += 1

            annot = annot.next

    base = os.path.splitext(os.path.basename(pdf_path))[0]
    out_dir = os.path.dirname(os.path.abspath(pdf_path))
    out_path = os.path.join(out_dir, f"{base}_comentarios.txt")

    if total_annots == 0:
        output = ["Nenhum comentário encontrado."]
    else:
        header = [
            f"Arquivo: {os.path.basename(pdf_path)}",
            f"Total de comentários: {total_annots}",
            "=" * 60,
        ]
        output = header + output_lines

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output) + "\n")

    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

