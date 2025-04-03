# Quran, Tafsirs and Translations Static API

### Base URLs -

1. JS Delivr: `https://cdn.jsdelivr.net/gh/Rootwrx/quran-api@master`
2. Git Hack: `https://rawcdn.githack.com/Rootwrx/quran-api/6865286890f2bdd6c3829bd5683b620b484c919f`
3. Staticaly: `https://cdn.statically.io/gh/Rootwrx/quran-api/master`
4. Github: `https://raw.githubusercontent.com/Rootwrx/quran-api/refs/heads/master`
5. Github  `https://raw.githubusercontent.com/Rootwrx/quran-api/master`
## Endpoints Overview

### Note 

fetch the api with base Urls + endpoints
#### Example in Javascript 
```js
const Base_Api_Url = "https://cdn.statically.io/gh/Rootwrx/quran-api/master";

fetch(Base_Api_Url+"/surah/1/1.json")
.then(r=>r.json())
.then(verse=> {
  console.log(verse.text)
})
```

### Quran Content

| Endpoint                                      | Description                               |
| --------------------------------------------- | ----------------------------------------- |
| `GET /surah/info.json`                        | Get information about all surahs          |
| `GET /surah/:surah-number/index.json`         | Get complete text of a specific surah     |
| `GET /surah/:surah-number/:verse-number.json` | Get a specific verse from a surah         |
| `GET /surah/:surah-number/info.json`          | Get information about a specific surah    |
| `GET /surah/:surah-number/about.en.json`      | Get information about a surah in English  |
| `GET /surah/:surah-number/index.info.json`    | Get both surah information and its verses |

### Translations

| Endpoint                                                                                   | Description                                               |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| `GET /translations/translations.json`                                                      | List all available translations                           |
| `GET /translations/languages.json`                                                         | List all available languages                              |
| `GET /translations/isocodes.json`                                                          | Get mapping between language names and ISO codes          |
| `GET /translations/:lang-code/info.json`                                                   | Get info about default translation version for a language |
| `GET /translations/:lang-code/:surah-number/index.json`                                    | Get translation of a surah in default version             |
| `GET /translations/:lang-code/:surah-number/index.min.json`                                | Get minified translation of a surah                       |
| `GET /translations/:lang-code/:surah-number/:verse-number.json`                            | Get translation of a specific verse                       |
| `GET /translations/list/:lang-code/info.json`                                              | List all translation versions in a language               |
| `GET /translations/:lang-code/:translation-version/surah/:surah-number/index.json`         | Get translation of a surah in specific version            |
| `GET /translations/:lang-code/:translation-version/surah/:surah-number/:verse-number.json` | Get translation of a verse in specific version            |
| `GET /translations/:lang-code/:translation-version/info.json`                              | Get info about a specific translation version             |

### Tafsirs

| Endpoint                                                                   | Description                            |
| -------------------------------------------------------------------------- | -------------------------------------- |
| `GET /tafsirs/editions.json`                                               | List all available tafsir editions     |
| `GET /tafsirs/:lang-code/:surah-number.json`                               | Get default tafsir for a surah         |
| `GET /tafsirs/:lang-code/:surah-number/:verse-number.json`                 | Get default tafsir for a verse         |
| `GET /tafsirs/:lang-code/info.json`                                        | List all tafsir versions in a language |
| `GET /tafsirs/:lang-code/:tafsir-version/:surah-number.json`               | Get specific tafsir for a surah        |
| `GET /tafsirs/:lang-code/:tafsir-version/:surah-number/:verse-number.json` | Get specific tafsir for a verse        |

## Quran Content API

### 1. Get All Surahs Information

Retrieves comprehensive information about all chapters (surahs) of the Quran.

**Endpoint:** `GET /surah/info.json`

**Response:**

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

**Endpoint:** `GET /surah/:surah-number/index.json`

**Example Request:**

```
GET /surah/112/index.json
```

**Response:**

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

**Endpoint:** `GET /surah/:surah-number/:verse-number.json`

**Example Request:**

```
GET /surah/112/1.json
```

**Response:**

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

Retrieves information about a specific surah.

**Endpoint:** `GET /surah/:surah-number/info.json`

**Example Request:**

```
GET /surah/112/info.json
```

**Response:**

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

Retrieves information about a surah in English.

**Endpoint:** `GET /surah/:surah-number/about.en.json`

**Example Request:**

```
GET /surah/112/about.en.json
```

**Response:**

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

**Endpoint:** `GET /surah/:surah-number/index.info.json`

**Example Request:**

```
GET /surah/112/index.info.json
```

**Response:**

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
