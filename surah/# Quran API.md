# Quran,Tafsirs and Translations static  API



## Endpoints

### 1. Get All Surahs Information

Retrieves comprehensive information about all chapters (surahs) of the Quran.

**Endpoint:** `GET /surah/info.json`

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

**Endpoint:** `GET /surah/:surah-number/index.json`

**Example Request:**
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

**Endpoint:** `GET /surah/:surah-number/:verse-number.json`

**Example Request:**
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

**Endpoint:** `GET /surah/:surah-number/info.json`

**Example Request:**
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

**Endpoint:** `GET /surah/:surah-number/about.en.json`

**Example Request:**
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

**Endpoint:** `GET /surah/:surah-number/index.info.json`

**Example Request:**
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

## Quran Translations

### 1. Get All Available Translations

Retrieves a list of all available translations with their details.

**Endpoint:** `GET /translations/translations.json`

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



# Quran Tafsirs 
## Available Languages

The Tafsirs API supports the following languages:
- Arabic (ar)
- Bengali (bn)
- English (en)
- Kurdish (kurd)
- Russian (ru)
- Urdu (ur)

## Endpoints

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
### Getting Tafsir 
Each language has a default tafsir, but specific tafsir versions can be accessed using their slugs 
### 2. Get Default Tafsir for a Language

Each language has a default tafsir that is used when no specific tafsir version is specified.

#### Get a Surah in Default Tafsir

Retrieves the default tafsir for a specific surah in a given language.

```
GET /tafsirs/:lang-code/:surah-number.json
```

##### Example
```
GET /tafsirs/en/1.json
```

### Response Example
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
#### Get a Verse in Default Tafsir

Retrieves the default tafsir for a specific verse in a given language.

```
GET /tafsirs/:lang-code/:surah-number/:verse-number.json
```

##### Example
```
GET /tafsirs/ru/1/1.json
```
```json
{
  "text": "Это означает: я начинаю во имя Аллаха. Из лексического анализа этого словосочетания ясно, что подразумеваются все прекрасные имена Всевышнего Господа. Аллах - одно из этих имен, означающее «Бог, Которого обожествляют и Которому поклоняются, Единственный, Кто заслуживает поклонения в силу Своих божественных качеств - качеств совершенства и безупречности». Прекрасные имена Милостивый и Милосердный свидетельствуют о Его великом милосердии, объемлющем всякую вещь и всякую тварь. Милосердия Аллаха в полной мере будут удостоены Его богобоязненные рабы, которые следуют путем Божьих пророков и посланников. А все остальные творения получат лишь часть Божьей милости. Следует знать, что все праведные богословы единодушно говорили о необходимости веры в Аллаха и Его божественные качества. Господь - Милостивый и Милосердный, то есть обладает милосердием, которое проявляется на Его рабах. Все блага и щедроты являются одним из многочисленных проявлений Его милости и сострадания. То же самое можно сказать и об остальных именах Аллаха. Он всеведущ, то есть обладает знанием обо всем сущем. Он всемогущ, то есть обладает могуществом и властен над всякой тварью.",
  "ayah": 1,
  "surah": 1
}

```
### 3. Get Tafsir Versions in a Language

Retrieves a list of all tafsir versions available in a specific language.

```
GET /tafsirs/:lang-code/info.json
```

#### Example
```
GET /tafsirs/ar/info.json
```

#### Response Example
```json
[
 {
    "author_name": "المیسر",
    "id": 16,
    "language_name": "arabic",
    "name": "Tafsir Muyassar",
    "slug": "tafsir-muyassar",
    "source": "https://quran.com/"
  },
  {
    "author_name": "Qurtubi",
    "id": 90,
    "language_name": "arabic",
    "name": "Tafseer Al Qurtubi",
    "slug": "tafseer-al-qurtubi",
    "source": "https://quran.com/"
  }
]
```

### 4. Get Specific Tafsir Version

Retrieves a specific tafsir version for a surah or verse.

#### Get a Surah in a Specific Tafsir Version

Retrieves a specific tafsir version for a surah.

```
GET /tafsirs/:lang-code/:tafsir-version/:surah-number.json
```

##### Example
```
GET /tafsirs/en/al-jalalayn/110.json
```

##### Response Example
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

Retrieves a specific tafsir version for a verse.

```
GET /tafsirs/:lang-code/:tafsir-version/:surah-number/:verse-number.json
```

##### Example
```
GET /tafsirs/en/al-jalalayn/110/1.json
```

##### Response Example
```json
{
  "surah": 110,
  "ayah": 1,
  "text": "When the help of God for His Prophet s against his enemies comes together with victory the victory over Mecca"
}
```

## Response Fields

### Tafsir Edition Fields
- `author_name`: Name of the tafsir author
- `id`: Unique identifier for the tafsir
- `language_name`: Language of the tafsir
- `name`: Name of the tafsir
- `slug`: URL-friendly identifier for the tafsir
- `source`: Source of the tafsir

### Tafsir Content Fields
- `ayahs`: Array of verses with their tafsir
  - `ayah`: Verse number
  - `surah`: Surah number
  - `text`: Tafsir text for the verse

## URL Parameters

### Language Codes
- `ar`: Arabic
- `bn`: Bengali
- `en`: English
- `kurd`: Kurdish
- `ru`: Russian
- `ur`: Urdu

### Tafsir Versions
Each language has specific tafsir versions available. The version is specified by the `slug` parameter in the URL.

#### English Tafsir Versions
- `al-jalalayn`: Tafsir Al-Jalalayn
- `tafisr-ibn-kathir`: Tafsir Ibn Kathir (abridged)
- `tafsir-maarif-ul-quran`: Maarif-ul-Quran

#### Arabic Tafsir Versions
- `tafisr-ibn-kathir`: Tafsir Ibn Kathir
- `tafisr-al-muyassar`: Tafsir Al-Muyassar
- `tafisr-al-mukhtasar`: Tafsir Al-Mukhtasar

#### Other Language Tafsir Versions
Each language has its own set of available tafsir versions. Use the `/tafsirs/:lang-code/index.json` endpoint to get a complete list of available tafsir versions for a specific language.

