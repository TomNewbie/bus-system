import pandas as pd
from sklearn.metrics import precision_recall_curve
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import joblib

# loading training data
data_train = pd.read_csv('scripts\dataset\pre_processed_data.csv')


X = data_train[['arrival_hour', 'arrival_minute', 'stop_sequence_x', 'route_id', 'start_stop_id', 'end_stop_id']]
y = data_train['congestion_level']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model initialization and fitting
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(X_train)
# Apply transform to both the training set and the test set.
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
# optimizer "newton-cg", "sag", "lbfgs" and "liblinear"
#model = LogisticRegression(solver = 'newton-cg')
#model = LogisticRegression(class_weight='balanced')


model = LogisticRegression(solver = 'sag')
model.fit(X_train, y_train)
# use the model to make predictions with the test data
y_pred = model.predict(X_test).round()
y_score = model.predict_proba(X_test)
# how did our model perform?
count_misclassified = (y_test != y_pred).sum()
# print('Misclassified samples: {}'.format(count_misclassified))


#Use score method to get accuracy of model
print("Accuracy score (training): {0:.3f}".format(model.score(X_train, y_train)))
print("Accuracy score (validation): {0:.3f}".format(model.score(X_test, y_test)))


# test last record in test.csv manually and the answer is correct which is 4 minutes i.e. 240 seconds
# print("(((((((())))))))")
# # test last record in test.csv manually and the answer is correct which is 4 minutes i.e. 240 seconds
# print(precision_recall_fscore_support(y_test, y_pred, average='micro'))
# print('accuracy score', accuracy_score(y_test,y_pred))
# print(confusion_matrix(y_test,y_pred))
# print(classification_report(y_test,y_pred))

# print(metrics.confusion_matrix(y_test, y_pred))

# # Print the precision and recall, among other metrics
# print(metrics.classification_report(y_test, y_pred, digits=5))

values = y_test
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)

onehot_encoder = OneHotEncoder(sparse_output=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
#precision, recall, thresholds = precision_recall_curve(y_test,y_pred)
## precision recall curve
precision = dict()
recall = dict()
for i in range(5):
    precision[i], recall[i], _ = precision_recall_curve(onehot_encoded[:, i],
                                                        y_score[:, i])
    plt.plot(recall[i], precision[i], lw=5, label='class {}'.format(i))

plt.xlabel("recall")
plt.ylabel("precision")
plt.legend(loc="best")
plt.title("PR CURVE FOR LOGISTIC REGESSION")
plt.show()


# Save model
model_file = r'scripts/new_scripts/new_model/logistic_regession_model.joblib'
joblib.dump(model, model_file)
print(f"Model saved to {model_file}")