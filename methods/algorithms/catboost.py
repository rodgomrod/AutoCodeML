
class cat(object):

    def __init__(self, file, mode, params):

        self.file = file
        self.mode = mode
        self.params = params


    def create_model(self):

        self.file.write('## CatBoost ##\n')
        self.file.write('import catboost\n\n')

        self.file.write('params = {}\n'.format(str(self.params)))

        if self.mode == 'classifier':
            self.file.write('model = catboost.CatBoostClassifier(**params)\n\n')
        elif self.mode == 'regressor':
            self.file.write('model = catboost.CatBoostRegressor(**params)\n\n')

