
class lgb(object):

    def __init__(self, file, mode):

        self.file = file
        self.mode = mode


    def create_model(self):

        self.file.write('## LightGBM ##\n')
        self.file.write('import lightgbm as lgb\n\n')

        if self.mode == 'classifier':
            self.file.write('model = lgb.LGBMClassifier()\n')
        elif self.mode == 'regressor':
            self.file.write('model = lgb.LGBMRegressor()\n')


