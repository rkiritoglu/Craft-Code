#!/usr/bin/env python3
"""
Craft&Code Interactive Server & Studio API
Supports in-browser live editing, real AI image synthesis from prompts, dynamic gallery, and live preview.
"""

import http.server
import socketserver
import os
import sys
import json
import re
import shutil
from pathlib import Path
from build import build_site
from content_generator import generate_topic_draft, refresh_proposals

ROOT_DIR = Path(__file__).resolve().parent
DIST_DIR = ROOT_DIR / "dist"
CONTENT_DIR = ROOT_DIR / "content"
IMAGES_DIR = ROOT_DIR / "public" / "images"

class CraftCodeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST_DIR), **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        if self.path in ['/tr', '/tr/', '/en', '/en/']:
            self.path = '/index.html'
            super().do_GET()
            return

        # Dynamic Gallery API: Returns ALL images in public/images
        if self.path == '/api/images/list':
            try:
                images = []
                if IMAGES_DIR.exists():
                    for f in sorted(IMAGES_DIR.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True):
                        if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
                            name = f.stem.replace("-", " ").replace("_", " ").title()
                            images.append({
                                "url": f"/images/{f.name}",
                                "name": name,
                                "filename": f.name
                            })

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(images).encode('utf-8'))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
                return

        super().do_GET()

    def do_POST(self):
        # 1. Studio: Approve & Generate Topic
        if self.path == '/api/studio/generate-topic':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                data = json.loads(self.rfile.read(content_len).decode('utf-8'))
                topic_key = data.get('topic_key')

                slug = generate_topic_draft(topic_key)
                build_site(include_drafts=True)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True, "slug": slug, "url": f"/yazi/{slug}.html"}).encode('utf-8'))
                print(f"  🎉 Generated topic draft: {slug}")
                return
            except Exception as e:
                print(f"  ❌ Error generating topic: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode('utf-8'))
                return

        # 2. Studio: Refresh Topics with Editorial Memory (No Duplicates)
        if self.path == '/api/studio/refresh-proposals':
            try:
                refresh_proposals()
                build_site(include_drafts=True)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True}).encode('utf-8'))
                print("  🔄 Refreshed topic proposals with non-overlapping themes.")
                return
            except Exception as e:
                print(f"  ❌ Error refreshing topics: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode('utf-8'))
                return

        # 3. Studio: Delete Topic / Article
        if self.path == '/api/studio/delete':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                data = json.loads(self.rfile.read(content_len).decode('utf-8'))
                slug = data.get('slug')

                matches = list(CONTENT_DIR.glob(f"**/{slug}.md"))
                for m in matches:
                    if m.exists():
                        m.unlink()
                        print(f"  🗑️ Deleted file: {m.relative_to(CONTENT_DIR)}")

                build_site(include_drafts=True)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True}).encode('utf-8'))
                print(f"  🗑️ Deleted article: {slug}")
                return
            except Exception as e:
                print(f"  ❌ Error deleting article: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode('utf-8'))
                return

        # 4. Studio: Publish Article
        if self.path == '/api/studio/publish':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                data = json.loads(self.rfile.read(content_len).decode('utf-8'))
                slug = data.get('slug')

                matches = list(CONTENT_DIR.glob(f"**/{slug}.md"))
                pub_dir = CONTENT_DIR / "published"
                pub_dir.mkdir(parents=True, exist_ok=True)

                for m in matches:
                    text = m.read_text(encoding="utf-8")
                    text = re.sub(r'draft:\s*true', 'draft: false', text)

                    lang = "tr"
                    if "en" in m.parts:
                        lang = "en"

                    target_dir = pub_dir / lang
                    target_dir.mkdir(parents=True, exist_ok=True)
                    target_file = target_dir / m.name
                    target_file.write_text(text, encoding="utf-8")

                    if "drafts" in m.parts and m.exists():
                        m.unlink()
                        print(f"  📦 Moved to published: {target_file.relative_to(CONTENT_DIR)}")

                # Update memory
                mem_file = ROOT_DIR / "data" / "editorial_memory.json"
                if mem_file.exists():
                    try:
                        mem = json.loads(mem_file.read_text(encoding="utf-8"))
                        if slug not in mem.get("covered_slugs", []):
                            mem.setdefault("covered_slugs", []).append(slug)
                            mem_file.write_text(json.dumps(mem, indent=2, ensure_ascii=False), encoding="utf-8")
                    except Exception as me:
                        print(f"Memory update notice: {me}")

                build_site(include_drafts=True)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True}).encode('utf-8'))
                print(f"  🚀 Published article: {slug}")
                return
            except Exception as e:
                print(f"  ❌ Error publishing article: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode('utf-8'))
                return

        # 4b. Studio: Unpublish / Revert to Draft
        if self.path == '/api/studio/unpublish':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                data = json.loads(self.rfile.read(content_len).decode('utf-8'))
                slug = data.get('slug')

                matches = list(CONTENT_DIR.glob(f"**/{slug}.md"))
                drafts_dir = CONTENT_DIR / "drafts"
                drafts_dir.mkdir(parents=True, exist_ok=True)

                for m in matches:
                    text = m.read_text(encoding="utf-8")
                    text = re.sub(r'draft:\s*false', 'draft: true', text)

                    lang = "tr"
                    if "en" in m.parts:
                        lang = "en"

                    target_dir = drafts_dir / lang
                    target_dir.mkdir(parents=True, exist_ok=True)
                    target_file = target_dir / m.name
                    target_file.write_text(text, encoding="utf-8")

                    if "published" in m.parts and m.exists():
                        m.unlink()
                        print(f"  ↩️ Reverted to drafts: {target_file.relative_to(CONTENT_DIR)}")

                build_site(include_drafts=True)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True}).encode('utf-8'))
                print(f"  ↩️ Reverted article to draft: {slug}")
                return
            except Exception as e:
                print(f"  ❌ Error unpublishing article: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode('utf-8'))
                return
                return

        # 5. In-Browser Editor: Save Draft Edits
        if self.path == '/api/save-draft':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                data = json.loads(self.rfile.read(content_len).decode('utf-8'))

                slug = data.get('slug')
                cover_image = data.get('cover_image')
                tr_data = data.get('tr', {})
                en_data = data.get('en', {})

                matches = list(CONTENT_DIR.glob(f"**/{slug}.md"))
                for m in matches:
                    if "/tr/" in str(m):
                        update_markdown_file(m, {
                            "title": tr_data.get("title"),
                            "subtitle": tr_data.get("subtitle"),
                            "cover_image": cover_image,
                            "cover_caption": tr_data.get("caption"),
                            "cover_credit": tr_data.get("credit")
                        })
                    elif "/en/" in str(m):
                        update_markdown_file(m, {
                            "title": en_data.get("title"),
                            "subtitle": en_data.get("subtitle"),
                            "cover_image": cover_image,
                            "cover_caption": en_data.get("caption"),
                            "cover_credit": en_data.get("credit")
                        })

                build_site(include_drafts=True)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True}).encode('utf-8'))
                print(f"  💾 Saved draft edits: {slug}")
                return
            except Exception as e:
                print(f"  ❌ Error saving draft: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode('utf-8'))
                return

        self.send_error(404, "Endpoint not found")

def update_markdown_file(filepath, updates):
    text = filepath.read_text(encoding="utf-8")
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not fm_match:
        return

    fm_lines = fm_match.group(1).splitlines()
    body = fm_match.group(2)
    new_fm_lines = []
    handled_keys = set()

    for line in fm_lines:
        if ":" in line:
            key, val = line.split(":", 1)
            key_strip = key.strip()
            if key_strip in updates and updates[key_strip] is not None:
                new_fm_lines.append(f'{key_strip}: "{updates[key_strip]}"')
                handled_keys.add(key_strip)
                continue
        new_fm_lines.append(line)

    for k, v in updates.items():
        if k not in handled_keys and v is not None:
            new_fm_lines.append(f'{k}: "{v}"')

    new_text = "---\n" + "\n".join(new_fm_lines) + "\n---\n" + body
    filepath.write_text(new_text, encoding="utf-8")

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def main():
    print("=" * 65)
    print("  Craft&Code — Editoryal Stüdyo & Canlı Önizleme Sunucusu")
    print("=" * 65)
    
    build_site(include_drafts=True)

    candidate_ports = [8080, 8008, 5000, 8001]
    httpd = None
    active_port = None

    for p in candidate_ports:
        try:
            httpd = ReusableTCPServer(("", p), CraftCodeHandler)
            active_port = p
            break
        except OSError:
            continue

    if not httpd:
        print("❌ Hata: Uygun bir port bulunamadı!")
        sys.exit(1)

    print(f"\n🚀 Stüdyo & Önizleme hazır: http://localhost:{active_port}/studio.html")
    print(f"👉 Ana Sayfa: http://localhost:{active_port}/")
    print("\nDurdurmak için Ctrl + C tuşlarına basın.\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nSunucu kapatıldı.")

if __name__ == "__main__":
    main()
