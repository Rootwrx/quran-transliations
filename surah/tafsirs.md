
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
      "text": "and you see people entering God’s religion that is to say Islam in throngs in large droves after they had been entering one by one — this was after the conquest of Mecca when the Arabs from all corners of the land came to him willingly in obedience to his command —"
    },
    {
      "ayah": 3,
      "surah": 110,
      "text": "then glorify with praise of your Lord that is continuously praising Him and seek forgiveness from Him; for verily He is ever ready to relent. The Prophet s after this sūra had been revealed would frequently repeat the words subhāna’Llāhi wa bi-hamdihi ‘Glory and praise be to God’ and astaghfiru’Llāha wa-atūbu ilayhi ‘I seek forgiveness from God and I repent to Him’; with the revelation of this final sūra he realised that his end was near. The victory over Mecca was in Ramadān of year 8; the Prophet s passed away in Rabī‘ I of the year 10."
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

## Notes
- All tafsirs are provided in their respective languages
- The API is static and doesn't require authentication
- All responses are in JSON format
- Tafsirs provide detailed explanations of Quranic verses
- Some tafsirs may be abridged versions of longer works
- The API supports a wide range of languages to make Quranic interpretations accessible to people worldwide
- Each language has a default tafsir, but specific tafsir versions can be accessed using their slugs 