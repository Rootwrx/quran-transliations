# Quran Translations
### 1. Get All Available Translations

Retrieves a list of all available translations with their details.

```
GET /translations/translations.json
```

#### Response Example
```json
{
  "translations": [
    {
      "key": "english_rwwad",
      "direction": "ltr",
      "language_iso_code": "en",
      "version": "1.0.15",
      "last_update": 1711763763,
      "title": "English Translation - Rowwad Translation Center",
      "description": "Translation of the Quran meanings into Englsih by Rowwad Translation Center in cooperation with Islamhouse.com"
    },
    {
      "key": "english_saheeh",
      "direction": "ltr",
      "language_iso_code": "en",
      "version": "1.1.1",
      "last_update": 1658318019,
      "title": "English Translation - Saheeh International",
      "description": "Translation of the Quran meanings into English - Saheeh International - Al-Muntada Al-Islami (Islamic Forum)"
    },
    {
      "key": "chinese_makin",
      "direction": "ltr",
      "language_iso_code": "zh",
      "version": "1.0.2",
      "last_update": 1662501318,
      "title": "Chinese Translation - Muhammad Makin",
      "description": "Translation of the Quran meanings into Chinese by Muhammad Makin. Corrected by supervision of Rowwad Translation Center. The original translation is available for suggestions, continuous evaluation and development."
    }
  ]
}
```

### 2. Get Available Languages

Retrieves a list of all languages for which translations are available.

```
GET /translations/languages.json
```

#### Response Example
```json
{
  "languages": [
    "en",
    "fr",
    "es",
    "pt",
    "de",
    "nl",
    "tr",
    "az",
    "mk",
    "sq",
    "bs",
    "sr",
    "lt",
    "uz",
    "tg",
    "ky",
    "id",
    "tl"
  ]
}
```

### 3. Get Language ISO Codes

Retrieves a mapping between language names and their ISO codes, and vice versa.

```
GET /translations/isocodes.json
```

#### Response Example
```json
{
  "languages_isocodes": {
    "arabic": "ar",
    "english": "en",
    "french": "fr",
    "indonesian": "id",
    "bosnian": "bs",
    "spanish": "es",
    "russian": "ru"
  },
  "isocodes_languages": {
    "ar": "arabic",
    "en": "english",
    "fr": "french",
    "id": "indonesian",
    "bs": "bosnian",
    "es": "spanish",
    "ru": "russian"
  }
}
```

### 4. get info about default translation version
/translations/:lang-code/info.json

#### Example 
/translations/zh/inf.json

### Response Example
```json
{
  "key": "chinese_makin",
  "direction": "ltr",
  "language_iso_code": "zh",
  "version": "1.0.2",
  "last_update": 1662501318,
  "title": "Chinese Translation - Muhammad Makin",
  "description": "Translation of the Quran meanings into Chinese by Muhammad Makin. Corrected by supervision of Rowwad Translation Center. The original translation is available for suggestions, continuous evaluation and development."
}
```
### 4. Get Translation for a Surah in default translation version

Retrieves a specific translation for a surah.

```
GET /translations/:lang-code/:surah-number.json
```

### Example 
```
GET /translations/zh/1/index.json 
```
```json
{
  "verses": [
    {
      "id": 1,
      "verse_number": 1,
      "page_number": 1,
      "verse_key": "1:1",
      "juz_number": 1,
      "hizb_number": 1,
      "rub_el_hizb_number": 1,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
      "translation": "奉至仁至慈的安拉之名",
      "footnotes": ""
    },
    {
      "id": 7,
      "verse_number": 7,
      "page_number": 1,
      "verse_key": "1:7",
      "juz_number": 1,
      "hizb_number": 1,
      "rub_el_hizb_number": 1,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ غَيۡرِ ٱلۡمَغۡضُوبِ عَلَيۡهِمۡ وَلَا ٱلضَّآلِّينَ",
      "translation": "你所祐助者的路，不是受谴怒者的路，也不是迷误者的路。",
      "footnotes": ""
    }
  ]
}
```

### Get a minified surah for a specifc language 
/translations/:lang-code/:surah-number/index.min.json
### Example 
```
GET /translations/zh/1/index.min.json
```
```json
{
  "verses": [
    {
      "number": "1",
      "arabic_text": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
      "translation": "奉至仁至慈的安拉之名"
    },
   ...,
    {
      "number": "6",
      "arabic_text": "ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ",
      "translation": "求你引领我们上正路，"
    },
    {
      "number": "7",
      "arabic_text": "صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ غَيۡرِ ٱلۡمَغۡضُوبِ عَلَيۡهِمۡ وَلَا ٱلضَّآلِّينَ",
      "translation": "你所祐助者的路，不是受谴怒者的路，也不是迷误者的路。"
    }
  ]
}
```
### 5. Get Translation for a Verse 

Retrieves a specific translation for a verse.

```
GET /translations/:lang-code/:surah-number/:verse-number.json
```

### Example 
```
GET /translats/yo/1/1.json
```
### Response Example 
```json
{
  "id": 1,
  "verse_number": 1,
  "page_number": 1,
  "verse_key": "1:1",
  "juz_number": 1,
  "hizb_number": 1,
  "rub_el_hizb_number": 1,
  "sajdah_type": null,
  "sajdah_number": null,
  "text": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
  "translation": "Ní orúkọ Allāhu, Àjọkẹ́-ayé, Àṣàkẹ́-ọ̀run.[1]",
  "footnotes": "1. Sūratun Mọkkiyyah túmọ̀ sí sūrah tí ó sọ̀kalẹ̀ ṣíwájú Hijrah. Bákan náà, sūratun Mọdaniyyah túmọ̀ sí sūrah tí ó sọ̀kalẹ̀ lẹ́yìn Hijrah."
}
```
### Translation Versions

Get list all available translaitons versions  in a language 

```
Get /translations/list/:lang-code/info.json
```
### Example 
```
GEt /translations/list/vi/info.json
```
```json
{
  "translations": [
    {
      "key": "vietnamese_rwwad",
      "direction": "ltr",
      "language_iso_code": "vi",
      "version": "1.0.7",
      "last_update": 1714305616,
      "title": "Vietnamese translation - Rowwad Translation Center",
      "description": "Translation of the Quran meanings into Vietnamese by Rowwad Translation Center with cooperation with Islamhouse.com"
    }
  ]
}
```

### Geting Surah,Verse

### Get translation of a surah in translation version 

```
GET /translations/:lang-code/:translation-version/surah/index.json
```
### Example
```
GET /translations/ug/uyghur_saleh/surah/110/index.json
```
```json
{
  "verses": [
    {
      "id": 1,
      "verse_number": 1,
      "page_number": 603,
      "verse_key": "110:1",
      "juz_number": 30,
      "hizb_number": 60,
      "rub_el_hizb_number": 240,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "إِذَا جَآءَ نَصۡرُ ٱللَّهِ وَٱلۡفَتۡحُ",
      "translation": " ئاللاھنىڭ ياردىمى ۋە غەلىبىسى كەلگەن ۋە ئاللاھنىڭ دىنىغا كىشىلەرنىڭ توپ ـ توپ بولۇپ كىرگەنلىكىنى كۆرگىنىڭدە[1ـ2]،",
      "footnotes": null
    },
    {
      "id": 2,
      "verse_number": 2,
      "page_number": 603,
      "verse_key": "110:2",
      "juz_number": 30,
      "hizb_number": 60,
      "rub_el_hizb_number": 240,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "وَرَأَيۡتَ ٱلنَّاسَ يَدۡخُلُونَ فِي دِينِ ٱللَّهِ أَفۡوَاجٗا",
      "translation": " ئاللاھنىڭ ياردىمى ۋە غەلىبىسى كەلگەن ۋە ئاللاھنىڭ دىنىغا كىشىلەرنىڭ توپ ـ توپ بولۇپ كىرگەنلىكىنى كۆرگىنىڭدە[1ـ2]،",
      "footnotes": null
    },
    {
      "id": 3,
      "verse_number": 3,
      "page_number": 603,
      "verse_key": "110:3",
      "juz_number": 30,
      "hizb_number": 60,
      "rub_el_hizb_number": 240,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "فَسَبِّحۡ بِحَمۡدِ رَبِّكَ وَٱسۡتَغۡفِرۡهُۚ إِنَّهُۥ كَانَ تَوَّابَۢا",
      "translation": "رەببىڭغا تەسبىھ ئېيتقىن، ھەمدى ئېيتقىن ۋە ئۇنىڭدىن مەغپىرەت تىلىگىن. ئاللاھ ھەقىقەتەن تەۋبىنى بەك قوبۇل قىلغۇچىدۇر[3].",
      "footnotes": null
    }
  ]
}
```

Get a verse in a language in a specifc version
```
GET /translations/:lang-code/:translation-version/surah/:surah-number/:verse-number.json
```

### Example
```
GET /translations/ug/uyghur_saleh/surah/110/2.json
```
```json
{
  "id": 2,
  "verse_number": 2,
  "page_number": 603,
  "verse_key": "110:2",
  "juz_number": 30,
  "hizb_number": 60,
  "rub_el_hizb_number": 240,
  "sajdah_type": null,
  "sajdah_number": null,
  "text": "وَرَأَيۡتَ ٱلنَّاسَ يَدۡخُلُونَ فِي دِينِ ٱللَّهِ أَفۡوَاجٗا",
  "translation": " ئاللاھنىڭ ياردىمى ۋە غەلىبىسى كەلگەن ۋە ئاللاھنىڭ دىنىغا كىشىلەرنىڭ توپ ـ توپ بولۇپ كىرگەنلىكىنى كۆرگىنىڭدە[1ـ2]،",
  "footnotes": null
}
```

Get info about  a  translation version
```
GET /translations/:lang-code/:translation-version/info.json
```
### Exmaple 
```
GET /translations/ja/japanese_saeedsato/info.json
```
```json
{
  "key": "japanese_saeedsato",
  "direction": "ltr",
  "language_iso_code": "ja",
  "version": "1.0.11",
  "last_update": 1730715411,
  "title": "Japanese translation - Saeed Sato",
  "description": "Translation of the Quran meanings into Japanese by Saeed Sato. printed in 1440 H."
}
```

## Response Fields

### Translation Fields
- `key`: Unique identifier for the translation
- `direction`: Text direction (ltr for left-to-right, rtl for right-to-left)
- `language_iso_code`: ISO code for the language (e.g., "en" for English)
- `version`: Version number of the translation
- `last_update`: Timestamp of the last update
- `title`: Title of the translation
- `description`: Description of the translation

### Language Fields
- `languages`: Array of language ISO codes
- `languages_isocodes`: Mapping from language names to ISO codes
- `isocodes_languages`: Mapping from ISO codes to language names


