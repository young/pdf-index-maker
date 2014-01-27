import string
import time
import argparse

from sys import argv
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


class IndexMaker():
    def __init__(self, args):
        self.run(args)

    def run(self, args):
        try:
            # get the word list and create a dict of words
            words_list = [line.strip() for line in open(args.w)]
        except IOError as e:
            print e
            exit()

        # start the timer
        start = time.clock()

        # buil the index
        index = create_index(args.f, words_list)

        f = open(args.o,'w')

        for word in index:
            # write the index to a file
            f.write("%s: %s \n" % (word, index[word]))
            if args.p:
                print "%s: %s \n" % (word, index[word]) 
        f.close()

        end = time.clock()

        print "Finished in %f seconds" % (end - start)

def get_pdf_text(path):
    """ Reads a pdf file and returns a dict of the text where the
        index represents the page number.
        http://stackoverflow.com/a/20905381
    """
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    # change to to utf-8 if the text comes out garbled
    codec = 'ascii'
    #codec = 'utf-8'
    laparams = LAParams()
    pages = {}
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams, showpageno=True, pages=pages)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    retstr.close()
    return pages

def find_whole_word(needle, haystack, case_sensitive = False):
    """ Searches text for a whole word match. Ignores whitespace and punctuation.
        Example: find_whole_word('test', 'This is a test; This is also a tester')
        matches 'test;' but not 'tester'
        http://stackoverflow.com/a/4155029
    """
    if case_sensitive:
        index = haystack.find(needle)
    else:
        index = haystack.lower().find(needle.lower())

    if index == -1:
        return False
    if index != 0 and haystack[index-1].isalnum():
        return False
    L = index + len(needle)
    if L < len(haystack) and haystack[L].isalnum():
        return False
    return True

def create_index(pdf_path, words_list):
    """ Create a word index from pdf file
    """
    text_data = get_pdf_text(pdf_path)
    word_index = {}
    for page in text_data:
        for word in words_list:
            if find_whole_word(word, text_data[page]):
                if word in word_index:
                    word_index[word].append( (page * 2) - 4 )
                else:
                    word_index[word] = [(page * 2) - 4]
    return word_index


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates an index of words from a PDF file.')
    parser.add_argument('--version', action='version', version='0.02')
    parser.add_argument('-o', default='index.txt', help='The file to output the index to')
    parser.add_argument('-p', default=False, help='Print output to console')
    parser.add_argument('-w', required=True, help='A text file of new line delimited words')
    parser.add_argument('-f', required=True, help='The pdf file to create the index from')

    args = parser.parse_args()
    IndexMaker(args)