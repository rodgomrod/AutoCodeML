#!/usr/bin/env python
# -*- coding: utf-8 -*-

class scale(object):

    def __init__(self, file, separate):
        self.file = file
        self.separate = separate


    def transform(self):
        self.file.write('## Scale Method ##\n')
        self.file.write('from sklearn.preprocessing import scale\n\n')
        self.file.write('X_fit[numerical_cols] = scale(X_fit[numerical_cols])\n')
        self.file.write('X_val[numerical_cols] = scale(X_val[numerical_cols])\n')
        if self.separate:
            self.file.write('X_test[numerical_cols] = scale(X_test[numerical_cols])\n')
        self.file.write('\n\n')