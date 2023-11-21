import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize
from sklearn.model_selection import train_test_split
import joblib

# loading training data
data_train = pd.read_csv('scripts\dataset\pre_processed_data.csv')


X = data_train[['arrival_hour', 'arrival_minute', 'stop_sequence_x', 'route_id', 'start_stop_id', 'end_stop_id']]
y = data_train['congestion_level']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,shuffle=True)
# model initialization and fitting
clf = RandomForestClassifier(n_estimators=150)
# clf = Lasso(alpha=0.0004)
# clf = LinearRegression()
# clf = KNeighborsClassifier(n_neighbors=10)
clf.fit(X_train, y_train)



#
# predict the testing data, round() their results and store them into y_pred
# round means 4.6 will be converted into 5 while 4.4 will be converted into 4
# because minutes are not in points and round() yields better results
y_pred = clf.predict(X_test).round()

y_score = clf.predict_proba(X_test)


# print root mean squared error by comparing y_pred and y_test
# print(np.sqrt(mean_squared_error(y_test, y_pred)))

print("Accuracy score (training): {0:.3f}".format(clf.score(X_train, y_train)))
print("Accuracy score (validation): {0:.3f}".format(clf.score(X_test, y_test)))

n_classes = len(set(y_train))

Y = label_binarize(y_train, classes=[*range(n_classes)])



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
plt.title("PR CURVE FOR RANDOM FOREST")
plt.show()

# Save model
model_file = r'scripts/new_scripts/new_model/random_forest_model.joblib'
joblib.dump(clf, model_file)
print(f"Model saved to {model_file}")