#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 13:27
# @Author  : shucun tian
# @File    : data_processing.py
# @Software: PyCharm

import os
import cPickle as pickle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def ReadData(file_src):
    with open(file_src, 'rb') as file_read:
        l = file_read.readlines()
    return l

def Word2Index(sentences):
    word_to_index = {}
    index_to_word = {}
    count = 0  #NUll index is 0
    for sentence in sentences:
        for word in sentence.split():
            if not word_to_index.has_key(word.lower()):
                word_to_index[word.lower()] = count
                index_to_word[count] = word.lower()
                count += 1
    return word_to_index, index_to_word

def Sentence2Embedding(sentences, word_to_index):
    result = []
    for sentence in sentences:
        temp = []
        for word in sentence.split():
            temp.append(word_to_index[word.lower()])
        result.append(temp)
    return result

def RunDataProcess():
    foreign_file_src = os.path.join(os.path.abspath('..'), 'data', 'fbis.en.10k')
    foreign_sentences = ReadData(foreign_file_src)
    foreign_word_to_index, foreign_index_to_word = Word2Index(foreign_sentences)
    # print len(foreign_word_to_index)  # 14154
    foreign_sentences_embedding = Sentence2Embedding(foreign_sentences, foreign_word_to_index)
    native_file_src = os.path.join(os.path.abspath('..'), 'data', 'fbis.zh.10k')
    native_sentences = ReadData(native_file_src)
    # print native_sentences[0].decode('utf-8')
    native_word_to_index, native_index_to_word = Word2Index(native_sentences)
    # print len(native_word_to_index)  #17011
    native_sentences_embedding = Sentence2Embedding(native_sentences, native_word_to_index)
    index_to_word_src = os.path.join(os.path.abspath('..'), 'result', 'index2word.pkl')
    with open(index_to_word_src, 'wb') as file_write:
        pickle.dump((native_index_to_word, foreign_index_to_word),file_write )
    return foreign_sentences_embedding, native_sentences_embedding, \
           foreign_index_to_word, native_index_to_word

# if __name__ == '__main__':
#     a, b = run()


