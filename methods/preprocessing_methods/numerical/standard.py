#!/usr/bin/env python
# -*- coding: utf-8 -*-

class standard(object):

    def __init__(self, file, separate):
        self.file = file
        self.separate = separate


    def transform(self):
        self.file.write('## Standard Scaler Method ##\n')
        self.file.write('from sklearn.preprocessing import StandardScaler\n\n')
        self.file.write('scaler = StandardScaler()\n')
        self.file.write('scaler.fit(X_fit[numerical_cols])\n'
                        'X_fit[numerical_cols] = scaler.transform(X_fit[numerical_cols])\n'
                        'X_val[numerical_cols] = scaler.transform(X_val[numerical_cols])\n\n')
        if self.separate:
            self.file.write('X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])\n')
