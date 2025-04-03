# Quran API

A static API providing access to the complete text of the Quran in Arabic, along with detailed information about each surah and verse.

## Base URL

```
https://api.example.com
```

## Endpoints

### 1. Get All Surahs Information

Retrieves information about all chapters (surahs) of the Quran.

```
GET /surah/info.json
```

#### Response Example
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
      "en": "meccan"
    },
    "revelation_order": 5,
    "bismillah_pre": false,
    "verses_count": 7,
    "words_count": 29,
    "letters_count": 139,
    "pages": [1, 1],
    "name_simple": "Al-Fatihah",
    "name_complex": "Al-Fātiĥah",
    "name_arabic": "الفاتحة",
    "translated_name": "The Opener",
    "start_page": 1,
    "end_page": 1
  }
]
```

### 2. Get Single Surah

Retrieves the complete text of a specific surah.

```
GET /surah/:surah-number/index.json
```

#### Example
```
GET /surah/112/index.json
```

#### Response Example
```json
{
  "verses": [
    {
      "id": 6222,
      "number": 1,
      "verse_key": "112:1",
      "hizb_number": 60,
      "rub_el_hizb_number": 240,
      "ruku_number": 556,
      "manzil_number": 7,
      "sajdah_number": null,
      "page_number": 604,
      "juz_number": 30,
      "text": "قُلۡ هُوَ ٱللَّهُ أَحَدٌ"
    }
  ]
}
```

### 3. Get Single Verse

Retrieves a specific verse from a surah.

```
GET /surah/:surah-number/:verse-number.json
```

#### Example
```
GET /surah/112/1.json
```

#### Response Example
```json
{
  "id": 6222,
  "number": 1,
  "verse_key": "112:1",
  "hizb_number": 60,
  "rub_el_hizb_number": 240,
  "ruku_number": 556,
  "manzil_number": 7,
  "sajdah_number": null,
  "page_number": 604,
  "juz_number": 30,
  "text": "قُلۡ هُوَ ٱللَّهُ أَحَدٌ"
}
```

### 4. Get Surah Information

Retrieves  information about a specific surah.

```
GET /surah/:surah-number/info.json
```

#### Example
```
GET /surah/112/info.json
```

#### Response Example
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
    "en": "meccan"
  },
  "revelation_order": 22,
  "bismillah_pre": true,
  "verses_count": 4,
  "words_count": 15,
  "letters_count": 47,
  "pages": [604, 604],
  "name_simple": "Al-Ikhlas",
  "name_complex": "Al-'Ikhlāş",
  "name_arabic": "الإخلاص",
  "translated_name": "The Sincerity",
  "start_page": 604,
  "end_page": 604
}
```

### 5. Get Surah About Information (English)

Retrieves detiled information about a surah in English.

```
GET /surah/:surah-number/about.en.json
```

#### Example
```
GET /surah/112/about.en.json
```

#### Response Example
```json
{
  "chapter_info": {
    "id": 112,
    "chapter_id": 112,
    "language_name": "english",
    "short_text": "Al-Ikhlas is not merely the name of this Surah but also the title of its contents, for it deals exclusively with Tauhid...",
    "source": "Sayyid Abul Ala Maududi - Tafhim al-Qur'an - The Meaning of the Quran",
    "text": "long text"
  }
}
```

### 6. Get Combined Surah Info with Verses

Retrieves both surah information and its verses in a single request.

```
GET /surah/:surah-number/index.info.json
```

#### Example
```
GET /surah/112/index.info.json
```

#### Response Example
```json
{
  "number": 112,
  "revelation_order": 22,
  "bismillah_pre": true,
  "verses_count": 4,
  "words_count": 15,
  "letters_count": 47,
  "name_simple": "Al-Ikhlas",
  "name_complex": "Al-'Ikhlāş",
  "name_arabic": "الإخلاص",
  "translated_name": "The Sincerity",
  "start_page": 604,
  "end_page": 604,
  "revelation_place": {
    "ar": "مكية",
    "en": "meccan"
  },
  "name": {
    "ar": "الإخلاص",
    "en": "Sincerity",
    "transliteration": "Al-Ikhlas"
  },
  "juz": [
    {
      "index": "30",
      "verse": {
        "start": "1",
        "end": "4"
      }
    }
  ],
  "verses": {
    "0": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
    "1": "قُلْ هُوَ ٱللَّهُ أَحَدٌ",
    "2": "ٱللَّهُ ٱلصَّمَدُ",
    "3": "لَمْ يَلِدْ وَلَمْ يُولَدْ",
    "4": "وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ"
  }
}
```
