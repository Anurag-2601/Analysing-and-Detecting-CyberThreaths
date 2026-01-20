def train_autoencoder(model, X_train):
    model.fit(
        X_train, X_train,
        epochs=30,
        batch_size=64,
        verbose=1
    )
    return model

def train_dnn(model, X_train, y_train):
    model.fit(
        X_train, y_train,
        epochs=30,
        batch_size=32,
        verbose=1
    )
    return model

