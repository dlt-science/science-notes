# dsfblog


### Clone this repository

```zsh
git clone https://github.com/dlt-science/science-notes.git
```

Navigate to the directory of the cloned repo

```zsh
cd dsfblog
```

### Create a python virtual environment

- MacOS / Linux

```zsh
python3 -m venv venv
```

- Windows

```zsh
python -m venv venv
```


### Activate the virtual environment

- iOS

```zsh
. venv/bin/activate
```

- Windows (in Command Prompt, NOT Powershell)

```zsh
venv\Scripts\activate.bat
```

### Install the project in editable mode

```zsh
pip install -r requirements.txt
```

## Build the book

### Build html

Use `--all` to force rebuild all

```zsh
jupyter-book build --all blogs/
```

View the book in browser

- iOS

```zsh
open blogs/_build/html/index.html
```

- Windows

```zsh
start blogs/_build/html/index.html
```

### Build pdf

<!-- Must first install the right version of `urllib3` if haven't
```zsh
pip install -U "urllib3<1.25"
``` -->

Build pdfhtml:

```zsh
jupyter-book build blogs/ --builder pdfhtml
```

This command times out, so you'll need to override the timeout manually in the
file : `venv/lib/python3.11/site-packages/pyppeteer/page.py` by changing the line 134 to:
`self._defaultNavigationTimeout = 3000000  # milliseconds`


The generated pdf can be found [here](blogs/_build/pdf/book.pdf).
The latex generated pdf can be found [here](blogs/_build/latex/pdf/book.pdf).

Or build pdf through latex

```zsh
jupyter-book build blogs/ --builder pdflatex
```

### Update the data github pages link
```zsh
ghp-import -n -p -f blogs/_build/html
```