
class prepro(object):

    def __init__(self, file):
        self.file = file


    def scale(self):
        self.file.write('## Scale Method ##\n')
        self.file.write('from sklearn.preprocessing import scale\n\n')
        self.file.write('X_train[numerical_cols] = scale(X_train[numerical_cols])\n')
        self.file.write('X_test[numerical_cols] = scale(X_test[numerical_cols])\n\n')
        self.file.write('\n\n')


    def select_scale(self, name):

        if name == 'standard':
            self.file.write('## Standard Scaler Method ##\n')
            self.file.write('from sklearn.preprocessing import StandardScaler\n\n')
            self.file.write('scaler = StandardScaler()\n')

        elif name == 'minmax':
            self.file.write('## MinMax Scaler Method ##\n')
            self.file.write('from sklearn.preprocessing import MinMaxScaler\n\n')
            self.file.write('scaler = MinMaxScaler()\n')

        elif name == 'maxabs':
            self.file.write('## MaxAbs Scaler Method ##\n')
            self.file.write('from sklearn.preprocessing import MaxAbsScaler\n\n')
            self.file.write('scaler = MaxAbsScaler()\n')

        else:
            raise ValueError('{} is not in the name list: ["standard", "minmax", "maxabs"]'.format(name))


    def scale_fit_transform(self, name):

        self.select_scale(name)
        self.file.write('scaler.fit(X_train[numerical_cols])\n'
                        'X_train[numerical_cols] = scaler.transform(X_train[numerical_cols])\n'
                        'X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])\n\n')
        self.file.write('\n\n')


    def select_cat_transform(self, name):

        if name == 'label':
            self.file.write('## Label Encoder Method ##\n')
            self.file.write('from sklearn.preprocessing import LabelEncoder\n\n')
            self.file.write('encoder = LabelEncoder()\n'
                            'for col in catergorical_cols:\n'
                                '\tencoder.fit(X_train[col])\n'
                                '\tX_train[col] = encoder.transform(X_train[col])\n'
                                '\tX_test[col] = encoder.transform(X_test[col])\n')


        elif name == 'ohehot':
            self.file.write('## OneHot Encoder Method ##\n\n')
            '''
            # Optional Method (sklearn)
            self.file.write('from sklearn.preprocessing import OneHotEncoder\n\n')
            self.file.write('encoder = OneHotEncoder(sparse=False)\n'
                            'encoder.fit(X_train[catergorical_cols])\n'
                            'X_train[categorical_cols] = encoder.transform(X_train[catergorical_cols])\n'
                            'X_test[categorical_cols] = encoder.transform(X_test[catergorical_cols])\n')
            '''

            self.file.write('train_shape = X_train.shape[0]\n'
                            'full_df = pd.concat([X_train, X_test], axis=0)\n'
                            'for col in catergorical_cols:\n'
                                '\tdf_dummies = pd.get_dummies(full_df[col], prefix=col)\n'
                                '\tfull_df = pd.concat([full_df.drop(col, axis=1), df_dummies], axis=1)\n\n'
                            'X_train = full_df[:train_shape]\n'
                            'X_test = full_df[train_shape:]\n\n'
                            'del full_df\n'
                            'gc.collect()\n\n')

        elif name == 'freq':
            self.file.write('## Frequency Encoder Method ##\n\n')
            self.file.write('def freq_parser(x):\n'
                                '\ttry:\n'
                                    '\t\treturn dict_freq(x)\n'
                                '\texcept:\n'
                                    '\t\treturn len(dict_freq)\n\n')

            self.file.write('for col in catergorical_cols:\n'
                                '\tcategories = X_train[col].value_counts().index.tolist()\n'
                                '\tdict_freq = dict()\n'
                                '\tfor i, cat in enumerate(categories):\n'
                                    '\t\tdict_freq[cat] = i\n\n'
                                '\tX_train[col] = X_train[col].apply(lambda x: freq_parser(x))\n'
                                '\tX_test[col] = X_test[col].apply(lambda x: freq_parser(x))\n')


