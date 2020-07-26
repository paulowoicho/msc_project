"""
- This script handles the TextRank, LexRank and LSA summaries
- https://github.com/miso-belica/sumy
"""


from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import nltk
nltk.download('punkt')

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
#{lex_rank: LexRankSummarizer, lsa: LsaSummarizer, text_rank: TextRankSummarizer}

from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 2

summarizers = {'lex_rank': LexRankSummarizer, 'lsa': LsaSummarizer, 'text_rank': TextRankSummarizer}

def summarize(string, summarizer_type):
    
    # url = "https://en.wikipedia.org/wiki/Automatic_summarization"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    #from text
    parser = PlaintextParser.from_string(string, Tokenizer(LANGUAGE))
    # or for plain text files
    #parser = PlaintextParser.from_file("concatenated\\0bTrkuk4ReA2ysnhY2BaYs.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = summarizers[summarizer_type](stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    result = ''
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        result += str(sentence) + ' '

    return result



