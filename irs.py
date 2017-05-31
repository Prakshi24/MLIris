from sklearn import svm
from sklearn import datasets
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score #works
import yaml
clf = svm.SVC()
iris = datasets.load_iris()
validation_size = 0.30
X, Y = iris.data, iris.target
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=validation_size)
clf.fit(X_train, Y_train)
predictions = clf.predict(X_test)
print(accuracy_score(Y_test, predictions))
accuracy = float(accuracy_score(Y_test, predictions))
print type(accuracy)

data = dict(
	acc = accuracy,
	acc2 = 0.5)
with open('data.yml', 'w') as outfile:
	yaml.dump(data, outfile, default_flow_style=False)
	