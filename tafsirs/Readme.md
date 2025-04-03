## Quran Tafsirs API

### Available Languages

The Tafsirs API supports the following languages:

- Arabic (ar)
- Bengali (bn)
- English (en)
- Kurdish (kurd)
- Russian (ru)
- Urdu (ur)

### 1. Get All Available Tafsirs

Retrieves a list of all available tafsir editions and their languages.

**Endpoint:** `GET /tafsirs/editions.json`

**Response:**

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

### 2. Get Default Tafsir for a Surah

Retrieves the default tafsir for a specific surah in a given language.

**Endpoint:** `GET /tafsirs/:lang-code/:surah-number.json`

**Example Request:**

```
GET /tafsirs/en/110.json
```

**Response:**

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

### 3. Get Default Tafsir for a Verse

Retrieves the default tafsir for a specific verse in a given language.

**Endpoint:** `GET /tafsirs/:lang-code/:surah-number/:verse-number.json`

**Example Request:**

```
GET /tafsirs/ru/1/1.json
```

**Response:**

```json
{
  "text": "Это означает: я начинаю во имя Аллаха. Из лексического анализа этого словосочетания ясно, что подразумеваются все прекрасные имена Всевышнего Господа. Аллах - одно из этих имен, означающее «Бог, Которого обожествляют и Которому поклоняются, Единственный, Кто заслуживает поклонения в силу Своих божественных качеств - качеств совершенства и безупречности». Прекрасные имена Милостивый и Милосердный свидетельствуют о Его великом милосердии, объемлющем всякую вещь и всякую тварь. Милосердия Аллаха в полной мере будут удостоены Его богобоязненные рабы, которые следуют путем Божьих пророков и посланников. А все остальные творения получат лишь часть Божьей милости. Следует знать, что все праведные богословы единодушно говорили о необходимости веры в Аллаха и Его божественные качества. Господь - Милостивый и Милосердный, то есть обладает милосердием, которое проявляется на Его рабах. Все блага и щедроты являются одним из многочисленных проявлений Его милости и сострадания. То же самое можно сказать и об остальных именах Аллаха. Он всеведущ, то есть обладает знанием обо всем сущем. Он всемогущ, то есть обладает могуществом и властен над всякой тварью.",
  "ayah": 1,
  "surah": 1
}
```

### 4. Get Tafsir versions for a language

Retrieves a list of all tafsir versions available in a specific language.

**Endpoint:** `GET /tafsirs/:lang-code/info.json`

**Example Request:**

```
GET /tafsirs/ar/info.json
```

**Response:**

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

### 5. Get Specific Tafsir Version

Retrieves a specific tafsir version for a surah or verse.

#### 5.1 Get a Surah in a Specific Tafsir Version

Retrieves a specific tafsir version for a surah.

**Endpoint:** `GET /tafsirs/:lang-code/:tafsir-version/:surah-number.json`

**Request Example:**

```
GET /tafsirs/en/al-jalalayn/110.json
```

**Response:**

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

#### 5.2 Get a Verse in a Specific Tafsir Version

Retrieves a specific tafsir version for a verse.

**Endpoint:** `GET /tafsirs/:lang-code/:tafsir-version/:surah-number/:verse-number.json`

**Example Request:**

```
GET /tafsirs/en/al-jalalayn/110/1.json
```

**Response:**

```json
{
  "surah": 110,
  "ayah": 1,
  "text": "When the help of God for His Prophet s against his enemies comes together with victory the victory over Mecca"
}
```

## Available Tafsirs

| ID  | Tafsir Name                            | Author                                 | Language | Source       |
| --- | -------------------------------------- | -------------------------------------- | -------- | ------------ |
| 169 | Tafsir Ibn Kathir (abridged)           | Hafiz Ibn Kathir                       | English  | quran.com    |
| 168 | Maarif-ul-Quran                        | Mufti Muhammad Shafi                   | English  | quran.com    |
| 817 | Tazkirul Quran                         | Maulana Wahid Uddin Khan               | English  | quran.com    |
| 109 | Kashf Al-Asrar Tafsir                  | Kashf Al-Asrar Tafsir                  | English  | altafsir.com |
| 108 | Al Qushairi Tafsir                     | Al Qushairi Tafsir                     | English  | altafsir.com |
| 107 | Kashani Tafsir                         | Kashani Tafsir                         | English  | altafsir.com |
| 93  | Tafsir al-Tustari                      | Tafsir al-Tustari                      | English  | altafsir.com |
| 86  | Asbab Al-Nuzul by Al-Wahidi            | Asbab Al-Nuzul by Al-Wahidi            | English  | altafsir.com |
| 73  | Tanwîr al-Miqbâs min Tafsîr Ibn 'Abbâs | Tanwîr al-Miqbâs min Tafsîr Ibn 'Abbâs | English  | altafsir.com |
| 74  | Al-Jalalayn                            | Al-Jalalayn                            | English  | altafsir.com |
| 14  | Tafsir Ibn Kathir                      | Hafiz Ibn Kathir                       | Arabic   | quran.com    |
| 91  | Tafseer Al Saddi                       | Saddi                                  | Arabic   | quran.com    |
| 94  | Tafseer Al-Baghawi                     | Baghawy                                | Arabic   | quran.com    |
| 92  | Tafseer Tanwir al-Miqbas               | Tanweer                                | Arabic   | quran.com    |
| 93  | Tafsir Al Wasit                        | Waseet                                 | Arabic   | quran.com    |
| 15  | Tafsir al-Tabari                       | Tabari                                 | Arabic   | quran.com    |
| 16  | Tafsir Muyassar                        | المیسر                                 | Arabic   | quran.com    |
| 90  | Tafseer Al Qurtubi                     | Qurtubi                                | Arabic   | quran.com    |
| 381 | Tafsir Fathul Majid                    | AbdulRahman Bin Hasan Al-Alshaikh      | Bengali  | quran.com    |
| 164 | Tafseer ibn Kathir                     | Tawheed Publication                    | Bengali  | quran.com    |
| 165 | Tafsir Ahsanul Bayaan                  | Bayaan Foundation                      | Bengali  | quran.com    |
| 166 | Tafsir Abu Bakr Zakaria                | King Fahd Quran Printing Complex       | Bengali  | quran.com    |
| 157 | Fi Zilal al-Quran                      | Sayyid Ibrahim Qutb                    | Urdu     | quran.com    |
| 160 | Tafsir Ibn Kathir                      | Hafiz Ibn Kathir                       | Urdu     | quran.com    |
| 159 | Tafsir Bayan ul Quran                  | Dr. Israr Ahmad                        | Urdu     | quran.com    |
| 818 | Tazkirul Quran                         | Maulana Wahid Uddin Khan               | Urdu     | quran.com    |
| 170 | Tafseer Al Saddi                       | Saddi                                  | Russian  | quran.com    |
| 804 | Rebar Kurdish Tafsir                   | Rebar Kurdish Tafsir                   | Kurdish  | quran.com    |

## Language Distribution

The Tafsirs are available in the following languages:

- Arabic: 8 Tafsirs
- English: 10 Tafsirs
- Bengali: 4 Tafsirs
- Urdu: 4 Tafsirs
- Russian: 1 Tafsir
- Kurdish: 1 Tafsir
