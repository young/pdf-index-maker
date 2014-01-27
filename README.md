PDF Index Maker
========

PDF Index Maker is a tool for creating an index from a PDF file.

It uses a very slightly modified <a href="http://www.unixuser.org/~euske/python/pdfminer/">PDFMiner</a> to extract readable text from a pdf file along with page numbers of the text. PDF Index Maker takes a list of words, scans the text, and outputs every word (if it was found) along with the associated page numbers.

Usage
------
    $ git clone https://github.com/jemuelyoung/pdf-index-maker
    $ cd pdf-index-maker
    $ python setup.py install

To make create an index, add the words to a text file separating each word with a newline.

* Use the -w flag to indicate the location of the file to read the words list from 
* Use the -f flag to indicate the location of the pdf file

* [Optional] Use the -p if you want the output printed to the console (default: False)
* [Optional] Use the -o to indicate the file to output the index to (default: index.txt)


    `$ python indexMaker.py -w words.txt -f some_pdf.pdf -o output.txt`



License
-----

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
