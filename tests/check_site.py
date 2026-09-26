#!/usr/bin/env python3
"""Validate generated pages without restricting editable content."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = (ROOT / "_site").resolve()


class ResourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ("src", "href", "poster") and value:
                self.references.append((tag, name, value))

    handle_startendtag = handle_starttag


def main():
    if not (SITE / "index.html").is_file():
        raise AssertionError("Missing homepage: index.html")

    pages = sorted(SITE.rglob("*.html"))
    checked = 0

    for page in pages:
        parser = ResourceParser()
        parser.feed(page.read_text(encoding="utf-8"))

        for tag, attribute, value in parser.references:
            url = urlsplit(value)

            # Skip external URLs and fragment-only links.
            if url.scheme or url.netloc or not url.path:
                continue

            path = unquote(url.path)
            if path.startswith("/"):
                target = SITE / path.lstrip("/")
            else:
                target = page.parent / path
            target = target.resolve()

            try:
                target.relative_to(SITE)
            except ValueError:
                raise AssertionError(
                    f"{page.relative_to(SITE)}: "
                    f"resource escapes site root: {value}"
                )

            if not target.exists():
                raise AssertionError(
                    f"{page.relative_to(SITE)}: "
                    f"missing local resource ({tag} {attribute}): {value}"
                )

            checked += 1

    # Prevent build tooling from being published as website content.
    for name in (
        "README.md",
        "Gemfile",
        "Gemfile.lock",
        "Gemfile.ci",
        "Gemfile.ci.lock",
        "tests",
        "scripts",
    ):
        if (SITE / name).exists():
            raise AssertionError(
                f"Build-only file included in website: {name}"
            )

    print(
        f"PASS: {len(pages)} HTML pages and "
        f"{checked} local resource references checked."
    )


if __name__ == "__main__":
    main()
