#!/usr/bin/env python
# -*- coding: utf-8 -*-

from methods.reading import *
from methods.preprocessing import *
from methods.feature_selection import *
from methods.modeling import *
from methods.validation import *

import sys, os


class main(read, prepro, feature_selection, model, validation):

    def __init__(self, file, data_path, separate, how_cat, how_num, how_ft_sel, mode, params, alg, how_val):
        self.file = file
        self.data_path = data_path
        self.separate = separate
        self.how_cat = how_cat
        self.how_num = how_num
        self.how_ft_sel = how_ft_sel
        self.mode = mode
        self.params = params
        self.alg = alg
        self.how_val = how_val

        read.__init__(self, file=self.file, data_path=self.data_path, separate=self.separate)
        prepro.__init__(self, file=self.file, separate=self.separate,
                        how_cat=self.how_cat, how_num=self.how_num)
        feature_selection.__init__(self, file=self.file, how_ft_sel=self.how_ft_sel)
        model.__init__(self, file=self.file, mode=self.mode, params=self.params, alg=self.alg)
        validation.__init__(self, file=self.file, how_val=self.how_val, separate=self.separate)

    def data_reading(self, train_path, test_path=None, target_label='target', drop_cols=[]):
        read.reading(self, train_path, test_path)

        read.X_y_split(self, target_label=target_label, drop_cols=drop_cols)

        read.fit_val_train_split(self)

    def data_preprocessing(self):
        prepro.transform(self)

    def data_ft_selection(self):
        feature_selection.select_ft_method(self)

    def model_selection(self):
        model.create(self)

    def model_validation(self):
        validation.create(self)

    def title_maker(self, text):
        self.file.write('\n\n')
        len_text = len(text)
        self.file.write('{0}\n'.format('#' * 42 + (len_text * '#')))
        self.file.write('{0} {1} {2}\n'.format('#' * 20, text.upper(), '#' * 20))
        self.file.write('{0}\n'.format('#' * 42 + (len_text * '#')))
        self.file.write('\n\n')


if __name__ == '__main__':
    file_name = sys.argv[1]
    data_path = sys.argv[2]
    separate = eval(sys.argv[3])
    how_cat = sys.argv[4]
    how_num = sys.argv[5]
    how_ft_sel = sys.argv[6]
    mode = sys.argv[7]
    params = str(sys.argv[8])
    alg = sys.argv[9]
    how_val = sys.argv[10]
    train_path = sys.argv[11]
    test_path = sys.argv[12]
    target_label = sys.argv[13]
    drop_cols = sys.argv[14]

    file_path = '/'.join(file_name.split('/')[:-1])
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file = open(file_name, 'w')
    file.write('#!/usr/bin/env python\n# -*- coding: utf-8 -*-')

    project = main(file, data_path, separate, how_cat, how_num, how_ft_sel, mode, params, alg, how_val)

    project.title_maker('reading data')
    project.data_reading(train_path, test_path, target_label, drop_cols)

    project.title_maker('preprocessing data')
    project.data_preprocessing()

    project.title_maker('feature selection')
    project.data_ft_selection()

    project.title_maker('model selection')
    project.model_selection()

    project.title_maker('model validation')
    project.model_validation()

    file.close()
