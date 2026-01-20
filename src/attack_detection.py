import numpy as np

def detect_attack(model, sample, scaler, is_dnn=False):
    sample_scaled = scaler.transform(np.array([sample]))

    if is_dnn:
        prediction = model.predict(sample_scaled).argmax(axis=1)[0]
    else:
        prediction = model.predict(sample_scaled)[0]

    return prediction
