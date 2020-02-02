#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
#################### READING DATA ####################
######################################################

## Reading Data ##
import pandas as pd
import numpy as np

train = pd.read_csv("datasets/iris.data", sep=",", header=None)
test = pd.read_csv("datasets/None", sep=",", header=None)

columns = train.columns

categorical_cols = list()
for col, dt in zip(columns, train.dtypes):
	if dt in ["O", "object"]:
		categorical_cols.append(col)

numerical_cols = [col for col in columns if col not in categorical_cols]


## X, y Split ##

target_label = "None"
drop_cols = []
y_train = train[target_label]
X_train = train[[x for x in train.columns if x not in [target_label]+drop_cols]]
y_test = test[target_label]
X_test = test[[x for x in X_train.columns]]

## Fit, val Split ##
from sklearn.model_selection import train_test_split

X_fit, X_val, y_fit, y_val = train_test_split(X_train, y_train,
test_size=0.25,
random_state=42)


############################################################
#################### PREPROCESSING DATA ####################
############################################################

## Frequency Encoder Method ##

def freq_parser(x):
	try:
		return dict_freq[x]
	except:
		return len(dict_freq)

for col in categorical_cols:
	categories = X_fit[col].value_counts().index.tolist()
	dict_freq = dict()
	for i, cat in enumerate(categories):
		dict_freq[cat] = i

	X_fit[col] = X_fit[col].apply(lambda x: freq_parser(x))
	X_val[col] = X_val[col].apply(lambda x: freq_parser(x))
	X_test[col] = X_test[col].apply(lambda x: freq_parser(x))


## Standard Scaler Method ##
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_fit[numerical_cols])
X_fit[numerical_cols] = scaler.transform(X_fit[numerical_cols])
X_val[numerical_cols] = scaler.transform(X_val[numerical_cols])

X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])


###########################################################
#################### FEATURE SELECTION ####################
###########################################################

## Permutation Importance with RadomForest ##
from sklearn.ensemble import RandomForestClassifier
from eli5.sklearn import PermutationImportance

model_rf = RandomForestClassifier(n_estimators=200, oob_score=True, n_jobs=-1, random_state=42, max_depth=6)

model_rf.fit(X_fit, y_fit)
perm_rf = PermutationImportance(model_rf).fit(X_val, y_val)

df_perm = pd.DataFrame({"feature": X_fit.columns, "Importance": perm_rf.feature_importances_}).sort_values("Importance", ascending=False)
df_perm.head()
# df_imp["Importance"] = df_imp["Importance"]/df_imp["Importance"].max()

# plt.figure(figsize=(14, 25))
# sns.barplot(x="Importance", y="Feature", data=df_imp)
# plt.title("Feature Importance")
# plt.tight_layout()
# ft_imp_path = "x"
# plt.savefig(ft_imp_path + ".png")
# plt.close()

# path_out = "x"
# file_name = "{0}_PermutationImportance_RF.csv".format(path_out)
#df_perm.to_csv(file_name, header=True, index=None)



#########################################################
#################### MODEL SELECTION ####################
#########################################################

## LightGBM ##
import lightgbm as lgb

params = {'num_leaves': 31, 'max_depth': 4, 'max_leaf_nodes': 10, 'min_sample_leaf': 20, 'first_metric_only': 1, 'n_estimators': 5000, 'num_threads': -1, 'learning_rate': 0.01, 'colsample_bytree': 0.6, 'bagging_fraction': 0.7, 'bagging_freq': 5, 'importance_type': 'gain', 'bagging_seed': 42, 'random_state':42, 'seed': 42, 'feature_fraction_seed': 42, 'drop_seed': 42, 'data_random_seed': 42}
model = lgb.LGBMClassifier(**params)



##########################################################
#################### MODEL VALIDATION ####################
##########################################################

k = 5 # number of folds

## Stratified K Fold ##
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)

fold_strategy = skf.split(X_train, y_train)

counter = 1
auc_score = 0
iterat = 0
list_iter = list()
y_preds = np.zeros(X_test.shape[0])
importances = np.zeros(X_fit.shape[1])

for train_index, test_index in fold_strategy:
	print("Training fold {}".format(counter))
	X_batch_fit, X_batch_val = X_fit.iloc[train_index, :], X_val.iloc[test_index, :]
	y_batch_fit, y_batch_val = y_fit.iloc[train_index], y_val.iloc[test_index]
	model.fit(X_batch_fit, y_batch_fit, eval_set=[(X_batch_val, y_batch_val)], verbose=50, early_stopping_rounds=10)
	print("Best AUC in this fold: {}".format(model.best_score_["valid_0"]["auc"]))
	print("Best iteration in this fold: {}".format(model.best_iteration_))
	auc_score += model.best_score_["valid_0"]["auc"]
	it = model.best_iteration_
	iterat += it
	list_iter.append(it)
	importances += model.feature_importances_ / k
	predictions = model.predict_proba(X_test)[:, 1]
	y_preds += predictions / k
	counter += 1

mean_auc_score = auc_score / k
mean_iterat = iterat / k

print("Mean AUC in {0} folds: {1}".format(k, mean_auc_score))
print("Mean iterations in {0} folds: {1}".format(k, mean_iterat))

