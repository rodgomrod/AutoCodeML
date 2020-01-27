
class lgb(object):

    def __init__(self, file, mode, params):

        self.file = file
        self.mode = mode
        self.params = params


    def create_model(self):

        self.file.write('## LightGBM ##\n')
        self.file.write('import lightgbm as lgb\n\n')

        self.file.write('params = {}'.format(str(self.params)))

        if self.mode == 'classifier':
            self.file.write('model = lgb.LGBMClassifier(**params)\n\n')
        elif self.mode == 'regressor':
            self.file.write('model = lgb.LGBMRegressor(**params)\n\n')


