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

Retrieves detailed information about a specific surah.

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

Retrieves detailed information about a surah in English.

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

## Quran Tafsirs API

The Quran Tafsirs API provides access to various interpretations and commentaries of the Quran in multiple languages. Available languages include Arabic (ar), Bengali (bn), English (en), Kurdish (kurd), Russian (ru), and Urdu (ur).

### 1. Get All Available Tafsirs

Retrieves a list of all available tafsir editions and their languages.

```
GET /tafsirs/editions.json
```

#### Response Example
```json
[
  {
    "author_name": "AbdulRahman Bin Hasan Al-Alshaikh",
    "id": 381,
    "language_name": "bengali",
    "name": "Tafsir Fathul Majid",
    "slug": "tafisr-fathul-majid",
    "source": "https://quran.com/"
  },
  {
    "author_name": "Hafiz Ibn Kathir",
    "id": 169,
    "language_name": "english",
    "name": "Tafsir Ibn Kathir (abridged)",
    "slug": "tafisr-ibn-kathir",
    "source": "https://quran.com/"
  },
  {
    "author_name": "Saddi",
    "id": 170,
    "language_name": "russian",
    "name": "Tafseer Al Saddi",
    "slug": "ru-tafseer-al-saddi",
    "source": "https://quran.com/"
  },
  {
    "author_name": "Rebar Kurdish Tafsir",
    "id": 804,
    "language_name": "Kurdish",
    "name": "Rebar Kurdish Tafsir",
    "slug": "tafsir-rebar",
    "source": "https://quran.com/"
  }
]
```

### 2. Get Default Tafsir for a Language

Retrieves the default tafsir for a specific language.

#### Get a Surah in Default Tafsir
```
GET /tafsirs/:lang-code/:surah-number.json
```

#### Example
```
GET /tafsirs/en/1.json
```

#### Get a Verse in Default Tafsir
```
GET /tafsirs/:lang-code/:surah-number/:verse-number.json
```

#### Example
```
GET /tafsirs/en/1/1.json
```

### 3. Get Tafsir Versions in a Language

Retrieves a list of all tafsir versions available in a specific language.

```
GET /tafsirs/:lang-code/index.json
```

#### Example
```
GET /tafsirs/ar/index.json
```

#### Response Example
```json
[
  {
    "author_name": "Hafiz Ibn Kathir",
    "id": 169,
    "language_name": "english",
    "name": "Tafsir Ibn Kathir (abridged)",
    "slug": "tafisr-ibn-kathir",
    "source": "https://quran.com/"
  },
  {
    "author_name": "Mufti Muhammad Shafi",
    "id": 168,
    "language_name": "english",
    "name": "Maarif-ul-Quran",
    "slug": "tafsir-maarif-ul-quran",
    "source": "https://quran.com/"
  }
]
```

### 4. Get Specific Tafsir Version

Retrieves a specific tafsir version for a surah or verse.

#### Get a Surah in a Specific Tafsir Version
```
GET /tafsirs/:lang-code/:tafsir-version/:surah-number.json
```

#### Example
```
GET /tafsirs/en/al-jalalayn/110.json
```

#### Response Example
```json
{
  "ayahs": [
    {
      "ayah": 1,
      "surah": 110,
      "text": "When the help of God for His Prophet s against his enemies comes together with victory the victory over Mecca"
    },
    {
      "ayah": 2,
      "surah": 110,
      "text": "and you see people entering God's religion that is to say Islam in throngs in large droves after they had been entering one by one — this was after the conquest of Mecca when the Arabs from all corners of the land came to him willingly in obedience to his command —"
    },
    {
      "ayah": 3,
      "surah": 110,
      "text": "then glorify with praise of your Lord that is continuously praising Him and seek forgiveness from Him; for verily He is ever ready to relent. The Prophet s after this sūra had been revealed would frequently repeat the words subhāna'Llāhi wa bi-hamdihi 'Glory and praise be to God' and astaghfiru'Llāha wa-atūbu ilayhi 'I seek forgiveness from God and I repent to Him'; with the revelation of this final sūra he realised that his end was near. The victory over Mecca was in Ramadān of year 8; the Prophet s passed away in Rabī' I of the year 10."
    }
  ]
}
```

#### Get a Verse in a Specific Tafsir Version
```
GET /tafsirs/:lang-code/:tafsir-version/:surah-number/:verse-number.json
```

#### Example
```
GET /tafsirs/en/al-jalalayn/110/1.json
```

#### Response Example
```json
{
  "surah": 110,
  "ayah": 1,
  "text": "When the help of God for His Prophet s against his enemies comes together with victory the victory over Mecca"
}
```

## Response Fields

### Common Fields
- `number`: The surah number
- `name`: Object containing names in different languages
  - `ar`: Arabic name
  - `en`: English name
  - `transliteration`: Transliterated name
- `revelation_place`: Place of revelation
  - `ar`: Arabic text
  - `en`: English text
- `verses_count`: Total number of verses
- `words_count`: Total number of words
- `letters_count`: Total number of letters
- `pages`: Array of page numbers
- `start_page`: Starting page number
- `end_page`: Ending page number

### Verse Fields
- `id`: Unique identifier for the verse
- `number`: Verse number within the surah
- `verse_key`: Combined surah and verse number
- `hizb_number`: Hizb number
- `rub_el_hizb_number`: Rub el hizb number
- `ruku_number`: Ruku number
- `manzil_number`: Manzil number
- `sajdah_number`: Sajdah number (if applicable)
- `page_number`: Page number in the Mushaf
- `juz_number`: Juz number
- `text`: The actual text of the verse in Arabic

### Tafsir Fields
- `author_name`: Name of the tafsir author
- `id`: Unique identifier for the tafsir
- `language_name`: Language of the tafsir
- `name`: Name of the tafsir
- `slug`: URL-friendly identifier for the tafsir
- `source`: Source of the tafsir
- `ayahs`: Array of verses with their tafsir
  - `ayah`: Verse number
  - `surah`: Surah number
  - `text`: Tafsir text for the verse

## Notes
- All text is provided in Arabic script
- The API is static and doesn't require authentication
- All responses are in JSON format
- The API provides comprehensive information about the Quran's structure and content
- Tafsirs are available in multiple languages: Arabic (ar), Bengali (bn), English (en), Kurdish (kurd), Russian (ru), and Urdu (ur)
- Each language has a default tafsir, but specific tafsir versions can be accessed using their slugs 
