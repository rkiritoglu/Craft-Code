#!/usr/bin/env python3
"""
Craft&Code Static Site Generator
Unified Bilingual (TR/EN) Engine with Curatorial Studio.
"""

import os
import sys
import re
import shutil
import json
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent
CONTENT_DIR = ROOT_DIR / "content"
PUBLIC_DIR = ROOT_DIR / "public"
DIST_DIR = ROOT_DIR / "dist"
TEMPLATES_DIR = ROOT_DIR / "templates"

def parse_markdown(text):
    frontmatter = {}
    content = text

    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        content = text[fm_match.end():]
        for line in fm_text.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if val.lower() == "true":
                    val = True
                elif val.lower() == "false":
                    val = False
                elif val.startswith("[") and val.endswith("]"):
                    val = [item.strip().strip('"').strip("'") for item in val[1:-1].split(",") if item.strip()]
                frontmatter[key] = val

    lines = content.splitlines()
    html_parts = []
    in_list = False
    list_type = "ul"
    in_curatorial = False

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            continue

        if stripped.startswith(":::curatorial"):
            badge_text = stripped.replace(":::curatorial", "").strip() or "Curatorial Note"
            html_parts.append(f'<div class="curatorial-box"><span class="badge">{badge_text}</span>')
            in_curatorial = True
            continue
        elif stripped == ":::":
            if in_curatorial:
                html_parts.append('</div>')
                in_curatorial = False
            continue

        h3_match = re.match(r"^###\s+(.*)", stripped)
        h2_match = re.match(r"^##\s+(.*)", stripped)
        h1_match = re.match(r"^#\s+(.*)", stripped)

        if h3_match:
            html_parts.append(f"<h3>{format_inline(h3_match.group(1))}</h3>")
            continue
        if h2_match:
            html_parts.append(f"<h2>{format_inline(h2_match.group(1))}</h2>")
            continue
        if h1_match:
            html_parts.append(f"<h1>{format_inline(h1_match.group(1))}</h1>")
            continue

        if stripped.startswith(">"):
            quote_text = stripped.lstrip(">").strip()
            if " -- " in quote_text:
                q, cite = quote_text.split(" -- ", 1)
                html_parts.append(f"<blockquote><p>{format_inline(q)}</p><cite>— {cite}</cite></blockquote>")
            else:
                html_parts.append(f"<blockquote><p>{format_inline(quote_text)}</p></blockquote>")
            continue

        if stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list:
                in_list = True
                list_type = "ul"
                html_parts.append("<ul>")
            html_parts.append(f"<li>{format_inline(stripped[2:])}</li>")
            continue

        num_match = re.match(r"^\d+\.\s+(.*)", stripped)
        if num_match:
            if not in_list:
                in_list = True
                list_type = "ol"
                html_parts.append("<ol>")
            html_parts.append(f"<li>{format_inline(num_match.group(1))}</li>")
            continue

        if in_list:
            html_parts.append(f"</{list_type}>")
            in_list = False

        fig_match = re.match(r'^!\[(.*?)\]\((.*?)(?:\s+"(.*?)")?\)$', stripped)
        if fig_match:
            alt = fig_match.group(1)
            src = fig_match.group(2)
            meta = fig_match.group(3) or ""
            caption = meta
            credit = ""
            if "|" in meta:
                caption, credit = [x.strip() for x in meta.split("|", 1)]
            
            fig_html = f'<figure class="article-figure"><img src="{src}" alt="{alt}" loading="lazy"/>'
            if caption or credit:
                fig_html += f'<figcaption><strong>{caption}</strong>'
                if credit:
                    fig_html += f'<span class="credit">{credit}</span>'
                fig_html += '</figcaption>'
            fig_html += '</figure>'
            html_parts.append(fig_html)
            continue

        html_parts.append(f"<p>{format_inline(stripped)}</p>")

    if in_list:
        html_parts.append(f"</{list_type}>")
    if in_curatorial:
        html_parts.append('</div>')

    return frontmatter, "\n".join(html_parts)

def format_inline(text):
    text = re.sub(r"\*\*\*(.*?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.*?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', text)
    return text

def calculate_reading_time(text):
    words = len(re.findall(r"\w+", text))
    return max(1, round(words / 180))

def build_site(include_drafts=True):
    print("✨ Building Craft&Code...")
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    for child in list(DIST_DIR.iterdir()):
        try:
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
        except Exception:
            pass

    if PUBLIC_DIR.exists():
        shutil.copytree(PUBLIC_DIR, DIST_DIR, dirs_exist_ok=True)

    base_tpl = (TEMPLATES_DIR / "base.html").read_text(encoding="utf-8")
    index_tpl = (TEMPLATES_DIR / "index.html").read_text(encoding="utf-8")
    article_tpl = (TEMPLATES_DIR / "article.html").read_text(encoding="utf-8")
    studio_tpl = (TEMPLATES_DIR / "studio.html").read_text(encoding="utf-8")

    search_dirs = [CONTENT_DIR / "published"]
    if include_drafts:
        search_dirs.append(CONTENT_DIR / "drafts")

    articles_map = {}

    for s_dir in search_dirs:
        if not s_dir.exists():
            continue
        is_dir_draft = "drafts" in s_dir.parts

        for lang in ["tr", "en"]:
            lang_dir = s_dir / lang
            if not lang_dir.exists():
                continue
            for md_file in lang_dir.glob("*.md"):
                raw_text = md_file.read_text(encoding="utf-8")
                fm, html_body = parse_markdown(raw_text)
                slug = fm.get("slug", md_file.stem)
                file_is_draft = is_dir_draft and (fm.get("draft") is not False)

                if slug not in articles_map:
                    articles_map[slug] = {
                        "slug": slug,
                        "is_draft": file_is_draft,
                        "date": fm.get("date", datetime.now().strftime("%Y-%m-%d")),
                        "cover_image": fm.get("cover_image", "/images/weaving-and-code-cover.jpg"),
                        "tr": {},
                        "en": {}
                    }
                else:
                    if not file_is_draft:
                        articles_map[slug]["is_draft"] = False
                
                articles_map[slug][lang] = {
                    "title": fm.get("title", ""),
                    "subtitle": fm.get("subtitle", ""),
                    "summary": fm.get("summary", ""),
                    "author": fm.get("author", "Craft&Code Araştırma Masası" if lang == "tr" else "Craft&Code Editorial Desk"),
                    "tags": fm.get("tags", []),
                    "caption": fm.get("cover_caption", ""),
                    "credit": fm.get("cover_credit", ""),
                    "reading_time": calculate_reading_time(raw_text),
                    "html": html_body,
                    "filepath": md_file
                }
                if fm.get("cover_image"):
                    articles_map[slug]["cover_image"] = fm.get("cover_image")

    articles_list = list(articles_map.values())
    articles_list.sort(key=lambda x: str(x.get("date", "")), reverse=True)

    out_articles_dir = DIST_DIR / "yazi"
    out_articles_dir.mkdir(parents=True, exist_ok=True)

    for art in articles_list:
        slug = art["slug"]
        tr_data = art.get("tr", {})
        en_data = art.get("en", {})

        if art["is_draft"]:
            draft_banner_html = f'''<div class="draft-banner">
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; flex-wrap:wrap; gap:0.6rem;">
      <div>
        <span class="lang-tr"><strong>⚠️ TASLAK ÖNİZLEME MODU</strong> — Bu yazı henüz internette canlıda değildir. İnceleyip düzenleyebilir veya doğrudan yayına alabilirsiniz.</span>
        <span class="lang-en" style="display:none;"><strong>⚠️ DRAFT PREVIEW MODE</strong> — This piece is not yet live. You can review, edit or publish it.</span>
      </div>
      <button class="editor-btn primary" onclick="publishCurrentArticle('{slug}')" style="background:#047857; color:#fff; border-color:#047857; padding:0.4rem 0.85rem; font-size:0.82rem; cursor:pointer;">
        <span>🚀</span> <span class="lang-tr">Bu Yazıyı Yayına Al</span><span class="lang-en" style="display:none;">Publish This Article</span>
      </button>
    </div>
  </div>'''
            publish_toolbar_btn = f'''<button class="editor-btn" onclick="publishCurrentArticle('{slug}')" style="background:#047857; color:#ffffff; border-color:#047857;">
    <span>🚀</span>
    <span class="lang-tr">Yayına Al</span>
    <span class="lang-en" style="display:none;">Publish</span>
  </button>'''
        else:
            draft_banner_html = f'''<div style="background:#ecfdf5; border-bottom:1px solid #a7f3d0; padding:0.5rem 1.5rem; font-size:0.8rem; color:#065f46; display:flex; justify-content:space-between; align-items:center;">
    <div>
      <span class="lang-tr"><strong>● YAYINDA</strong> — Bu makale Craft&Code editoryal arşivinde canlıdır.</span>
      <span class="lang-en" style="display:none;"><strong>● PUBLISHED</strong> — This article is live in the Craft&Code editorial archive.</span>
    </div>
    <button onclick="unpublishCurrentArticle('{slug}')" style="background:none; border:none; color:#047857; font-size:0.75rem; text-decoration:underline; cursor:pointer;">
      <span class="lang-tr">Taslağa Geri Al</span>
      <span class="lang-en" style="display:none;">Revert to Draft</span>
    </button>
  </div>'''
            publish_toolbar_btn = f'''<span style="font-size:0.75rem; color:#047857; font-weight:600; padding:0.35rem 0.6rem; display:inline-flex; align-items:center; gap:0.25rem;">
    <span>●</span>
    <span class="lang-tr">Yayında</span>
    <span class="lang-en" style="display:none;">Published</span>
  </span>'''

        body = article_tpl
        replacements = {
            "{{SLUG}}": slug,
            "{{DATE}}": str(art["date"]),
            "{{COVER_IMAGE}}": art["cover_image"],
            "{{DRAFT_BANNER}}": draft_banner_html,
            "{{PUBLISH_TOOLBAR_BTN}}": publish_toolbar_btn,
            "{{TITLE_TR}}": tr_data.get("title", ""),
            "{{SUBTITLE_TR}}": tr_data.get("subtitle", ""),
            "{{AUTHOR_TR}}": tr_data.get("author", "Craft&Code"),
            "{{READING_TIME_TR}}": f"{tr_data.get('reading_time', 5)} dk",
            "{{TAGS_TR}}": " ".join([f'<span class="tag">#{t}</span>' for t in tr_data.get("tags", [])]),
            "{{COVER_CAPTION_TR}}": tr_data.get("caption", ""),
            "{{COVER_CREDIT_TR}}": tr_data.get("credit", ""),
            "{{CONTENT_TR}}": tr_data.get("html", ""),

            "{{TITLE_EN}}": en_data.get("title", tr_data.get("title", "")),
            "{{SUBTITLE_EN}}": en_data.get("subtitle", tr_data.get("subtitle", "")),
            "{{AUTHOR_EN}}": en_data.get("author", "Craft&Code"),
            "{{READING_TIME_EN}}": f"{en_data.get('reading_time', 5)} min read",
            "{{TAGS_EN}}": " ".join([f'<span class="tag">#{t}</span>' for t in en_data.get("tags", [])]),
            "{{COVER_CAPTION_EN}}": en_data.get("caption", tr_data.get("caption", "")),
            "{{COVER_CREDIT_EN}}": en_data.get("credit", tr_data.get("credit", "")),
            "{{CONTENT_EN}}": en_data.get("html", ""),
        }
        for k, v in replacements.items():
            body = body.replace(k, str(v))

        page = base_tpl
        page = page.replace("{{PAGE_TITLE}}", f"{tr_data.get('title', 'Craft&Code')} — Craft&Code")
        page = page.replace("{{MAIN_CONTENT}}", body)

        out_file = out_articles_dir / f"{slug}.html"
        out_file.write_text(page, encoding="utf-8")
        print(f"  ✓ Rendered unified article: {out_file.relative_to(DIST_DIR)}")

        # Redirects for /tr/ and /en/
        for p_sub in [DIST_DIR / "tr" / "yazilar", DIST_DIR / "en" / "articles"]:
            p_sub.mkdir(parents=True, exist_ok=True)
            r_html = f'<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=/yazi/{slug}.html"></head><body><script>window.location.replace("/yazi/{slug}.html");</script></body></html>'
            (p_sub / f"{slug}.html").write_text(r_html, encoding="utf-8")

    # Render Unified Index Page
    cards_html = []
    for art in articles_list:
        slug = art["slug"]
        tr_data = art.get("tr", {})
        en_data = art.get("en", {})
        url = f"/yazi/{slug}.html"

        card = f'''<article class="article-card">
          <a href="{url}" class="card-image-wrap">
            <img src="{art['cover_image']}" alt="{tr_data.get('title', '')}" loading="lazy"/>
          </a>
          <div class="card-content">
            <div class="card-meta">
              <span class="lang-tr">{tr_data.get('tags', ['ARAŞTIRMA'])[0] if tr_data.get('tags') else 'ARAŞTIRMA'}</span>
              <span class="lang-en" style="display:none;">{en_data.get('tags', ['RESEARCH'])[0] if en_data.get('tags') else 'RESEARCH'}</span>
              <span>•</span>
              <span class="date">{art['date']}</span>
              <span>•</span>
              <span class="lang-tr">{tr_data.get('reading_time', 5)} dk okuma</span>
              <span class="lang-en" style="display:none;">{en_data.get('reading_time', 5)} min read</span>
            </div>
            <h2>
              <a href="{url}">
                <span class="lang-tr">{tr_data.get('title', '')}</span>
                <span class="lang-en" style="display:none;">{en_data.get('title', tr_data.get('title', ''))}</span>
              </a>
            </h2>
            <p class="summary">
              <span class="lang-tr">{tr_data.get('summary', '')}</span>
              <span class="lang-en" style="display:none;">{en_data.get('summary', '')}</span>
            </p>
          </div>
        </article>'''
        cards_html.append(card)

    index_body = index_tpl.replace("{{ARTICLE_CARDS}}", "\n".join(cards_html))
    index_page = base_tpl.replace("{{PAGE_TITLE}}", "Craft&Code — Art, Craft & Computational Inquiries")
    index_page = index_page.replace("{{MAIN_CONTENT}}", index_body)
    (DIST_DIR / "index.html").write_text(index_page, encoding="utf-8")

    # Render Studio Page
    from content_generator import get_active_proposals
    active_topics = get_active_proposals()

    topic_cards_html = []
    for item in active_topics:
        t_id = item["id"]
        t_title_escaped = item["title"].replace("'", "\\'")
        card = f'''<div class="topic-card" id="card-{t_id}">
          <div>
            <div class="card-top-bar">
              <span class="category-pill">{item['category']}</span>
              <button class="btn-dismiss-topic" onclick="dismissTopic('card-{t_id}')" title="Bu öneriyi kaldır">✕</button>
            </div>
            <h3>{item['title']}</h3>
            <p class="thesis">{item['thesis']}</p>
            <div class="detail-box">
              <strong>Vakalar:</strong> {item['cases']}
            </div>
          </div>
          <button class="btn-approve" onclick="approveTopic('{t_id}', '{t_title_escaped}')">
            <span>🚀</span> Bu Konuyu Onayla & Üret
          </button>
        </div>'''
        topic_cards_html.append(card)

    rows_html = []
    for art in articles_list:
        slug = art["slug"]
        tr_data = art.get("tr", {})
        title_escaped = tr_data.get('title', slug).replace("'", "\\'")
        if art["is_draft"]:
            status_cls = "draft"
            status_txt = "TASLAK"
            pub_btn = f'<button class="action-btn publish" onclick="publishArticle(\'{slug}\')">🚀 Yayına Al</button>'
        else:
            status_cls = "published"
            status_txt = "● YAYINDA"
            pub_btn = f'<button class="action-btn" onclick="unpublishArticle(\'{slug}\')" style="color:#047857;border-color:#a7f3d0;" title="Yazıyı tekrar taslak moduna al">↩️ Taslağa Al</button>'

        row = f'''<tr>
          <td>
            <a href="/yazi/{slug}.html" style="text-decoration:none; color:inherit;">
              <strong>{tr_data.get('title', slug)}</strong>
            </a><br>
            <small style="color:var(--text-muted);font-family:var(--font-mono);">/yazi/{slug}.html</small>
          </td>
          <td><span class="status-badge {status_cls}">{status_txt}</span></td>
          <td>{art['date']}</td>
          <td>
            <div class="actions-cell">
              <a class="action-btn" href="/yazi/{slug}.html">👁️ Aç</a>
              {pub_btn}
              <button class="action-btn delete" onclick="deleteArticle('{slug}', '{title_escaped}')">🗑️ Sil</button>
            </div>
          </td>
        </tr>'''
        rows_html.append(row)

    studio_page = studio_tpl.replace("{{TOPIC_CARDS}}", "\n".join(topic_cards_html))
    studio_page = studio_page.replace("{{ARTICLES_ROWS}}", "\n".join(rows_html))
    (DIST_DIR / "studio.html").write_text(studio_page, encoding="utf-8")

    print("✅ Build complete!")

if __name__ == "__main__":
    include_drafts = "--no-drafts" not in sys.argv
    build_site(include_drafts=include_drafts)
