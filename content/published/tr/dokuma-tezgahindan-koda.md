---
title: "Delikli Kartlardan Algoritmalara: Dokuma Tezgâhı ve Generatif Sanatın Kadim Kökleri"
subtitle: "Anadolu çulfalıklarından Basile Bouchon ve Joseph Marie Jacquard'ın delikli kart zincirine; çözgü-atkı matris cebirinden Ada Lovelace'a ve çağdaş tekstil bilgisayarlarına."
summary: "Hesaplamalı sanat genellikle 20. yüzyılın bir icadı olarak görülür. Oysa kodun ilk somut sintaksı silikon çiplerde değil; ahşap dokuma tezgâhlarında, çözgü ile atkının 'yukarı (1)' ve 'aşağı (0)' ikili geriliminde doğdu."
slug: "dokuma-tezgahindan-koda"
date: "2026-11-14"
author: "Craft&Code Araştırma Masası"
tags: ["Dokuma", "Jacquard", "Örgü Matrisi", "Generatif Sanat", "Yeni Medya"]
cover_image: "/images/weaving-and-code-cover.jpg"
cover_caption: "Kavramsal Enstalasyon: Geleneksel ahşap tezgâhtaki el dokuması yün ipliklerin optik fiberlere ve pikselli ikili matrise dönüşümü."
cover_credit: "Görsel: Craft&Code / Yapay Zekâ ve Küratöryel Konsept Tasarımı"
draft: false
---
Günümüz dijital kültüründe "kod", ekranların arkasında görünmezce işleyen, maddeden bağımsız, steril bir mantık sistemi olarak algılanır. Oysa bilgisayar biliminin kurucu hafızasına ve ilk algoritmik makine mimarilerine indiğimizde çarpıcı bir gerçekle karşılaşırız: **Bilinen ilk programlanabilir ikili donanım sistemleri silikon çiplerde değil; ahşap dokuma tezgâhlarında, yün çözgülerin geriliminde ve delikli kart zincirlerinde doğmuştur.**

Dokumacılık özü itibarıyla iki boyutlu saf bir **ikili cebir** (*binary algebra*) pratiğidir. Dikey yönde gerili her çözgü ipliği, yatay atılan her atkı sırasının **ya üstünden (1)** ya da **altından (0)** geçmek zorundadır; araya üçüncü bir durum giremez. Bu zorunlu ikilik nedeniyle Anadolu köylerindeki kirkitli *ıstar* ve pedallı *çulfalık* tezgâhlarından Lyon'un ipek atölyelerine kadar her dokuma ustası, tarih boyunca aslında bellek kartları ve döngü altprogramlarıyla çalışan bir donanım mimarı gibi düşünmüştür.

## 1. Tarihsel Kökler: Anadolu Çulfalıklarından Lyon'un Delikli Kartlarına

İpliğin ve tezgâhın tarihi, insanlığın yerleşik matematiksel düzen kurma tarihidir. Anadolu'nun köklü dokuma kültüründe iki ana tezgâh ailesi gelişmiştir: Halı, kilim, *cicim*, *zili* ve *sumak* gibi serbest desenli dokumaların yapıldığı dikey ve kirkitli **ıstar / kirmen tezgâhları** ile yatay düzlemde ayak pedallarıyla (**ayakça**) çalışan çok çerçeveli **çulfalık (düzen) tezgâhları**. Anadolu çulfası ayağıyla belirli bir **ayakça** pedalına bastığında, pedala bağlı **gücü çerçevesi** yukarı kalkar; böylece ilgili **çözgü** iplikleri açılır (**ağızlık / shed** oluşur) ve mekik o boşluktan geçerek atkıyı yatırır. Aslında ayak pedallarıyla gücü çerçeveleri arasındaki bağlama düzeni (**bağlantı matrisi / tie-up**), bugün programlamadaki bir **mantık kapısı matrisi**nden (*logic gate*) farksızdır.

Avrupa ipek merkezlerinde karmaşık brokar ve çiçek desenlerini dokumak yüzyıllarca "çekici çocukların" (*drawboy*) tezgâh tepesinde oturup her satırda yüzlerce kordonu eliyle yukarı çekmesine dayanıyordu. Bu ağır emeği ve insan hatasını otomatikleştirmek için Fransa'nın Lyon kentinde tarihi bir yazılım-donanım evrimi yaşandı:
- **1725 — Basile Bouchon:** İğneleri seçmek için ilk kez delikli sürekli kâğıt şeridi tezgâha uyarladı.
- **1728 — Jean-Baptiste Falcon:** Kırılgan kâğıt rulosu yerine birbirine zincirle bağlı **sert delikli mukavva kartlar** dizisini icat etti.
- **1745 — Jacques Vaucanson:** Çekici çocuğu tamamen ortadan kaldırmayı amaçlayan ilk mekanik delikli kart silindirini kurdu.
- **1804 — Joseph Marie Jacquard:** Tüm önceki buluşları tek bir kusursuz sistemde birleştirerek **Jacquard Tezgâhı**nı kurdu. Kart zincirindeki her delik iğneyi geçirip çözgüyü kaldırıyor (**1**), deliksiz karton yüzeyi ise iğneyi itip çözgüyü altta tutuyordu (**0**). Kart zinciri baştan sona döndüğünde karmaşık bir portre veya damasko deseni sıfır hatayla dokunuyordu.

Tam bu teknolojiyi gören İngiliz matematikçi **Charles Babbage** ile şair Lord Byron'un kızı **Ada Lovelace**, Jacquard kartlarını mekanik genel amaçlı hesap makinesinin programlama belleği olarak seçtiler:

> "Analitik Motor, tıpkı Jakarlı tezgâhın çiçek ve yaprakları dokuduğu gibi, cebirsel örüntüleri dokur." -- Ada Lovelace, 1843 (Analitik Motor Üzerine Notlar)

Kültür kuramcısı **Sadie Plant**'ın *Zeros and Ones* (1997) kitabında altını çizdiği üzere, yüzyıllarca kadın zanaatı sayılarak teknik tarihten dışlanan dokuma; aslında ikili hesaplama ve yazılım geliştirme geleneğinin kurucu matrisidir.

## 2. Anadolu ve Klasik Tezgâhta Araç, Örgü ve Malzeme Anatomisi

Bir kumaşı kâğıt üstündeki bir çizimden ayıran ve onu üç boyutlu yapısal bir mimariye dönüştüren temel unsur; ipliğin büküm yönü, gerginliği ve temel örgü topolojisidir:

![Üç temel dokuma örgü yapısının (Bezayağı 1/1, 2/2 Dimi ve 5-Saten) ikili 0-1 matrisleri ve karşılık gelen çözgü-atkı kesişim diyagramları](/images/dokuma-orgu-matris.svg "Dokuma Örgü Cebiri: Bezayağı, 2/2 Dimi ve 5-end Saten örüntülerinin ikili (0/1) matris gösterimi ve fiziksel iplik örgüsü | Görsel: Craft&Code Hesaplamalı Diyagram Arşivi")

- **Tezgâh Organları (*Çözgü, Gücü, Tarak, Mekik, Ayakça*):** Tezgâhın omurgasını gerilen boylamasına **çözgü** (warp) iplikleri oluşturur; bükümü yüksek ve sağlam yün veya pamuktan seçilir. Her çözgü teli dikey bir gücü gözünden (*gücü*) ve dişleri sık metal ya da kamış **tarak** (*reed*) arasından geçer. Ayak **ayakçalarına** basıldığında gücü çerçeveleri iki katmanlı bir **ağızlık** açar. İçinde masuraya sarılı **atkı** (weft) ipliği bulunan şimşir veya ceviz **mekik**, bu ağızlıktan hızla geçirilir ve **tarak** çekilerek yeni sırayı kumaşa sıkıştırır (*dövmek*).
- **Üç Temel Örgü Yapısı (*Bezayağı, Dimi, Saten*):** Tüm tekstil tarihinin neredeyse tamamı üç matematiksel temel modül üzerine kurulur:
  1. **Bezayağı (*Tabby / 1-1 Plain Weave*):** En sıkı ve en kadim örgüdür (`(satır + sütun) mod 2`). Her çözgü bir atkı üstünden, bir atkı altından geçer; sürtünmesi yüksektir, tersi düzü aynıdır.
  2. **Dimi (*Twill 2/2*):** Çözgülerin çapraz basamaklarla kaydırılmasıyla (`(sütun - satır) mod 4 < 2`) oluşan verev çizgili sağlam yapıdır. Şayak, gabardin ve denim kumaşların belkemiğidir.
  3. **Saten / Atlas (*5-Saten*):** Kesişme noktalarının periyodik ve birbirine değmeyecek şekilde modüler adımla dağıtılması (`(sütun - 2*satır) mod 5 == 0`) sayesinde yüzeyde uzun kesintisiz iplik atlamaları (**float**) bırakır; ışığı kesintisiz yansıtarak pürüzsüz ipek parlaklığı sağlar.
- **Kirkitli Geleneksel Anadolu Teknikleri (*Cicim, Zili, Sumak*):** Düz kilim tekniğinde atkı tamamen çözgünün içinden giderken, *zili* ve *sumak* dokumalarında ekstra renkli **desen ipliği**, belirli sayıdaki çözgü telinin üzerinden atlanıp arkadan sarılarak ("3 üstte 1 altta", "5 üstte 1 altta") doğrudan **çalışma zamanlı döngüsel sayma algoritması** (*counting stitch*) gibi işlenir.

## 3. Gelenekselden Koda: Yapısal Karşılıklar ve Algoritmik Çeviri

1920'lerde **Bauhaus Dokuma Atölyesi**'nin büyük kuramcısı **Anni Albers** ve **Gunta Stölzl**, tekstili süsleme sanatından çıkarıp "iki boyutlu mekânda çizgi ve gerilim mühendisliği" olarak tanımladıklarında; aslında bugün Processing, Python ve matris cebiriyle yazdığımız örgü programlamasının önünü açmışlardı.

| Geleneksel Dokuma Zanaatı Unsuru | Tezgâhtaki Fiziksel İşlevi | Koddaki / Matris Cebirindeki Karşılığı |
| :--- | :--- | :--- |
| Çözgü (Dikey) ve Atkı (Yatay) Kesişimi | Mekik geçerken çözgünün atkı üstünde kalması veya altında saklanması. | İkili piksel/matris elemanı: `1` (Çözgü Üstte) veya `0` (Atkı Üstte) |
| *Gücü* Geçiş Planı (*Tahşiye / Threading*) | Her çözgü telinin hangi hareketli gücü çerçevesine bağlanacağını belirler. | Matris $T$ (Threading Matrix — Çözgü-Çerçeve ataması) |
| Pedallara Bağlama Planı (*Armür / Tie-up*) | Tek bir ayak pedalına basıldığında hangi gücülerin aynı anda kalkacağını yönetir. | Matris $P$ (Tie-up Boolean Logic Gate — Çerçeve gruplama) |
| Dokumacı Pedal Sırası (*Ayakça / Treadling*) | Dokuma süresince satır satır hangi pedala basılacağını gösteren zaman dizisi. | Matris $L$ (Treadling Sequence — Saat darbesi / Program Counter) |
| Nihai Kumaş Yüzey Deseni (*Çizim / Drawdown*) | Yukarıdaki üç planın fiziksel olarak örülmesiyle ortaya çıkan dokunmuş yüzey. | Üçlü Matris Çarpımı: $D = T \times P \times L^{T}$ (Binary Drawdown) |
| *Jacquard* Delikli Mukavva Kart Zinciri | Her atkı sırası için binlerce bağımsız çözgü iğnesini tek satırda adreslemek. | Salt Okunur Bellek Şeridi (ROM Punched Bytecode Array) |
| Kumaş Çekme Toleransı ve İplik *Float* Uzunluğu | Çok uzun atlamalı (*float*) noktaların kopup çözülmesini engellemek. | Max run-length sınırlayıcı kısıt doğrulaması (`max_float_constraint`) |

:::bridge Zanaattan Koda Köprü
Tezgâhçı için dokuma taslağı (*draft*) ile bilgisayar mühendisi için mantıksal devre cebiri **birebir aynı matematiksel nesnedir**. Çözgülerin çerçevelere dağılımını $T$, çerçevelerin pedallara bağlanmasını $P$ ve pedal basış sırasını $L$ ikili matrisleri olarak kodladığınızda; tezgâhın dokuyacağı gerçek kumaş yüzeyi doğrudan matris çarpımı $D = \text{clip}(L \cdot P \cdot T)$ ile elde edilir! Bauhaus'tan günümüze kadar hiçbir endüstriyel CAD yazılımı bu temel üçlü matris cebirini değiştirmemiştir.
:::

Aşağıdaki Python kodu, hem **üçlü dokuma taslağı matris cebirini (`compute_drawdown_matrix`)** uygulayarak verilen çözgü-bağlama-pedal düzeninden Bezayağı ve 2/2 Dimi kumaş örgüsünü matematiksel olarak hesaplar hem de bir **Jacquard delikli kart** okuyucusunun her atkı satırı için ürettiği ikili delik şeridini oluşturur.

```python title="Jakar Delikli Kartı ve Örgü Matris Cebiri (Bezayağı / Dimi / Saten)"
# Craft&Code — Çözgü-Gücü-Ayakça Matris Cebiri ve Jacquard Delik Şeridi

def compute_drawdown_matrix(treadling, tieup, threading):
    """D = (Treadling x Tie-up x Threading) matris çarpımı ile kumaş örgüsünü çözer."""
    num_weft = len(treadling)
    num_shafts = len(tieup)
    num_warp = len(threading[0])

    # 1. Adim: Pedal basısına göre hangi gücü çerçeveleri kalkıyor (L x P)
    active_shafts = []
    for row in treadling:
        shaft_mask = [0] * num_shafts
        for ped_idx, pressed in enumerate(row):
            if pressed:
                for sh_idx in range(num_shafts):
                    shaft_mask[sh_idx] |= tieup[sh_idx][ped_idx]
        active_shafts.append(shaft_mask)

    # 2. Adim: Kalkan çerçevelere bağlı olan çözgü tellerini belirle ((L x P) x T)
    drawdown = []
    for s_mask in active_shafts:
        weft_row = []
        for w_idx in range(num_warp):
            raised = any(s_mask[sh] and threading[sh][w_idx] for sh in range(num_shafts))
            weft_row.append(1 if raised else 0)  # 1 = Çözgü üstte, 0 = Atkı üstte
        drawdown.append(weft_row)
    return drawdown

def build_twill_draft(num_warp=8, num_weft=8):
    """4-cerceveli klasik 2/2 Dimi (Twill) için tahsiye, armür ve ayakça kurar."""
    threading = [[1 if (w % 4 == sh) else 0 for w in range(num_warp)] for sh in range(4)]
    tieup = [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
    ]
    treadling = [[1 if (r % 4 == p) else 0 for p in range(4)] for r in range(num_weft)]
    return compute_drawdown_matrix(treadling, tieup, threading)

def jacquard_punch_cards(motif_matrix):
    """Bir motifi Jacquard makinesinin mekanik iğnelerine göre ikili delik şeridine çevirir."""
    return ["".join("O" if bit == 1 else "." for bit in row) for row in motif_matrix]
```

Bu kod bloğunda `raised = any(s_mask[sh] and threading[sh][w_idx] ...)` satırı; Anadolu'da tahta tezgâhın başında ayak pedalıyla gücü çerçevesini çekip mekiğin önüne çözgü açan dokumacının mekanik hareketini tam satır kod olarak ifade eder.

## 4. Çağdaş Sanat, Laboratuvar ve Vaka İncelemeleri

Dokuma tezgâhı ile dijital algoritmanın buluşması, günümüz medya sanatında yalnızca sembolik bir metafor olarak kalmamış; çalışan fiziksel bilgisayarlara ve dokunabilir veri tekstillerine dönüşmüştür.

![Delikli Jacquard mukavva kartındaki ikili deliklerin iğne aktarım çizgileriyle dokunmuş geometrik motife dönüşümünü gösteren diyagram](/images/dokuma-jakar-kart.svg "Jacquard İkili Veri Yolu: Mukavva karttaki delikler (1) ve dolgu alanlar (0) doğrudan çözgü iğnelerini tetikleyerek tekrarlı tekstil motifini örer | Görsel: Craft&Code Hesaplamalı Diyagram Arşivi")

### Vaka 1: Anni Albers & Bauhaus Dokuma Atölyesi (Dessau & Black Mountain, 1922–1965)
1920'lerde Dessau Bauhaus Dokuma Atölyesi'nde **Gunta Stölzl** ve **Anni Albers**, tekstili burjuva duvar süsünden çıkarıp yapısal bir sanat ve mühendislik pratiğine dönüştürdüler. Albers'ın *On Weaving* (1965) adlı klasik kitabında geliştirdiği "yapısal ızgara" (*structural grid*) yaklaşımı; çözgü-atkı matrisindeki ufak permütasyonlarla nasıl sonsuz akustik, mimari ve optik etkiler üretilebileceğini gösterdi. Bugün ekran başında `for` döngüleriyle üretken sanat (*generative art*) yapan her kodlayıcı, farkında olarak veya olmayarak Albers'ın izinden yürür.

### Vaka 2: Ebru Kurbak & Irene Posch — *The Embroidered Computer* (Viyana, 2014–2018)
Viyana Uygulamalı Sanatlar Üniversitesi'nde yürütülen *Stitching Worlds* projesi kapsamında sanatçı-araştırmacı **Ebru Kurbak** ve **Irene Posch**, modern teknoloji tarihine köklü bir karşı-soru yöneltti: *"Eğer bilgisayarlar silikon yerine dokuma ve nakış zanaatının içinden evrilseydi donanım nasıl görünürdü?"* İkili; bakır, gümüş ve altın sırmalı iletken iplikler, manyetik cam boncuklar ve ahşap dokuma kasnakları kullanarak geleneksel el nakışı ile çalışan tam işlevsel **8-bitlik elektromekanik bir bilgisayar** ördü. Bu eserde mantık kapıları kapalı kara kutularda değil; her dikişi gözle izlenebilen şeffaf bir tekstil halısının üzerinde işlemektedir.

### Vaka 3: Phillip Stearns — *Glitch Textiles* (Brooklyn, 2012–Günümüz)
Brooklyn merkezli sanatçı ve mühendis **Phillip Stearns**, çağdaş bilgisayarların en kırılgan anları olan **ham RAM bellek dökümlerini**, çekirdek çökmelerini (*kernel panic*) ve dijital görsel bozulmaları doğrudan sanayi tipi bilgisayarlı **Jacquard dokuma tezgâhlarına** aktarır. Ekranda birkaç milisaniye parlayıp yok olan sayısal parazitler, yün ve merinos pamuğundan kalın yorganlara ve duvar halılarına dönüşerek dijital belleğe sıcak, ağır ve dokunulabilir bir fiziksel ömür kazandırır.

## 5. Eleştirel Sentez: Zanaatın Direnci ve Kodun Sınırı

Endüstriyel bilgisayarlı dokuma tezgâhları saniyeler içinde dijital piksel haritalarını okuyup devasa karmaşıklıktaki kumaşları hatasız üretebilir. Ne var ki bilgisayar algoritması ipliğin hava nemiyle gerilmesini, çözgü telinin aniden kopup el ile düğümlenmesini veya bir Anadolu kilim dokuyucusunun mekiği geçirirken desenin ortasında içinden gelerek açtığı kişisel "nazarlık/kusur" değişimini asla kendi başına seçemez.

Kod dünyasının maddeden kopuk hızına karşı dokuma tezgâhı bize şunu hatırlatır: **Her algoritma günün sonunda fiziksel bir gerilim, sabır ve örüntü emeğidir.** İkili kodun (*0 ve 1*) kurduğu dünyanın temeli, sanıldığından çok daha sıcak, çok daha dokulu ve binlerce yıllık el emeğinin hafızasıyla örülüdür.

:::curatorial Küratöryel Not
1804'te Lyon tezgâhında delikli karttan geçen demir iğne de, bugün bir Python betiğinde hesaplanan `drawdown` ikili matrisi de aynı tarihsel cümleyi okur: **Yukarı kalk ve atkıyı geçir (1), altta bekle (0) — çünkü en karmaşık dünya bile bu iki basit seçimin sabırlı tekrarından örülür.**
:::

---

### Kaynakça ve İleri Okumalar
1. **Albers, Anni.** *On Weaving*. Wesleyan University Press, Middletown, CT, 1965 (Genişletilmiş Baskı: Princeton University Press, 2017).
2. **Plant, Sadie.** *Zeros and Ones: Digital Women and the New Technoculture*. Doubleday, New York, 1997.
3. **Kurbak, Ebru (Ed.).** *Stitching Worlds: Exploring Textiles and Electronics*. Revolver Publishing, Berlin, 2018.
4. **Lovelace, Ada.** *Notes on Luigi Menabrea's Sketch of the Analytical Engine Invented by Charles Babbage*. Taylor's Scientific Memoirs, Vol. 3, Londra, 1843.
5. **Essinger, James.** *Jacquard's Web: How a Hand-Loom Led to the Birth of the Information Age*. Oxford University Press, Oxford, 2004.
6. **Görgünay Kırzıoğlu, Neriman.** *Anadolu Düz Dokuma Yaygıları: Kilim, Cicim, Zili, Sumak*. Kültür Bakanlığı Yayınları, Ankara.
