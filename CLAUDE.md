# CLAUDE.md — Learn Python Repository

## What This Repo Is

A teaching repository originally used for live Python classes, now transitioning to YouTube tutorials. The instructor teaches Python from scratch. Students/viewers are beginners.

## Audience

- Beginner students/viewers learning Python for the first time.
- The instructor also covers broader topics like Git/GitHub, software engineering mindset, and entrepreneurial thinking alongside Python basics.

## Repository Structure

```
learn_python/
├── CLAUDE.md              ← this file
├── README.md              ← index of all sessions
├── transcript/            ← raw transcripts for YouTube tutorial sessions
│   ├── functions.txt
│   └── classes_and_objects.txt
├── summary/               ← session summaries
│   ├── 2026-06-26.md      ← (live class) Python basics + Git/GitHub + Cybersecurity
│   ├── 2026-06-29.md      ← (live class) Hello World, Variables, Lists, Operators, Strings, Conditions
│   ├── 2026-06-30.md      ← (live class) Problem solving mindset, market research, entrepreneurship
│   ├── functions.md       ← (YouTube) Functions
│   └── classes_and_objects.md ← (YouTube) Classes & Objects
├── 01_hello.py
├── 02_condition.py
├── 03_more_basics.py
├── 04_lists.py
├── 05_ops.py
├── 06_string_ops.py
├── 07_string_ops2.py
├── 08_conditions.py
├── 09_loops.py
├── 10_functions.py
├── 11_functions_2.py
└── 12_classes.py
```

## Session Summaries

Summaries switched naming convention when the format moved from live classes to YouTube tutorials:
- **Live classes (historical):** `summary/YYYY-MM-DD.md`, one file per class date.
- **YouTube tutorials (current):** `summary/<topic>.md`, one file per topic/video (e.g. `functions.md`), since sessions are no longer tied to a single class day.

When generating a new summary:
- For YouTube tutorials, use the transcript in `transcript/<topic>.txt` (if present) and/or the commit history to identify what was covered.
- For historical live classes, use the commit history for the session date.
- Keep the tone friendly and encouraging — audience is beginners.
- Include a homework or discussion section where appropriate.

## Python Files

Files are numbered sequentially (`01_`, `02_`, ...) and are self-contained exercises written during class or in a tutorial video.

## Curriculum Progress (as of 2026-07-03)

Curriculum progress:

| # | Topic | File | Status |
|---|-------|------|--------|
| 1 | Hello, World! | 01_hello.py | ✅ Done |
| 2 | Variables and Types | 02_condition.py, 03_more_basics.py | ✅ Done |
| 3 | Lists | 04_lists.py | ✅ Done |
| 4 | Basic Operators | 05_ops.py | ✅ Done |
| 5 | String Formatting | 03_more_basics.py | ✅ Done |
| 6 | Basic String Operations | 06_string_ops.py, 07_string_ops2.py | ✅ Done |
| 7 | Conditions | 08_conditions.py | ✅ Done |
| 8 | Loops | 09_loops.py | ✅ Done |
| 9 | Functions | 10_functions.py, 11_functions_2.py | ✅ Done |
| 10 | Classes and Objects | 12_classes.py | 🔄 In Progress |
