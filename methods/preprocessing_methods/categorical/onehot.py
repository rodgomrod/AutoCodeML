#!/usr/bin/env python
# -*- coding: utf-8 -*-

class onehot(object):

    def __init__(self, file, separate):
        self.file = file
        self.separate = separate


    def transform(self):
        self.file.write('## OneHot Encoder Method ##\n\n')

        '''
        # Optional Method (sklearn)
        self.file.write('from sklearn.preprocessing import OneHotEncoder\n\n')
        self.file.write('encoder = OneHotEncoder(sparse=False)\n'
                        'encoder.fit(X_fit[catergorical_cols])\n'
                        'X_fit[categorical_cols] = encoder.transform(X_fit[catergorical_cols])\n'
                        'X_val[categorical_cols] = encoder.transform(X_val[catergorical_cols])\n'
                        'X_test[categorical_cols] = encoder.transform(X_test[catergorical_cols])\n')
        '''

        self.file.write('fit_shape = X_fit.shape[0]\n'
                        'val_shape = X_val.shape[0]\n')
        if self.separate:
            self.file.write('full_df = pd.concat([X_fit, X_val, X_test], axis=0)\n'
                            'for col in catergorical_cols:\n'
                            '\tdf_dummies = pd.get_dummies(full_df[col], prefix=col)\n'
                            '\tfull_df = pd.concat([full_df.drop(col, axis=1), df_dummies], axis=1)\n\n'
                            'X_fit = full_df[:fit_shape]\n'
                            'X_val = full_df[fit_shape:fit_shape+val_shape]\n'
                            'X_test = full_df[fit_shape+val_shape:]\n\n')
        else:
            self.file.write('full_df = pd.concat([X_fit, X_val], axis=0)\n'
                            'for col in catergorical_cols:\n'
                            '\tdf_dummies = pd.get_dummies(full_df[col], prefix=col)\n'
                            '\tfull_df = pd.concat([full_df.drop(col, axis=1), df_dummies], axis=1)\n\n'
                            'X_fit = full_df[:fit_shape]\n'
                            'X_val = full_df[fit_shape:]\n\n')

        self.file.write('del full_df\n'
                        'gc.collect()\n\n')
