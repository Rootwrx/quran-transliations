
### Quran Text (Arabic) 

get info about all chapters 
/surah/info.json

get one surah of the quran
/surah/:surah-number/index.json
get info about one surah 
/surah/:surah-number/info.json
get story of the surah (english only) 
/surah/:surah-number/about.en.json
get verse of the Quran 
/surah/:surah-number/:verse-number.json
get surah info with verses 
/surah/:surah-number/index.info.json




### about translations section  
Avaiblabe Translation languages 
/translations/translations.json


get Avaiblabe languages 
/translations/languages.json

get isocodes of all languages
/translations/isocodes.json




### quran trasnaltions section 

default translation of quran in a specifc lanuage is   under 
/translations/:lang-code/  that contins surahs i.e /1/1.json for verse 1 of surah 1 
get surah for a specifc translation 
/translations/:lang-code/:surah-number/index.json


get a minified surah for a specifc translation 
/translations/:lang-code/:surah-number/index.min.json

get verse in a specifc translation  
/translations/:lang-code/:surah-number/:verse-number.json

get info about the default trasnaltion 
/translations/:lang-code/info.json


### Quran trasnaltions versions 

see Avaiblabe translations versions
/translations/translations.json

get a surah in a lanuage in a specific version 
/translations/:lang-code/:translation-version/surah/index.json

get a minifed surah in a lanuage in a specific version 
/translations/:lang-code/:translation-version/surah/:surah-number/index.min.json

et a verse in a language in a specifc version
/translations/:lang-code/:translation-version/surah/:surah-number/:verse-number.json


get info about a about a  translation version
/translations/:lang-code/:translation-version/info.json



get availbe translation versions in language 
/translations/translations/:lang-code/index.json




### Quran Tafsirs
get list of editions i.e availbe tafsirs and their languages
/tafsirs/editions.json
availbe lanuages
ar,bn,en,kurd,ru,ur



## default tafisr in a specific lanuage  is under /tafsirs/:lang-code/

get a  surah  in a default tafsir
/tafsirs/:lang-code/1.json

get a verse in default tafisr 
/tafsirs/:lang-code/:surah-number/:verse-number.json


get info about default tafsir  in lanuage 
/Tafsirs/:lang-code/info

### tafsirs  versions 


get a  surah  in a tafir version 
/tafsirs/:lang-code/:tafsir-version/info.json

get a verse in  tafisr  version 
/tafsirs/:lang-code/:surah-number/:verse-number.json


get info about  tafsir  in lanuage 
/Tafsirs/:lang-code/:tafsir-version/info.json














############ Examples 

### Quran Text (Arabic) 

get info about all chapters 
/surah/info.json

# response exmaple 
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
    "pages": [
      1,
      1
    ],
    "name_simple": "Al-Fatihah",
    "name_complex": "Al-Fātiĥah",
    "name_arabic": "الفاتحة",
    "translated_name": "The Opener",
    "start_page": 1,
    "end_page": 1
  },
  ...,
  ...,
  {
    "number": 114,
    "name": {
      "ar": "الناس",
      "en": "Mankind",
      "transliteration": "An-Nas"
    },
    "revelation_place": {
      "ar": "مكية",
      "en": "meccan"
    },
    "revelation_order": 21,
    "bismillah_pre": true,
    "verses_count": 6,
    "words_count": 20,
    "letters_count": 80,
    "pages": [
      604,
      604
    ],
    "name_simple": "An-Nas",
    "name_complex": "An-Nās",
    "name_arabic": "الناس",
    "translated_name": "Mankind",
    "start_page": 604,
    "end_page": 604
  }
]

get one surah of the quran
/surah/:surah-number/index.json

# example get surah al ikhlas
/surah/112/index.json

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
      "text": "قُلۡ هُوَ ٱللَّهُ أَحَدٌ"
    },
    {
      "id": 6223,
      "number": 2,
      "verse_key": "112:2",
      "hizb_number": 60,
      "rub_el_hizb_number": 240,
      "ruku_number": 556,
      "manzil_number": 7,
      "sajdah_number": null,
      "page_number": 604,
      "juz_number": 30,
      "text": "ٱللَّهُ ٱلصَّمَدُ"
    },
    {
      "id": 6224,
      "number": 3,
      "verse_key": "112:3",
      "hizb_number": 60,
      "rub_el_hizb_number": 240,
      "ruku_number": 556,
      "manzil_number": 7,
      "sajdah_number": null,
      "page_number": 604,
      "juz_number": 30,
      "text": "لَمۡ يَلِدۡ وَلَمۡ يُولَدۡ"
    },
    {
      "id": 6225,
      "number": 4,
      "verse_key": "112:4",
      "hizb_number": 60,
      "rub_el_hizb_number": 240,
      "ruku_number": 556,
      "manzil_number": 7,
      "sajdah_number": null,
      "page_number": 604,
      "juz_number": 30,
      "text": "وَلَمۡ يَكُن لَّهُۥ كُفُوًا أَحَدُۢ"
    }
  ]
}





get verse of the Quran 
/surah/:surah-number/:verse-number.json

# example surah ikhlas vere 1
/surah/112/1.json

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
  "text": "قُلۡ هُوَ ٱللَّهُ أَحَدٌ"
}


get info about one surah 
/surah/112/info.json
# response exmaple 
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
  "pages": [
    604,
    604
  ],
  "name_simple": "Al-Ikhlas",
  "name_complex": "Al-'Ikhlāş",
  "name_arabic": "الإخلاص",
  "translated_name": "The Sincerity",
  "start_page": 604,
  "end_page": 604
}


get aboout  the surah (english only) 

/surah/:surah-number/about.en.json
{
  "chapter_info": {
    "id": 112,
    "chapter_id": 112,
    "language_name": "english",
    "short_text": "Al-Ikhlas is not merely the name of this Surah but also the title of its contents, for it deals exclusively with Tauhid. The other Surahs of the Quran generally have been designated after a word occurring in them, but in this Surah the word Ikhlas has occurred nowhere. It has been given this name in view of its meaning and subject matter. Whoever understands it and believes in its teaching, will get rid of shirk (polytheism) completely.",
    "source": "Sayyid Abul Ala Maududi - Tafhim al-Qur'an - The Meaning of the Quran",
    "text": "long text "
    }
}

get surah info with verses 
/surah/:surah-number/index.info.json

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
    "0": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
    "1": "قُلْ هُوَ ٱللَّهُ أَحَدٌ",
    "2": "ٱللَّهُ ٱلصَّمَدُ",
    "3": "لَمْ يَلِدْ وَلَمْ يُولَدْ",
    "4": "وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ"
  }
}



### about translations section  
Avaiblabe Translations languages with their versions 
/translations/translations.json

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
    ...,
    {
      "key": "chinese_makin",
      "direction": "ltr",
      "language_iso_code": "zh",
      "version": "1.0.2",
      "last_update": 1662501318,
      "title": "Chinese Translation - Muhammad Makin",
      "description": "Translation of the Quran meanings into Chinese by Muhammad Makin. Corrected by supervision of Rowwad Translation Center. The original translation is available for suggestions, continuous evaluation and development."
    },
    {
    ...,
   ]
}


get Avaiblabe languages 
/translations/languages.json
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
    "tl",
    ...,
    ...,
    ]
}

get isocodes of all languages
/translations/isocodes.json
{
  "languages_isocodes": {
    "arabic": "ar",
    "english": "en",
    "french": "fr",
    "indonesian": "id",
    "bosnian": "bs",
    "spanish": "es",
    "russian": "ru",
    ...,
    ...,
    }
    
  "isocodes_languages": {
    "ar": "arabic",
    "en": "english",
    "fr": "french",
    "id": "indonesian",
    "bs": "bosnian",
    "es": "spanish",
    "ru": "russian",
    ...,
    ...,
    ...,
  }
}
    




### quran trasnaltions section 

default translation of quran in a specifc lanuage is   under 
/translations/:lang-code/  that contins surahs i.e /1/1.json for verse 1 of surah 1 
get surah for a specifc translation 
/translations/:lang-code/:surah-number/index.json

# example 
/translations/zh/1/index.json 
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
      "id": 2,
      "verse_number": 2,
      "page_number": 1,
      "verse_key": "1:2",
      "juz_number": 1,
      "hizb_number": 1,
      "rub_el_hizb_number": 1,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "ٱلۡحَمۡدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ",
      "translation": "一切赞颂，全归安拉，养育众世界的主，",
      "footnotes": ""
    },
    {
      "id": 3,
      "verse_number": 3,
      "page_number": 1,
      "verse_key": "1:3",
      "juz_number": 1,
      "hizb_number": 1,
      "rub_el_hizb_number": 1,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
      "translation": "至仁至慈的主，",
      "footnotes": ""
    },
    {
      "id": 4,
      "verse_number": 4,
      "page_number": 1,
      "verse_key": "1:4",
      "juz_number": 1,
      "hizb_number": 1,
      "rub_el_hizb_number": 1,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "مَٰلِكِ يَوۡمِ ٱلدِّينِ",
      "translation": "报应日的主。",
      "footnotes": ""
    },
    {
      "id": 5,
      "verse_number": 5,
      "page_number": 1,
      "verse_key": "1:5",
      "juz_number": 1,
      "hizb_number": 1,
      "rub_el_hizb_number": 1,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "إِيَّاكَ نَعۡبُدُ وَإِيَّاكَ نَسۡتَعِينُ",
      "translation": "我们只崇拜你，我们只求你祐助。",
      "footnotes": ""
    },
    {
      "id": 6,
      "verse_number": 6,
      "page_number": 1,
      "verse_key": "1:6",
      "juz_number": 1,
      "hizb_number": 1,
      "rub_el_hizb_number": 1,
      "sajdah_type": null,
      "sajdah_number": null,
      "text": "ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ",
      "translation": "求你引领我们上正路，",
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


get a minified surah for a specifc translation 
/translations/:lang-code/:surah-number/index.min.json
# Example 
/translations/zh/1/
{
  "verses": [
    {
      "number": "1",
      "arabic_text": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
      "translation": "奉至仁至慈的安拉之名"
    },
    {
      "number": "2",
      "arabic_text": "ٱلۡحَمۡدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ",
      "translation": "一切赞颂，全归安拉，养育众世界的主，"
    },
    {
      "number": "3",
      "arabic_text": "ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
      "translation": "至仁至慈的主，"
    },
    {
      "number": "4",
      "arabic_text": "مَٰلِكِ يَوۡمِ ٱلدِّينِ",
      "translation": "报应日的主。"
    },
    {
      "number": "5",
      "arabic_text": "إِيَّاكَ نَعۡبُدُ وَإِيَّاكَ نَسۡتَعِينُ",
      "translation": "我们只崇拜你，我们只求你祐助。"
    },
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

get verse in a specifc translation  
/translations/:lang-code/:surah-number/:verse-number.json

# Example 
/translats/yo/1/1.json
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


get info about the default trasnaltion 
/translations/:lang-code/info.json

/Translations/yo/info.json
{
  "key": "yoruba_mikail",
  "direction": "ltr",
  "language_iso_code": "yo",
  "version": "1.0.7",
  "last_update": 1720592188,
  "title": "Yoruba translation",
  "description": "Translation of the Quran meanings into Yoruba by Abu Rahima Mikhail Aikweiny, printed in 1432 H."
}


### Quran trasnaltions versions 

see Avaiblabe translations versions
/translations/translations.json

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
    ...,
    ...,
  ]
}
    

get a surah in a lanuage in a specific version 
/translations/:lang-code/:translation-version/surah/index.json

# example
/translations/ug/uyghur_saleh/surah/110/index.json
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


get a minifed surah in a lanuage in a specific version 
/translations/:lang-code/:translation-version/surah/:surah-number/index.min.json

# example
/translations/ug/uyghur_saleh/surah/110/index.min.json

{
  "verses": [
    {
      "number": "1",
      "arabic_text": "إِذَا جَآءَ نَصۡرُ ٱللَّهِ وَٱلۡفَتۡحُ",
      "translation": " ئاللاھنىڭ ياردىمى ۋە غەلىبىسى كەلگەن ۋە ئاللاھنىڭ دىنىغا كىشىلەرنىڭ توپ ـ توپ بولۇپ كىرگەنلىكىنى كۆرگىنىڭدە[1ـ2]،"
    },
    {
      "number": "2",
      "arabic_text": "وَرَأَيۡتَ ٱلنَّاسَ يَدۡخُلُونَ فِي دِينِ ٱللَّهِ أَفۡوَاجٗا",
      "translation": " ئاللاھنىڭ ياردىمى ۋە غەلىبىسى كەلگەن ۋە ئاللاھنىڭ دىنىغا كىشىلەرنىڭ توپ ـ توپ بولۇپ كىرگەنلىكىنى كۆرگىنىڭدە[1ـ2]،"
    },
    {
      "number": "3",
      "arabic_text": "فَسَبِّحۡ بِحَمۡدِ رَبِّكَ وَٱسۡتَغۡفِرۡهُۚ إِنَّهُۥ كَانَ تَوَّابَۢا",
      "translation": "رەببىڭغا تەسبىھ ئېيتقىن، ھەمدى ئېيتقىن ۋە ئۇنىڭدىن مەغپىرەت تىلىگىن. ئاللاھ ھەقىقەتەن تەۋبىنى بەك قوبۇل قىلغۇچىدۇر[3]."
    }
  ]
}



get a verse in a language in a specifc version
/translations/:lang-code/:translation-version/surah/:surah-number/:verse-number.json

# example
/translations/ug/uyghur_saleh/surah/110/2.json

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

get info about a about a  translation version
/translations/:lang-code/:translation-version/info.json

# exmaple 
/translations/ja/japanese_saeedsato/info.json

{
  "key": "japanese_saeedsato",
  "direction": "ltr",
  "language_iso_code": "ja",
  "version": "1.0.11",
  "last_update": 1730715411,
  "title": "Japanese translation - Saeed Sato",
  "description": "Translation of the Quran meanings into Japanese by Saeed Sato. printed in 1440 H."
}

get availbe translation versions in language 
/translations/translations/:lang-code/index.json
# Example 
/translations/translations/zh/
{
  "translations": [
    {
      "key": "chinese_suliman",
      "direction": "ltr",
      "language_iso_code": "zh",
      "version": "1.0.7",
      "last_update": 1739956759,
      "title": "Chinese Translation - Mohammed Suleiman",
      "description": "Translation of the Qur’an meanings into Chinese, translated by Mohammed Makin, reviewed by Mohammed Suleiman with other specialists."
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



### Quran Tafsirs
get list of editions i.e availbe tafsirs and their languages
availbe lanuages
ar,bn,en,kurd,ru,ur

/tafsirs/editions.json

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
  ...,
  {
    "author_name": "Saddi",
    "id": 170,
    "language_name": "russian",
    "name": "Tafseer Al Saddi",
    "slug": "ru-tafseer-al-saddi",
    "source": "https://quran.com/"
  },
  ...,
   {
    "author_name": "Rebar Kurdish Tafsir",
    "id": 804,
    "language_name": "Kurdish",
    "name": "Rebar Kurdish Tafsir",
    "slug": "tafsir-rebar",
    "source": "https://quran.com/"
  },
  ..,
]



## default tafisr in a specific lanuage  is under /tafsirs/:lang-code/

get a  surah  in a default tafsir
/tafsirs/:lang-code/1.json

/tafsirs/en/al-jalalayn/110/1.json
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

get a verse in default tafisr 
/tafsirs/:lang-code/:surah-number/:verse-number.json


### tafsirs  versions 

get list of tafsir versions in a language

/tafsirs/:lang-code/index.json

# example 
/tafsirs/ar/index.json
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
  },
  ...,
  ...,
]


get a  surah  in a tafir version 
/tafsirs/:lang-code/:tafsir-version/info.json

# example 
/tafsirs/en/al-jalalayn/110.json
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



get a verse in  tafisr  version 
/tafsirs/:lang-code/:surah-number/:verse-number.json

# example
/tafsirs/en/al-jalalayn/110/1.json

{
  "surah": 110,
  "ayah": 1,
  "text": "When the help of God for His Prophet s against his enemies comes together with victory the victory over Mecca"
}




















































