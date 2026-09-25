# Template origin

This site uses Songlin Yang's customized **al-folio** template directly:

- Source: https://github.com/sustcsonglin/sustcsonglin.github.io
- Pinned commit: `f22b5b71ced1aaed7e667510a3ba51efa65f65b5`
- License: MIT. The upstream `LICENSE` is preserved.
- Original al-folio: https://github.com/alshedivat/al-folio

The Sass styles, main page layouts, header, footer, fonts, and theme
scripts are retained from this snapshot. This is not a separately designed
approximation. `UPSTREAM_FILES.json` records the original Git blob hashes.

Changes:

- Replace personal information, portraits, links, CV data, and publications.
- Do not import blog posts or the Blog page; disable blog/RSS features.
- Enable the native publication `preview` field and image zoom.
- Widen publication images to four Bootstrap columns, with eight columns
  for the text. Raise the preview size cap from 200px to 320px.
- Enable News above Selected Publications, with a non-linking heading and
  date-sorted entries. Leave the section empty pending the owner's updates.
- Hide Talks until the owner has talk entries.
- Trim unused build plugins and add a GitHub Pages deployment workflow.

No biography, publications, social accounts, analytics identifiers, or
photographs belonging to the reference site's author are used.
