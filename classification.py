import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from encoder import encoding

def classification(data, state, district, year):
    # Feature columns for classification
    feature_columns = ['STATE/UT', 'DISTRICT', 'YEAR']

    # Define a crime profile threshold (using total IPC crimes)
    threshold = data['TOTAL IPC CRIMES'].median()  # Separate high-crime and low-crime
    data['CRIME_PROFILE'] = (data['TOTAL IPC CRIMES'] > threshold).astype(int)  # 1 for high-crime, 0 for low-crime

    STATE_MAPPINGS, DISTRICT_MAPPINGS = encoding(data)
    data['STATE/UT'] =  data['STATE/UT'].apply(lambda var : STATE_MAPPINGS[var])
    data['DISTRICT'] = data['DISTRICT'].apply(lambda var: DISTRICT_MAPPINGS[var])

    # Prepare features and target for the model
    X = data[feature_columns]
    y = data['CRIME_PROFILE']

    # Split data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    user_input = {
    'STATE/UT': state.upper(),
    'DISTRICT': district.upper(),
    'YEAR': year  # Initialize to None to handle invalid input
    }

    user_input_df = pd.DataFrame([user_input])

    user_input_df['STATE/UT'] = STATE_MAPPINGS[user_input_df.iloc[0,0]]
    user_input_df['DISTRICT'] = DISTRICT_MAPPINGS[user_input_df.iloc[0,1]]

    predicted_profile = model.predict(user_input_df)

    classification_result = "High-Crime" if predicted_profile[0] == 1 else "Low-Crime"

    return classification_result
