PDF Index Maker
========

PDF Index Maker is a tool for creating an index for a PDF file.

It uses <a href="http://www.unixuser.org/~euske/python/pdfminer/">PDFMiner</a> to extract readable text from a pdf file along with 
page numbers of the text. PDF Index Maker takes a list of words, scans the text, and outputs every word (if it was found) along with the associated page numbers.

Usage
------
    $ git clone https://github.com/jemuelyoung/pdf-index-maker
    $ cd pdf-index-maker
    $ python setup.py install
    $ python indexMaker.py

To make create an index, simply add the words the words_list.

TODO
-----
* Get words list from command line