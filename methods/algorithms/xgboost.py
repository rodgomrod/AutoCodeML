#!/usr/bin/env python
# -*- coding: utf-8 -*-


class xgb(object):

    def __init__(self, file, mode, params):

        self.file = file
        self.mode = mode
        self.params = params


    def create_model(self):

        self.file.write('## XGBoost ##\n')
        self.file.write('import xgboost as xgb\n\n')

        self.file.write('params = {}\n'.format(str(self.params)))

        if self.mode == 'classifier':
            self.file.write('model = xgb.XGBClassifier(**params)\n\n')
        elif self.mode == 'regressor':
            self.file.write('model = xgb.XGBRegressor(**params)\n\n')

