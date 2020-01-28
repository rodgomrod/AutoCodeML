#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .validation_methods.stratifiedkfold import *
from .validation_methods.groupkfold import *
from .validation_methods.timeseriessplit import *

class validation(skf, gkf, tss):

    def __init__(self, file, how_val, separate):

        self.file = file
        self.how_val = how_val
        self.separate = separate

        skf.__init__(self, file=self.file)
        gkf.__init__(self, file=self.file)
        tss.__init__(self, file=self.file)


    def validation_iterator(self):
        self.file.write('counter = 1\n'
                        'auc_score = 0\n'
                        'iterat = 0\n'
                        'list_iter = list()\n')
        if self.separate:
            self.file.write('y_preds = np.zeros(X_test.shape[0])\n')
        else:
            self.file.write('y_preds = np.zeros(X_val.shape[0])\n')

        self.file.write('importances = np.zeros(X_fit.shape[1])\n\n'

                        'for train_index, test_index in fold_strategy:\n'
                        '\tprint("Training fold {}".format(counter))\n'
                        '\tX_batch_fit, X_batch_val = X_fit.iloc[train_index, :], X_val.iloc[test_index, :]\n'
                        '\ty_batch_fit, y_batch_val = y_fit.iloc[train_index], y_val.iloc[test_index]\n'
                        '\tmodel.fit(X_batch_fit, '
                        'y_batch_fit, '
                        'eval_set=[(X_batch_val, y_batch_val)], '
                        'verbose=50, '
                        'early_stopping_rounds=10)\n'
                        '\tprint("Best AUC in this fold: {}".format(model.best_score_["valid_0"]["auc"]))\n'
                        '\tprint("Best iteration in this fold: {}".format(model.best_iteration_))\n'
                        '\tauc_score += model.best_score_["valid_0"]["auc"]\n'
                        '\tit = model.best_iteration_\n'
                        '\titerat += it\n'
                        '\tlist_iter.append(it)\n'
                        '\timportances += model.feature_importances_ / k\n')
        if self.separate:
            self.file.write('\tpredictions = model.predict_proba(X_test)[:, 1]\n')
        else:
            self.file.write('\tpredictions = model.predict_proba(X_val)[:, 1]\n')

        self.file.write('\ty_preds += predictions / k\n'
                        '\tcounter += 1\n\n'

                        'mean_auc_score = auc_score / k\n'
                        'mean_iterat = iterat / k\n\n'

                        'print("Mean AUC in {0} folds: {1}".format(k, mean_auc_score))\n'
                        'print("Mean iterations in {0} folds: {1}".format(k, mean_iterat))\n\n'
                        )


    def create(self):

        self.file.write('k = 5 # number of folds\n\n')

        if self.how_val == 'sfk':
            skf.create(self)
        elif self.how_val == 'gkf':
            gkf.create(self)
        elif self.how_val == 'tss':
            tss.create(self)
        else:
            raise ValueError('{} is not in the how list: ["sfk", "gkf", "tss"]'.format(self.how))

        self.validation_iterator()




