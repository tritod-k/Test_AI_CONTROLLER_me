import re
from pathlib import Path
import pytest

SITE_ROOT = Path(__file__).parent.parent


def _read(rel_path: str) -> str:
    p = SITE_ROOT / rel_path
    assert p.is_file(), f"File {rel_path} does not exist"
    return p.read_text(encoding="utf-8")


def test_html_structure_and_doctype():
    '''1. HTML5 DOCTYPE, lang='en', head, body, and title exist.'''
    html = _read("index.html")
    assert "<!DOCTYPE html>" in html
    assert '<html lang="en">' in html
    assert "<head>" in html and "</head>" in html
    assert "<body>" in html and "</body>" in html
    assert "<title>" in html and "K.TRITOD" in html


def test_viewport_meta_tag():
    '''2. Responsive viewport meta tag configured.'''
    html = _read("index.html")
    assert '<meta name="viewport" content="width=device-width, initial-scale=1.0">' in html


def test_all_required_sections_exist():
    '''3. All 7 required sections exist with correct IDs.'''
    html = _read("index.html")
    required_ids = [
        "home",
        "about",
        "engineering-skills",
        "software-automation",
        "projects",
        "contact",
        "github",
    ]
    for section_id in required_ids:
        assert f'id="{section_id}"' in html, f"Missing required section id='{section_id}'"


def test_internal_anchor_links():
    '''4. Every internal anchor link targets an existing element ID.'''
    html = _read("index.html")
    hrefs = re.findall(r'href="(#[a-zA-Z0-9_\-]+)"', html)
    assert len(hrefs) >= 5, "Expected at least 5 internal anchor links"
    for href in hrefs:
        target_id = href[1:]
        assert f'id="{target_id}"' in html, f"Broken internal anchor href='{href}' targets missing id='{target_id}'"


def test_images_exist_and_non_empty():
    '''5. All referenced images exist on disk and have non-zero size.'''
    html = _read("index.html")
    srcs = re.findall(r'<img[^>]+src="([^">]+)"', html)
    assert len(srcs) >= 4, "Expected at least 4 image references"
    for src in srcs:
        img_path = SITE_ROOT / src
        assert img_path.is_file(), f"Referenced image {src} not found on disk"
        assert img_path.stat().st_size > 0, f"Image {src} is empty"


def test_images_have_alt_attributes():
    '''6. Accessibility: All images have non-empty alt attributes.'''
    html = _read("index.html")
    img_tags = re.findall(r'<img[^>]+>', html)
    assert len(img_tags) >= 4
    for tag in img_tags:
        assert 'alt="' in tag, f"Image tag missing alt: {tag}"
        alt_match = re.search(r'alt="([^"]*)"', tag)
        assert alt_match and alt_match.group(1).strip(), f"Image has empty alt: {tag}"


def test_nav_accessibility_attributes():
    '''7. Accessibility: Mobile navigation toggle button has aria-label, aria-expanded, aria-controls.'''
    html = _read("index.html")
    assert 'class="nav-toggle"' in html
    assert 'aria-label="Toggle navigation menu"' in html
    assert 'aria-expanded="false"' in html
    assert 'aria-controls="nav-links"' in html


def test_github_links_valid():
    '''8. External GitHub links point to https://github.com/tritod-k.'''
    html = _read("index.html")
    gh_links = re.findall(r'href="(https://github\.com/tritod-k[^"]*)"', html)
    assert len(gh_links) >= 2, "Expected at least 2 github.com/tritod-k links"
    for link in gh_links:
        assert link.startswith("https://github.com/tritod-k")


def test_css_responsive_rules():
    '''9. CSS includes custom variables, flex/grid layouts, and responsive media queries.'''
    css = _read("css/style.css")
    assert ":root" in css
    assert "--bg-primary:" in css
    assert "@media (max-width: 768px)" in css
    assert "display: flex" in css
    assert "display: grid" in css


def test_privacy_leak_protection():
    '''10. Privacy Guard: Zero occurrences of private emails, personal photos, or credentials.'''
    forbidden_terms = [
        "hot" + "mail.com",
        "joke.jpg",
        "carE30.jpg",
        "081-",
        "089-",
        "086-",
        "password",
        "secret_key",
    ]
    for ext in ["*.html", "*.css", "*.js", "*.py", "*.md", "*.yaml"]:
        for file_path in SITE_ROOT.rglob(ext):
            if ".git" in file_path.parts or file_path.name == "test_website.py" or "artifacts" in file_path.parts:
                continue
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            for term in forbidden_terms:
                assert term.lower() not in text.lower(), f"Forbidden privacy leak '{term}' found in {file_path}"


def test_nojekyll_and_readme():
    '''11. GitHub Pages .nojekyll flag and README documentation exist.'''
    assert (SITE_ROOT / ".nojekyll").is_file(), ".nojekyll missing"
    readme = _read("README.md")
    assert "# K.TRITOD" in readme or "Personal Portfolio" in readme
    assert len(readme) > 200, "README.md is too short"


def test_antigravity_live_enhancement():
    '''12. Live verification badge and back-to-top accessibility link.'''
    html = _read("index.html")
    assert 'id="aipc-live-badge"' in html
    assert 'aria-label="Back to top"' in html

