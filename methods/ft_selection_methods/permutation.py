#!/usr/bin/env python
# -*- coding: utf-8 -*-

class permutation_importance(object):

    def __init__(self, file):

        self.file = file


    def select(self):

        self.file.write('## Permutation Importance with RadomForest ##\n')
        self.file.write('from sklearn.ensemble import RandomForestClassifier\n')
        self.file.write('from eli5.sklearn import PermutationImportance\n\n')
        self.file.write('model_rf = RandomForestClassifier(n_estimators=200, oob_score=True, n_jobs=-1, '
                        'random_state=42, max_depth=6)\n\n'
                        'model_rf.fit(X_fit, y_fit)\n'
                        'perm_rf = PermutationImportance(model_rf).fit(X_val, y_val)\n\n'
                        'df_perm = pd.DataFrame({"feature": X_fit.columns, "Importance": perm_rf.feature_importances_})'
                        '.sort_values("Importance", ascending=False)\n'
                        'df_perm.head()\n'
                        '# df_imp["Importance"] = df_imp["Importance"]/df_imp["Importance"].max()\n\n'
                        '# plt.figure(figsize=(14, 25))\n'
                        '# sns.barplot(x="Importance", y="Feature", data=df_imp)\n'
                        '# plt.title("Feature Importance")\n'
                        '# plt.tight_layout()\n'
                        '# ft_imp_path = "x"\n'
                        '# plt.savefig(ft_imp_path + ".png")\n'
                        '# plt.close()\n\n'
                        '# path_out = "x"\n'
                        '# file_name = "{0}_PermutationImportance_RF.csv".format(path_out)\n'
                        '#df_perm.to_csv(file_name, header=True, index=None)\n\n')