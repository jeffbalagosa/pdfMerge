# Project: PDF Merge

## Description:

Simple script that merges multiple PDF files into one. No clunky interfaces, pressure to purchase, or ads to deal with. Runs locally, so no need to worry about some sketchy website stealing our data.

## Features:

- Combine as many PDFs as you want!
- Lightweight!
- Simple to use!

## Requirements

**Windows 10** or later. But only if you want to run the _run.bat_ file to launch it. You can run the app, _main.py_, from any terminal.

## Installation:

### Install Python 3

Download and run the [installer](https://www.python.org/downloads/)

### Install PyPDF2

Once you have Python installed. Open a terminal use this command to install PyPDF2.

```
pip install PyPDF2
```

..or if you don't have admin rights, you can use the following

```
pip install --user PyPDF2
```

Here's the PyPDF2 install [docs](https://pypdf2.readthedocs.io/en/latest/user/installation.html) if you need more info.

### This App

- Once you have Python and PyPDF2 installed. You can download the [zip](https://github.com/jeffbalagosa/pdfMerge/archive/refs/heads/main.zip) file from here.
- Extract it to wherever you want.
- And follow the instructions below!

## How to Use:

1. Navigate into the _pdfMerge_ directory. (Could be named _pdfMerge-main_, depending on how you downloaded it.)
2. Copy the .pdf files you want to merge into the _input_ directory.
   - Keep in mind the script will merge everything in alphabetical order. So rename files, if you have to.
3. Double click on _run.bat_
   - Or you can use the command _python main.py_ from whatever terminal you use.
4. Name the output file when prompted.
   - You can leave off the _.pdf_ extension.
   - Leave blank to default to _\_merged.pdf_.
5. Press _Enter_.
6. Choose 'y' or 'n' if you'd like to delete the contents of the input folder, when prompted.
   - Note: **THIS DELETE IS PERMANENT**
7. Retrieve your merged file from the _output_ directory.

## Technologies:

- Python
- Windows Terminal
- PyPDF2 Library

## License:

MIT License

Copyright (c) 2022 Jeff Balagosa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
