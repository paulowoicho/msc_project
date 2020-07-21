"""
Simple extractive model that generates summaries based on sentence weights

https://blog.floydhub.com/gentle-introduction-to-text-summarization-in-machine-learning/
"""
#libraries
# import nltk
# nltk.download('punkt')
import sys
from pathlib import Path
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize


def create_dict_table(input):
    stop_words = set(stopwords.words("english"))

    words = word_tokenize(input)

    stemmer = PorterStemmer()

    frequency_table = {}

    for word in words:
        word = stemmer.stem(word)
        if word in stop_words:
            pass
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1
    
    return frequency_table

def calculate_sentence_scores(sentences, frequency_table):
    sentence_weight = {}

    for sentence in sentences:
        sentence_wordcount = len(word_tokenize(sentence))
        sentence_wordcount_no_stopwords = 0
        for word_weight in frequency_table:
            if word_weight in sentence.lower():
                sentence_wordcount_no_stopwords += 1
                if sentence[:7] in sentence_weight:
                    sentence_weight[sentence[:7]] += frequency_table[word_weight]
                else:
                    sentence_weight[sentence[:7]] = frequency_table[word_weight]
        
        sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_no_stopwords
    
    return sentence_weight


def calculate_average_score(sentence_weight):
    sum_values = 0
    for entry in sentence_weight:
        sum_values += sentence_weight[entry]
    
    average_score = (sum_values / len(sentence_weight))

    return average_score

def get_article_summary(sentences, sentence_weight, threshold):
    sentence_counter = 0
    article_summary = ''

    for sentence in sentences:
        if sentence[:7] in sentence_weight and sentence_weight[sentence[:7]] >= (threshold):
            article_summary += ' ' + sentence
            sentence_counter += 1
    
    return article_summary


def run_article_summary(article):
    frequency_table = create_dict_table(article)

    sentences = sent_tokenize(article)

    sentence_scores = calculate_sentence_scores(sentences, frequency_table)

    threshold = calculate_average_score(sentence_scores)

    article_summary = get_article_summary(sentences, sentence_scores, 1.5 * threshold)

    return article_summary

if __name__ == '__main__':
    podcast = sys.argv[1]
    file = open(podcast ,mode='r')
    article_content = file.read()
    file.close()
    summary_results = run_article_summary(article_content)
    f = open('summaries/simple_extractive_summaries/'+ Path(podcast).stem + '_summary.txt', "a")
    f.write(summary_results)
    f.close()