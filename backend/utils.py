import pickle


def load_model():
    f = open("../models/sentiment_model.pickle", "rb")
    classifier = pickle.load(f)
    f.close()

    return classifier
