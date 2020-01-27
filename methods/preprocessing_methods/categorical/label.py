#!/usr/bin/env python
# -*- coding: utf-8 -*-

class label(object):

    def __init__(self, file, separate):
        self.file = file
        self.separate = separate


    def transform(self):
        self.file.write('## Label Encoder Method ##\n')
        self.file.write('from sklearn.preprocessing import LabelEncoder\n\n')
        self.file.write('encoder = LabelEncoder()\n'
                        'for col in catergorical_cols:\n'
                        '\tencoder.fit(X_fit[col])\n'
                        '\tX_fit[col] = encoder.transform(X_fit[col])\n'
                        '\tX_val[col] = encoder.transform(X_val[col])\n')
        if self.separate:
            self.file.write('\tX_test[col] = encoder.transform(X_test[col])\n')
        self.file.write('\n\n')