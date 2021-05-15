## Background

pdf-inert-blank was written to add blank pages to a PDF document in order to ensure specified pages are always printed on front side with a blank page in the back.

This could be useful if you want some pages to be single-sided when doing double-sided printing on a PDF file.

## Installation

[PyPDF2](https://pythonhosted.org/PyPDF2/) and [pdfminer.six](https://pdfminersix.readthedocs.io/en/latest/) are required to run the code.

```bash
pip install PyPDF2
pip install pdfminer.six
```

## Usage

Change the values in `# Settings` and run it in Python 3 environment. Blank pages will be added before/after pages with `search_str`.
