#!/usr/bin/env python3
"""Static build checks; no browser or visual approximation involved."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
home = (SITE / "index.html").read_text()
pubs = (SITE / "publications/index.html").read_text()
cv = (SITE / "cv/index.html").read_text()

assert "Yulong" in home and "Chen" in home
assert 'class="post home-about"' in home
assert "Selected Publications" in home
assert '<h2 id="news">News</h2>' in home
assert home.index('<h2 id="news">') < home.index("Selected Publications")
assert "Replace this text with your news" not in home
assert not (SITE / "news/announcement-template").exists()
assert 'class="resource-grid"' in home
assert "Roboto:300,400,500,700" in home
assert 'class="fixed-bottom"' in home
assert "yulong-2026.jpg" in home
assert not (SITE / "blog").exists()
assert not (SITE / "talk").exists()
assert not re.search(r'href=["\'][^"\']*/blog/', home)

for page in (home, pubs, cv):
    for forbidden in ("bestsonta", "SonglinYang4", "sonta.png", "cv_songlin_yang", "Thinking Machines Lab"):
        assert forbidden not in page, forbidden
    assert "{{" not in page and "{%" not in page, "Unrendered Liquid"
    for match in re.finditer(r'(?:src|href)=["\']([^"\']+)["\']', page):
        url = urlsplit(match.group(1))
        if url.scheme or url.netloc or not url.path or not url.path.startswith("/"):
            continue
        target = SITE / unquote(url.path.lstrip("/"))
        assert target.exists(), f"Missing local resource: {url.path}"

assert "chen2026dust" in pubs and "wang2023remote" in pubs
assert "<em>Yulong Chen*</em>" in home
assert "Research Interests" in cv and "Education" in cv
assert not (SITE / "README.md").exists()
assert not (SITE / "Gemfile.ci").exists()
assert not (SITE / "Gemfile.ci.lock").exists()
assert not (SITE / "tests").exists()

manifest = json.loads((ROOT / "UPSTREAM_FILES.json").read_text())
checked = 0
# Deliberate user-requested changes: enlarged paper images and a News heading.
customized = {"_sass/_base.scss", "_layouts/about.html"}
for name, expected in manifest["files"].items():
    if name in customized:
        continue
    if name.startswith(("_sass/", "assets/css/", "assets/fonts/", "assets/webfonts/")) or name in (
        "_layouts/about.html", "_layouts/default.html",
        "_includes/header.html", "_includes/footer.html", "_includes/head.html"
    ):
        raw = (ROOT / name).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        assert actual == expected, f"Original template changed: {name}"
        checked += 1

print(f"PASS: original template ({checked} files), portrait, publication images,")
print("      content migration, local resources, no Blog, no reference-owner data.")
