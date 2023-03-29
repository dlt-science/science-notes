# dsfblog


### Clone this repository

```zsh
git clone https://github.com/xujiahuayz/dsfblog.git
```

Navigate to the directory of the cloned repo

```zsh
cd dsfblog
```

### Create a python virtual environment

- iOS

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
pip install -e ".[dev]"
```

## Build the book

### Build html

Use `--all` to force rebuild all

```zsh
jupyter-book build --all defianddata/
```

View the book in browser

- iOS

```zsh
open defianddata/_build/html/index.html
```

- Windows

```zsh
start defianddata/_build/html/index.html
```

### Build pdf

<!-- Must first install the right version of `urllib3` if haven't
```zsh
pip install -U "urllib3<1.25"
``` -->

Build pdfhtml:

```zsh
jupyter-book build defianddata/ --builder pdfhtml
```

The generated pdf can be found [here](defianddata/_build/pdf/book.pdf).

Or build pdf through latex

```zsh
jupyter-book build defianddata/ --builder pdflatex
```
