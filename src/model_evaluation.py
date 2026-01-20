from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_classification(model, X_test, y_test, is_dnn=False):
    if is_dnn:
        y_pred = model.predict(X_test).argmax(axis=1)
    else:
        y_pred = model.predict(X_test)

    return {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average="weighted"),
        "Recall": recall_score(y_test, y_pred, average="weighted"),
        "F1 Score": f1_score(y_test, y_pred, average="weighted")
    }

