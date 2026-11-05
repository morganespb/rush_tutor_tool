# 42 Rush Tutor Tool

A terminal app for 42 tutors. After evaluating a rush, use it live with candidates to explain the basics behind the subject: `argc`/`argv`, memory and pointers, file descriptors, `write()`, shell redirections and common mistakes.

## Install

Requires Python 3.10+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python3 main.py
```

Pick a lesson by number, `q` to quit. `Ctrl+C` exits from anywhere.

## Project layout

```
main.py                  entry point
tutor/
  app.py                 main menu (add a lesson = add one line to MENU)
  ui.py                  shared console, card() panel helper, show() / wait()
  diagrams.py            static lesson panels and the argv table
  screens.py             simple one-frame lessons
  argv_tools.py          live argc/argv simulator and char **argv playground
  code_cases.py          "Break This Code" snippets
  memory_simulator.py    step-by-step pointer playground
```
