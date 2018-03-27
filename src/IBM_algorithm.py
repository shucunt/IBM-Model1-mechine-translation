#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 13:27
# @Author  : shucun tian
# @File    : IBM_algorithm.py
# @Software: PyCharm

def Init(foreign_sentences_embedding, native_sentences_embedding):
    t = {}  #key is (native, foreign)
    for sentence_index in xrange(len(foreign_sentences_embedding)):
        for word_index in xrange(len(native_sentences_embedding[sentence_index])):
            # if t.has_key((native_sentences_embedding[sentence_index][word_index], 0)):
            #     #native word map to NULL, NULL's index is 0
            #     t[(native_sentences_embedding[sentence_index][word_index], 0)] += 1
            # else:
            #     t[(native_sentences_embedding[sentence_index][word_index], 0)] = 1
            for i in xrange(len(foreign_sentences_embedding[sentence_index])):
                if t.has_key((native_sentences_embedding[sentence_index][word_index], \
                              foreign_sentences_embedding[sentence_index][i])):
                    t[(native_sentences_embedding[sentence_index][word_index], \
                              foreign_sentences_embedding[sentence_index][i])] += 1
                else:
                    t[(native_sentences_embedding[sentence_index][word_index], \
                       foreign_sentences_embedding[sentence_index][i])] = 1
    for key in t.keys():
        t[key] = (1.0/t[key])
    return t

def IBMAlgorithm(foreign_sentences_embedding, native_sentences_embedding, t, \
                 foreign_index_to_word, native_index_to_word):
    threshold = 1e-3
    avg_change = 1
    s = {}
    count = {}
    total = {}
    while avg_change > threshold:
        print avg_change
        sum_change = 0.0
        count.clear()
        total.clear()
        for sentence_index in xrange(len(foreign_sentences_embedding)):
            s.clear()
            for native_word in native_sentences_embedding[sentence_index]:
                s[native_word] = 0.0
                for foreign_word in foreign_sentences_embedding[sentence_index]:
                    s[native_word] += t[(native_word, foreign_word)]
            for native_word in native_sentences_embedding[sentence_index]:
                for foreign_word in foreign_sentences_embedding[sentence_index]:
                    if count.has_key((native_word, foreign_word)):
                        count[(native_word, foreign_word)] += (t[(native_word, foreign_word)] / s[native_word])
                    else:
                        count[(native_word, foreign_word)] = (t[(native_word, foreign_word)] / s[native_word])
                    if total.has_key((foreign_word)):
                        total[foreign_word] += (t[(native_word, foreign_word)] / s[native_word])
                    else:
                        total[foreign_word] = (t[(native_word, foreign_word)] / s[native_word])
        for foreign_word in foreign_index_to_word:
            for native_word in native_index_to_word:
                if count.has_key((native_word, foreign_word)):
                    new_t = count[(native_word, foreign_word)] / total[foreign_word]
                    sum_change += abs(new_t - t[(native_word, foreign_word)])
                    t[(native_word, foreign_word)] = new_t
        avg_change = sum_change / len(t)
    return t


