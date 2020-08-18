import csv
import numpy as np
data_benign1 = np.genfromtxt('a1.csv',delimiter=',')
data_benign2 = np.genfromtxt('a2.csv',delimiter=',')
data_benign3 = np.genfromtxt('a3.csv',delimiter=',')
data_botnet1 = np.genfromtxt('a4.csv',delimiter=',')
data_botnet2 = np.genfromtxt('a5.csv',delimiter=',')
# data_trojandropper = np.genfromtxt('a6.csv',delimiter=',')
data = np.concatenate((data_botnet1, data_benign1, data_benign2, data_benign3))
y = np.ones(data_botnet1.shape[0])
y = np.concatenate((y, np.zeros(data_benign1.shape[0]+data_benign2.shape[0]+data_benign3.shape[0])))

print(y[-1])

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data,y,test_size=0.75)
clf = RandomForestClassifier(n_estimators=5)
clf.fit(X_train,y_train)

clf.score(X_test,y_test)

from sklearn.metrics import confusion_matrix
y_pred = clf.predict(X_test)
confusion_matrix(y_test, y_pred)

import pickle
rf = RandomForestClassifier(n_estimators=5)
rf.fit(X_train, y_train)

# with open('dynamic_model', 'wb') as f:
#     pickle.dump(rf, f)

# with open('/content/dynamic_model', 'rb') as f:
#     rf = pickle.load(f)
# rf.score(X_test, y_test)
