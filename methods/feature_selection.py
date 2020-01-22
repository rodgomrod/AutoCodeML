
class feature_selection(object):

    def __init__(self, file):

        self.file = file

        from sklearn.ensemble import RandomForestClassifier
        from eli5.sklearn import PermutationImportance


    def permutation_importance(self):
        pass

