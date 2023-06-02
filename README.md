# Science Notes

## Steps to add a new blog post
- Create a new folder in `blogs/` with the name of the blog post
- Add your markdown file in the new folder and images in in the `<folder-name>/images/` folder.
- Add the markdown in _toc.yml under relevant category
- Build the book as mentioned in [section](#build-the-book)
- Verify the changes in the browser as mentioned in [section](#local-testing-of-the-website)
- Build the regular pdf as mentioned in [section](#build-pdf)
- Build the latex pdf as mentioned in [section](#build-pdf-through-latex)
- Push the changes to the repo and get the merge request approved.
- After the merge request is approved to be merged with main, the changes will be reflected in the website after workflow is completed in github actions.


## Setup
### Clone this repository

```zsh
git clone https://github.com/dlt-science/science-notes.git
```

Navigate to the directory of the cloned repo

```zsh
cd science-notes
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
Run the below command. Use `--all` to force rebuild all

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

## Build pdf

Must first install the right version of `urllib3` if haven't
```zsh
pip install -U "urllib3<1.25"
```

```zsh
jupyter-book build blogs/ --builder pdfhtml
```

This command times out, so you'll need to override the timeout manually in the
file : `venv/lib/python3.11/site-packages/pyppeteer/page.py` by changing the line 134 to:
`self._defaultNavigationTimeout = 3000000  # milliseconds`


The generated pdf can be found [here](blogs/_build/pdf/book.pdf).
The latex generated pdf can be found [here](blogs/_build/latex/pdf/book.pdf).

## Build pdf through latex

```zsh
jupyter-book build blogs/ --builder pdflatex
```

## Update the data github pages link
*Can only be run by admins/maintainers of the repo.*
```zsh
ghp-import -n -p -f blogs/_build/html
```

## Local testing of the website
- Install VSCode extension `Live Server`
- Right-click `blogs/_build/html/index.html` in VSCode and select `Open with Live Server`.
- You can now see the changes in the browser everytime you rebuild the book (`jupyter-book build --all blogs/`).