## Quran Translations API

### 1. Get All Available Translations

Retrieves a list of all available translations with their details.

**Endpoint:** `GET /translations/translations.json`

**Response:**

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

**Endpoint:** `GET /translations/languages.json`

**Response:**

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

**Endpoint:** `GET /translations/isocodes.json`

**Response:**

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

### 4. Get Info About Default Translation Version

Retrieves information about the default translation version for a specific language.

**Endpoint:** `GET /translations/:lang-code/info.json`

**Example Request:**

```
GET /translations/zh/info.json
```

**Response:**

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

### 5. Get Translation for a Surah in Default Translation Version

Retrieves a translation of a specific surah in the default version for a language.

**Endpoint:** `GET /translations/:lang-code/:surah-number/index.json`

**Example Request:**

```
GET /translations/zh/1/index.json
```

**Response:**

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
      "text": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
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
      "text": "صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ غَيۡرِ ٱلۡمَغۡضُوبِ عَلَيۡهِمۡ وَلَا ٱلضَّآلِّينَ",
      "translation": "你所祐助者的路，不是受谴怒者的路，也不是迷误者的路。",
      "footnotes": ""
    }
  ]
}
```

### 6. Get a Minified Surah for a Specific Language

Retrieves a minified translation of a surah for a specific language.

**Endpoint:** `GET /translations/:lang-code/:surah-number/index.min.json`

**Example Request:**

```
GET /translations/zh/1/index.min.json
```

**Response:**

```json
{
  "verses": [
    {
      "number": "1",
      "arabic_text": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
      "translation": "奉至仁至慈的安拉之名"
    },
    {
      "number": "6",
      "arabic_text": "ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ",
      "translation": "求你引领我们上正路，"
    },
    {
      "number": "7",
      "arabic_text": "صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ غَيۡرِ ٱلۡمَغۡضُوبِ عَلَيۡهِمۡ وَلَا ٱلضَّآلِّينَ",
      "translation": "你所祐助者的路，不是受谴怒者的路，也不是迷误者的路。"
    }
  ]
}
```

### 7. Get Translation for a Verse

Retrieves a translation of a specific verse in the default version for a language.

**Endpoint:** `GET /translations/:lang-code/:surah-number/:verse-number.json`

**Example Request:**

```
GET /translations/yo/1/1.json
```

**Response:**

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
  "text": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
  "translation": "Ní orúkọ Allāhu, Àjọkẹ́-ayé, Àṣàkẹ́-ọ̀run.[1]",
  "footnotes": "1. Sūratun Mọkkiyyah túmọ̀ sí sūrah tí ó sọ̀kalẹ̀ ṣíwájú Hijrah. Bákan náà, sūratun Mọdaniyyah túmọ̀ sí sūrah tí ó sọ̀kalẹ̀ lẹ́yìn Hijrah."
}
```

### 8. Get List of All Available Translation Versions in a Language

Retrieves a list of all available translation versions for a specific language.

**Endpoint:** `GET /translations/list/:lang-code/info.json`

**Example Request:**

```
GET /translations/list/vi/info.json
```

**Response:**

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

### 9. Get Translation of a Surah in a Specific Translation Version

Retrieves a translation of a surah in a specific translation version.

**Endpoint:** `GET /translations/:lang-code/:translation-version/surah/:surah-number/index.json`

**Example Request:**

```
GET /translations/ug/uyghur_saleh/surah/110/index.json
```

**Response:**

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
      "text": "إِذَا جَآءَ نَصۡرُ ٱللَّهِ وَٱلۡفَتۡحُ",
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
      "text": "وَرَأَيۡتَ ٱلنَّاسَ يَدۡخُلُونَ فِي دِينِ ٱللَّهِ أَفۡوَاجٗا",
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
      "text": "فَسَبِّحۡ بِحَمۡدِ رَبِّكَ وَٱسۡتَغۡفِرۡهُۚ إِنَّهُۥ كَانَ تَوَّابَۢا",
      "translation": "رەببىڭغا تەسبىھ ئېيتقىن، ھەمدى ئېيتقىن ۋە ئۇنىڭدىن مەغپىرەت تىلىگىن. ئاللاھ ھەقىقەتەن تەۋبىنى بەك قوبۇل قىلغۇچىدۇر[3].",
      "footnotes": null
    }
  ]
}
```

### 10. Get a Verse in a Specific Language and Version

Retrieves a translation of a specific verse in a specific translation version.

**Endpoint:** `GET /translations/:lang-code/:translation-version/surah/:surah-number/:verse-number.json`

**Example Request:**

```
GET /translations/ug/uyghur_saleh/surah/110/2.json
```

**Response:**

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
  "text": "وَرَأَيۡتَ ٱلنَّاسَ يَدۡخُلُونَ فِي دِينِ ٱللَّهِ أَفۡوَاجٗا",
  "translation": " ئاللاھنىڭ ياردىمى ۋە غەلىبىسى كەلگەن ۋە ئاللاھنىڭ دىنىغا كىشىلەرنىڭ توپ ـ توپ بولۇپ كىرگەنلىكىنى كۆرگىنىڭدە[1ـ2]،",
  "footnotes": null
}
```

### 11. Get Info About a Translation Version

Retrieves information about a specific translation version.

**Endpoint:** `GET /translations/:lang-code/:translation-version/info.json`

**Example Request:**

```
GET /translations/ja/japanese_saeedsato/info.json
```

**Response:**

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

## Available Quran Translations

| Language    | Translation Key       | Title                                                                   | Version | Last Update | Direction |
| ----------- | --------------------- | ----------------------------------------------------------------------- | ------- | ----------- | --------- |
| English     | english_rwwad         | English Translation - Rowwad Translation Center                         | 1.0.15  | 2024-03-30  | LTR       |
| English     | english_saheeh        | English Translation - Saheeh International                              | 1.1.1   | 2022-07-20  | LTR       |
| English     | english_hilali_khan   | English Translation - Hilali and Khan                                   | 1.1.1   | 2025-01-15  | LTR       |
| French      | french_rashid         | French Translation - Rashid Maash                                       | 1.0.1   | 2024-07-05  | LTR       |
| French      | french_montada        | French Translation - Noor International Center                          | 1.0.0   | 2018-10-10  | LTR       |
| French      | french_hameedullah    | French Translation - Muhammad Hamidullah                                | 1.0.1   | 2022-01-10  | LTR       |
| Spanish     | spanish_montada_eu    | Spanish Translation - Noor International Center                         | 1.0.0   | 2018-10-08  | LTR       |
| Spanish     | spanish_garcia        | Spanish Translation - Isa Garcia                                        | 1.0.1   | 2024-06-20  | LTR       |
| Spanish     | spanish_montada_latin | Spanish Translation (Latin America) - Noor International                | 1.0.0   | 2018-10-08  | LTR       |
| Portuguese  | portuguese_nasr       | Portuguese Translation - Helmy Nasr                                     | 1.3.2   | 2023-04-15  | LTR       |
| German      | german_bubenheim      | German Translation - Bubenheim                                          | 1.1.4   | 2025-02-03  | LTR       |
| Dutch       | dutch_center          | Dutch translation                                                       | 2.0.6   | 2024-05-25  | LTR       |
| Turkish     | turkish_rwwad         | Turkish translation - Rowwad Tanslation Center                          | 1.0.1   | 2024-05-14  | LTR       |
| Turkish     | turkish_shaban        | Turkish translation - Shaaban Britsh                                    | 1.1.0   | 2019-12-26  | LTR       |
| Turkish     | turkish_shahin        | Turkish Translation - Ali Ozek                                          | 1.0.0   | 2017-05-22  | LTR       |
| Azerbaijani | azeri_musayev         | Azerbaijani translation - Ali Khan Mosaiv                               | 1.0.4   | 2023-12-04  | LTR       |
| Macedonian  | macedonian_group      | Macedonian Translation                                                  | 1.0.1   | 2024-12-15  | LTR       |
| Albanian    | albanian_nahi         | Albanian Translation - Hasan Nahi                                       | 1.1.0   | 2019-12-22  | LTR       |
| Bosnian     | bosnian_rwwad         | Bosnian translation - Rowwad Translation Center                         | 2.0.4   | 2025-03-01  | LTR       |
| Bosnian     | bosnian_mihanovich    | Bosnian Translation - Muhammad Mihanovich                               | 1.1.0   | 2019-12-21  | LTR       |
| Serbian     | serbian_rwwad         | Serbian Translation - Rowwad Translation Center                         | 1.0.4   | 2024-04-01  | LTR       |
| Lithuanian  | lithuanian_rwwad      | Lithuanian Translation                                                  | 1.0.8   | 2024-07-23  | LTR       |
| Uzbek       | uzbek_rwwad           | Uzbek Translation - Rowwad Translation Center                           | 1.0.4   | 2023-10-31  | LTR       |
| Uzbek       | uzbek_mansour         | Uzbek translation - Alauddin Mansour                                    | 1.0.0   | 2017-03-25  | LTR       |
| Tajik       | tajik_arifi           | Tajik translation - Arfy                                                | 1.0.2   | 2024-04-23  | LTR       |
| Kyrgyz      | kyrgyz_hakimov        | Kyrgyz translation                                                      | 1.0.2   | 2024-02-20  | LTR       |
| Indonesian  | indonesian_sabiq      | Indonesian Translation - Sabeq Company                                  | 1.1.2   | 2022-05-26  | LTR       |
| Indonesian  | indonesian_affairs    | Indonesian Translation - Ministry of Islamic Affairs                    | 1.0.1   | 2021-04-04  | LTR       |
| Indonesian  | indonesian_complex    | Indonesian Translation - King Fahd Complex                              | 1.0.0   | 2018-04-19  | LTR       |
| Tagalog     | tagalog_rwwad         | Filipino (Tagalog) Translation                                          | 1.1.4   | 2025-02-05  | LTR       |
| Chinese     | chinese_suliman       | Chinese Translation - Mohammed Suleiman                                 | 1.0.7   | 2025-02-19  | LTR       |
| Chinese     | chinese_makin         | Chinese Translation - Muhammad Makin                                    | 1.0.2   | 2022-09-06  | LTR       |
| Uyghur      | uyghur_saleh          | Uyghur translation - Sh. Muhammad Saleh                                 | 1.0.0   | 2018-02-20  | RTL       |
| Japanese    | japanese_saeedsato    | Japanese translation - Saeed Sato                                       | 1.0.11  | 2024-11-04  | LTR       |
| Vietnamese  | vietnamese_rwwad      | Vietnamese translation - Rowwad Translation Center                      | 1.0.7   | 2024-04-28  | LTR       |
| Khmer       | khmer_cambodia        | Khmer translation                                                       | 1.0.2   | 2024-08-08  | LTR       |
| Persian     | persian_ih            | Persian Translation - Rowwad Translation Center                         | 1.1.2   | 2025-02-18  | RTL       |
| Kurdish     | kurdish_bamoki        | Kurdish Translation                                                     | 1.1.1   | 2023-02-16  | RTL       |
| Pashto      | pashto_rwwad          | Pashto Translation - Rowwad Translation Center                          | 1.0.1   | 2024-02-15  | RTL       |
| Urdu        | urdu_junagarhi        | Urdu Translation                                                        | 1.1.2   | 2021-11-29  | RTL       |
| Hindi       | hindi_omari           | Hindi Translation                                                       | 1.1.4   | 2023-01-30  | LTR       |
| Telugu      | telugu_muhammad       | Telugu translation - Abder-Rahim ibn Muhammad                           | 1.0.6   | 2024-02-20  | LTR       |
| Gujarati    | gujarati_omari        | Gujarati translation                                                    | 1.1.3   | 2025-02-27  | LTR       |
| Malayalam   | malayalam_kunhi       | Malayalam translation - Abdul-Hamid Haidar Al-Madany and Kanhi Muhammad | 1.0.3   | 2021-05-30  | LTR       |
| Kannada     | kannada_hamza         | Kannada translation                                                     | 1.0.3   | 2024-03-17  | LTR       |
| Assamese    | assamese_rafeeq       | Assamese translation                                                    | 1.0.5   | 2024-06-07  | LTR       |
| Punjabi     | punjabi_arif          | Bunjabi translation                                                     | 1.0.0   | 2022-10-26  | LTR       |
| Tamil       | tamil_omar            | Tamil Translation - Omar Sharif                                         | 1.0.2   | 2022-12-13  | LTR       |
| Tamil       | tamil_baqavi          | Tamil Translation - Abdulhamid Albaqoi                                  | 1.0.1   | 2021-01-07  | LTR       |
| Sinhalese   | sinhalese_mahir       | Sinhalese translation                                                   | 1.0.5   | 2024-02-22  | LTR       |
| Swahili     | swahili_barawani      | Swahili translation - Ali Muhsen Alberwany                              | 1.0.0   | 2021-03-09  | LTR       |
| Somali      | somali_yacob          | Somali translation - Jacob                                              | 1.0.18  | 2025-02-06  | LTR       |
| Amharic     | amharic_sadiq         | Amharic translation                                                     | 1.1.1   | 2023-12-04  | LTR       |
| Yoruba      | yoruba_mikail         | Yoruba translation                                                      | 1.0.7   | 2024-07-10  | LTR       |
| Hausa       | hausa_gummi           | Hausa language - Abu Bakr Jomy                                          | 1.2.1   | 2021-01-07  | LTR       |
| Oromo       | oromo_ababor          | Oromo translation                                                       | 1.0.1   | 2023-08-01  | LTR       |
| Afar        | afar_hamza            | Afar translation                                                        | 1.0.1   | 2024-05-22  | LTR       |
| N'ko        | ankobambara_dayyan    | N'ko translation - Baba Mamadi                                          | 1.0.4   | 2024-08-05  | RTL       |
| Kinyarwanda | kinyarwanda_assoc     | Kinyarwanda Translation                                                 | 1.0.4   | 2024-03-12  | LTR       |
| Ikirundi    | ikirundi_gehiti       | (No title available)                                                    | 1.0.4   | 2024-11-24  | LTR       |
| Moore       | moore_rwwad           | (No title available)                                                    | 1.0.1   | 2024-06-05  | LTR       |
| Ashanti     | asante_harun          | Ashanti Translation                                                     | 1.0.3   | 2023-08-15  | LTR       |
| Lingala     | lingala_zakaria       | Lingala translation                                                     | 1.0.0   | 2021-09-27  | LTR       |
