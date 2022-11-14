# Project: PDF Merge

## Description:

Simple script that merges multiple PDF files into one. No clunky interfaces, pressure to purchase, or ads to deal with.

## Features:

- Combine as many PDFs as you want!
- Lightweight!
- Simple to use!

## Requirements:

- [Python3](https://www.python.org/downloads/)
- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/user/installation.html)
- Windows 10 OS or later, to run the .bat file. But main.py will run on any terminal as long as you've installed the two above.

## How to Use:

1. Copy the .pdf files you want to merge into the _input_ directory.
   - Keep in mind the script will merge everything in alphabetical order. So rename files, if you have to.
2. Double click on _run.bat_
   - Or you can use the command _python main.py_ from a non-Windows terminal.
3. Name the output file when prompted.
   - You can leave off the _.pdf_ extension.
   - Leave blank to default to _\_merged.pdf_.
4. Press _Enter_.
5. Choose 'y' or 'n' if you'd like to delete the contents of the input folder, when prompted.
   - Note: **THIS DELETE IS PERMANENT**
6. Retrieve your merged file from the _output_ directory.

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
