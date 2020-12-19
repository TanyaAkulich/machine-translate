# Imports
import nltk
import sys

# import pdfminer.high_level
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

DOT = '.'
COMMA = ','
GRAMMAR_RULES = r"""
        P: {<IN>}
        V: {<V.*>}
        N: {<NN.*>}
        NP: {<N|PP>+<DT|CD|PR.*|JJ|CC>}
        NP: {<DT|CD|PR.*|JJ|CC><N|PP>+}
        PP: {<P><NP>}
        VP: {<NP|N><V.*>}
        VP: {<V.*><NP|N>}
        VP: {<VP><PP>}
        """

# Core logic
def download_nltk_dependecies():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

def draw_tree(text):
    text = " ".join(text)
    text = text.replace('\n', '')
    if text != '':
        download_nltk_dependecies()
        doc = nltk.word_tokenize(text)
        doc = nltk.pos_tag(doc)
        new_doc = []
        for item in doc:
            if item[1] != COMMA and item[1] != DOT:
                new_doc.append(item)
        cp = nltk.RegexpParser(GRAMMAR_RULES)
        result = cp.parse(new_doc)
        result.draw()


draw_tree(sys.argv[1:])
