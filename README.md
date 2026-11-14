# Craft&Code (Sanat, Zanaat ve Algoritmik İncelemeler)

> **Motto:** Kadim Zanaatların Hafızası, Güncel Sanatın ve Kodun Dili  
> **Editorial Vision:** The Memory of Ancient Crafts, the Syntax of Code and Contemporary Art

---

## 📁 Proje Yapısı

```
RKblog/
├── content/
│   ├── drafts/                  # 📝 Sizin onayınızı bekleyen taslaklar (Yayında görünmez)
│   │   ├── tr/                  # Türkçe taslak makaleler (.md)
│   │   └── en/                  # İngilizce taslak makaleler (.md)
│   └── published/               # 🚀 Onayladığınız, yayına hazır makaleler
│       ├── tr/
│       └── en/
├── public/                      # Statik dosyalar (Görseller, CSS, fontlar)
│   ├── images/
│   └── css/style.css
├── templates/                   # Zarif editoryal HTML şablonları
├── dist/                        # Derlenmiş statik site (Yayına giden klasör)
├── build.py                     # Site derleyici (Markdown -> HTML)
├── serve.py                     # Bilgisayarınızda yerel önizleme sunucusu
└── README.md
```

---

## 🛠️ Nasıl Kullanılır? (Editoryal İş Akışınız)

### 1. Yerel Önizlemeyi Başlatma (Taslakları Okuma & İnceleme)
Terminalde şu komutu çalıştırarak önizleme sunucusunu başlatın:

```bash
python3 serve.py
```

Tarayıcınızı açıp şu adreslere gidin:
* **Ana Sayfa:** [http://localhost:8000/tr/](http://localhost:8000/tr/)
* **Türkçe İlk Taslak:** [http://localhost:8000/tr/yazilar/dokuma-tezgahindan-koda.html](http://localhost:8000/tr/yazilar/dokuma-tezgahindan-koda.html)
* **English Draft:** [http://localhost:8000/en/articles/dokuma-tezgahindan-koda.html](http://localhost:8000/en/articles/dokuma-tezgahindan-koda.html)

### 2. Yazıyı Düzenleme
* Metni okurken değiştirmek istediğiniz bir yer olursa doğrudan şu dosyayı açıp dilediğiniz gibi düzenleyebilirsiniz:
  * Türkçe: `content/drafts/tr/dokuma-tezgahindan-koda.md`
  * İngilizce: `content/drafts/en/from-looms-to-code.md`
* Ya da bana *"Şu paragrafı şöyle değiştirelim"* demeniz yeterlidir; sizin için anında güncellerim.

### 3. Yayına Onay Verme (Publish)
Bir yazıyı beğendiğinizde ve yayınlamak istediğinizde:
1. Dosyayı `content/drafts/tr/` klasöründen `content/published/tr/` klasörüne taşıyın (veya frontmatter'daki `draft: true` satırını `draft: false` yapın).
2. Siteyi derleyin:
   ```bash
   python3 build.py
   ```

### 4. İnternette Canlıya Alma (Vercel / Cloudflare Pages / GitHub)
1. Kodları GitHub deponuza gönderin:
   ```bash
   git init
   git add .
   git commit -m "İlk makale ve Craft&Code yayında"
   git push origin main
   ```
2. Vercel veya Cloudflare Pages paneline GitHub reponuzu bağlayın.
   * **Build Command:** `python3 build.py --no-drafts`
   * **Output Directory:** `dist`
   * Böylece Vercel her `git push` yaptığınızda sadece **onaylanmış** yazılarınızı otomatik olarak dünyaya yayınlar!
