#!/usr/bin/env python3
"""
Build a reading-ready EPUB (and optionally PDF) from a Book_XX folder of the
Memories Of A Ghost Obsidian vault.

Every chapter .md file in the vault carries two blocks of writer/production
metadata that must NOT reach the reader:

  - a header block between the "# Chapter N — Title" line and the first
    "---", holding the italic saga/part subtitle plus the bold
    Protagonistas / Ventana temporal / Lugar lines.
  - a trailer block starting at a line "*Conecta con: ..." (Obsidian
    [[wikilinks]] to character/concept pages) followed by a "*Nota
    narrativa: ...*" paragraph of editorial history.

This script strips both, concatenates the remaining prose from every part
folder (00_Prologue, Part_01_..., Part_02_..., ...) in reading order, and
hands the result to Pandoc.

Usage:
    python build_epub.py                  # build Book 02 EPUB with defaults
    python build_epub.py --pdf            # also build a PDF
    python build_epub.py --book "11_Books/Book_03_Whatever"  --title "..."
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent

TRAILER_RE = re.compile(r"^\*Conecta con:")


def divider_title(folder_name: str) -> str:
    """'Part_01_Price_of_Vengeance' -> 'Part 01 — Price of Vengeance'
    '00_Prologue' -> 'Prologue'"""
    parts = folder_name.split("_")
    if parts[0].lower() == "part" and len(parts) >= 3:
        return f"Part {parts[1]} — {' '.join(parts[2:])}"
    # drop a leading purely-numeric sort prefix (e.g. "00")
    if parts and parts[0].isdigit():
        parts = parts[1:]
    return " ".join(parts)


def strip_chapter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"{path}: expected first line to be a '# ' title")
    title_line = lines[0]

    try:
        header_end = next(i for i, l in enumerate(lines) if l.strip() == "---")
    except StopIteration:
        raise ValueError(f"{path}: no '---' found to close the header block")

    trailer_start = next(
        (i for i, l in enumerate(lines) if TRAILER_RE.match(l)), len(lines)
    )
    if trailer_start == len(lines):
        print(f"  ! warning: no '*Conecta con:' trailer found in {path.name} "
              f"— kept whole body, check manually", file=sys.stderr)

    body = lines[header_end + 1 : trailer_start]
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()

    return title_line + "\n\n" + "\n".join(body) + "\n"


def collect_manuscript(book_dir: Path) -> str:
    part_dirs = sorted(
        d for d in book_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )
    if not part_dirs:
        raise SystemExit(f"No part folders found under {book_dir}")

    sections = []
    for part_dir in part_dirs:
        chapter_files = sorted(part_dir.glob("*.md"))
        if not chapter_files:
            continue
        print(f"[{part_dir.name}] {len(chapter_files)} chapter(s)")
        sections.append(f"# {divider_title(part_dir.name)}\n")
        for f in chapter_files:
            print(f"  + {f.name}")
            sections.append(strip_chapter(f))

    return "\n\n".join(sections) + "\n"


def build_frontmatter(title: str, subtitle: str, author: str, lang: str) -> str:
    return (
        "---\n"
        f'title: "{title}"\n'
        f'subtitle: "{subtitle}"\n'
        f'author: "{author}"\n'
        f'lang: {lang}\n'
        "---\n\n"
    )


def run_pandoc(manuscript_path: Path, output_path: Path, cover: Path | None,
                css: Path | None, fmt: str) -> None:
    cmd = [
        "pandoc",
        str(manuscript_path),
        "-o", str(output_path),
        "--toc",
        "--toc-depth=1",
        "--split-level=1",
        "--standalone",
    ]
    if cover and cover.exists():
        cmd += ["--epub-cover-image", str(cover)]
    elif cover:
        print(f"  ! warning: cover image not found at {cover}, building without one",
              file=sys.stderr)
    if css and css.exists() and fmt == "epub":
        cmd += ["--css", str(css)]

    print("  $", " ".join(f'"{c}"' if " " in c else c for c in cmd))
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--book", default="11_Books/Book_02_The_King_Of_Shapes",
                     help="book folder, relative to the vault root")
    ap.add_argument("--title", default="King of Shapes")
    ap.add_argument("--subtitle", default="Memories of a Ghost — Book 02")
    ap.add_argument("--author", default="Vic")
    ap.add_argument("--lang", default="es")
    ap.add_argument("--cover",
                     default="99_Reference/book_covers/king_of_shapes_cover.png",
                     help="cover image, relative to the vault root")
    ap.add_argument("--css", default="tools/epub-build/epub_style.css",
                     help="stylesheet, relative to the vault root")
    ap.add_argument("--output-name", default="King_of_Shapes",
                     help="output filename stem, written to tools/epub-build/output/")
    ap.add_argument("--pdf", action="store_true",
                     help="also build a PDF (needs a pandoc PDF engine installed)")
    ap.add_argument("--keep-manuscript", action="store_true",
                     help="don't delete the intermediate combined .md file")
    args = ap.parse_args()

    book_dir = (VAULT_ROOT / args.book).resolve()
    cover = (VAULT_ROOT / args.cover).resolve() if args.cover else None
    css = (VAULT_ROOT / args.css).resolve() if args.css else None
    out_dir = SCRIPT_DIR / "output"
    out_dir.mkdir(exist_ok=True)

    print(f"Building manuscript from {book_dir} ...")
    body = collect_manuscript(book_dir)
    manuscript = build_frontmatter(args.title, args.subtitle, args.author, args.lang) + body

    manuscript_path = out_dir / f"{args.output_name}.manuscript.md"
    manuscript_path.write_text(manuscript, encoding="utf-8")
    print(f"Manuscript written: {manuscript_path} ({len(manuscript):,} chars)")

    epub_path = out_dir / f"{args.output_name}.epub"
    print("Running Pandoc (EPUB) ...")
    run_pandoc(manuscript_path, epub_path, cover, css, "epub")
    print(f"EPUB ready: {epub_path}")

    if args.pdf:
        pdf_path = out_dir / f"{args.output_name}.pdf"
        print("Running Pandoc (PDF) ...")
        try:
            run_pandoc(manuscript_path, pdf_path, cover, css, "pdf")
            print(f"PDF ready: {pdf_path}")
        except subprocess.CalledProcessError:
            print("  ! PDF build failed — you likely need a PDF engine "
                  "(e.g. `choco install miktex` or `--pdf-engine=wkhtmltopdf`).",
                  file=sys.stderr)
            raise

    if not args.keep_manuscript:
        manuscript_path.unlink()


if __name__ == "__main__":
    main()
