from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from encoder import encoding

def regression(data, state, district, year):
    STATE_MAPPINGS, DISTRICT_MAPPINGS = encoding(data)
    data['STATE/UT'] =  data['STATE/UT'].apply(lambda var : STATE_MAPPINGS[var])
    data['DISTRICT'] = data['DISTRICT'].apply(lambda var: DISTRICT_MAPPINGS[var])

    # Ensure 'YEAR' is an integer
    data['YEAR'] = data['YEAR'].astype(int)

    # Select the features and the crime types to predict
    feature_columns = ['STATE/UT', 'DISTRICT', 'YEAR']
    crime_types = ['MURDER', 'RAPE', 'THEFT', 'BURGLARY', 'ROBBERY', 'KIDNAPPING & ABDUCTION']

    # Prepare the feature matrix and the target matrix
    X = data[feature_columns]
    y = data[crime_types]

    # Check for missing values or invalid data
    if X.isnull().any().any() or y.isnull().any().any():
        raise ValueError("Dataset contains missing or invalid data")

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    state = state.upper()
    district = district.upper()

    # Collect user input for prediction
    user_input = {
        'STATE/UT': state,
        'DISTRICT': district,
        'YEAR': year
    }

    # Convert the user input to a DataFrame
    user_input_df = pd.DataFrame([user_input])

    user_input_df['STATE/UT'] = STATE_MAPPINGS[user_input_df.iloc[0,0]]
    user_input_df['DISTRICT'] = DISTRICT_MAPPINGS[user_input_df.iloc[0,1]]

    # Predict the rates for various crime types
    predicted_rates = model.predict(user_input_df)

    return crime_types, predicted_rates
