#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

class read(object):

    def __init__(self, file, data_path, separate):

        self.file = file
        self.data_path = data_path
        self.separate = separate


    def reading(self, train_path, test_path=None):

        self.file.write('## Reading Data ##\n')
        self.file.write('import pandas as pd\n')
        self.file.write('import numpy as np\n\n')

        separator = ','

        try:
            # Separator recognizer
            with open(self.data_path + train_path) as f:
                first_line = f.readline()

            for i in first_line:
                if i in [',', ' ', ';', '\t']:
                    separator = i
                    break

            f.close()

            # Header recognizer
            def has_header(file, nrows=3):
                df = pd.read_csv(file, header=None, nrows=nrows)
                df_header = pd.read_csv(file, nrows=nrows)
                return tuple(df.dtypes) != tuple(df_header.dtypes)

            header = has_header(self.data_path + train_path)
            if not header:
                header = None

        except:
            pass

        if self.separate:
            self.file.write('train = pd.read_csv("{0}", sep="{2}", header={3})\n'
            'test = pd.read_csv("{1}", sep="{2}, header={3}")\n\n'.format(self.data_path + train_path,
                                                                           self.data_path + test_path,
                                                                           separator, header))

        else:
            self.file.write('train = pd.read_csv("{0}", sep="{1}", header={2})\n\n'.format(self.data_path + train_path,
                                                                                            separator, header))

        self.file.write('columns = train.columns\n\n'
                        'categorical_cols = list()\n'
                        'for col, dt in zip(columns, train.dtypes):\n'
                            '\tif dt in ["O", "object"]:\n'
                                '\t\tcategorical_cols.append(col)\n\n')

        self.file.write('numerical_cols = '
                        '[col for col in columns if col not in categorical_cols]\n\n')


    def X_y_split(self, target_label='target', drop_cols=[]):

        self.file.write('## X, y Split ##\n\n')
        self.file.write('target_label = "{}"\n'.format(target_label))
        self.file.write('drop_cols = {}\n'.format(str(drop_cols)))
        self.file.write('y_train = train[target_label]\n')
        self.file.write('X_train = train[[x for x in train.columns if x not in [target_label]+drop_cols]]\n')
        if self.separate:
            self.file.write('y_test = test[target_label]\n')
            self.file.write('X_test = test[[x for x in X_train.columns]]\n\n')


    def fit_val_train_split(self):

        self.file.write('## Fit, val Split ##\n')
        self.file.write('from sklearn.model_selection import train_test_split\n\n')
        self.file.write('X_fit, X_val, y_fit, y_val = train_test_split(X_train, y_train,\n'
                       'test_size=0.25,\n'
                       'random_state=42)\n')









