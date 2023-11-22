import pandas as pd
from sklearn.metrics import precision_recall_curve
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import joblib

# loading training data
data_train = pd.read_csv('scripts\dataset\pre_processed_data.csv')


X = data_train[['arrival_hour', 'arrival_minute', 'stop_sequence_x', 'route_id', 'start_stop_id', 'end_stop_id']]
y = data_train['congestion_level']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,shuffle=True)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


#for learning_rate in lr_list:
gb_clf = GradientBoostingClassifier(n_estimators=1000, learning_rate=1, max_features=9, max_depth=2, random_state=42)
gb_clf.fit(X_train, y_train)
y_pred = gb_clf.predict(X_test).round()



y_score = gb_clf.predict_proba(X_test)

print("Accuracy score (training): {0:.3f}".format(gb_clf.score(X_train, y_train)))
print("Accuracy score (validation): {0:.3f}".format(gb_clf.score(X_test, y_test)))

# model initialization and fitting
# fit model no training data
# fit model no training data
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
plt.title("PR CURVE FOR GRADIENT BOOST")
plt.show()


# Save model
model_file = r'scripts/new_scripts/new_model/gradient_boost_model.joblib'
joblib.dump(gb_clf, model_file)
print(f"Model saved to {model_file}")