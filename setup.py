from setuptools import setup, find_packages

setup(
    name="ctd",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "jupyter-book", "jupyter-book", "pyppeteer"],
    extras_require={"dev": ["pylint", "black"]},
)