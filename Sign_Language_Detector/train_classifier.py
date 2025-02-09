import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(x_train, y_train)

num_features_train = x_train.shape[1]
print(f"Number of features during training: {num_features_train}")

num_features_test = x_test.shape[1]
print(f"Number of features in prediction data: {num_features_test}")

y_predict = model.predict(x_test)

# print(y_predict)
score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()