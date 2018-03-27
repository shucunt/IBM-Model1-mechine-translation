#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 13:23
# @Author  : shucun tian
# @File    : run.py
# @Software: PyCharm

import cPickle as pickle
from data_processing import *
from IBM_algorithm import *

if __name__ == '__main__':

    foreign_sentences_embedding, native_sentences_embedding, foreign_index_to_word, \
        native_index_to_word = RunDataProcess()
    t = Init(foreign_sentences_embedding, native_sentences_embedding)
    t = IBMAlgorithm(foreign_sentences_embedding, native_sentences_embedding, t, foreign_index_to_word\
                 , native_index_to_word)
    result_file_src = os.path.join(os.path.abspath('..'), 'result', 't.pkl')
    with open(result_file_src, 'wb') as file_write:
        pickle.dump(t, file_write)
