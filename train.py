# PW6. 23B031056 Abdimutalipov Zhaxylyk
# train a simple classifier on wine dataset and save it

import joblib
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

SEED = 42

# load data
data = load_wine(as_frame=True)
X = data.data
y = data.target
print("shape:", X.shape)
print("classes:", data.target_names.tolist())

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED, stratify=y
)

# train model
model = RandomForestClassifier(n_estimators=100, random_state=SEED)
model.fit(X_train, y_train)

# evaluate
y_pred = model.predict(X_test)
print("accuracy:", round(accuracy_score(y_test, y_pred), 4))
print("f1 macro:", round(f1_score(y_test, y_pred, average="macro"), 4))
print(classification_report(y_test, y_pred, target_names=data.target_names))

# save model
joblib.dump(model, "model.joblib")
print("model saved to model.joblib")
