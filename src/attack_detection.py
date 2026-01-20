import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def load_dataset(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df, label_column):
    df = df.dropna()

    X = df.drop(columns=[label_column])
    y = df[label_column]

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train, y_test, scaler

