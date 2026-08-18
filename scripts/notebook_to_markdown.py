#!/usr/bin/env python3
"""Convert a Jupyter notebook into a Markdown include for the Jekyll site.

Each notebook in notebooks/ becomes _includes/notebooks/<slug>.md, which a page in
_resources/ pulls in with {% include notebooks/<slug>.md %}. Images produced by the
notebook are written alongside into images/notebooks/<slug>/.

Because the output is Markdown rather than HTML, Kramdown renders it with the site's
own styling: code picks up Rouge highlighting and prose picks up the normal body type.

Usage:
    python3 scripts/notebook_to_markdown.py                     # convert every notebook
    python3 scripts/notebook_to_markdown.py notebooks/foo.ipynb # convert just one

Cell tags that are honoured:
    remove_cell   drop the cell entirely
    remove_input  keep the output, drop the source
    remove_output keep the source, drop the output
"""

import base64
import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOK_DIR = os.path.join(REPO, "notebooks")
INCLUDE_DIR = os.path.join(REPO, "_includes", "notebooks")
IMAGE_DIR = os.path.join(REPO, "images", "notebooks")

ANSI = re.compile(r"\x1b\[[0-9;]*[a-zA-Z]")

# Notebook language -> fence label used for syntax highlighting.
LANGUAGES = {"python": "python", "ipython": "python", "r": "r", "julia": "julia"}


def text_of(value):
    """Notebook fields are either a string or a list of lines."""
    if isinstance(value, list):
        return "".join(value)
    return value or ""


def fence(body, language=""):
    """Wrap code in a fence, guarding it from Liquid.

    Liquid runs over included files before Markdown does, so a stray {{ or {% in
    notebook code would otherwise be evaluated as template syntax.
    """
    body = body.rstrip("\n")
    if not body.strip():
        return ""
    return "{%% raw %%}\n```%s\n%s\n```\n{%% endraw %%}\n" % (language, body)


class Converter:
    def __init__(self, slug):
        self.slug = slug
        self.image_count = 0
        self.image_dir = os.path.join(IMAGE_DIR, slug)

    def save_image(self, data_b64, extension):
        """Write an embedded image out to disk and return its site-relative URL."""
        if not os.path.isdir(self.image_dir):
            os.makedirs(self.image_dir)
        self.image_count += 1
        name = "output_%d.%s" % (self.image_count, extension)
        with open(os.path.join(self.image_dir, name), "wb") as handle:
            handle.write(base64.b64decode(data_b64))
        return "/images/notebooks/%s/%s" % (self.slug, name)

    def render_bundle(self, bundle):
        """Render one MIME bundle, preferring the richest representation available."""
        for mime, extension in (("image/png", "png"), ("image/jpeg", "jpg")):
            if mime in bundle:
                url = self.save_image(text_of(bundle[mime]).strip(), extension)
                return "![](%s)\n" % url

        if "image/svg+xml" in bundle:
            return '<div class="notebook-output">\n%s\n</div>\n' % text_of(bundle["image/svg+xml"])

        if "text/html" in bundle:
            # Pandas tables and the like. Kramdown passes raw HTML blocks through.
            return '<div class="notebook-output">\n%s\n</div>\n' % text_of(bundle["text/html"])

        if "text/latex" in bundle:
            return text_of(bundle["text/latex"]) + "\n"

        if "text/plain" in bundle:
            return fence(ANSI.sub("", text_of(bundle["text/plain"])))

        return ""

    def render_outputs(self, outputs):
        chunks = []
        for output in outputs:
            kind = output.get("output_type")

            if kind == "stream":
                chunks.append(fence(ANSI.sub("", text_of(output.get("text")))))

            elif kind in ("execute_result", "display_data"):
                chunks.append(self.render_bundle(output.get("data", {})))

            elif kind == "error":
                traceback = "\n".join(output.get("traceback", []))
                chunks.append(fence(ANSI.sub("", traceback)))

        return [c for c in chunks if c]

    def convert(self, notebook):
        language = (
            notebook.get("metadata", {})
            .get("language_info", {})
            .get("name", "python")
            .lower()
        )
        fence_language = LANGUAGES.get(language, language)

        parts = []
        for cell in notebook.get("cells", []):
            tags = cell.get("metadata", {}).get("tags", []) or []
            if "remove_cell" in tags:
                continue

            source = text_of(cell.get("source"))

            if cell.get("cell_type") == "markdown":
                if source.strip():
                    if not parts:
                        # The page supplies its own <h1>, so drop the notebook's.
                        source = re.sub(r"\A\s*#(?!#)[^\n]*\n?", "", source)
                    if source.strip():
                        parts.append(source.rstrip("\n") + "\n")
                continue

            if cell.get("cell_type") != "code":
                continue

            if "remove_input" not in tags:
                block = fence(source, fence_language)
                if block:
                    parts.append(block)

            if "remove_output" not in tags:
                parts.extend(self.render_outputs(cell.get("outputs", [])))

        return "\n".join(parts)


def convert_file(path):
    slug = os.path.splitext(os.path.basename(path))[0]

    with io.open(path, encoding="utf-8") as handle:
        notebook = json.load(handle)

    body = Converter(slug).convert(notebook)

    if not os.path.isdir(INCLUDE_DIR):
        os.makedirs(INCLUDE_DIR)

    banner = (
        "<!-- Generated from %s by scripts/notebook_to_markdown.py. Do not edit by hand. -->\n\n"
        % os.path.relpath(path, REPO)
    )
    destination = os.path.join(INCLUDE_DIR, slug + ".md")
    with io.open(destination, "w", encoding="utf-8") as handle:
        handle.write(banner + body)

    print("%s -> %s" % (os.path.relpath(path, REPO), os.path.relpath(destination, REPO)))


def main(argv):
    paths = argv[1:]

    if not paths:
        if not os.path.isdir(NOTEBOOK_DIR):
            sys.exit("no notebooks/ directory found")
        paths = sorted(
            os.path.join(NOTEBOOK_DIR, name)
            for name in os.listdir(NOTEBOOK_DIR)
            if name.endswith(".ipynb") and not name.startswith(".")
        )

    if not paths:
        sys.exit("no notebooks to convert")

    for path in paths:
        convert_file(path)


if __name__ == "__main__":
    main(sys.argv)
