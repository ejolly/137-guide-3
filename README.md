# AI assisted study guides & challenge generation

## Recipe

### 1. Generate optional reading summaries

- copy all `optional-readings` PDFs to `./papers/pdfs/
- adapt `prompts/claude-paper-orchestrator` and `parallel` to create summary files in a new sub-dir
- create new files for each week in `docs/paper-summaries/` and index file for next part
- have claude/cursor-composer refactor summaries into the right places following previous Parts examples

### 2. Generate Glossary

- download lecture podcasts and transcripts
- upload slide PDFs, transcripts, syllabus, and previous glossary to ChatGPT Pro
- verify project files
- use `prompts/gpt-glossarizer*.md` to generate glossary file in correct format

### 3. Generate Lecture summaries

- upload each week's paper summaries, glossary, example-part, example-week, and index-page to ChatGPT as *project files*
- in a new chat upload a single week's lecture PDF + transcript at a time and ask for as summary following example files for schema and referencing glossary and papers

### 4. Review & update TOC

- verify glossary links and unnecessary terms
- verify paper summaries and social-cognitive-scientist hat sub-sections
- move previous challenge guide below in TOC
- set current challenge guide to `/` route

---

## Requires
- chatgpt pro 
- `claude-code` or local llm
- `pandoc`
- `typst`
- `docsify` 