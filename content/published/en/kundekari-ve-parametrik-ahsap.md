---
title: "Çivisiz Geometri: Selçuk Kundekari Doğramacılığı ve Robotik Ahşap Yapılar"
subtitle: "Konya ve Beyşehir'deki çivisiz, tutkalsız kırmalı Anadolu Selçuklu ahşap doğramalarından, higroskopik tolerans çalışmalarına ve 7 eksenli robotik kereste frezeleme sistemlerine kadar."
summary: "Tutkal ve çivi kullanmadan ahşabın nefes almasını sağlayan zıvanalı kündekâri zanaatı; parametrik robotik ahşap strüktürleri ve tolerans algoritmalarıyla canlanıyor."
slug: "kundekari-ve-parametrik-ahsap"
date: "2026-11-14"
author: "Craft&Code Editorial Desk"
tags: ["Kundekari", "Timber Joinery", "Robotic CNC", "Parametric Architecture", "New Media"]
cover_image: "/images/kundekari-ahsap-cover.jpg"
cover_caption: "Kavramsal Sentez: Geleneksel Selçuk ceviz ağacı kundekari yıldız kırma teknolojisinin, parametrik ihlal toleransları ve robotik ahşap işleme ile yasak."
cover_credit: "Görsel: Craft&Code / Yapay Zeka ve Küratöryel Kavram Sentezi"
draft: false
---
To a hurried contemporary eye, geometric star octagons and hexagons across historic Anatolian mosque pulpits (*minbers*) and sanctuary doors appear merely ornamental carving. In authentic **hakikî kündekâri**, however, geometry is never superficial decoration; it represents high-precision **structural wood engineering engineered completely without nails, screws, or structural glue**—designed specifically to endure centuries by embedding wood moisture dynamics inside interlocking topology.

Every winter-to-summer humidity shift triggers anisotropic swelling and shrinkage across timber grain. Lock a broad solid wood board flat with iron nails or rigid glue, and seasonal stress inevitably splits the slab down the middle. Anatolian Seljuk and early Ottoman master carpenters (*neccârân*) inverted resistance into principle: locking small floating polygon **infill panels** inside grooved **frame rails** with deliberate expansion clearances, forging a physical mechanical tolerance algorithm. Today, robotic timber laboratories in Zurich and Lausanne translate these exact nail-less joinery principles into parametric CNC toolpaths.

## 1. Historical Roots: From Malatya and Konya Minbers to Imperial Joinery

Rooted in Persian terminology denoting "assembled molding," *kündekâri* synthesis traveled through eleventh-century Egypt, Syria, and Iran before reaching structural zenith inside **Anatolian Seljuk woodwork**. The iconic **minber of Konya's Alâeddin Mosque** (dated 1155 and signed by craftsman Mengü Berti of Ahlat) stands as one of Islamic architecture's earliest surviving masterpieces of genuine floating geometric assembly.

Landmark monuments construct an unbroken lineage across centuries: Malatya Great Mosque, Siirt Great Mosque, **Birgi Great Mosque (1322)**, and the extraordinary columned hall of **Beyşehir Eşrefoğlu Mosque (1299)**. While later centuries introduced cheaper imitation relief carving (*taklit kündekâri* nailed atop solid boards) that warped noticeably over decades, authentic nail-less *hakikî* joinery remains tight and self-supporting seven centuries after carving.

## 2. Mortise, Groove, and Hygroscopic Clearance Anatomy

Master joiners approached seasoned hardwood not as uniform inert lumber, but as living cellulose responsive across decades of humid springs and dry winters:

![Seljuk kundekari architectural cross-section and star topology diagram depicting grooved frame rails enclosing floating panels with seasonal moisture gap delta-t](/images/kundekari-zivana-diagram.svg "Kündekâri Joinery Mechanics: Interlocking 8-fold star panel frame topology (left) paired with cross-sectional groove tolerance delta-t and 7-axis CNC toolpath (right) | Visual: Craft&Code Computational Diagram Archive")

- **Timber Selection & Multi-Year Seasoning:** Carpenters chose dense, tight-grained species balancing toughness with carved stability: **Anatolian walnut**, **cedar**, **ebony**, **pear**, and **boxwood**. Felled boards rested shaded outdoors under gentle ventilation for **five to ten years** before chisels ever scored wood fibers.
- **Two Structural Classes (*Dolgu* Infill & *Kayıt* Rails):**
  - **Floating Geometric Panels (*Dolgu*):** Small diamond, kite, pentagon, and 8-to-12 pointed star cores trimmed cleanly along every perimeter edge into tapered beveled tongues (**zıvana dili / chamfer**), orienting annual growth rings concentrically across symmetry lines.
  - **Grooved Structural Rails (*Kayıt*):** Linear skeleton ribs bounding stars tightly together. Inside rails, craftsmen channeled V- or U-profiled slots (**lamba / kiniş**) using narrow planes and steel *ıskarpela* chisels—interlocking rail intersections cleanly via mitered **mortise-and-tenon** locks.
- **The Essential Secret — *Hygroscopic Expansion Gap* ($\Delta t$):** Masters deliberately never seat floating infill tongues flush against inner rail groove floors, nor introduce animal hide glue inside grooves. Milling channel sockets **1.5–2.5 mm deeper** than each panel tongue preserves safe slip room ($\Delta t$): even in dry winters panels stay captured safely, while summer swelling slides calmly deeper without fracturing neighboring rails outward.

> "Glue imprisons wood until tension breaks it; tenon gives timber sovereignty—true kündekâri endures precisely because it builds seasonal motion directly into geometry." -- Traditional Anatolian Woodcraft Principle

## 3. Craft to Code: Structural Correspondences & Algorithmic Translation

Calculating groove depths relative to species swelling factors ($\Delta t$) while computing multi-bevel angles across compound domes translates directly into **parametric timber joinery algorithms** and **5/7-axis collision-free CNC toolpaths**.

| Traditional Kündekâri Element | Physical & Mechanical Role on the Bench | Equivalent Construct in Parametric Joinery & Code |
| :--- | :--- | :--- |
| True Nail-less Assembly (*Hakikî Geçme*) | Allows reversible disassembly and stress-free replacement of damaged blocks. | Topological interlocking constraints (`interlocking_constraint` graph) |
| Skeletal Structural Frame Rails (*Kayıt*) | Distributes mechanical loads across polygonal boundary vertices cleanly. | Dual skeletal edge mesh graph (`dual_frame_edges`) & miter nodes |
| Floating Polygon Infill Blocks (*Dolgu*) | Isolates localized wood swelling within discrete small planar elements. | Parameterized cell polygons & aligned timber grain vectors (`grain_vector`) |
| Recessed Groove Channel (*Lamba / Kiniş*) | Captures chamfered panel bevels preventing out-of-plane buckling safely. | Boolean pocket subtraction (`channel_cut = panel_offset - depth`) |
| Seasonal Moisture Expansion Gap ($\Delta t$) | Absorbs ambient humidity swelling quietly inside recessed frame sockets. | Hygroscopic clearance solver (`tolerance_mm = width * moisture_coeff`) |
| Chamfered Panel Edge Bevels | Locks miter angles crisply across 22.5°, 36°, or 45° polygon corners. | Multi-axis tool orientation vector (**5/7-axis CNC normal tilt**) |
| Grain-Aware Cut Direction | Prevents fiber tear-out when slicing crisp bevel shoulders cleanly. | Climb vs. conventional milling path aligned against local grain field |

:::bridge Craft-to-Code Bridge
Whenever an Anatolian carpenter gauged walnut panel widths against ambient moisture to cut `1.8 mm` extra recess depth inside surrounding rail grooves, that craft executed an intuitive **anisotropic hygroscopic strain calculation**: wood stays dimensionally static along axial grain while expanding tangentially proportional to ambient humidity swings. Encoding this species law directly into **7-axis CNC robotics** computes safe slip tolerances per vertex automatically—carrying thirteenth-century Seljuk wisdom seamlessly into contemporary multi-story timber architecture.
:::

The Python model below calculates seasonal moisture clearances (`compute_hygroscopic_clearance`) across walnut, cedar, and oak parameters, outputting exact bevel angles and robotic groove depths ready for digital fabrication.

```python title="Seljuk Kündekâri Hygroscopic Tolerance & Robotic Joinery Spec"
# Craft&Code — Seasonal Timber Clearance & Multi-Axis Joint Specification
import math

WOOD_TANGENTIAL_SHRINKAGE = {
    "Walnut (Ceviz)": 0.0026,   # Tangential swelling rate per humidity step
    "Cedar (Sedir)":  0.0018,
    "Oak (Mese)":     0.0034,
}

def compute_hygroscopic_clearance(panel_span_mm, wood_species, delta_humidity_pct=18.0):
    """Calculates required lamba groove expansion room (delta-t) cleanly."""
    coeff = WOOD_TANGENTIAL_SHRINKAGE[wood_species]
    max_expansion = panel_span_mm * coeff * (delta_humidity_pct / 5.0)
    safety_margin = 0.65  # Acoustic dust and surface asperity clearance
    return round(max_expansion + safety_margin, 2)

def generate_kundekari_joint_spec(arms=8, outer_radius_mm=140.0, wood_species="Walnut (Ceviz)"):
    """Outputs parametric bevel angles, tongue thickness, and grooved rail depths."""
    miter_angle_deg = round(180.0 / (arms * 2), 2)
    clearance = compute_hygroscopic_clearance(outer_radius_mm, wood_species)
    tongue_depth_mm = 7.5
    groove_depth_mm = round(tongue_depth_mm + clearance, 2)

    nodes = []
    for k in range(arms * 2):
        angle = k * math.pi / arms
        rad = outer_radius_mm if k % 2 == 0 else outer_radius_mm * 0.54
        nodes.append((round(rad * math.cos(angle), 2), round(rad * math.sin(angle), 2)))

    return {
        "wood": wood_species,
        "miter_bevel_deg": miter_angle_deg,
        "tongue_depth_mm": tongue_depth_mm,
        "groove_depth_mm": groove_depth_mm,
        "hygroscopic_gap_mm": clearance,
        "bevel_vertices": nodes,
    }
```

Notice how `groove_depth_mm = tongue_depth_mm + clearance` formalizes the oral atelier safeguard that prevented hundreds of medieval Anatolian walnut pulpits from fracturing across centuries.

## 4. Contemporary Practice & Scientific Case Studies

Three decisive architectural benchmarks tie historic Anatolian woodwork directly to modern structural computation and carbon-negative fabrication.

### Case Study 1: Konya Alâeddin & Beyşehir Eşrefoğlu Mosque Pulpits (12th–13th Century)
Standing across highland central Anatolia where harsh dry winters clash violently against lakeside humidity, the 1155 **Alâeddin Mosque Minber** and 1299 **Eşrefoğlu Mosque** wood ensembles survive virtually intact without warping after eight centuries. Modern conservation endoscopy confirms over three hundred discrete polygonal panels per flank float cleanly unglued inside mitered grooved rails—proving passive algorithmic tolerance outlasts iron fasteners reliably across millennia.

### Case Study 2: Gramazio Kohler Research (ETH Zürich) — *Robotic Timber Construction* (2012–2023)
At ETH Zürich, **Gramazio Kohler Research** pioneered automated robotic timber assembly systems driving multi-axis CNC routers straight from structural CAD topologies. By generating exact compound miter cuts, stepped tenons, and zero-bolt interlocking joints across long-span roof trusses, their robotic platforms revive craft timber assembly at contemporary architectural infrastructure scales without synthetic adhesive dependency.

### Case Study 3: IBOIS Laboratory (EPFL Lausanne, Yves Weinand) — *Integral Timber Joints* (2014–Present)
Led by Prof. Yves Weinand at EPFL's Laboratory for Timber Construction (**IBOIS**), **Integral Mechanical Attachment** research unifies traditional woodworking joints with finite-element structural solvers—engineering massive folded cross-laminated timber shells held aloft exclusively through CNC-milled dovetails, slots, and floating wedges inspired directly by nail-less Asian and Seljuk carpentry.

## 5. Critical Synthesis: Resistance of Matter, Horizons of Code

Seven-axis milling arms execute compound polygon chamfers rapidly without fatigue, yet raw steel blades feel neither latent timber knots nor subtle seasonal resin tension humming beneath crisp grain paths. True *kündekâri* reminds digital architecture of an urgent ecological lesson: **durable design never cages living materials inside rigid constraints; it carves generous tolerances allowing change to dwell safely inside geometry.**

:::curatorial Curatorial Note
From the thirteenth-century Beyşehir master seating unglued walnut stars inside grooved rails to ETH roboticists scripting hygroscopic tolerances in Python, one enduring axiom binds craft and code: **longevity belongs not to what resists movement, but to geometry smart enough to welcome breath.**
:::

---

### Bibliography & Further Reading
1. **Öney, Gönül.** *Anadolu Selçuklu Mimari Süslemesi ve El Sanatları*. Türkiye İş Bankası Kültür Yayınları, Ankara, 1978.
2. **Sönmez, Zeki.** *Başlangıcından 16. Yüzyıla Kadar Anadolu Türk-İslam Mimarisinde Sanatçılar*. Türk Tarih Kurumu, Ankara, 1995.
3. **Weinand, Yves (Ed.).** *Advanced Timber Structures: Architectural Designs and Digital Dimensioning*. Birkhäuser, Basel, 2016.
4. **Willmann, Jan, et al.** "Robotic Timber Construction — Expanding Additive Fabrication to New Dimensions." *Automation in Construction*, Vol. 61, 2016, pp. 16–23.
5. **Bozer, Rüstem.** *Ahşap İşçiliği: Anadolu Selçuklu ve Beylikler Dönemi Minberleri*. Ministry of Culture Publications, Ankara.
