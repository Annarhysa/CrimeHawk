from sklearn.preprocessing import LabelEncoder
import pandas as pd

def encoding(data):

    encoder = LabelEncoder()

    encoder.fit(data['STATE/UT'])
    STATE_MAPPINGS = dict(zip(encoder.classes_,encoder.transform(encoder.classes_)))

    encoder.fit(data['DISTRICT'])
    DISTRICT_MAPPINGS = dict(zip(encoder.classes_,encoder.transform(encoder.classes_)))

    return STATE_MAPPINGS, DISTRICT_MAPPINGS

