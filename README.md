# Quran API

A simple API to retrieve Quranic text, Surah information, and verse details in Arabic and English.

## 📌 Endpoints

### 1️⃣ Get Info About All Chapters
**Endpoint:**
```bash
/surah/info.json
```
**Response Example:**
```json
[
  {
    "number": 1,
    "name": {
      "ar": "الفاتحة",
      "en": "The Opening",
      "transliteration": "Al-Fatihah"
    },
    "revelation_place": {
      "ar": "مكية",
      "en": "Meccan"
    },
    "revelation_order": 5,
    "bismillah_pre": false,
    "verses_count": 7,
    "words_count": 29,
    "letters_count": 139,
    "pages": [1, 1],
    "name_simple": "Al-Fatihah",
    "translated_name": "The Opener",
    "start_page": 1,
    "end_page": 1
  },
  ...
]
```

---

### 2️⃣ Get A Specific Surah
**Endpoint:**
```bash
/surah/:surah-number/index.json
```
**Example:**
```bash
/surah/112/index.json
```
**Response Example:**
```json
{
  "verses": [
    {
      "id": 6222,
      "number": 1,
      "verse_key": "112:1",
      "text": "قُلۡ هُوَ ٱللَّهُ أَحَدٌ"
    },
    {
      "id": 6223,
      "number": 2,
      "verse_key": "112:2",
      "text": "ٱللَّهُ ٱلصَّمَدُ"
    }
  ]
}
```

---

### 3️⃣ Get A Specific Verse
**Endpoint:**
```bash
/surah/:surah-number/:verse-number.json
```
**Example:**
```bash
/surah/112/1.json
```
**Response Example:**
```json
{
  "id": 6222,
  "number": 1,
  "verse_key": "112:1",
  "text": "قُلۡ هُوَ ٱللَّهُ أَحَدٌ"
}
```

---

### 4️⃣ Get Surah Info
**Endpoint:**
```bash
/surah/:surah-number/info.json
```
**Example:**
```bash
/surah/112/info.json
```
**Response Example:**
```json
{
  "number": 112,
  "name": {
    "ar": "الإخلاص",
    "en": "Sincerity",
    "transliteration": "Al-Ikhlas"
  },
  "revelation_place": {
    "ar": "مكية",
    "en": "Meccan"
  },
  "revelation_order": 22,
  "bismillah_pre": true,
  "verses_count": 4,
  "words_count": 15,
  "letters_count": 47,
  "start_page": 604,
  "end_page": 604
}
```

---

### 5️⃣ Get Surah About Info (English Only)
**Endpoint:**
```bash
/surah/:surah-number/about.en.json
```
**Example:**
```bash
/surah/112/about.en.json
```
**Response Example:**
```json
{
  "chapter_info": {
    "id": 112,
    "chapter_id": 112,
    "language_name": "English",
    "short_text": "Al-Ikhlas is not merely the name of this Surah but also the title of its contents...",
    "source": "Sayyid Abul Ala Maududi - Tafhim al-Qur'an"
  }
}
```

---

### 6️⃣ Get Surah Info with Verses
**Endpoint:**
```bash
/surah/:surah-number/index.info.json
```
**Example:**
```bash
/surah/112/index.info.json
```
**Response Example:**
```json
{
  "number": 112,
  "revelation_order": 22,
  "verses_count": 4,
  "words_count": 15,
  "letters_count": 47,
  "name_simple": "Al-Ikhlas",
  "translated_name": "The Sincerity",
  "revelation_place": {
    "ar": "مكية",
    "en": "Meccan"
  },
  "verses": {
    "1": "قُلْ هُوَ ٱللَّهُ أَحَدٌ",
    "2": "ٱللَّهُ ٱلصَّمَدُ",
    "3": "لَمْ يَلِدْ وَلَمْ يُولَدْ",
    "4": "وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ"
  }
}
```
