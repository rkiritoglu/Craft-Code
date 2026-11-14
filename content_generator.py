#!/usr/bin/env python3
"""
Craft&Code Editorial Topic Generator & Memory Engine
Maintains editorial history to prevent duplicate themes and generates fresh, non-overlapping research topics.
"""

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
CONTENT_DIR = ROOT_DIR / "content"
DATA_DIR = ROOT_DIR / "data"
MEMORY_FILE = DATA_DIR / "editorial_memory.json"

# Master catalog of research topics across diverse, rich craft disciplines
MASTER_TOPIC_CATALOG = [
    {
        "id": "kintsugi-glitch",
        "slug": "kintsugi-ve-dijital-kusur",
        "category": "Seramik & Glitch Art",
        "craft_domain": "kintsugi seramik porselen wabi-sabi",
        "title": "Kırığın Poetikası: Kintsugi, Dijital Kusur ve Veri Onarımı",
        "title_en": "The Poetics of the Fracture: Kintsugi, Digital Glitch, and Data Mending",
        "thesis": "Kusuru gizlemek yerine yüceltmek. 15. yüzyıl Japon Kintsugi felsefesinin, yeni medya sanatındaki bozuk veri onarımı ve glitch estetiğiyle felsefi diyaloğu.",
        "cases": "Rachel Sussman, Wabi-sabi ontolojisi, Algoritmik 3D kırık onarımı ve altın neon fiberler."
    },
    {
        "id": "ebru-algoritmalar",
        "slug": "ebru-ve-sivi-algoritmalar",
        "category": "Ebru & Akışkan Simülasyonu",
        "craft_domain": "ebru marbling akiskan sivi pigment kitre",
        "title": "Sıvı Algoritmalar: Ebru Sanatının Kaos Matematiği ve Generatif Akışkanlar",
        "title_en": "Liquid Algorithms: The Chaotic Mathematics of Ebru and Generative Fluid Dynamics",
        "thesis": "Ebru, dünyanın ilk generatif sanatıdır. Kitre ve yüzey geriliminin mikro-akışkan dinamiği ile modern Navier-Stokes kod simülasyonları arasındaki organik köprü.",
        "cases": "Garip Ay performansları, p5.js/GLSL vektör akış alanları, Refik Anadol veri pigmentleri."
    },
    {
        "id": "selcuklu-cini-3d",
        "slug": "selcuklu-cini-ve-3d-baski",
        "category": "Mimari Çini & 3D Fabrikasyon",
        "craft_domain": "cini seramik girih selcuklu mimari karo",
        "title": "Parametrik Çini: Selçuklu Girih Geometrisi ve Robotik Kil",
        "title_en": "Parametric Faience: Seljuk Girih Geometry and Robotic Clay Fabrication",
        "thesis": "Selçuklu ustalarının Batı'dan 500 yıl önce keşfettiği yarı-kristal (quasicrystal) geometrinin, günümüz robotik 3D seramik ekstrüzyonu ile yeniden doğuşu.",
        "cases": "Peter Lu (Harvard Science 2007 araştırması), Ronald Rael & 3D kil basımı, parametrik cepheler."
    },
    {
        "id": "hat-generatif-tipografi",
        "slug": "hat-sanati-ve-robotik-kaligrafi",
        "category": "Hat Sanatı & Robotik Kaligrafi",
        "craft_domain": "hat kaligrafi yazi murekkep kamis tipografi",
        "title": "Kamış Kalemin Nefesi: Hat Sanatının Geometrisi ve Robotik Kaligrafi",
        "title_en": "The Breath of the Reed: Calligraphic Geometry and Robotic Scribes",
        "thesis": "Hat sanatındaki 'nokta' tabanlı parametrik oran sistemi ile yapay zekâ fırça algoritmaları ve robotik kolların insan-makine kaligrafi düetleri.",
        "cases": "Aklâm-ı Sitte nokta matematiği, Sougwen Chung (Drawing Operations), AxiDraw generatif kodlama."
    },
    {
        "id": "cam-ve-raymarching",
        "slug": "cam-ufleme-ve-isik-kirilmasi",
        "category": "Cam Zanaatı & Shader Kodları",
        "craft_domain": "cam glassblowing optik isik kirilma fırın",
        "title": "Ateşin Viskozitesi: Venedik Cam Zanaatı ve Algoritmik Işık Kırılması (Raymarching)",
        "title_en": "Viscosity of Fire: Venetian Glassblowing and Algorithmic Caustics",
        "thesis": "1000 derecede eriyen silika camının yerçekimi ve nefesle şekillenmesi ile bilgisayar grafiklerindeki foton haritalama ve caustics shader simülasyonları.",
        "cases": "Murano ustaları, Neri Oxman (MIT Glass 3D printing), GLSL gerçek zamanlı optik shader'lar."
    },
    {
        "id": "kok-boya-biyohesaplama",
        "slug": "kok-boyacilik-ve-biyo-tasarim",
        "category": "Doğal Pigment & Biyo-Tasarım",
        "craft_domain": "boya kokboya pigment liken dogal kumas",
        "title": "Toprağın Moleküler Rengi: Kadim Kök Boyacılık ve Bakteriyel Pigment Kodlaması",
        "title_en": "Molecular Earth: Ancient Natural Dyeing and Bacterial Pigment Algorithms",
        "thesis": "Köklerden ve likenlerden elde edilen kadim boyama simyası; günümüzde sentetik biyoloji, bakteriyel fermentasyon ve generatif renk haritalarıyla buluşuyor.",
        "cases": "Anadolu kök boya gelenekleri, Faber Futures (Natsai Audrey Chieza), biyolojik algoritmik boyama."
    },
    {
        "id": "kundekari-robotik-ahsap",
        "slug": "kundekari-ve-parametrik-ahsap",
        "category": "Ahşap Kündekâri & Dijital Eklemler",
        "craft_domain": "ahsap marangozluk kundekari gecme civi marangoz",
        "title": "Çivisiz Geometri: Selçuklu Kündekâri Zanaatı ve Robotik Ahşap Eklemleri",
        "title_en": "Nail-less Geometry: Seljuk Kundekari Joinery and Robotic Timber Structures",
        "thesis": "Tutkal ve çivi kullanmadan ahşabın nefes almasını sağlayan zıvanalı kündekâri zanaatı; parametrik robotik ahşap strüktürleri ve tolerans algoritmalarıyla canlanıyor.",
        "cases": "Tarihi ahşap cami minberleri, Gramazio Kohler Research (ETH Zürih), 7 eksenli robotik ahşap frezeleme."
    },
    {
        "id": "dovme-bakir-ses",
        "slug": "dovme-bakir-ve-akustik-rezonans",
        "category": "Bakır Zanaatı & Ses Heykelleri",
        "craft_domain": "bakir maden dovme celik ses akustik rezonans",
        "title": "Çekicin Yankısı: Dövme Bakır Zanaatı ve Algoritmik Akustik Rezonans",
        "title_en": "Echoes of the Anvil: Coppersmithing and Algorithmic Acoustic Resonance",
        "thesis": "Bakır levhayı çekiç vuruşlarının ritmiyle sertleştirip form verme zanaatı; fiziksel modelleme sentezi ve mikrotonal rezonans frekanslarıyla çalışan ses heykelleriyle kesişiyor.",
        "cases": "Kazancılar Çarşısı çekiç poliritimleri, Harry Bertoia ses heykelleri, MaxMSP fiziksel akustik simülasyonları."
    }
]

def init_memory():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not MEMORY_FILE.exists():
        initial_data = {
            "covered_slugs": ["dokuma-tezgahindan-koda"],
            "covered_keywords": ["dokuma", "jakar", "tezgah", "tekstil"],
            "active_proposals": ["kintsugi-glitch", "ebru-algoritmalar", "selcuklu-cini-3d"]
        }
        MEMORY_FILE.write_text(json.dumps(initial_data, indent=2, ensure_ascii=False), encoding="utf-8")

def get_covered_slugs():
    """Scans all published and drafted markdown files in content directory."""
    slugs = set()
    for md in CONTENT_DIR.glob("**/*.md"):
        slugs.add(md.stem)
    return slugs

def load_memory():
    init_memory()
    try:
        data = json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    except Exception:
        data = {"covered_slugs": [], "covered_keywords": [], "active_proposals": []}

    # Synchronize with actual files on disk
    disk_slugs = get_covered_slugs()
    data["covered_slugs"] = list(set(data.get("covered_slugs", [])).union(disk_slugs))
    return data

def save_memory(data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    MEMORY_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def get_active_proposals():
    mem = load_memory()
    covered = set(mem.get("covered_slugs", []))

    # Retrieve proposal objects from catalog
    active_ids = mem.get("active_proposals", [])
    results = []
    for item in MASTER_TOPIC_CATALOG:
        if item["id"] in active_ids and item["slug"] not in covered:
            results.append(item)

    # If fewer than 3, refresh to fill
    if len(results) < 3:
        results = refresh_proposals()

    return results

def refresh_proposals():
    """
    Intelligently generates 3 non-overlapping, fresh topic proposals
    by strictly excluding already written crafts and topics!
    """
    mem = load_memory()
    covered = set(mem.get("covered_slugs", []))
    current_active_ids = set(mem.get("active_proposals", []))

    # Candidates that have NOT been written yet
    available_candidates = [
        item for item in MASTER_TOPIC_CATALOG 
        if item["slug"] not in covered
    ]

    # Prioritize candidates not currently active
    fresh_candidates = [c for c in available_candidates if c["id"] not in current_active_ids]

    selected = []
    # Take from fresh
    for c in fresh_candidates:
        selected.append(c)
        if len(selected) == 3:
            break

    # If still need more, fill from available
    if len(selected) < 3:
        for c in available_candidates:
            if c not in selected:
                selected.append(c)
            if len(selected) == 3:
                break

    mem["active_proposals"] = [s["id"] for s in selected]
    save_memory(mem)
    return selected

def generate_topic_draft(topic_key):
    """Generates the full markdown draft files for an approved topic."""
    # Find in catalog
    match = None
    for item in MASTER_TOPIC_CATALOG:
        if item["id"] == topic_key:
            match = item
            break

    if not match:
        raise ValueError(f"Unknown topic key: {topic_key}")

    slug = match["slug"]

    # Map bespoke museum-grade diffusion image for each topic
    img_map = {
        "kintsugi-ve-dijital-kusur": "/images/kintsugi-porselen-macro.jpg",
        "ebru-ve-sivi-algoritmalar": "/images/ebru-cover.jpg",
        "dokuma-tezgahindan-koda": "/images/weaving-and-code-cover.jpg",
        "selcuklu-cini-ve-3d-baski": "/images/selcuklu-cini-cover.jpg",
        "hat-sanati-ve-robotik-kaligrafi": "/images/hat-sanati-cover.jpg",
        "cam-ufleme-ve-isik-kirilmasi": "/images/cam-ufleme-cover.jpg",
        "kok-boyacilik-ve-biyo-tasarim": "/images/kok-boya-cover.jpg",
        "kundekari-ve-parametrik-ahsap": "/images/kundekari-ahsap-cover.jpg",
        "dovme-bakir-ve-akustik-rezonans": "/images/dovme-bakir-cover.jpg",
    }
    cover_image = img_map.get(slug, "/images/kintsugi-porselen-macro.jpg")

    # Turkish Markdown content
    tr_body = f"""
{match['thesis']}

## 1. Kadim Sözdizimi: Malzemenin ve Bedenin Hafızası
Her kadim zanaat, kendi çağının en ileri malzeme teknolojisi ve ontolojik bilgi sistemidir. Ustanın eli malzemeye değerken, fiziksel dünyanın kurallarıyla doğrudan bir müzakere yürütür.

> "Zanaatkâr, eylemi esnasında maddeyle sürekli ve samimi bir diyalog kurar; onu boyunduruk altına almaz, onun direncini dinler." -- Richard Sennett, The Craftsman

## 2. Sayısal Dönüşüm ve Algoritmik Müdahale
Çağdaş yeni medya sanatçıları ve yaratıcı kodlayıcılar, bu geleneksel disiplini müzelik bir nostalji olmaktan çıkarıp, güncel algoritmik sistemlerin (generatif kod, yapay zekâ, robotik üretim) eleştirel bir aynası olarak kullanmaktadır.

:::curatorial Küratöryel Not
Zanaatın bedensel sabrı ile kodun sonsuz soyutlama yeteneği karşılaştığında; ne gelenek geride kalır ne de teknoloji tek başına hükmeder. Ortaya çıkan form, insan hafızasının hibrit bir manifestosudur.
:::

## 3. Vaka İncelemeleri
{match['cases']}

## 4. Eleştirel Sentez
Zanaat ile kodun bu kesişimi, bize geleceğin teknolojisini tasarlarken kadim el bilgisini unutmamamız gerektiğini fısıldar.

---
### Kaynakça ve İleri Okumalar
1. **Sennett, Richard.** *The Craftsman*. Yale University Press, 2008.
2. **Ingold, Tim.** *Making: Anthropology, Archaeology, Art and Architecture*. Routledge, 2013.
3. **Craft&Code Araştırma Arşivi**, 2026.
"""

    tr_md = f"""---
title: "{match['title']}"
subtitle: "{match['thesis'][:120]}..."
summary: "{match['thesis']}"
slug: "{slug}"
date: "2026-11-14"
author: "Craft&Code Araştırma Masası"
tags: ["{match['category'].split('&')[0].strip()}", "Çağdaş Sanat", "Generatif Kod", "Yeni Medya"]
cover_image: "{cover_image}"
cover_caption: "Kavramsal Eser: {match['title']} üzerine küratöryel stüdyo araştırması."
cover_credit: "Görsel: Craft&Code / Yapay Zekâ & Küratöryel Konsept Tasarımı"
draft: true
---
{tr_body.strip()}
"""
    tr_file = CONTENT_DIR / "drafts" / "tr" / f"{slug}.md"
    tr_file.parent.mkdir(parents=True, exist_ok=True)
    tr_file.write_text(tr_md, encoding="utf-8")

    # English Markdown content
    en_body = f"""
{match['thesis']}

## 1. The Ancient Syntax: Material and Bodily Memory
Every ancient craft represents the vanguard material intelligence of its epoch. In negotiating with material resistance, the artisan executes an intimate epistemic inquiry.

> "The craftsman conducts a continuous and candid dialogue with matter; they do not subdue it, but heed its intrinsic resistance." -- Richard Sennett, The Craftsman

## 2. Computational Transitions & Algorithmic Intervention
Contemporary new media artists and creative coders emancipate traditional craft from ethnographic sentimentality, harnessing its structural logic as a critical mirror against algorithmic hegemony.

:::curatorial Curatorial Note
When bodily craft knowledge encounters computational abstraction, neither tradition nor code remains static; the emergent form is a hybrid manifesto of human consciousness.
:::

## 3. Curated Case Studies
{match['cases']}

## 4. Critical Synthesis
This convergence between craft and code urges us never to divorce future computational paradigms from primordial tactile intelligence.

---
### Bibliography & References
1. **Sennett, Richard.** *The Craftsman*. Yale University Press, 2008.
2. **Ingold, Tim.** *Making: Anthropology, Archaeology, Art and Architecture*. Routledge, 2013.
3. **Craft&Code Editorial Archive**, 2026.
"""

    en_md = f"""---
title: "{match['title_en']}"
subtitle: "{match['thesis'][:120]}..."
summary: "{match['thesis']}"
slug: "{slug}"
date: "2026-11-14"
author: "Craft&Code Editorial Desk"
tags: ["{match['category'].split('&')[0].strip()}", "Contemporary Art", "Generative Code", "New Media"]
cover_image: "{cover_image}"
cover_caption: "Conceptual Artwork: Curatorial studio exploration of {match['title_en']}."
cover_credit: "Visual: Craft&Code / AI & Curatorial Concept Synthesis"
draft: true
---
{en_body.strip()}
"""
    en_file = CONTENT_DIR / "drafts" / "en" / f"{slug}.md"
    en_file.parent.mkdir(parents=True, exist_ok=True)
    en_file.write_text(en_md, encoding="utf-8")

    # Record in memory
    mem = load_memory()
    if slug not in mem["covered_slugs"]:
        mem["covered_slugs"].append(slug)
    # Remove from active proposals
    if topic_key in mem.get("active_proposals", []):
        mem["active_proposals"].remove(topic_key)
    save_memory(mem)

    return slug
