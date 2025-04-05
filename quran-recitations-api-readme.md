# Quran API - Audio Documentation

This documentation provides a comprehensive guide to the audio endpoints of the Quran API, allowing developers to access and utilize Quranic recitations in their applications.

## Table of Contents

- [Overview](#overview)
- [Base URLs](#base-urls)
- [Endpoints](#endpoints)
  - [Reciters](#reciters)
  - [Chapter Recitations](#chapter-recitations)
  - [Verse Recitations](#verse-recitations)
- [Playing Audio](#playing-audio)
- [Pagination](#pagination)
- [Examples](#examples)

## Overview

The Quran API provides access to various Quranic audio recitations by different reciters in various styles (Mujawwad, Murattal, etc.). You can retrieve audio files for complete chapters (surahs) or individual verses (ayahs), filtered by different Quranic divisions like juz, hizb, rub el hizb, or page number.

## Base URLs

- API Base URL: `https://api.quran.com/api/v4`
- Audio Base URL: `https://verses.quran.foundation`
- Download URL: `https://download.quranicaudio.com`

## Endpoints

### Reciters

#### List All Reciters

Retrieves a list of all available reciters and their recitation styles.

```
GET /resources/recitations
```

**Response Example:**

```json
{
  "recitations": [
    {
      "id": 2,
      "reciter_name": "AbdulBaset AbdulSamad",
      "style": "Murattal",
      "translated_name": {
        "name": "AbdulBaset AbdulSamad",
        "language_name": "english"
      }
    },
    {
      "id": 1,
      "reciter_name": "AbdulBaset AbdulSamad",
      "style": "Mujawwad",
      "translated_name": {
        "name": "AbdulBaset AbdulSamad",
        "language_name": "english"
      }
    },
    // ... more reciters
  ]
}
```

### Chapter Recitations

#### Get All Chapter Audio Files for a Reciter

Retrieves a list of all chapter (surah) audio files for a specific reciter.

```
GET /chapter_recitations/:recitation_id
```

**Parameters:**
- `recitation_id`: The ID of the recitation/reciter

**Example:** `/chapter_recitations/1`

**Response Example:**

```json
{
  "audio_files": [
    {
      "id": 10734,
      "chapter_id": 1,
      "file_size": 1595520,
      "format": "mp3",
      "audio_url": "https://download.quranicaudio.com/qdc/abdul_baset/mujawwad/1.mp3"
    },
    // ... more chapters
    {
      "id": 10834,
      "chapter_id": 114,
      "file_size": 1345664,
      "format": "mp3",
      "audio_url": "https://download.quranicaudio.com/qdc/abdul_baset/mujawwad/114.mp3"
    }
  ]
}
```

#### Get Audio File for a Specific Chapter

Retrieves the audio file for a specific chapter (surah) by a specific reciter.

```
GET /chapter_recitations/:recitation_id/:chapter_number
```

**Parameters:**
- `recitation_id`: The ID of the recitation/reciter
- `chapter_number`: The number of the chapter (surah)

**Example:** `/chapter_recitations/1/1`

**Response Example:**

```json
{
  "audio_file": {
    "id": 10734,
    "chapter_id": 1,
    "file_size": 1595520,
    "format": "mp3",
    "audio_url": "https://download.quranicaudio.com/qdc/abdul_baset/mujawwad/1.mp3"
  }
}
```

### Verse Recitations

#### Get All Audio Files for a Recitation

Retrieves a list of all verse (ayah) audio files for a specific reciter.

```
GET /quran/recitations/:recitation_id
```

**Parameters:**
- `recitation_id`: The ID of the recitation/reciter

**Example:** `/quran/recitations/1`

**Response Example:**

```json
{
  "audio_files": [
    {
      "verse_key": "1:1",
      "url": "AbdulBaset/Mujawwad/mp3/001001.mp3"
    },
    {
      "verse_key": "1:2",
      "url": "AbdulBaset/Mujawwad/mp3/001002.mp3"
    },
    // ... more verses
    {
      "verse_key": "114:6",
      "url": "AbdulBaset/Mujawwad/mp3/114006.mp3"
    }
  ],
  "meta": {
    "reciter_name": "AbdulBaset AbdulSamad",
    "recitation_style": "Mujawwad",
    "filters": {}
  }
}
```

#### Get Audio File for a Specific Verse

Retrieves the audio file for a specific verse (ayah) by a specific reciter.

```
GET /recitations/:recitation_id/by_ayah/:ayah_key
```

**Parameters:**
- `recitation_id`: The ID of the recitation/reciter
- `ayah_key`: The key of the verse in format "surah:ayah" (e.g., "1:2")

**Example:** `/recitations/1/by_ayah/1:2`

**Response Example:**

```json
{
  "audio_files": [
    {
      "verse_key": "1:2",
      "url": "AbdulBaset/Mujawwad/mp3/001002.mp3"
    }
  ],
  "pagination": {
    "per_page": 10,
    "current_page": 1,
    "next_page": null,
    "total_pages": 1,
    "total_records": 1
  }
}
```

#### Get Audio Files for a Specific Chapter

Retrieves all verse audio files for a specific chapter (surah) by a specific reciter.

```
GET /recitations/:recitation_id/by_chapter/:chapter_number
```

**Parameters:**
- `recitation_id`: The ID of the recitation/reciter
- `chapter_number`: The number of the chapter (surah)

**Example:** `/recitations/1/by_chapter/1`

**Response Example:**

```json
{
  "audio_files": [
    {
      "verse_key": "1:1",
      "url": "AbdulBaset/Mujawwad/mp3/001001.mp3"
    },
    {
      "verse_key": "1:2",
      "url": "AbdulBaset/Mujawwad/mp3/001002.mp3"
    },
    // ... more verses
    {
      "verse_key": "1:7",
      "url": "AbdulBaset/Mujawwad/mp3/001007.mp3"
    }
  ],
  "pagination": {
    "per_page": 10,
    "current_page": 1,
    "next_page": null,
    "total_pages": 1,
    "total_records": 7
  }
}
```

#### Get Audio Files for a Specific Juz

Retrieves all verse audio files for a specific juz by a specific reciter.

```
GET /recitations/:recitation_id/by_juz/:juz_number
```

**Parameters:**
- `recitation_id`: The ID of the recitation/reciter
- `juz_number`: The number of the juz

**Example:** `/recitations/1/by_juz/1`

**Response Example:**

```json
{
  "audio_files": [
    {
      "verse_key": "1:1",
      "url": "AbdulBaset/Mujawwad/mp3/001001.mp3"
    },
    // ... more verses
    {
      "verse_key": "2:141",
      "url": "AbdulBaset/Mujawwad/mp3/002141.mp3"
    }
  ],
  "pagination": {
    "per_page": 1000,
    "current_page": 1,
    "next_page": null,
    "total_pages": 1,
    "total_records": 148
  }
}
```

#### Get Audio Files for a Specific Page

Retrieves all verse audio files for a specific page of the Madani Mushaf by a specific reciter.

```
GET /recitations/:recitation_id/by_page/:page_number
```

**Parameters:**
- `recitation_id`: The ID of the recitation/reciter
- `page_number`: The page number of the Madani Mushaf

**Example:** `/recitations/1/by_page/604`

**Response Example:**

```json
{
  "audio_files": [
    {
      "verse_key": "112:1",
      "url": "AbdulBaset/Mujawwad/mp3/112001.mp3"
    },
    // ... more verses
    {
      "verse_key": "114:6",
      "url": "AbdulBaset/Mujawwad/mp3/114006.mp3"
    }
  ],
  "pagination": {
    "per_page": 100,
    "current_page": 1,
    "next_page": 2,
    "total_pages": 2,
    "total_records": 15
  }
}
```

#### Get Audio Files for a Specific Rub el Hizb

Retrieves all verse audio files for a specific rub el hizb by a specific reciter.

```
GET /recitations/:recitation_id/by_rub/:rub_el_hizb_number
```

**Parameters:**
- `recitation_id`: The ID of the recitation/reciter
- `rub_el_hizb_number`: The number of the rub el hizb

**Example:** `/recitations/1/by_rub/1?per_page=10000000000000000`

**Response Example:**

```json
{
  "audio_files": [
    {
      "verse_key": "1:1",
      "url": "AbdulBaset/Mujawwad/mp3/001001.mp3"
    },
    // ... more verses
    {
      "verse_key": "2:25",
      "url": "AbdulBaset/Mujawwad/mp3/002025.mp3"
    }
  ],
  "pagination": {
    "per_page": 10000000000000000,
    "current_page": 1,
    "next_page": null,
    "total_pages": 1,
    "total_records": 32
  }
}
```

#### Get Audio Files for a Specific Hizb

Retrieves all verse audio files for a specific hizb by a specific reciter.

```
GET /recitations/:recitation_id/by_hizb/:hizb_number
```

**Parameters:**
- `recitation_id`: The ID of the recitation/reciter
- `hizb_number`: The number of the hizb

**Example:** `/recitations/1/by_hizb/1?per_page=1000000000033333333`

**Response Example:**

```json
{
  "audio_files": [
    {
      "verse_key": "1:1",
      "url": "AbdulBaset/Mujawwad/mp3/001001.mp3"
    },
    // ... more verses
    {
      "verse_key": "2:74",
      "url": "AbdulBaset/Mujawwad/mp3/002074.mp3"
    }
  ],
  "pagination": {
    "per_page": 1.0000000000333334e+18,
    "current_page": 1,
    "next_page": null,
    "total_pages": 1,
    "total_records": 81
  }
}
```

## Playing Audio

To play the audio files, use the following base URL combined with the URL path returned by the API:

```
https://verses.quran.foundation/{url}
```

**Example:**
For a verse with URL `"AbdulBaset/Mujawwad/mp3/001002.mp3"`, the full playable URL would be:
```
https://verses.quran.foundation/AbdulBaset/Mujawwad/mp3/001002.mp3
```

For chapter audio files, use the `audio_url` directly as provided in the response, e.g.:
```
https://download.quranicaudio.com/qdc/abdul_baset/mujawwad/1.mp3
```

## Pagination

The API uses pagination for endpoints that return multiple audio files. By default, most endpoints return a limited number of records per page (e.g., 10).

To retrieve all records in a single request, set the `per_page` parameter to a very high value:

```
?per_page=1000000
```

Example: `/recitations/1/by_juz/1?per_page=1000000`

The pagination information is included in the response:

```json
"pagination": {
  "per_page": 10,
  "current_page": 1,
  "next_page": null,
  "total_pages": 1,
  "total_records": 7
}
```

## Examples

### Playing a Complete Surah

1. Get the surah audio URL:
```
GET /chapter_recitations/1/1
```

2. Play the audio using the returned `audio_url`:
```
https://download.quranicaudio.com/qdc/abdul_baset/mujawwad/1.mp3
```

### Playing Individual Verses

1. Get the verse audio URL:
```
GET /recitations/1/by_ayah/1:2
```

2. Play the audio using the base URL and returned `url`:
```
https://verses.quran.foundation/AbdulBaset/Mujawwad/mp3/001002.mp3
```

### Getting All Verses for a Juz

```
GET /recitations/1/by_juz/1?per_page=1000
```

This will return all verses in the first juz recited by reciter with ID 1.
