#!/usr/bin/env python3
"""
Craft&Code — YouTube Shorts Video Generator
Automatically converts published research articles into broadcast-quality vertical (9:16, 1080x1920) YouTube Shorts videos.
Features:
- High-res diffusion artwork with cinematic Ken Burns zoom.
- Curated storyboard (Hook -> Craft Origin -> Computational Transition -> Synthesis & CTA).
- Voiceover narration with ambient drone soundtrack.
- Kinetic typographic captions, progress bar, and branding.
- YouTube Shorts SEO package (Title, Description, Hashtags).
"""

import os
import sys
import json
import math
import wave
import struct
import shutil
import tempfile
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = Path(__file__).resolve().parent
CONTENT_DIR = ROOT_DIR / "content"
PUBLIC_DIR = ROOT_DIR / "public"
DIST_DIR = ROOT_DIR / "dist"
VIDEOS_DIR = PUBLIC_DIR / "videos"
FONTS_DIR = Path("/usr/share/fonts")

# Fonts
FONT_BOLD = str(FONTS_DIR / "google-noto/NotoSans-Bold.ttf")
FONT_SERIF = str(FONTS_DIR / "google-noto/NotoSerif-Bold.ttf")

# Video Constants
WIDTH = 1080
HEIGHT = 1920
FPS = 25

# Color Palette
COLOR_BG_DARK = (14, 13, 12)
COLOR_TEXT_WHITE = (248, 250, 252)
COLOR_TEXT_MUTED = (148, 163, 184)
COLOR_ACCENT_AMBER = (245, 158, 11)
COLOR_ACCENT_CYAN = (6, 182, 212)
COLOR_CARD_BG = (18, 17, 16, 225)
COLOR_CARD_BORDER = (255, 255, 255, 35)

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                lines.append(word)
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def generate_ambient_track(duration_sec, output_path):
    """Synthesizes a rich, meditative ambient drone in E minor."""
    sample_rate = 44100
    n_samples = int(sample_rate * duration_sec)
    
    # E minor harmonics: E2 (82.41), B2 (123.47), E3 (164.81), G3 (196.00), B3 (246.94)
    freqs = [82.41, 123.47, 164.81, 196.00, 246.94]
    
    with wave.open(str(output_path), 'w') as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        
        frames = bytearray()
        for i in range(n_samples):
            t = i / sample_rate
            # Smooth breathing LFO (0.2 Hz)
            lfo = 0.75 + 0.25 * math.sin(2 * math.pi * 0.15 * t)
            
            sample_l = 0.0
            sample_r = 0.0
            
            for idx, f in enumerate(freqs):
                amp = (0.20 / (idx + 1)) * lfo
                sample_l += amp * math.sin(2 * math.pi * f * t)
                sample_r += amp * math.sin(2 * math.pi * f * t + 0.4)
                
            # Subtle warm shimmer
            shimmer = 0.04 * math.sin(2 * math.pi * 329.63 * t) * (0.5 + 0.5 * math.sin(2 * math.pi * 0.3 * t))
            sample_l += shimmer
            sample_r += shimmer
            
            # Fade out at the very end
            fade_dur = 2.0
            if t > duration_sec - fade_dur:
                fade = (duration_sec - t) / fade_dur
                sample_l *= fade
                sample_r *= fade
                
            val_l = max(-32767, min(32767, int(sample_l * 32767 * 0.55)))
            val_r = max(-32767, min(32767, int(sample_r * 32767 * 0.55)))
            frames.extend(struct.pack('<hh', val_l, val_r))
            
        wav.writeframes(frames)

def normalize_phonetics_tr(text):
    """
    Normalizes foreign terms, abbreviations, numbers, and technical jargon
    into authentic, natural phonetic Turkish spelling for the TTS engine.
    """
    replacements = [
        ("Craft and Code", "Kraft ve Kod"),
        ("Craft & Code", "Kraft ve Kod"),
        ("Craft&Code", "Kraft ve Kod"),
        ("Craft", "Kraft"),
        ("Code", "Kod"),
        ("glitch'i", "gliçi"),
        ("glitch", "gliç"),
        ("Glitch", "Gliç"),
        ("Jacquard", "Jakar"),
        ("Navier-Stokes", "Navye Stoks"),
        ("Navier Stokes", "Navye Stoks"),
        ("3D", "üç boyutlu"),
        ("3d", "üç boyutlu"),
        ("Wabi-Sabi", "Vabi Sabi"),
        ("wabi-sabi", "vabi sabi"),
        ("Wabi Sabi", "Vabi Sabi"),
        ("Sidewalk Kintsukuroi", "Saydvolk Kintsukuroi"),
        ("Sidewalk", "Saydvolk"),
        ("Peter Lu", "Piitır Lu"),
        ("Sougwen Chung", "Sovgen Çang"),
        ("p5.js", "pe beş cey es"),
        ("GLSL shader", "grafik şeydır"),
        ("GLSL", "ce el es el"),
        ("shader", "şeydır"),
        ("15. yüzyıl", "on beşinci yüzyıl"),
        ("15. Yüzyıl", "on beşinci yüzyıl"),
        ("15.", "on beşinci"),
        ("1804'te", "bin sekiz yüz dörtte"),
        ("1804", "bin sekiz yüz dört"),
        ("7 eksenli", "yedi eksenli"),
        ("7 eksen", "yedi eksen"),
        ("AxiDraw", "Aksi Drov"),
        ("YouTube", "Yuutub"),
        ("Shorts", "Şorts"),
        ("point cloud", "nokta bulutu"),
        ("SID", "sid"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def synthesize_speech(text, output_path):
    """
    Synthesizes a deep, resonant, natural male baritone voice in fluent Turkish.
    Applies phonetic normalization and professional broadcast EQ/compression.
    """
    phonetic_text = normalize_phonetics_tr(text)

    # Generate raw audio with deep pitch male voice (tr+m3)
    raw_path = output_path.with_name(f"raw_{output_path.name}")
    cmd = [
        "espeak-ng",
        "-v", "tr+m3",      # Deep male voice 3
        "-s", "126",        # Measured, calm documentary narration tempo
        "-p", "26",         # Deep baritone pitch (tok erkek sesi)
        "-k", "10",         # Grounded pitch variation
        "-a", "140",        # Confident amplitude
        phonetic_text,
        "-w", str(raw_path)
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Professional broadcast audio enhancement:
    # 1. bass boost at 110Hz (+9dB) for a deep, warm chest resonance ("tok ses")
    # 2. gentle dip at 3000Hz (-4dB) to remove harsh synthetic sibilance
    # 3. broadcast dynamic compression for a thick, solid presence
    cmd_filter = [
        "ffmpeg", "-y", "-i", str(raw_path),
        "-af", "bass=g=9:f=110,equalizer=f=3000:t=q:w=1.2:g=-4,acompressor=threshold=-15dB:ratio=3.5:attack=15:release=120,volume=1.35",
        str(output_path)
    ]
    subprocess.run(cmd_filter, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if raw_path.exists():
        raw_path.unlink()

def get_audio_duration(filepath):
    """Retrieves duration of audio file via ffmpeg."""
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(filepath)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        return float(res.stdout.strip())
    except Exception:
        return 5.0

def create_base_canvas(image_path):
    """Scales and crops the article cover image to vertical 1080x1920."""
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception:
        img = Image.new("RGB", (WIDTH, HEIGHT), COLOR_BG_DARK)
        
    iw, ih = img.size
    target_ratio = WIDTH / HEIGHT
    img_ratio = iw / ih
    
    if img_ratio > target_ratio:
        new_w = int(ih * target_ratio)
        offset_x = (iw - new_w) // 2
        img = img.crop((offset_x, 0, offset_x + new_w, ih))
    else:
        new_h = int(iw / target_ratio)
        offset_y = (ih - new_h) // 2
        img = img.crop((0, offset_y, iw, offset_y + new_h))
        
    return img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

def render_scene_overlay(scene_num, total_scenes, category, headline, quote_text, cta_mode=False):
    """Creates a transparent 1080x1920 PNG overlay with badges, text, and captions."""
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # 1. Top Cinematic Gradient (Dark vignette)
    for y in range(460):
        alpha = int(230 * (1 - (y / 460) ** 1.3))
        draw.line([(0, y), (WIDTH, y)], fill=(12, 11, 10, alpha))
        
    # 2. Bottom Cinematic Gradient
    for y in range(1150, HEIGHT):
        ratio = (y - 1150) / (HEIGHT - 1150)
        alpha = int(245 * (ratio ** 1.2))
        draw.line([(0, y), (WIDTH, y)], fill=(12, 11, 10, alpha))
        
    # 3. Top Editorial Brand Badge
    badge_y = 120
    badge_text = f"✦ CRAFT & CODE  •  {category.upper()}"
    font_badge = get_font(FONT_BOLD, 26)
    
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw = bbox[2] - bbox[0] + 50
    bh = 54
    bx = (WIDTH - bw) // 2
    
    draw.rounded_rectangle([bx, badge_y, bx + bw, badge_y + bh], radius=27, fill=(20, 19, 18, 220), outline=(245, 158, 11, 180), width=2)
    draw.text((bx + 25, badge_y + 12), badge_text, fill=COLOR_ACCENT_AMBER, font=font_badge)
    
    # 4. Headline / Hook Banner
    font_headline = get_font(FONT_SERIF, 54)
    head_lines = wrap_text(headline, font_headline, 920, draw)
    
    head_y = 215
    for line in head_lines[:3]:
        draw.text(((WIDTH - draw.textbbox((0, 0), line, font=font_headline)[2]) // 2, head_y), line, fill=COLOR_TEXT_WHITE, font=font_headline)
        head_y += 72
        
    # 5. Bottom Kinetic Captions Glass Card
    card_margin = 60
    card_w = WIDTH - (card_margin * 2)
    card_y = 1320
    
    font_body = get_font(FONT_BOLD, 36)
    body_lines = wrap_text(quote_text, font_body, card_w - 70, draw)
    card_h = max(240, len(body_lines) * 58 + 80)
    
    # Rounded glassmorphism card
    draw.rounded_rectangle(
        [card_margin, card_y, card_margin + card_w, card_y + card_h],
        radius=20,
        fill=COLOR_CARD_BG,
        outline=COLOR_CARD_BORDER,
        width=2
    )
    
    # Accent indicator bar on card
    draw.rounded_rectangle([card_margin, card_y, card_margin + 8, card_y + card_h], radius=4, fill=COLOR_ACCENT_AMBER)
    
    # Text inside card
    text_y = card_y + 35
    for idx, bline in enumerate(body_lines[:5]):
        text_color = COLOR_ACCENT_AMBER if (idx == 0 or idx == len(body_lines)-1) else COLOR_TEXT_WHITE
        draw.text((card_margin + 35, text_y), bline, fill=text_color, font=font_body)
        text_y += 56
        
    # 6. Call to Action / Footer Branding
    footer_y = 1750
    font_footer = get_font(FONT_BOLD, 26)
    if cta_mode:
        cta_str = "👉 Araştırmanın Tamamı: rkiritoglu.github.io/Craft-Code"
        draw.text(((WIDTH - draw.textbbox((0, 0), cta_str, font=font_footer)[2]) // 2, footer_y), cta_str, fill=COLOR_ACCENT_CYAN, font=font_footer)
    else:
        ft_str = "CRAFT & CODE  |  BİLİM • ZANAAT • ALGORİTMA"
        draw.text(((WIDTH - draw.textbbox((0, 0), ft_str, font=font_footer)[2]) // 2, footer_y), ft_str, fill=COLOR_TEXT_MUTED, font=font_footer)
        
    # 7. Progress Bar at bottom
    bar_y = 1860
    bar_h = 8
    draw.rectangle([card_margin, bar_y, WIDTH - card_margin, bar_y + bar_h], fill=(255, 255, 255, 40))
    progress_w = int((WIDTH - card_margin * 2) * (scene_num / total_scenes))
    draw.rectangle([card_margin, bar_y, card_margin + progress_w, bar_y + bar_h], fill=COLOR_ACCENT_AMBER)
    
    return overlay

def parse_article_markdown(filepath):
    """Parses frontmatter and content from markdown file."""
    text = filepath.read_text(encoding="utf-8")
    fm = {}
    content = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            content = parts[2]
            for line in fm_text.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, content

def build_storyboard(slug, fm, content):
    """Creates an engaging 4-scene storyboard customized for YouTube Shorts."""
    title = fm.get("title", "Craft & Code")
    summary = fm.get("summary", "")
    category = fm.get("tags", "Sanat & Teknoloji")
    if isinstance(category, str) and category.startswith("["):
        category = category.strip("[]'\" ").split(",")[0].strip("'\" ")
        
    # Map curated storylines for each craft
    storyboards = {
        "kintsugi-ve-dijital-kusur": [
            {
                "headline": "Kırığın Poetikası: Kintsugi",
                "caption": "Kusuru gizlemek yerine altınla parlatmak... Kırık bir ayıp değil, nesnenin en dürüst hafızasıdır.",
                "voice": "Kusuru gizlemek yerine altınla parlatmak... Kintsugi ve dijital glitch sanatı.",
                "image": "kintsugi-porselen-macro.jpg"
            },
            {
                "headline": "15. Yüzyıl Japon Felsefesi",
                "caption": "Wabi-Sabi öğretisinde kırılan çay kasesi altın tozuyla birleştirilir; çatlak nesnenin ruhuna dönüşür.",
                "voice": "15. yüzyıl Japonya'sında kırılan porselenler altın tozu ve reçineyle onarılırdı. Kırık nesnenin onurlu hafızasıydı.",
                "image": "kintsugi-glitch-cover.jpg"
            },
            {
                "headline": "Dijital Glitch & Veri Onarımı",
                "caption": "Yeni medya sanatçıları bozuk 3D ağları ve kayıp pikselleri altın neon hatlarla onararak glitch'i yüceltiyor.",
                "voice": "Bugün yeni medya sanatçıları, bozuk 3D ağları ve kayıp veri bloklarını altın neon kodlarla onarıyor.",
                "image": "kintsugi-porselen-macro.jpg"
            },
            {
                "headline": "Yaralarımızı Kodlamak",
                "caption": "Geleceğin teknolojisi, geçmişin kırık hafızasını silmeden onunla birlikte inşa edilmelidir.",
                "voice": "Zanaat ve kodun kesişimindeki tüm araştırmalar Craft and Code'da. Takipte kalın.",
                "image": "kintsugi-glitch-cover.jpg",
                "cta": True
            }
        ],
        "dokuma-tezgahindan-koda": [
            {
                "headline": "Delikli Kartlardan Koda",
                "caption": "Bilgisayarın ilk somut dili silikonda değil; ahşap bir el dokuma tezgâhında doğdu.",
                "voice": "İlk bilgisayar kodu silikon çiplerde değil, bir el dokuma tezgâhında yazıldı desek?",
                "image": "weaving-and-code-cover.jpg"
            },
            {
                "headline": "Jacquard Tezgâhı ve İkili Kod",
                "caption": "1804'te Joseph Marie Jacquard, delikli kartlarla çözgü ve atkıyı 0 ve 1 ikili sistemine dönüştürdü.",
                "voice": "Jacquard delikli kartları, kumaş desenlerini sıfır ve bir ikili koduna dönüştüren ilk yazılımdı.",
                "image": "weaving-and-code-cover.jpg"
            },
            {
                "headline": "Dokunan Pikseller & Enstalasyon",
                "caption": "Çağdaş sanatçılar geleneksel el tezgâhlarında dijital algoritmaları ve veri akışlarını dokuyor.",
                "voice": "Bugün sanatçılar, pikselleri ve generatif kodları yün ipliklerle fiziksel hafızaya işliyor.",
                "image": "weaving-and-code-cover.jpg"
            },
            {
                "headline": "Kadim Zanaat & Sayısal Gelecek",
                "caption": "Dokuma ve hesaplamalı sanatın kadim bağlarını keşfetmek için bizi takip edin.",
                "voice": "Zanaat ile kodun büyüleyici hikâyesi Craft and Code'da. Takipte kalın.",
                "image": "weaving-and-code-cover.jpg",
                "cta": True
            }
        ],
        "selcuklu-cini-ve-3d-baski": [
            {
                "headline": "Parametrik Selçuklu Çinisi",
                "caption": "Batı'dan 500 yıl önce keşfedilen girih geometrisi, bugün robotik 3D kil ekstrüzyonu ile birleşiyor.",
                "voice": "Selçuklu ustalarının yüzyıllar önce keşfettiği geometri, robotik 3D kil baskıyla yeniden doğuyor.",
                "image": "selcuklu-cini-cover.jpg"
            },
            {
                "headline": "Yarı-Kristal Girih Matematiği",
                "caption": "Harvard fizikçisi Peter Lu, Selçuklu çinilerinde modern Penrose karolarından yüzyıllar önce yarı-kristal desenler buldu.",
                "voice": "Selçuklu mimarisindeki girih karoları, modern kuasi-kristal fiziğinin ilk somut örnekleriydi.",
                "image": "selcuklu-cini-cover.jpg"
            },
            {
                "headline": "Robotik Kil & Parametrik Cephe",
                "caption": "Çağdaş mimarlar 7 eksenli robot kollarıyla Selçuklu geometrisini akıllı cephe panellerine dönüştürüyor.",
                "voice": "Günümüzde robot kollar, kadim çini çamurunu parametrik kodlarla sıkarak yaşayan cepheler üretiyor.",
                "image": "selcuklu-cini-cover.jpg"
            },
            {
                "headline": "Kadim Mimari & Robotik",
                "caption": "Çini sanatından robotik üretime; tüm makale ve araştırmalar sitemizde.",
                "voice": "Geçmişin bilgisi geleceğin robotlarıyla buluşuyor. Detaylar Craft and Code'da.",
                "image": "selcuklu-cini-cover.jpg",
                "cta": True
            }
        ],
        "ebru-ve-sivi-algoritmalar": [
            {
                "headline": "Sıvı Algoritmalar: Ebru",
                "caption": "Ebru, dünyanın ilk generatif sanatıdır. Sanatçı tuvale değil; akışkanlar dinamiğine müdahale eder.",
                "voice": "Ebru sanatı, dünyanın bilinen ilk generatif kodlama pratiği olabilir mi?",
                "image": "ebru-cover.jpg"
            },
            {
                "headline": "Kitre ve Yüzey Gerilimi",
                "caption": "Mikro-akışkan matematiği ve Navier-Stokes denklemleri asırlardır ebru teknesinde hesaplanıyor.",
                "voice": "Kitre ve yüzey gerilimi, doğanın kendi diferansiyel denklemlerini boyalarla çözmesini sağlar.",
                "image": "ebru-cover.jpg"
            },
            {
                "headline": "Generatif Vektör Alanları",
                "caption": "Yeni medya kodlayıcıları p5.js ve shader simülasyonlarıyla dijital ebru dalgaları yaratıyor.",
                "voice": "Günümüzde kodlayıcılar, GLSL shader simülasyonlarıyla ebruyu veri pigmentlerine dönüştürüyor.",
                "image": "ebru-cover.jpg"
            },
            {
                "headline": "Doğanın Akışkan Kodu",
                "caption": "Ebru ve hesaplamalı akışkanların felsefi diyaloğu sitemizde yayında.",
                "voice": "Doğanın ve kodun akışkan uyumu Craft and Code'da. Takipte kalın.",
                "image": "ebru-cover.jpg",
                "cta": True
            }
        ],
        "hat-sanati-ve-robotik-kaligrafi": [
            {
                "headline": "Kamış Kalemin Nefesi",
                "caption": "Hat sanatındaki 'nokta' tabanlı oran matematiği ile robotik kaligrafi kollarının düeti.",
                "voice": "Kamış kalemin geometrik nefesi ve robotik kolların insan makine kaligrafisi.",
                "image": "hat-sanati-cover.jpg"
            },
            {
                "headline": "Aklâm-ı Sitte Nokta Geometrisi",
                "caption": "Geleneksel hat sanatında her harf, kamış kalemin tek bir noktasının altın oranıyla belirlenir.",
                "voice": "Hat sanatında her harf, kamış kalemin bastığı nokta ölçüsüyle parametrik olarak hesaplanır.",
                "image": "hat-sanati-cover.jpg"
            },
            {
                "headline": "Yapay Zekâ ve Robotik Kaligrafi",
                "caption": "Çağdaş sanatçılar Sougwen Chung ve generatif kollar, insan hattatın nefesini robotik fırçaya aktarıyor.",
                "voice": "Yapay zekâ ve robot kollar, hattatın el hareketlerini eşzamanlı generatif çizgilere dönüştürüyor.",
                "image": "hat-sanati-cover.jpg"
            },
            {
                "headline": "Bedenin ve Kodun Hattı",
                "caption": "Geleneksel hat ile robotik kaligrafinin tüm detayları Craft and Code'da.",
                "voice": "Kadim harflerin kodla dansı Craft and Code'da. Bizi takip etmeyi unutmayın.",
                "image": "hat-sanati-cover.jpg",
                "cta": True
            }
        ]
    }
    
    # Return matched storyboard or generic fallback based on frontmatter
    if slug in storyboards:
        return category, storyboards[slug]
        
    # Generic intelligent fallback
    cover_img_file = fm.get("cover_image", "weaving-and-code-cover.jpg").split("/")[-1]
    fallback_scenes = [
        {
            "headline": title[:40],
            "caption": summary[:110] + "...",
            "voice": f"{title}. Kadim zanaat ve generatif sanatın buluşması.",
            "image": cover_img_file
        },
        {
            "headline": "Kadim Sözdizimi & Malzeme",
            "caption": "Her geleneksel zanaat, insan bedeninin fiziksel dirençle kurduğu derin bir felsefi araştırmadır.",
            "voice": "Geleneksel zanaatlar, insan bedeninin malzemeyle kurduğu en derin bilgi sistemleridir.",
            "image": cover_img_file
        },
        {
            "headline": "Algoritmik Dönüşüm",
            "caption": "Çağdaş yaratıcı kodlayıcılar geleneksel el bilgisini modern yapay zekâ ve robotik üretimle harmanlıyor.",
            "voice": "Çağdaş kodlayıcılar, bu kadim bilgiyi yapay zekâ ve generatif sistemlerle geleceğe taşıyor.",
            "image": cover_img_file
        },
        {
            "headline": "Craft & Code Araştırmaları",
            "caption": "Zanaat ve teknolojinin kesiştiği tüm araştırmalar için profilimizdeki bağlantıyı ziyaret edin.",
            "voice": "Zanaat ve kodun kesişimindeki tüm araştırmalar Craft and Code'da. Takipte kalın.",
            "image": cover_img_file,
            "cta": True
        }
    ]
    return category, fallback_scenes

def render_shorts_video(slug, output_file=None):
    """Main rendering engine for a single YouTube Shorts video."""
    print(f"\n🎬 Starting YouTube Shorts generation for: {slug}...")
    
    # 1. Locate markdown file
    md_file = CONTENT_DIR / "published" / "tr" / f"{slug}.md"
    if not md_file.exists():
        md_file = CONTENT_DIR / "drafts" / "tr" / f"{slug}.md"
    if not md_file.exists():
        matches = list(CONTENT_DIR.glob(f"**/{slug}.md"))
        if matches:
            md_file = matches[0]
        else:
            raise FileNotFoundError(f"Article not found for slug: {slug}")
            
    fm, content = parse_article_markdown(md_file)
    category, storyboard = build_storyboard(slug, fm, content)
    total_scenes = len(storyboard)
    
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    if not output_file:
        output_file = VIDEOS_DIR / f"{slug}-shorts.mp4"
    else:
        output_file = Path(output_file)
        
    temp_dir = Path(tempfile.mkdtemp(prefix="craft_shorts_"))
    
    try:
        scene_video_clips = []
        total_duration = 0.0
        
        # Process each scene in storyboard
        for idx, scene in enumerate(storyboard):
            scene_num = idx + 1
            print(f"  • Generating Scene {scene_num}/{total_scenes}: {scene['headline']}...")
            
            # 1. Audio Narration
            speech_wav = temp_dir / f"speech_{scene_num}.wav"
            synthesize_speech(scene["voice"], speech_wav)
            audio_dur = get_audio_duration(speech_wav)
            scene_duration = max(5.0, round(audio_dur + 0.8, 2))
            total_duration += scene_duration
            
            # 2. Base Cropped Image
            img_filename = scene.get("image", "kintsugi-porselen-macro.jpg")
            img_path = PUBLIC_DIR / "images" / img_filename
            if not img_path.exists():
                img_path = PUBLIC_DIR / "images" / "weaving-and-code-cover.jpg"
                
            base_canvas = create_base_canvas(img_path)
            base_frame_path = temp_dir / f"base_{scene_num}.jpg"
            base_canvas.save(base_frame_path, quality=95)
            
            # Save thumbnail from Scene 1
            if scene_num == 1:
                thumb_path = VIDEOS_DIR / f"{slug}-shorts-thumb.jpg"
                base_canvas.save(thumb_path, quality=90)
                if DIST_DIR.exists():
                    (DIST_DIR / "videos").mkdir(parents=True, exist_ok=True)
                    shutil.copy2(thumb_path, DIST_DIR / "videos" / f"{slug}-shorts-thumb.jpg")
            
            # 3. Transparent Typographic Overlay
            overlay = render_scene_overlay(
                scene_num=scene_num,
                total_scenes=total_scenes,
                category=category,
                headline=scene["headline"],
                quote_text=scene["caption"],
                cta_mode=scene.get("cta", False)
            )
            overlay_path = temp_dir / f"overlay_{scene_num}.png"
            overlay.save(overlay_path, "PNG")
            
            # 4. Render Scene Video with Ken Burns Zoom & Graphic Overlay
            scene_clip = temp_dir / f"clip_{scene_num}.mp4"
            
            # Alternating zoom direction (zoom in on odd, zoom out on even)
            if scene_num % 2 == 1:
                zoom_expr = "zoompan=z='min(zoom+0.0007,1.15)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=25"
            else:
                zoom_expr = "zoompan=z='max(1.15-0.0007*on,1.0)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=25"
                
            render_cmd = [
                "ffmpeg", "-y",
                "-loop", "1", "-i", str(base_frame_path),
                "-loop", "1", "-i", str(overlay_path),
                "-i", str(speech_wav),
                "-filter_complex",
                f"[0:v]{zoom_expr},format=yuv420p[bg];"
                f"[bg][1:v]overlay=0:0:shortest=1[vout]",
                "-map", "[vout]",
                "-map", "2:a",
                "-c:v", "libopenh264",
                "-pix_fmt", "yuv420p",
                "-c:a", "aac",
                "-b:a", "192k",
                "-t", str(scene_duration),
                str(scene_clip)
            ]
            subprocess.run(render_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            scene_video_clips.append(scene_clip)
            
        # 5. Concatenate Scenes with Concat Demuxer
        print("  • Assembling and mixing ambient soundtrack...")
        concat_txt = temp_dir / "concat_list.txt"
        with open(concat_txt, "w") as f:
            for clip in scene_video_clips:
                f.write(f"file '{clip.resolve()}'\n")
                
        raw_concat_video = temp_dir / "raw_concat.mp4"
        cmd_concat = [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", str(concat_txt),
            "-c", "copy",
            str(raw_concat_video)
        ]
        subprocess.run(cmd_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # 6. Generate Master Ambient Track matching total duration
        ambient_wav = temp_dir / "master_ambient.wav"
        generate_ambient_track(total_duration + 1.0, ambient_wav)
        
        # 7. Final Audio Mix (Ducking narration over ambient music) + FastStart MP4
        cmd_final = [
            "ffmpeg", "-y",
            "-i", str(raw_concat_video),
            "-i", str(ambient_wav),
            "-filter_complex",
            "[0:a]volume=1.4[voice];"
            "[1:a]volume=0.28[music];"
            "[voice][music]amix=inputs=2:duration=first:dropout_transition=2[aout]",
            "-map", "0:v",
            "-map", "[aout]",
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-movflags", "+faststart",
            str(output_file)
        ]
        subprocess.run(cmd_final, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Copy to dist for instant web serving
        if DIST_DIR.exists():
            (DIST_DIR / "videos").mkdir(parents=True, exist_ok=True)
            shutil.copy2(output_file, DIST_DIR / "videos" / output_file.name)
            
        # 8. Create YouTube SEO Metadata Package
        clean_title = fm.get("title", slug)
        seo_meta = {
            "slug": slug,
            "youtube_title": f"{clean_title[:75]} | Craft&Code #Shorts",
            "youtube_description": (
                f"{clean_title}\n\n"
                f"{fm.get('summary', '')}\n\n"
                f"📖 Araştırmanın tamamını okumak ve küratöryel arşivi incelemek için: https://rkiritoglu.github.io/Craft-Code/yazi/{slug}.html\n\n"
                f"#Shorts #CraftAndCode #SanatTarihi #GeneratifSanat #Teknoloji #KreatifKodlama"
            ),
            "hashtags": [
                "#Shorts", "#CraftAndCode", "#GeneratifSanat",
                "#SanatTarihi", "#Teknoloji", "#GelenekselZanaat"
            ],
            "duration": round(total_duration, 1),
            "resolution": "1080x1920 (9:16)",
            "video_url": f"/videos/{output_file.name}",
            "thumb_url": f"/videos/{slug}-shorts-thumb.jpg",
            "file_size_kb": round(output_file.stat().st_size / 1024, 1)
        }
        
        meta_json_path = VIDEOS_DIR / f"{slug}-shorts-meta.json"
        meta_json_path.write_text(json.dumps(seo_meta, indent=2, ensure_ascii=False), encoding="utf-8")
        if DIST_DIR.exists():
            shutil.copy2(meta_json_path, DIST_DIR / "videos" / meta_json_path.name)
            
        print(f"✨ YouTube Shorts ready: {output_file} ({seo_meta['duration']}s, {seo_meta['file_size_kb']} KB)")
        return seo_meta
        
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def generate_daily_shorts():
    """Finds the most recent published article and generates a YouTube Shorts video for it."""
    pub_dir = CONTENT_DIR / "published" / "tr"
    if not pub_dir.exists() or not list(pub_dir.glob("*.md")):
        pub_dir = CONTENT_DIR / "drafts" / "tr"
        
    articles = list(pub_dir.glob("*.md"))
    if not articles:
        print("❌ No articles found to generate Shorts!")
        return None
        
    articles.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    latest_slug = articles[0].stem
    return render_shorts_video(latest_slug)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        pub_dir = CONTENT_DIR / "published" / "tr"
        for md in pub_dir.glob("*.md"):
            render_shorts_video(md.stem)
    elif len(sys.argv) > 1 and sys.argv[1] != "--latest":
        render_shorts_video(sys.argv[1])
    else:
        generate_daily_shorts()
