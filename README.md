# HeicGo — Free, Private HEIC to JPG Converter

Convert iPhone HEIC/HEIF photos to JPG **entirely in your browser** — no upload, no signup, no watermark. Live at **https://heicgo-ecc.pages.dev**

## Features

- 🔒 **100% private** — HEIC decoding runs as WebAssembly in the visitor's browser, photos never touch a server
- ⚡ **Batch conversion** with per-file or ZIP download
- 🌍 **8 languages** — English, Deutsch, Français, Español, 日本語, 한국어, 简体中文, 繁體中文 (each a static page with full hreflang wiring)
- 🌙 Dark mode with system-preference detection and persistence
- 📱 Responsive, zero dependencies at runtime beyond two MIT libraries

## Structure

```
template.html   single-source template (all pages build from this)
build.py        i18n page generator — add a language, rerun, done
index.html      English (default) — generated
de/fr/es/ja/ko/zh-cn/zh-tw.html — generated
assets/         heic2any + JSZip (MIT)
robots.txt / sitemap.xml / og.png
```

## Build

```bash
python build.py   # regenerates all 8 language pages from template.html
```

## Deploy

```bash
wrangler pages deploy deploy --project-name=heicgo
```

## Tech notes

- HEIC decode: [heic2any](https://github.com/nitin42/heic2any) (MIT), bundling libheif compiled to WASM
- ZIP: [JSZip](https://github.com/Stuk/jszip) (MIT)
- SEO: per-language canonical + hreflang + x-default, JSON-LD (WebApplication + FAQPage), Open Graph, sitemap
