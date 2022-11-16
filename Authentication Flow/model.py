from a import create_model
import joblib


def predict(x):
    # print(attrs)
    # print(ecg)
    create_model()

    m_jlib = joblib.load(r'C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Authentication Flow\model1.pkl')

    return m_jlib.predict([x])


# predict([59, 1, 0, 170, 326, 0, 0, 140, 0])
