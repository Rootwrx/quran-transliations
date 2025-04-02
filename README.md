# Quran Static API

This is a static API for the Quran that can be hosted without a backend server.

## API Endpoints

### Languages and Translations

- **Get all available languages:**
  - `/api/languages/index.json`

- **Get language ISO codes:**
  - `/api/isocodes/index.json`

- **Get all translations:**
  - `/api/translations/index.json`

- **Get translations for a specific language:**
  - `/api/{language_code}/index.json`

### Default Quran Structure

- **Get a specific surah:**
  - `/api/surah/{surah_number}/index.json`

- **Get a specific ayah:**
  - `/api/surah/{surah_number}/{ayah_number}.json`

### Translations

- **Get translation information:**
  - `/api/{language_code}/{translation_key}/info.json`

- **Get a surah in a specific translation:**
  - `/api/{language_code}/{translation_key}/surah/{surah_number}/index.json`

- **Get an ayah in a specific translation:**
  - `/api/{language_code}/{translation_key}/surah/{surah_number}/{ayah_number}.json`

## Examples

1. Get Surah Al-Fatiha (Surah 1):
   - `/api/surah/1/index.json`

2. Get Ayah 1 of Surah Al-Baqarah (Surah 2):
   - `/api/surah/2/1.json`

3. Get Surah Al-Ikhlas (Surah 112) in English (Saheeh International):
   - `/api/en/english_saheeh/surah/112/index.json`

4. Get Ayah 1 of Surah Al-Ikhlas in English:
   - `/api/en/english_saheeh/surah/112/1.json`

## Hosting Options

This static API can be hosted on:
- GitHub Pages
- jsDelivr (directly from a GitHub repository)
- Any static file hosting service
- Local file server

## Data Source

The data is sourced from the QuranEnc API.
