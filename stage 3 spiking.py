import nltk
import os
from nltk.tokenize import word_tokenize
import gensim
import spacy
import numpy as np
import json
import pprint
spacy.prefer_gpu()

en_model = spacy.load('en_core_web_sm')
stopwords = en_model.Defaults.stop_words

def abstract_comparison(abstract_list,abstract_check_list):
    token_list = []
    for abstract in abstract_list:
        tokens_word = word_tokenize(abstract)
        tokens_word = [word for word in tokens_word if not word in stopwords]
        for word in tokens_word:
            token_list.append(word.lower())

    dictionary = gensim.corpora.Dictionary([token_list])
    gen_docs = [[w.lower() for w in word_tokenize(text)]
                for text in abstract_list]
    corpus = [dictionary.doc2bow(abstract) for abstract in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    sims = gensim.similarities.Similarity(os.path.abspath('workdir/'), tf_idf[corpus],
                                              num_features=len(dictionary))
    for line in abstract_check_list:
        query_doc = [w.lower() for w in word_tokenize(line)]
        query_doc_bow = dictionary.doc2bow(query_doc)

    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(sims[query_doc_tf_idf])


if __name__ == '__main__':
    with open("asafsdf.json",encoding="utf8") as result_file:
        file = json.load(result_file)
        abstract_list1 = file["abstract"][:3]
        abstract_list2 = [file["abstract"][-1]]
        abstract_comparison(abstract_list1,abstract_list2)


