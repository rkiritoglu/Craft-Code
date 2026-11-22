#!/usr/bin/env python3
"""
Craft&Code Editorial Topic Generator & Memory Engine
Maintains editorial history to prevent duplicate themes and generates deep,
long-form bilingual (TR/EN) research drafts rich in traditional craft anatomy
and explicit Craft-to-Code structural translations.
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
        "cases": "Rosa Menkman (Glitch Studies), Rachel Sussman (Sidewalk Kintsukuroi), Bouke de Vries & Digital Kintsugi."
    },
    {
        "id": "ebru-algoritmalar",
        "slug": "ebru-ve-sivi-algoritmalar",
        "category": "Ebru & Akışkan Simülasyonu",
        "craft_domain": "ebru marbling akiskan sivi pigment kitre",
        "title": "Sıvı Algoritmalar: Ebru Sanatının Kaos Matematiği ve Generatif Akışkanlar",
        "title_en": "Liquid Algorithms: The Chaotic Mathematics of Ebru and Generative Fluid Dynamics",
        "thesis": "Ebru, dünyanın ilk generatif sanatıdır. Kitre ve yüzey geriliminin mikro-akışkan dinamiği ile modern Navier-Stokes kod simülasyonları arasındaki organik köprü.",
        "cases": "Necmeddin Okyay & Mustafa Düzgünman ekolü, Lu & Jaffer Matematiksel Ebru, Garip Ay & Refik Anadol."
    },
    {
        "id": "selcuklu-cini-3d",
        "slug": "selcuklu-cini-ve-3d-baski",
        "category": "Mimari Çini & 3D Fabrikasyon",
        "craft_domain": "cini seramik girih selcuklu mimari karo",
        "title": "Parametrik Çini: Selçuklu Girih Geometrisi ve Robotik Kil",
        "title_en": "Parametric Faience: Seljuk Girih Geometry and Robotic Clay Fabrication",
        "thesis": "Selçuklu ustalarının Batı'dan 500 yıl önce keşfettiği yarı-kristal (quasicrystal) geometrinin, günümüz robotik 3D seramik ekstrüzyonu ile yeniden doğuşu.",
        "cases": "Topkapı Tomarı & Peter Lu (Science 2007), Ronald Rael (Emerging Objects), Studio RAP Ceramic House."
    },
    {
        "id": "hat-generatif-tipografi",
        "slug": "hat-sanati-ve-robotik-kaligrafi",
        "category": "Hat Sanatı & Robotik Kaligrafi",
        "craft_domain": "hat kaligrafi yazi murekkep kamis tipografi",
        "title": "Kamış Kalemin Nefesi: Hat Sanatının Geometrisi ve Robotik Kaligrafi",
        "title_en": "The Breath of the Reed: Calligraphic Geometry and Robotic Scribes",
        "thesis": "Hat sanatındaki 'nokta' tabanlı parametrik oran sistemi ile yapay zekâ fırça algoritmaları ve robotik kolların insan-makine kaligrafi düetleri.",
        "cases": "Aklâm-ı Sitte nokta matematiği, Donald Knuth METAFONT, Sougwen Chung (Drawing Operations), AxiDraw."
    },
    {
        "id": "cam-ve-raymarching",
        "slug": "cam-ufleme-ve-isik-kirilmasi",
        "category": "Cam Zanaatı & Shader Kodları",
        "craft_domain": "cam glassblowing optik isik kirilma fırın",
        "title": "Ateşin Viskozitesi: Venedik Cam Zanaatı ve Algoritmik Işık Kırılması (Raymarching)",
        "title_en": "Viscosity of Fire: Venetian Glassblowing and Algorithmic Caustics",
        "thesis": "1100 derecede eriyen silika camının yerçekimi ve nefesle şekillenmesi ile bilgisayar grafiklerindeki foton haritalama ve caustics shader simülasyonları.",
        "cases": "Angelo Barovier & Murano Cristallo, Neri Oxman (MIT G3DP Glass Printing), Inigo Quilez SDF Caustics."
    },
    {
        "id": "kok-boya-biyohesaplama",
        "slug": "kok-boyacilik-ve-biyo-tasarim",
        "category": "Doğal Pigment & Biyo-Tasarım",
        "craft_domain": "boya kokboya pigment liken dogal kumas",
        "title": "Toprağın Moleküler Rengi: Kadim Kök Boyacılık ve Bakteriyel Pigment Kodlaması",
        "title_en": "Molecular Earth: Ancient Natural Dyeing and Bacterial Pigment Algorithms",
        "thesis": "Köklerden ve likenlerden elde edilen kadim boyama simyası; günümüzde sentetik biyoloji, bakteriyel fermentasyon ve generatif renk haritalarıyla buluşuyor.",
        "cases": "Harald Böhmer & DOBAG Projesi, Natsai Audrey Chieza (Project Coelicolor), Laura Luchtman (Living Colour)."
    },
    {
        "id": "kundekari-robotik-ahsap",
        "slug": "kundekari-ve-parametrik-ahsap",
        "category": "Ahşap Kündekâri & Dijital Eklemler",
        "craft_domain": "ahsap marangozluk kundekari gecme civi marangoz",
        "title": "Çivisiz Geometri: Selçuklu Kündekâri Zanaatı ve Robotik Ahşap Eklemleri",
        "title_en": "Nail-less Geometry: Seljuk Kundekari Joinery and Robotic Timber Structures",
        "thesis": "Tutkal ve çivi kullanmadan ahşabın nefes almasını sağlayan zıvanalı kündekâri zanaatı; parametrik robotik ahşap strüktürleri ve tolerans algoritmalarıyla canlanıyor.",
        "cases": "Konya Alâeddin ve Beyşehir Eşrefoğlu Camii minberleri, ETH Zürih Gramazio Kohler Research, EPFL IBOIS."
    },
    {
        "id": "dovme-bakir-ses",
        "slug": "dovme-bakir-ve-akustik-rezonans",
        "category": "Bakır Zanaatı & Ses Heykelleri",
        "craft_domain": "bakir maden dovme celik ses akustik rezonans",
        "title": "Çekicin Yankısı: Dövme Bakır Zanaatı ve Algoritmik Akustik Rezonans",
        "title_en": "Echoes of the Anvil: Coppersmithing and Algorithmic Acoustic Resonance",
        "thesis": "Bakır levhayı çekiç vuruşlarının ritmiyle sertleştirip form verme zanaatı; fiziksel modelleme sentezi ve mikrotonal rezonans frekanslarıyla çalışan ses heykelleriyle kesişiyor.",
        "cases": "Gaziantep ve Kahramanmaraş Kazancılar Çarşısı çekiç poliritimleri, Harry Bertoia Sonambient, IRCAM Modalys."
    }
]

TOPIC_ESSAYS = {
    "kundekari-robotik-ahsap": {
        "tags_tr": ["Ahşap Kündekâri", "Selçuklu", "Robotik Doğrama", "Parametrik Mimarlık", "Yeni Medya"],
        "tags_en": ["Kundekari", "Timber Joinery", "Robotic CNC", "Parametric Architecture", "New Media"],
        "subtitle_tr": "Konya Alâeddin ve Beyşehir Eşrefoğlu camilerindeki çivisiz, tutkalsız zıvana-lamba geçme sisteminden; higroskopik tolerans hesabına ve 7 eksenli robotik ahşap doğramacılığına.",
        "subtitle_en": "From nail-less, glue-free tongue-and-groove Anatolian Seljuk wood joinery in Konya and Beyşehir to hygroscopic tolerance algorithms and 7-axis robotic timber milling.",
        "cover_caption_tr": "Kavramsal Eser: Anadolu Selçuklu ceviz kündekâri yıldız geçmelerinin parametrik eklem vektörleri ve robotik ahşap frezeleme ile sentezi.",
        "cover_caption_en": "Conceptual Synthesis: Traditional Seljuk walnut kundekari star joinery integrated with parametric seam tolerances and robotic timber fabrication.",
        "body_tr": r'''Geleneksel ahşap işçiliğine uzaktan bakan modern bir göz, cami minberleri ve kapı kanatları üzerindeki sekizgen ve yıldızlı geometrileri çoğunlukla dekoratif bir kabartma olarak algılar. Oysa gerçek anlamıyla **hakikî kündekâri**, salt bir süsleme sanatı değil; **tutkal, demir çivi ve vida kullanmadan** yalnızca ahşabın fiziksel nem genleşmesini mühendislik hesaplarına katarak yüzyıllarca ayakta durabilen yüksek hassasiyetli bir **mekanik strüktür bilimi**dir.

Anadolu kışlarının kuru soğuğu ile yazlarının sıcak nemi arasında her ahşap lif grubu sürekli enine genleşip daralır. Büyük bir ahşap levhayı tek parça çivileyip tutkallarsanız, mevsim dönüşünde iç gerilim tahtayı boydan boya çatlatır. Selçuklu ve erken Osmanlı marangozları (*neccârân*) ise bu doğa yasasıyla savaşmak yerine onu tasarıma çevirdiler: küçük çokgen **dolgu** parçalarını oluklu **kayıt** çerçevelerinin içine serbestçe yüzer şekilde kilitleyerek, malzemenin nefes almasına izin veren algoritmik bir tolerans sistemi icat ettiler. Bugün Zürih ve Lozan'daki robotik mimarlık laboratuvarları aynı çivisiz tolerans kurallarını çok eksenli ahşap frezeleme kodlarına tercüme etmektedir.

## 1. Tarihsel Kökler: Malatya ve Konya Minberlerinden Osmanlı Edirnekârisine

Farsça "kalıpla biçimlendirmek" veya "ekleyip birleştirmek" anlamlarına gelen *kündekârî* kelimesinden doğan teknik, 12. yüzyılda Mısır (Tolunoğulları ve Fatımi ahşap oymacılığı), Suriye (Halep ve Şam) ve İran hatlarından Anadolu'ya taşınarak Selçuklu ustalığında doruğa ulaştı. 1155 tarihli **Konya Alâeddin Camii Minberi** (*Ahlatlı Mengü Berti* elinden çıkmıştır), İslam sanat tarihinde gerçek geçme tekniğinin bilinen en eski anıtsal örneklerinden biridir.

Anadolu'nun en saf **hakikî kündekâri** başyapıtları birbirini izleyen bir ustalık zinciri kurar: Malatya Ulu Camii, Siirt Ulu Camii, **Birgi Ulu Camii (1322)**, Ürgüp Damsa Köyü Taşkınpaşa Camii ve ahşap direkli yapısıyla benzersiz **Beyşehir Eşrefoğlu Camii (1299)**. 14. yüzyıl sonundan itibaren emek ve zaman maliyetini düşürmek için büyük tek parça ahşap üzerine oluk açılıp ince çıtalar çakılan *taklit (çakma-kabartma) kündekâri* yaygınlaştıysa da bu taklitler zamanla eğilip çatlamış; buna karşın çivisiz gerçek kündekâri minberler yedi yüz yıl sonra dahi eklem yerlerinden tek bir milimetre dağılmadan dimdik ayakta kalmıştır.

## 2. Zıvana, Lamba ve Higroskopik Tolerans Anatomisi

Bir kündekâri atölyesinde usta yalnızca marangoz değil, ağaç neminin yıllar içinde nasıl davranacağını hesaplayan bir botanik ve mekanik uzmanadır:

![Selçuklu kündekâri geçme kesiti: lamba oluklu kayıt çerçeveleri içinde mevsimsel genleşme boşluğu (delta-t) bırakılarak kilitlenen serbest yıldız dolgu paneli diyagramı](/images/kundekari-zivana-diagram.svg "Kündekâri Geçme & Tolerans Kesiti: Tutkalsız ve çivisiz yıldız dolgu geometrisi (sol) ile kayıt oluğundaki higroskopik genleşme boşluğu delta-t ve CNC takım yolu (sağ) | Görsel: Craft&Code Hesaplamalı Diyagram Arşivi")

- **Ağaç Seçimi ve Kurutma Süreci:** Büyük çekme-genleşme stresini dengelemek için kündekâri ustaları sert ve lif dokusu sık türler seçer: **ceviz**, **sedir**, **abanoz**, **armut** ve **şimşir**. Kesilen keresteler doğrudan tezgâha konmaz; açık havada ve gölge sundurmalarda en az **beş ila on yıl** boyunca mevsim nemine alıştırılır.
- **İki Ana Parça Sınıfı (*Dolgu* ve *Kayıt*):**
  - **Dolgu (Künde / Geometrik Parçalar):** Sekiz, on veya on iki köşeli yıldızlar, bademler ve beşgenlerden oluşan küçük bloklardır. Kenarları oluklu çerçevelerin içine girebilecek şekilde iki yandan **üçgen ya da kama profiliyle inceltilir (*zıvana dili / pah*)**. Ayrıca her dolgunun lif yönü geometrik simetriye göre merkeze hizalanır.
  - **Kayıt (İskelet Çerçeve Çubukları):** Yıldızları dışarıdan saran düz ahşap çıtalardır. Kayıtların iç kenarlarına ince **ıskarpela** (*chisel*) ve oluk rendesiyle V ya da U kesitli kanallar (**lamba / kiniş**) açılır; uçları ise birbirine **zıvana geçme** (*mortise-and-tenon*) ya da *kırlangıç kuyruğu* ile tutturulur.
- **Sırrın Kalbi — *Mevsimsel Nefes Payı* ($\Delta t$):** Hakikî kündekâri ustası hiçbir dolgu parçasını kayıt oluğunun dibine sıfıra sıfır dayamaz ve tutkalla sabitlemez. Oluğu dolgunun dilinden yaklaşık **1,5–2,5 mm daha derin** açar. Kışın kuruyan parça birkaç mikron daralsa da oluğun dışına düşmez; yazın nem çeken parça genleşse de bu güvenlik boşluğu ($\Delta t$) içinde rahatça hareket eder ve yan kayıtları asla dışa itip patlatmaz.

> "Tutkal ahşabın hapsidir, zıvana ise onun hürriyeti; hakikî kündekâri çiviyi reddettiği için değil, mevsimin ahşaba kattığı hareketi geometriye dahil ettiği için ölmez." -- Anadolu Ahşap Ustalığı Üzerine

## 3. Gelenekselden Koda: Yapısal Karşılıklar ve Algoritmik Çeviri

Selçuklu marangozunun *zıvana* derinliğini ağacın mevsimsel genleşme yüzdesine ($\Delta t$) göre hesaplayıp geometrik birleştirme kurması; bugün hesaplamalı mimarlıkta **parametrik eklem sentezi** (*Parametric Timber Joinery*) ve **çarpışmasız takım yolu planlaması** (*Toolpath Planning*) ile tamamen aynı veri yapılarını kullanır.

| Geleneksel Kündekâri Unsuru | Atölyedeki Fiziksel ve Mekanik İşlevi | Koddaki / Robotik Doğramadaki Karşılığı |
| :--- | :--- | :--- |
| *Hakikî Geçme* (Tutkalsız Birleştirme) | Parçaların sökülebilir, tek tek değiştirilebilir modüler bütünlük kurması. | Topolojik kenetlenme kısıtı (`interlocking_constraint`) ve sökülebilir ağaç grafiği |
| *Kayıt* İskelet Ağı (*Çerçeve*) | Desenin ana çizgilerini taşır ve tüm dolgu bloklarını kafes gibi birbirine kilitler. | Kenar çerçeve grafı (`dual_frame_edges`) ve açısal düğüm bağlantıları |
| Yıldız / Badem *Dolgu* Elemanları | Kayıt oluklarının içinde yüzen, lif yönü hizalanmış geometrik paneller. | Parametrik çokgen hücreleri ve lokal lif yönelimi vektörü (`grain_vector`) |
| *Lamba* (Kiniş) Oluk Derinliği | Dolgunun kenar dilini sararak düzlem dışına fırlamasını engeller. | Boolean çıkarma geometrisi (`channel_cut = panel_offset - depth`) |
| *Mevsimsel Genleşme Payı* ($\Delta t$) | Nem artışında şişen ceviz veya sedirin komşu kayıtları çatlatmasını önler. | Higroskopik tolerans katsayısı (`tolerance_mm = width * moisture_coeff`) |
| Pahlı Kenar Açısı (*Zıvana Dili*) | İki komşu kaydın 22,5° veya 36° açıyla birbirine tam öpüşmesini sağlar. | Çok eksenli CNC freze eğim açısı (**5/7-eksen tool normal vector**) |
| Kereste Lif Yönü (*Su Yönü*) | Keski ve frezenin lifi yarmadan temiz yüzey bırakması için kesim yönü tercihi. | Takım yolu yönü ile lif vektörü hizalaması (`climb vs. conventional milling`) |

:::bridge Zanaattan Koda Köprü
Geleneksel marangoz elindeki kumpasla ceviz bloğun enini ölçüp rutubet oranına göre oluğa `1.8 mm` boşluk bıraktığında, **anizotropik higroskopik deformasyon denklemini** çözer: Ahşap boyuna (lif yönünde) neredeyse hiç uzamazken, teğetsel yönde bağıl nemdeki her %1 değişimde eninin belirli bir katsayısı kadar şişer. Parametrik yazılımlar her bir yıldız paneli için bu formülü otomatik hesaplayıp **6 veya 7 eksenli robotik freze uçlarının** açacağı oluk derinliklerini dinamik olarak ayarladığında, 13. yüzyıl Konya minber ustalığı çağdaş robotik ahşap mimarisine dönüşür.
:::

Aşağıdaki Python kodu, belirli bir ağaç türü (ceviz, sedir, meşe) ve mevsimsel nem farkı için gereken **lamba oluk boşluğu (`compute_hygroscopic_clearance`)** toleransını hesaplar ve robotik CNC freze kolu için çokgen eklem pah açılarını üretir.

```python title="Kündekâri Higroskopik Tolerans ve Robotik Zıvana Geometri Üreticisi"
# Craft&Code — Selçuklu Kündekâri Tolerans Hesabı & 7-Eksen Eklem Üretimi
import math

WOOD_TANGENTIAL_SHRINKAGE = {
    "Ceviz (Walnut)": 0.0026,   # Her %1 bagil nem degisiminde boyutsal genlesme katsayisi
    "Sedir (Cedar)":  0.0018,
    "Mese (Oak)":     0.0034,
}

def compute_hygroscopic_clearance(panel_span_mm, wood_species, delta_humidity_pct=18.0):
    """Mevsimsel nem farkina gore kayıt lamba olugundaki guvenlik boslugunu (delta-t) hesaplar."""
    coeff = WOOD_TANGENTIAL_SHRINKAGE[wood_species]
    max_expansion = panel_span_mm * coeff * (delta_humidity_pct / 5.0)
    safety_margin = 0.65  # Ahşap tozu ve yuzey puruzu icin minimum hareket payi
    return round(max_expansion + safety_margin, 2)

def generate_kundekari_joint_spec(arms=8, outer_radius_mm=140.0, wood_species="Ceviz (Walnut)"):
    """8 veya 10 koseli yildiz dolgular icin zivana acisini ve oluk derinligini cikarir."""
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

Görüldüğü üzere `groove_depth_mm = tongue_depth_mm + clearance` ilişkisi; eski ustaların hiçbir zaman yazılı formüle dökmediği ancak yüzlerce cami kapısını çatlamaktan kurtaran sözlü kuralın doğrudan geometrik tanımıdır.

## 4. Çağdaş Sanat, Laboratuvar ve Vaka İncelemeleri

Tutkalsız ve çivisiz ahşap birleştirme teknolojisi, bugün dünyanın önde gelen mimarlık araştırma merkezlerinde düşük karbonlu dev strüktürlerin inşasında anahtar rol oynamaktadır.

### Vaka 1: Konya Alâeddin & Beyşehir Eşrefoğlu Camii Minberleri (12.–13. Yüzyıl)
Anadolu'nun en yüksek rakımlı sert kara iklimine sahip Konya ve Beyşehir havzasında kışın dondurucu kuruluğu ile göl kaynaklı nem arasındaki dev salınıma rağmen 1155 tarihli **Alâeddin Camii Minberi** ve 1299 tarihli **Eşrefoğlu Camii** doğrama unsurları, tam 700–850 yıldır yapısal bütünlüğünü korumaktadır. Yakın dönem konservasyon taramaları, bu dayanıklılığın arkasında her bir minber kanadında üç yüzü aşkın ayrı ayrı kesilmiş ahşap modülün birbirine tutkal sürmeden zıvana ve lamba kanallarıyla serbestçe kilitlenmiş olmasının yattığını belgelemektedir.

### Vaka 2: Gramazio Kohler Research (ETH Zürih) — *Robotik Ahşap Eklemleri* (2012–2023)
Zürih Federal Teknoloji Enstitüsü (**ETH Zürih**) bünyesindeki *Gramazio Kohler Research* grubu, robotik kollar kullanarak karmaşık ahşap kafes strüktürleri otomatikleştiren çığır açıcı projelere imza attı. 6 ve 7 eksenli CNC kesici uçlarla donatılmış robotlar, insan elinin keskiyle açtığı karmaşık açılı *zıvana* ve *kırlangıç kuyruğu* geçmelerini doğrudan parametrik CAD dosyasından okuyarak keresteye milimetrik hassasiyetle işler; böylece metal bağlantı cıvatasına hiç ihtiyaç duymayan hafif ahşap kubbeler ve pavyonlar ortaya çıkar.

### Vaka 3: IBOIS (EPFL Lozan, Yves Weinand) — *Wood-to-Wood Integral Timber Joints* (2014–Günümüz)
Lozan Federal Teknoloji Enstitüsü (**EPFL**) Ahşap Yapılar Laboratuvarı *IBOIS*, Prof. Yves Weinand liderliğinde geliştirdiği **tutkalsız katlı plak ahşap eklemler** (*Integral Mechanical Attachment*) ile geleneksel Japon ve Selçuklu geçme zanaatlarını modern yapı mühendisliğiyle birleştirdi. Araştırmacılar, geleneksel geçme açılarını sonlu elemanlar (FEA) yük simülasyonlarıyla optimize ederek vidaya ya da epoksi tutkala ihtiyaç duymadan tonlarca çatı yükü taşıyabilen dev ahşap kemerler inşa etti — ki çalışma mantığı doğrudan Anadolu'nun *kündekâri* zıvana felsefesinin mühendislik uzantısıdır.

## 5. Eleştirel Sentez: Zanaatın Direnci ve Kodun Sınırı

7 eksenli bir CNC freze robotu saniyeler içinde on altı açılı kusursuz bir kündekâri yıldız eklemi oyabilir. Ancak robotik bıçak tek başına kerestenin içinde gizlenen bir budak düğümünü, bir yıl önce ağacın kuzey yüzünde büyümüş sık halkaların sertliğini veya keskinin ahşap lifini ayırırken çıkardığı o tok tıkırtıyı sezgisel olarak duyamaz.

Kündekâri bize modern yazılım ve mimarlık kültürü için son derece hayati bir ders verir: **Mükemmel tasarım malzemeyi donduran ve hapseden değil; onun zamanla değişen hareketine güvenli bir alan açan esnek bir geometridir.** Kod ile zanaat omuz omuza verdiğinde ortaya ne tekdüze fabrikasyon ürünler ne de sadece müzelere hapsolmuş geçmiş objeleri çıkar; nefes alan, yaşayan bir strüktür kültürü doğar.

:::curatorial Küratöryel Not
On üçüncü yüzyılda Beyşehir'de ceviz bloğu oluğa tutkal sürmeden kilitleyen neccâr ustası ile bugün Zürih laboratuvarında `hygroscopic_gap_mm` payını hesaplayarak robotik uç açısını programlayan araştırmacı aynı hakikati savunur: **Gerçek kalıcılık maddenin hareketini yasaklamakla değil, o harekete akıllı bir yuva tasarlamakla mümkündür.**
:::

---

### Kaynakça ve İleri Okumalar
1. **Öney, Gönül.** *Anadolu Selçuklu Mimari Süslemesi ve El Sanatları*. Türkiye İş Bankası Kültür Yayınları, Ankara, 1978.
2. **Sönmez, Zeki.** *Başlangıcından 16. Yüzyıla Kadar Anadolu Türk-İslam Mimarisinde Sanatçılar*. Türk Tarih Kurumu Yayınları, Ankara, 1995.
3. **Bozer, Rüstem.** *Ahşap İşçiliği: Anadolu Selçuklu ve Beylikler Dönemi Minberleri*. Kültür Bakanlığı Yayınları, Ankara.
4. **Weinand, Yves (Ed.).** *Advanced Timber Structures: Architectural Designs and Digital Dimensioning*. Birkhäuser, Basel, 2016.
5. **Willmann, Jan, Knauss, Michael, Bonwetsch, Tobias, Apolinarska, Aleksandra Anna, Gramazio, Fabio, & Kohler, Matthias.** "Robotic Timber Construction — Expanding Additive Fabrication to New Dimensions." *Automation in Construction*, Vol. 61, 2016, ss. 16–23.
''',
        "body_en": r'''To a hurried contemporary eye, geometric star octagons and hexagons across historic Anatolian mosque pulpits (*minbers*) and sanctuary doors appear merely ornamental carving. In authentic **hakikî kündekâri**, however, geometry is never superficial decoration; it represents high-precision **structural wood engineering engineered completely without nails, screws, or structural glue**—designed specifically to endure centuries by embedding wood moisture dynamics inside interlocking topology.

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
'''
    },
    "dovme-bakir-ses": {
        "tags_tr": ["Bakır Zanaatı", "Kazancılar", "Akustik Rezonans", "Chladni", "Fiziksel Modelleme"],
        "tags_en": ["Coppersmithing", "Acoustics", "Chladni Figures", "Modal Synthesis", "New Media"],
        "subtitle_tr": "Gaziantep ve Kahramanmaraş Kazancılar Çarşısı'ndaki tavlama, soğuk dövme ve çekiç poliritimlerinden; Chladni akustik düğüm haritalarına ve IRCAM modal ses sentezine.",
        "subtitle_en": "From annealing, work-hardening, and rhythmic hammer polyrhythms in Anatolian coppersmith bazaars to Chladni nodal acoustics and physical-modeling sound synthesis.",
        "cover_caption_tr": "Kavramsal Eser: El dövmesi bakır çanak üzerindeki konsantrik çekiç izlerinin Chladni akustik düğüm dalgaları ve armonik spektrumla sentezi.",
        "cover_caption_en": "Conceptual Synthesis: Concentric hand-hammered copper texture translated into glowing Chladni standing-wave acoustics and harmonic frequency bars.",
        "body_tr": r'''Anadolu'nun tarihî bedestenlerine ya da **Kazancılar Çarşısı**'na adım attığınızda sizi ilk karşılayan şey görsel bir vitrin değil, taş duvarlarda yankılanan çok katmanlı bir **metalik perküsyon senfonisidir**. Farklı ağırlıktaki çekiçlerin dövme çelik örs (*örs*) üzerindeki bakır sac levhaya vuruşları yalnızca bir kap biçimlendirmez; aynı zamanda metalin atomik kristal kafesini yeniden düzenler ve levhanın **doğal rezonans frekanslarını (tınısını)** akort eder.

Dışarıdan bakıldığında mutfak tenceresi veya ibrik üretimi sanılan bakırcılık (*kazancılık*), metalurji tarihinde **termal tavlama (annealing)** ve **soğuk dövme sertleştirme (work-hardening)** prensiplerini sesle okuyabilen en hassas zanaatlardan biridir. Bakırcı ustası levhayı döverken gözü kadar kulağını kullanır: Çekicin çıkardığı ses tizleşip metal direnci arttığında mikroskobik dislokasyonlar sıkışmış demektir; çatlamadan önce ateşe girmesi gerekir. Bugün bilgisayar müziğindeki **fiziksel modelleme sentezi (Modal Synthesis / IRCAM Modalys)** ve ses heykelleri, doğrudan örs üstündeki bakır plakanın diferansiyel titreşim fiziğini koda dökmektedir.

## 1. Tarihsel Kökler: Anadolu Bakır Ocaklarından Lonca Ritimlerine

Külçe bakırın ısıtılmadan dahi çekiçle şekillendirilebildiği Anadolu toprakları —Ergani Maden yataklarından Çayönü neolitik buluntularına, Urartu bronz kazanlarından Selçuklu ve Osmanlı bakırcılığına— insanlık tarihinin en eski metalürji beşiğidir. Orta Çağ ve Osmanlı şehir ekonomisinde bakır zanaatı *kazancılar*, *bakırcılar*, *kalaycılar* ve *savatsız kalemkârlar* olarak son derece disiplinli esnaf loncalarına ayrılmıştı.

**Gaziantep, Kahramanmaraş, Tokat, Trabzon, Siirt ve Diyarbakır** bakırcılar çarşılarında yüzyıllar boyu sürdürülen gelenek iki temel estetiği bir arada taşır: Biri ateş ve büyük ahşap tokmaklarla dev kazanları yekpare levhadan yükselten strüktürel **dövme** (*çökertme*), diğeri ise yüzeyde hem estetik hem dayanım sağlayan mikroskobik çekiç vurma izleri (**perdahlama**). Anadolu bakırcılığında usta çekiç darbelerini birbirine teğet düzenli halkalar halinde öyle sık vurur ki, yumuşak bakır plaka hem zırh gibi sertleşir hem de içinden geçen her ses darbesini berrak bir armonik çan gibi yankılar.

## 2. Tavlama, Soğuk Dövme ve Örsün Akustik Anatomisi

Bakırcının tezgâhında her vuruş, metalin kristal tane sınırlarını fiziksel olarak yeniden örgütleyen üç fazlı bir döngüdür:

![Üç dairesel bakır diskin matematiksel Chladni düğüm çizgileri ve tavlanmış vs soğuk dövülmüş bakırın harmonik frekans spektrum grafiği](/images/dovme-bakir-chladni-diagram.svg "Bakır Akustik Rezonans & Chladni Haritaları: Dövme bakır disklerdeki mod (1,2), (2,3), (3,5) durağan dalga düğümleri (sol) ve soğuk dövmenin harmonik sıklığa etkisi (sağ) | Görsel: Craft&Code Hesaplamalı Diyagram Arşivi")

- **Tavlama (*Annealing — Ateşle Sıfırlama*):** Bakır soğuk halde çekiçlendikçe kristal yapısı sıkışıp gerilir; ses donuklaşıp tizleşir ve biraz daha zorlanırsa kenarlardan yırtılır. Bu noktada usta bakırı kömür ocağına sokup **~500–650°C** dolayında kiraz kırmızısı köz rengine gelene kadar ısıtır, ardından suya daldırır (*su verme / tavlama*). Çeliğin aksine bakır suya batırıldığında sertleşmez; tersine, sıkışmış atomik kafesler yeniden kristalleşerek (**recrystallization**) lokum gibi yumuşar ve yeni dövme döngüsüne hazır hale gelir.
- **Soğuk Dövme (*Work-Hardening*) ve *Perdah* Çekiçleri:** Şekli *çökertme* ve *yanlama* çekiçleriyle kabaca çıkarılan kase, artık **örs** (*boynuzlu örs / ayak örsü*) üzerine geçirilir. Usta yuvarlak başlıklı parlak **perdah çekiciyle** dairesel sarmallar çizerek binlerce ölçülü darbe indirir. Bu soğuk dövme işlemi bakırın elastisite modülünü ve yüzey sertliğini artırır; her çekiç çukuru plakayı mikroskobik düzeyde gerginleştirip akustik rezonans kalitesini ($Q$-faktörünü) yükseltir.
- **Kalaylama (*Nişadır* Simyası):** Bakır gıda ile temas ettiğinde zehirli yeşil bakır karbonat (*jengar*) oksidi oluşturduğundan, geleneksel kaplar mutlaka saf **kalay** ile kaplanır. Usta kabı ateşte ısıtır, yüzey oksitlerini temizlemek için beyaz toz halinde amonyum klorür (**nişadır**) serper ve erimiş gümüş kalayı temiz pamuk üstüpüyle saniyeler içinde metal gözeneklerine yedirir.
- **Çekiç Poliritimleri:** Kazancılar Çarşısı'nda iki veya üç kalfanın aynı bakır kazanı tek örsün üstünde sırayla dövmesi (**3/4'lük veya aksak vuruş düzenleri**), hem darbe yorgunluğunu eşit dağıtır hem de metalin aynı saniyede farklı noktalarının soğuyup gerilmesini önleyen canlı bir müzikal zamanlama (*clock signal*) üretir.

> "Bakırcının kulağı çekicinin gözüdür; metal 'ben yoruldum' diye çığlık atmaya başladığı an ocak ateşine dönmezsen, emeğin bir darbede ikiye yarılır." -- Gaziantep Kazancılar Çarşısı Sözlü Ustalık Kuralı

## 3. Gelenekselden Koda: Yapısal Karşılıklar ve Algoritmik Çeviri

Bakır diski çekiçle şekillendirip sesinden kristal sertliğini okuyan usta ile modern bilgisayar müziğinde **Fiziksel Modelleme (Modal Synthesis)** ve **Chladni Durağan Dalga Denklemleri** yazan ses programcısı aynı akustik yasaları işler.

| Geleneksel Bakırcılık Unsuru | Örs ve Ocaktaki Fiziksel / Akustik İşlevi | Koddaki / Fiziksel Ses Sentezindeki Karşılığı |
| :--- | :--- | :--- |
| Bakır Levha Kalınlığı ve Çapı | Temel rezonans frekansını ($f_0$) ve armonik modların basamaklarını belirler. | Kirchoff-Love ince plaka özdeğer çözücüsü (`plate_eigenvalues(n, m)`) |
| *Soğuk Dövme / Perdah* Sertleştirme | Kristal dislokasyonları artırarak ses sönümünü azaltır ve tiz armonikleri parlatır. | Gençlik modülü ve rezonans kalite çarpanı (`stiffness_k`, `q_factor`) |
| *Tavlama* (Ateşte Yeniden Kristalleşme) | İç gerilimleri sıfırlar; sesi koyu, boğuk ve yüksek sönümlü hale getirir. | Yüksek frekans sönümleme katsayısı (`damping_alpha` artışı) |
| Konsantrik Çekiç Darbe İzleri (*Perdah*) | Yüzey sertliğini merkezcil gradyanlarla değiştirerek mod ayrışması yaratır. | Düğüm çizgisi pertürbasyonu (**Chladni** mod kaydırma katsayısı) |
| Çekiç Başının Malzemesi (Çelik vs. Şimşir) | Darbe temas süresini kısaltarak parlak (çelik) veya sıcak (ahşap) saldırı zarfı üretir. | Eksitasyon darbe spektrumu (*Impulse Response* / Alçak geçiren vuruş filtresi) |
| Örs Üstündeki Çok Kalfalı *Poliritim* | Vuruşlar arası zamanlamayı kilitler ve ısıl gerilimi simetrik dağıtır. | Algoritmik saatleyici / *MaxMSP-SuperCollider* poliritmik tetikleyici |
| Kazan Gövdesinin İç Hacmi (*Hava Rezonansı*) | Çukur bakır kavitenin Helmholtz benzeri alt bas rezonans desteği sağlaması. | Geri beslemeli gecikme ağı (**FDN Reverb / Cavity Filter**) |

:::bridge Zanaattan Koda Köprü
Bir bakır levhanın merkezinden veya kenarından çekilen bir vuruşla uyanan titreşimler, yüzlerce ayrı frekansın toplamından değil; levhanın geometrisine özgü ayrık **armonik modların (eigenmodes)** süperpozisyonundan oluşur. İki boyutlu daire ya da kare metal plaka üzerinde kum tanelerinin çizdiği klasik **Chladni düğüm çizgileri**, tam olarak $Z(r,\theta) = \sin(n\pi r) \cdot \cos(m\theta) = 0$ özdeğerlerinin sıfır noktalarıdır. Bilgisayar ortamında **Modal Ses Sentezi** yazarken bakırın her bir $(n,m)$ modunu sönümlenen birer sinüs osilatörüne dönüştürürüz; bakırı *tavlama*dan *soğuk dövmeye* geçirmek kodda yalnızca sertlik ($K$) ve sönüm ($\gamma$) parametrelerini değiştirmektir!
:::

Aşağıdaki Python kodu, dövme bakır bir diskin tavlama ve soğuk dövme aşamalarına göre nasıl farklı **armonik frekans spektrumu (modal bank)** ve **sönümleme eğrileri** ürettiğini ve **Chladni durağan dalga düğümlerini** nasıl hesapladığını gösterir.

```python title="Dövme Bakır Chladni Özdeğerleri ve Modal Ses Sentezi Modeli"
# Craft&Code — Bakır Plaka Chladni Modları ve Soğuk Dövme Akustik Sentezi
import math

def copper_modal_bank(radius_cm=18.0, work_hardening=0.85, annealed=False):
    """Tavlama veya soğuk dövme durumuna göre bakır kabın rezonans modlarını hesaplar."""
    # Soğuk dövme bakır sertliğini (Young modülü etkisi) ve yüksek armonikleri güçlendirir
    stiffness = 0.55 if annealed else (0.95 + 0.45 * work_hardening)
    base_freq_hz = (420.0 / (radius_cm / 15.0) ** 1.4) * stiffness
    decay_rate = 3.8 if annealed else (1.15 - 0.35 * work_hardening)

    # Disk mod çiftleri (radial n, angular m) ve Chladni frekans oranları
    mode_ratios = [
        ((1, 2), 1.00, 1.00),
        ((2, 3), 2.38, 0.72),
        ((3, 5), 4.42, 0.46),
        ((4, 6), 7.15, 0.29),
    ]
    modes = []
    for (n, m), ratio, base_amp in mode_ratios:
        freq = round(base_freq_hz * ratio, 1)
        amp = round(base_amp * (0.65 if annealed else 1.0), 3)
        t60_sec = round(6.91 / (decay_rate * (1.0 + 0.15 * n)), 2)
        modes.append({"mode": (n, m), "freq_hz": freq, "amp": amp, "decay_t60_s": t60_sec})
    return modes

def synthesize_hammer_strike(modes, time_sec, strike_r=0.45, strike_theta=0.3):
    """Örs üzerinde belirli noktaya vurulan çekiç darbesinin t=time anındaki ses genliği."""
    sample = 0.0
    for md in modes:
        n, m = md["mode"]
        # Chladni düğüm koşulu: Düğüm çizgisine vurulan çekiç o modu uyarmaz!
        spatial_coupling = abs(math.sin(n * math.pi * strike_r) * math.cos(m * strike_theta))
        envelope = math.exp(-3.5 * time_sec / max(md["decay_t60_s"], 0.1))
        sample += md["amp"] * spatial_coupling * envelope * math.sin(2.0 * math.pi * md["freq_hz"] * time_sec)
    return round(sample, 5)
```

Kodda yer alan `spatial_coupling = abs(math.sin(n * math.pi * strike_r) * math.cos(m * strike_theta))` satırı, akustik zanaatın temel gerçeğini özetler: Bir bakır tepsiye ya da gonga neresinden vurduğunuz, o plakanın hangi doğal armonik modlarını susturup hangilerini çınlatacağınızı doğrudan belirler.

## 4. Çağdaş Sanat, Laboratuvar ve Vaka İncelemeleri

Çekiç iziyle şekillenen metal yüzeylerin akustik hafızası, çağdaş heykeltraşlıkta ve bilimsel ses sentezinde üç büyük referans üzerinden yaşamaktadır.

### Vaka 1: Gaziantep & Kahramanmaraş Kazancılar Çarşısı Poliritimleri
Anadolu'nun tarihî bakırcı çarşılarında yüzlerce yıl boyunca geliştirilen ortak çekiç dövme geleneği, işçiliği doğrudan **kolektif bir poliritim orkestrasına** dönüştürmüştür. Aynı büyük bakır hamam kazanının çevresinde oturan üç ustanın farklı ağırlıktaki tahta ve demir tokmakları 3'lü ve 5'li döngüsel zamanlama (*devir*) içinde indirmesi, mekanik iş yükünü paylaşmanın ötesinde kazan cidarının akustik gerilimini anlık olarak dengeleyen işitsel bir geri besleme ağı oluşturur.

### Vaka 2: Harry Bertoia — *Sonambient* Ses Heykelleri (Pennsylvania, 1960–1978)
İtalyan-Amerikalı heykeltıraş **Harry Bertoia**, klasik mobilya ve metal tasarımının ardından bütün enerjisini bakır, pirinç ve berilyum-bakır çubuk ve gonglardan inşa ettiği **Sonambient** adlı ses heykellerine adadı. Bertoia metal alaşımları yüksek ısıda tavlayıp uçlarını döverek gerginleştirdi; rüzgârla veya insan dokunuşuyla çarpışan bu metal sütunlar hiçbir elektronik hoparlör olmadan doğanın kendi mikrotonal armonik modlarını ve derin çan rezonanslarını üreten yaşayan akustik enstrümanlara dönüştü.

### Vaka 3: IRCAM *Modalys* ve Zimoun'un Akustik Kinetik Sistemleri
Paris'teki **IRCAM** enstitüsü tarafından geliştirilen **Modalys** fiziksel modelleme motoru, ses dalgalarını önceden kaydedilmiş ses dosyalarından değil; sanal bir metal plakanın veya bakır telin matematiksel kütle, sertlik ve şekil özdeğerlerini çözerek gerçek zamanlı üretir. Paralel olarak İsviçreli ses sanatçısı **Zimoun**, yüzlerce basit DC motoru pamuk toplara, karton kutulara ve dövülmüş metal plaklara bağlayarak doğanın termodinamik sürtünme ritimlerini mekânsal perküsyon heykellerine çevirir — tıpkı küçük bakır çekiçlerin görünmez ellerle sonsuz ritim tutması gibi.

## 5. Eleştirel Sentez: Zanaatın Direnci ve Kodun Sınırı

Gelişmiş DSP sentezleyiciler tek bir tıklamayla mükemmel bir bakır gong rezonansı simüle edebilir; fakat hoparlör konisinin ürettiği hava dalgası, örs üstünde ellerin nasırıyla dövülmüş hakiki bir bakır çanağın tüm odaya yaydığı üç boyutlu **küresel ses basıncını** ve metalin dokundukça ısınıp soğuyan tenini tam olarak ikame edemez.

Öte yandan fiziksel modelleme kodu da bakırcılığa muazzam bir analiz gözlüğü sunar: Yüzyıllardır kulaktan kulağa aktarılan *"tavlama kıvamı"* ve *"perdah sıkılığı"* bilgilerinin aslında derin bir özdeğerler ve Chladni modları bilimi olduğunu ortaya çıkarır. Gerçek ses, örsün demir soğukluğu ile dijital osilatörün matematik berraklığı el ele verdiğinde en derin yankısını bulur.

:::curatorial Küratöryel Not
Gaziantep çarşısında çekiç vuruşunun incelen sesinden bakırın yorulduğunu anlayıp ocağa döndüren bakırcı ustası ile bugün ekranda `work_hardening` katsayısıyla harmonik modal banka kuran ses mühendisi aynı görünmez orkestrayı yönetir: **Kristalin ve sayının titreştiği ortak akustik rezonans.**
:::

---

### Kaynakça ve İleri Okumalar
1. **Belli, Oktay & Kayaoğlu, İ. Gündağ.** *Anadolu'da Türk Bakırcılık Sanatının Gelişimi*. Sandoz Kültür Yayınları, İstanbul, 1993.
2. **Chladni, Ernst Florens Friedrich.** *Entdeckungen über die Theorie des Klanges* (*Ses Kuramı Üzerine Keşifler*). Weidmanns Erben und Reich, Leipzig, 1787.
3. **Bilbao, Stefan.** *Numerical Sound Synthesis: Finite Difference Schemes and Simulation in Musical Acoustics*. Wiley, Chichester, 2009.
4. **Karpuz, Haşim.** *Trabzon ve Anadolu El Sanatları: Bakırcılık Geleneği*. Kültür Bakanlığı Yayınları.
5. **Bertoia, Val & Bertoia, Celia.** *The Life and Work of Harry Bertoia: The Man, the Artist, the Visionary*. Schiffer Publishing, 2015.
6. **Adrien, Jean-Marie.** "The Missing Link: Modal Synthesis." *Representations of Musical Signals*, MIT Press, 1991, ss. 269–298.
''',
        "body_en": r'''Stepping inside Anatolia's historic **Kazancılar Çarşısı** (Coppersmiths' Bazaar), what strikes your senses before gleaming crimson storefronts is a soaring, polyrhythmic **metallic percussion symphony** echoing cleanly off stone vaults. Weighted hammers striking sheet copper across horned steel anvils (*örs*) never merely bend vessels into form; each rhythmic blow dynamically restructures metallic crystal lattices while literally tuning the plate's acoustic resonances.

Far from simple kitchen pot shaping, traditional coppersmithing ranks among historical metallurgy's sharpest sensory engineering crafts—navigating **thermal annealing** and **cold work-hardening** directly by acoustic pitch. Masters listen continuously as they hammer: once high metallic ring tightens sharply, microscopic grain boundaries have jammed brittle, signaling immediate return to forge fire before tearing erupts. Today, contemporary computer music's **Modal Synthesis (IRCAM Modalys)** and kinetic sound sculptures formulate the exact vibrational physics of hammered bronze and copper plates directly inside code.

## 1. Historical Roots: From Anatolian Ore Cradles to Guild Orchestras

Home to Chalcolithic hammered native copper from Ergani mines—spanning Neolithic Çayönü blades, Urartian ceremonial cauldrons, and monumental Seljuk lamps—Anatolia stands among world metallurgy's deepest taproots. Across Ottoman urban guild frameworks, coppersmithing branched strictly across specialized professions: **kazancılar** raising thick-walled cauldrons from flat sheet ingots (*çökertme*), **bakırcılar** refining household pitchers, **kalaycılar** executing tin-plating chemistry, and *kalemkâr* engravers chiseling calligraphy cleanly into finished skins.

Historic bazaars across **Gaziantep, Kahramanmaraş, Tokat, Trabzon, Siirt, and Diyarbakır** preserve two tightly wedded material methods: structural raising over scorching hearth fire, followed by dense concentric planishing touches (**perdah**) laying dimpled facets completely side-by-side. Every uniform hammer facet tightens pure red copper progressively from malleable dead clay into bright acoustic bell armor ringing clearly with sustained harmonic overtones.

## 2. Annealing, Work-Hardening, and the Acoustic Anvil

Every session bridging red hearth fire and forged steel horn anvil follows a strict physical rhythm reorganizing atomic crystal geometry cycle by cycle:

![Three mathematically plotted circular hammered-copper Chladni plate nodal maps paired with harmonic spectrum bar chart comparing annealed vs cold-hardened modes](/images/dovme-bakir-chladni-diagram.svg "Copper Acoustic Resonance & Chladni Patterns: Standing-wave nodal contours for circular plate modes (1,2), (2,3), and (3,5) (left) alongside spectral mode hardening shifts (right) | Visual: Craft&Code Computational Diagram Archive")

- **Annealing (*Tavlama — Crystal Reset by Fire*):** Cold hammering tangles metallic crystalline dislocations tightly together; copper stiffens abruptly, acoustic strike tones pitch steeply sharp, and edges threaten radial cracking. Before fracture strikes, the coppersmith shoves blackened sheets deep inside coal embers reaching dull cherry red (~500–650°C), quenching swiftly inside cold water tanks. Unlike iron alloys that harden explosively during quenching, pure copper behaves reversely: sudden thermal drop locks freshly recrystallized loose grains (**recrystallization**), leaving the metal dead-soft and dull-toned again—ready cleanly for deeper raising passes.
- **Cold Planishing (*Soğuk Dövme / Perdah*):** Once rough curvature settles through heavier shaping hammers, vessels slip over horned iron stakes (**boynuzlu örs**) where mirror-polished **planishing hammers** tap thousands of crisp tight spiral dimples directly into chilled skin. Cold work-hardening boosts Young's modulus stiffness and boosts resonant quality factors ($Q$-factor), transforming damp copper back into crisp acoustic bell crystal.
- **Tinning Alchemy (*Kalaylama & Nişadır*):** Bare copper rapidly oxidizes against acidic meals into toxic green verdigris salts. Craftsmen heat copper gently while sprinkling snowy powdered ammonium chloride flux (**nişadır**) to strip dull surface oxides, wiping pure molten silver-tin cleanly with cotton wisps across reactive metallic pores.
- **Workshop Hammer Polyrhythms:** Watching three apprentices hammer alternating strokes around one massive kettle over twin iron stakes—often falling organically into crisp **3/4 or asymmetrical aksak meters**—reveals profound acoustic logic: staggered alternating blows prevent asymmetric heat buildup while delivering live tempo clock discipline across scorching shop floors.

> "The coppersmith's ear guides the hammer's eye; if you fail to heed rising pitch crying that copper is exhausted, one stray blow shears days of work in half." -- Gaziantep Coppersmith Bazaar Maxim

## 3. Craft to Code: Structural Correspondences & Algorithmic Translation

Judging copper hardness by acoustic overtones along horned stakes maps transparently onto **Kirchoff-Love thin plate eigenvalues**, **Chladni nodal patterns**, and real-time **Modal Audio Synthesis**.

| Traditional Coppersmith Element | Physical & Acoustic Role at Forge and Anvil | Equivalent Construct in Physics & Modal Audio Code |
| :--- | :--- | :--- |
| Copper Sheet Radius & Wall Thickness | Establishes base fundamental pitch ($f_0$) and modal ratio staircase. | Thin-plate differential eigenvalue solver (`plate_eigenvalues(n, m)`) |
| Cold Planishing (*Soğuk Dövme / Perdah*) | Compacts dislocations increasing structural rigidity and ringing overtone duration. | Stiffness coefficient & resonant quality factor (`stiffness_k`, `q_factor`) |
| Thermal Hearth Annealing (*Tavlama*) | Relaxes crystalline shear yielding dull low-pitched damped impact thuds. | High-frequency energy decay damping scalar (`damping_alpha`) |
| Concentric Spiraled Hammer Facets | Perturbs local boundary stiffness breaking degenerate symmetry smoothly. | Nodal frequency perturbation across **Chladni eigenmodes** |
| Hammer Head Material (Steel vs Boxwood) | Dictates pulse width: steel excites crisp upper modes; mallet drives warm bass. | Impact impulse envelope width (*Low-pass Exciter Kernel*) |
| Multi-Apprentice Bazaar Polyrhythms | Coordinates rotational thermal loading evenly around vessel rims cleanly. | Multi-voice rhythmic impulse scheduler / algorithmic clock |
| Hollow Hammered Vessel Cavity | Supplies low coupled air-cavity Helmholtz bass warmth beneath plate rings. | Coupled Feedback Delay Network (**FDN Cavity Filter**) |

:::bridge Craft-to-Code Bridge
Strike a hammered copper plate away from center and its metallic chime bursts forth not as arbitrary fuzz, but as the clean weighted sum of discrete **eigenmodes** fixed by diameter and alloy hardness. Classic **Chladni sand lines** track exact nodal lines where radial and angular plate modes cross zero amplitude ($Z(r,\theta) = \sin(n\pi r) \cos(m\theta) = 0$). Writing **Modal Synthesis** software maps each physical $(n,m)$ plate vibration cleanly into a bank of decaying sine oscillators—so toggling between *annealed softness* and *cold-hammered brilliance* reduces neatly to tuning stiffness (`stiffness`) and decay rates inside code.
:::

The Python model below encapsulates this acoustic bridge cleanly: computing copper vessel harmonic frequencies across annealing vs. cold planishing stages (`copper_modal_bank`), then evaluating how hammer strike placement couples selectively across Chladni nodes (`synthesize_hammer_strike`).

```python title="Hammered Copper Chladni Eigenvalues & Modal Synthesis Engine"
# Craft&Code — Copper Modal Resonator Bank & Work-Hardening Acoustics
import math

def copper_modal_bank(radius_cm=18.0, work_hardening=0.85, annealed=False):
    """Generates harmonic modal resonances across annealed vs cold-hardened states."""
    # Work-hardening boosts Young's modulus stiffness while reducing internal damping
    stiffness = 0.55 if annealed else (0.95 + 0.45 * work_hardening)
    base_freq_hz = (420.0 / (radius_cm / 15.0) ** 1.4) * stiffness
    decay_rate = 3.8 if annealed else (1.15 - 0.35 * work_hardening)

    # Disk eigenmode indices (radial n, angular m) and Chladni pitch ratios
    mode_ratios = [
        ((1, 2), 1.00, 1.00),
        ((2, 3), 2.38, 0.72),
        ((3, 5), 4.42, 0.46),
        ((4, 6), 7.15, 0.29),
    ]
    modes = []
    for (n, m), ratio, base_amp in mode_ratios:
        freq = round(base_freq_hz * ratio, 1)
        amp = round(base_amp * (0.65 if annealed else 1.0), 3)
        t60_sec = round(6.91 / (decay_rate * (1.0 + 0.15 * n)), 2)
        modes.append({"mode": (n, m), "freq_hz": freq, "amp": amp, "decay_t60_s": t60_sec})
    return modes

def synthesize_hammer_strike(modes, time_sec, strike_r=0.45, strike_theta=0.3):
    """Evaluates instantaneous acoustic pressure amplitude for a spatial strike point."""
    sample = 0.0
    for md in modes:
        n, m = md["mode"]
        # Striking straight atop a Chladni nodal line excites zero amplitude for that mode
        spatial_coupling = abs(math.sin(n * math.pi * strike_r) * math.cos(m * strike_theta))
        envelope = math.exp(-3.5 * time_sec / max(md["decay_t60_s"], 0.1))
        sample += md["amp"] * spatial_coupling * envelope * math.sin(2.0 * math.pi * md["freq_hz"] * time_sec)
    return round(sample, 5)
```

Notice `spatial_coupling = abs(math.sin(n * math.pi * strike_r) * math.cos(m * strike_theta))`: striking right atop a nodal ring cleanly suppresses that harmonic—capturing numerically why master percussionists and smiths subtly vary hammer strike radius to sculpt voice timbre.

## 4. Contemporary Practice & Scientific Case Studies

Three decisive milestones span historical Anatolian smithing workshops, modernist kinetic metal sculpture, and frontier acoustic computing.

### Case Study 1: Collective Hammer Polyrhythms in Gaziantep & Kahramanmaraş
In southern Anatolia's historic copper bazaars, teams of masters and apprentices beat giant circular pots synchronously atop common stakes—turning structural production straight into interlocking **3/4 and asymmetrical aksak polyrhythmic clocks**. Rather than mere musical embellishment, synchronized alternating strike choreography equilibrates uneven metal strain uniformly while letting smiths hear acoustic crystallization changes across every quadrant cleanly.

### Case Study 2: Harry Bertoia — *Sonambient* Sculptures (Pennsylvania, 1960–1978)
Italian-American sculptor and designer **Harry Bertoia** dedicated his mature decades to forging singing vertical rods and hammered beryllium-copper gongs inside his Pennsylvania barn—producing the legendary **Sonambient** sound sculptures. Manipulating thermal annealing and forged tip weights across brass and copper shafts without loudspeakers or electronics, Bertoia built tactile bronze forests vibrating solely via microtonal metallic acoustics.

### Case Study 3: IRCAM *Modalys* & Zimoun's Mechanical Percussion Architecture
At Paris's **IRCAM**, **Modalys** pioneers physical-modeling acoustic computing—generating rich metallic timbre mathematically from mesh geometry, crystal rigidity, and strike locations rather than dead recorded WAV samples. Concurrently, Swiss sound artist **Zimoun** wires hundreds of elementary DC motors to birch rods and reverberant metal plates, converting mechanical friction into cavernous spatial polyrhythms directly recalling the ceaseless hammer pulse of an ancient bazaar.

## 5. Critical Synthesis: Resistance of Matter, Horizons of Code

Digital DSP engines synthesize gleaming bronze gong rings cleanly on tiny chips. Yet studio speakers flattening sound pressure along paper cones never capture the radiant omnidirectional pressure waves humming tangibly inside one hand-raised Anatolian copper bowl warming against human skin.

Physical modeling acoustics offers smiths an illuminating analytic mirror—decoding oral lore of *"tired copper pitch"* cleanly into crystal eigenvalues and nodal maps. Real resonance blooms sharpest where cold iron stake discipline meets transparent mathematical acoustics.

:::curatorial Curatorial Note
Whether returning hammered copper cleanly back into glowing embers as its acoustic pitch warns of grain exhaustion, or tuning `work_hardening` modal resonance banks in code, both makers listen faithfully to one living teacher: **crystal structure singing back against impact.**
:::

---

### Bibliography & Further Reading
1. **Belli, Oktay & Kayaoğlu, İ. Gündağ.** *Anadolu'da Türk Bakırcılık Sanatının Gelişimi*. Sandoz Kültür Yayınları, Istanbul, 1993.
2. **Chladni, Ernst Florens Friedrich.** *Entdeckungen über die Theorie des Klanges*. Weidmanns Erben und Reich, Leipzig, 1787.
3. **Bilbao, Stefan.** *Numerical Sound Synthesis: Finite Difference Schemes and Simulation in Musical Acoustics*. Wiley, Chichester, 2009.
4. **Bertoia, Val & Bertoia, Celia.** *The Life and Work of Harry Bertoia*. Schiffer Publishing, 2015.
5. **Adrien, Jean-Marie.** "The Missing Link: Modal Synthesis." *Representations of Musical Signals*, MIT Press, 1991, pp. 269–298.
'''
    }
}

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
    for c in fresh_candidates:
        selected.append(c)
        if len(selected) == 3:
            break

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
    """Generates rich bilingual markdown draft files for an approved topic."""
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

    essay = TOPIC_ESSAYS.get(topic_key)
    if essay:
        tr_body = essay["body_tr"]
        en_body = essay["body_en"]
        tr_subtitle = essay["subtitle_tr"]
        en_subtitle = essay["subtitle_en"]
        tr_tags = json.dumps(essay["tags_tr"], ensure_ascii=False)
        en_tags = json.dumps(essay["tags_en"], ensure_ascii=False)
        tr_caption = essay["cover_caption_tr"]
        en_caption = essay["cover_caption_en"]
    else:
        tr_subtitle = match["thesis"]
        en_subtitle = match["thesis"]
        base_tag = match["category"].split("&")[0].strip()
        tr_tags = json.dumps([base_tag, "Çağdaş Sanat", "Generatif Kod", "Yeni Medya"], ensure_ascii=False)
        en_tags = json.dumps([base_tag, "Contemporary Art", "Generative Code", "New Media"], ensure_ascii=False)
        tr_caption = f"Kavramsal Eser: {match['title']} üzerine küratöryel stüdyo araştırması."
        en_caption = f"Conceptual Artwork: Curatorial studio exploration of {match['title_en']}."

        tr_body = f"""{match['thesis']}

## 1. Tarihsel Kökler: Zanaat Coğrafyası ve Ustalık Geleneği
Her kadim zanaat, kendi döneminin en gelişmiş malzeme kimyası, mekân geometrisi ve beden hafızası üzerine kurulur. Ustanın atölyesinde üretilen her form; hammadde seçimi, mevsimsel dinlendirme ve kuşaktan kuşağa aktarılan sözlü kuralların somut ürünüdür.

## 2. Malzeme, Araç ve Atölye Anatomisi
Fiziksel atölyede aletin malzemeyle buluştuğu her nokta dikkatle kalibre edilir; ham maddenin direnci zorlanmak yerine yapısal tasarımın ana değişkeni haline getirilir.

> "Zanaatkâr, eylemi esnasında maddeyle sürekli ve samimi bir diyalog kurar; onu boyunduruk altına almaz, onun direncini dinler." -- Richard Sennett, The Craftsman

## 3. Gelenekselden Koda: Yapısal Karşılıklar ve Algoritmik Çeviri

| Geleneksel Zanaat Unsuru | Atölyedeki Fiziksel İşlevi | Koddaki / Algoritmadaki Karşılığı |
| :--- | :--- | :--- |
| Hammadde & Doğal Değişken | Malzemenin lif, mineral veya nem tepkisi | Girdi parametreleri & malzeme sabiti (`material_coeff`) |
| Usta Aletleri & Kalibrasyon | Açılı kesim, basınç ve hız ayarı | Geometrik dönüşüm & sınır kısıtları (`constraints`) |
| Tekrarlı El Ritmi | Modüler yüzey veya strüktür kurulumu | Döngüsel algoritma & matris kuralı (`for step in cycle`) |

:::bridge Zanaattan Koda Köprü
Geleneksel zanaattaki her fiziksel oran ve malzeme sınırı, hesaplamalı sanatta doğrudan parametrik kısıtlara ve üretken kod döngülerine tercüme edilir.
:::

```python title="Zanaat Parametrelerinden Algoritmik Üretime Temel Şablon"
def craft_parameter_bridge(material_coeff, steps=12):
    \"\"\"Geleneksel malzeme katsayılarını algoritmik adımlara eşler.\"\"\"
    return [round(material_coeff * (i + 1) / steps, 4) for i in range(steps)]
```

## 4. Çağdaş Sanat ve Vaka İncelemeleri
{match['cases']}

## 5. Eleştirel Sentez
Zanaat ile kodun bu kesişimi, geleceğin teknolojisini tasarlarken kadim malzeme bilgisini yaşatmamız gerektiğini hatırlatır.

:::curatorial Küratöryel Not
Zanaatın bedensel sabrı ile kodun soyutlama gücü buluştuğunda; teknoloji gelenekten beslenir, gelenek ise güncel sanat aracılığıyla geleceğe taşınır.
:::

---
### Kaynakça ve İleri Okumalar
1. **Sennett, Richard.** *The Craftsman*. Yale University Press, 2008.
2. **Ingold, Tim.** *Making: Anthropology, Archaeology, Art and Architecture*. Routledge, 2013.
3. **Craft&Code Araştırma Arşivi**, 2026."""

        en_body = f"""{match['thesis']}

## 1. Historical Roots: Craft Geography and Workshop Lineages
Every ancient craft represents the vanguard material chemistry, spatial geometry, and tactile intelligence of its epoch—shaped across centuries of disciplined guild inquiry.

## 2. Materials, Tools, and Atelier Anatomy
Rather than forcing inert substance from above, the workshop negotiates directly with physical strain, humidity, temperature, and grain texture.

> "The craftsman conducts a continuous and candid dialogue with matter; they do not subdue it, but heed its intrinsic resistance." -- Richard Sennett, The Craftsman

## 3. Craft to Code: Structural Correspondences & Algorithmic Translation

| Traditional Craft Element | Physical Function in the Workshop | Computational / Algorithmic Equivalent |
| :--- | :--- | :--- |
| Raw Matter & Environmental State | Fiber, mineral, or humidity response | Input parameters & material coefficient (`material_coeff`) |
| Hand Tool Calibration | Bevel angles, pressure, and thermal cadence | Geometric transform & structural boundary constraints |
| Iterative Craft Cadence | Builds complex spatial continuity safely | Generative loops & transition rules (`for step in cycle`) |

:::bridge Craft-to-Code Bridge
Every tactile workshop proportion translates naturally into structural code parameters, unifying bodily endurance with mathematical rigor.
:::

```python title="Parametric Craft Bridge Base Model"
def craft_parameter_bridge(material_coeff, steps=12):
    \"\"\"Maps traditional material constraints smoothly across iterative code steps.\"\"\"
    return [round(material_coeff * (i + 1) / steps, 4) for i in range(steps)]
```

## 4. Contemporary Practice & Case Studies
{match['cases']}

## 5. Critical Synthesis
Where traditional craft meets open computation, material empathy anchors technological imagination.

:::curatorial Curatorial Note
When embodied atelier intuition meets formal computational abstraction, neither tradition stagnates nor software loses material gravity.
:::

---
### Bibliography & References
1. **Sennett, Richard.** *The Craftsman*. Yale University Press, 2008.
2. **Ingold, Tim.** *Making: Anthropology, Archaeology, Art and Architecture*. Routledge, 2013.
3. **Craft&Code Editorial Archive**, 2026."""

    tr_md = f"""---
title: "{match['title']}"
subtitle: "{tr_subtitle}"
summary: "{match['thesis']}"
slug: "{slug}"
date: "2026-11-14"
author: "Craft&Code Araştırma Masası"
tags: {tr_tags}
cover_image: "{cover_image}"
cover_caption: "{tr_caption}"
cover_credit: "Görsel: Craft&Code / Yapay Zekâ & Küratöryel Konsept Tasarımı"
draft: true
---
{tr_body.strip()}
"""
    tr_file = CONTENT_DIR / "drafts" / "tr" / f"{slug}.md"
    tr_file.parent.mkdir(parents=True, exist_ok=True)
    tr_file.write_text(tr_md, encoding="utf-8")

    en_md = f"""---
title: "{match['title_en']}"
subtitle: "{en_subtitle}"
summary: "{match['thesis']}"
slug: "{slug}"
date: "2026-11-14"
author: "Craft&Code Editorial Desk"
tags: {en_tags}
cover_image: "{cover_image}"
cover_caption: "{en_caption}"
cover_credit: "Visual: Craft&Code / AI & Curatorial Concept Synthesis"
draft: true
---
{en_body.strip()}
"""
    en_file = CONTENT_DIR / "drafts" / "en" / f"{slug}.md"
    en_file.parent.mkdir(parents=True, exist_ok=True)
    en_file.write_text(en_md, encoding="utf-8")

    mem = load_memory()
    if slug not in mem["covered_slugs"]:
        mem["covered_slugs"].append(slug)
    if topic_key in mem.get("active_proposals", []):
        mem["active_proposals"].remove(topic_key)
    save_memory(mem)

    return slug
