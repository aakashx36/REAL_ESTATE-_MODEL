import streamlit as st 
import pandas as pd 
import joblib

st.title("Real Estate Price Evaluation app ")
st.sidebar.title('About the Model')
st.sidebar.markdown('''
### Real Estate Price Evaluation Model 

This model predicts **real estate property prices** based on the following key features:
-  **State:** Location of the property.
-  **Number of Bedrooms**
-  **Number of Bathrooms**
-  **Lot Area** (in square meters)
-  **Categorical Features:** Size categories for bedrooms and bathrooms (small, medium, large, invalid).
-  **Living Area** (in square meters)
-  **Risk Evaluation:** Considers flood, earthquake, storm, criminal activities near the property, and the age of the structure (if the living area is not zero).

---

### Model Details
- The model is built using a **Random Forest Regressor**.
- Features include **state encoding, bedroom size encoding, and bathroom size encoding.**
- Hyperparameters are carefully tuned to **reduce overfitting and improve model reliability.**

---

### Usage Instructions
Adjust the input features in the sidebar to get an estimated property price.

---

''')

### Model Accuracy Display
model_accuracy = 0.63  # Or load this dynamically if needed
st.sidebar.write(f'**Model Performance:**  \n{model_accuracy * 100:.2f}% Variance Explained')

st.markdown('---')


st.write("""

### Model Considerations and Observations

**It is important to note that the model’s predictions are strongly influenced by size-related features, such as the number of bedrooms, number of bathrooms, living area, and lot area.**  
**These features naturally have a high impact on property prices and tend to dominate the model’s decision-making process.**

**As a result, the model may occasionally predict higher prices for properties with larger sizes, even if those properties are classified as high risk.**  
**This occurs because the model prioritizes size over risk in many scenarios, especially when the property’s physical attributes are substantial.**

While this reflects trends in the historical data, future improvements could involve:
- **Feature scaling** to balance the influence of size and risk features.
- **Interaction terms** to help the model understand how risk should adjust size-based pricing.
- **Risk-aware loss functions** that penalize high-price predictions for high-risk properties.
- **Additional data balancing techniques** to ensure that risk receives adequate attention during training.

These enhancements would help the model generate more **risk-sensitive and balanced price predictions.**

""")

# Separator line
st.markdown('---')

size_mapping = {'small': 1, 'medium': 2, 'large': 3, 'Invalid': 0}

df = pd.read_csv('./clean_datasets/real_estate_encoded.csv')  # Your file with State and State_Encoded columns

selected_state = st.selectbox('Select State', df['state'].unique())
state_encoded = df.loc[df['state'] == selected_state, 'state_encoded'].values[0]

st.write(f'Frequency Encoding: {state_encoded:.4f}')

bath_categories = df['num_full_baths_categorical'].unique()
bed_categories = df['num_bedrooms_categorical'].unique()



bedrooms = st.slider('Number of Bedrooms', 0, 6, 3)
selected_bed_category = st.selectbox('Select Bedroom Size Category', bed_categories)


bathrooms = st.slider('Number of Bathrooms', 0, 6, 2)
selected_bath_category = st.selectbox('Select Bathroom Size Category', bath_categories)

bath_size_encoded = size_mapping[selected_bath_category]
bed_size_encoded = size_mapping[selected_bed_category]

lot_area = st.number_input('Lot Area (sq_m)', min_value=27, max_value=5000, value=1000)
living_area = st.number_input('Living Area (sq_m)', min_value=27, max_value=600, value=400)
risk_score = st.slider('Total Risk Score (Normalized)', min_value=0.0, max_value=1.0, value=0.5)


input_data = pd.DataFrame({
    'lotArea': [lot_area],
    'livingArea': [living_area],
    'num_bedrooms.x': [bedrooms],
    'total_baths': [bathrooms],
    'total_risk_score_norm': [risk_score],
    'state_encoded': [state_encoded],
    'size_bath_encoded': [bath_size_encoded],
    'size_bed_encoded': [bed_size_encoded]
})

# Display Input Summary
st.write('### Input Feature Summary:')
st.write(input_data)

# Prediction
if st.button('Predict Price'):
    model = joblib.load('./model/final_model.pkl')  # Load your trained model
    predicted_price = model.predict(input_data)[0]
    st.success(f'🏷️ Estimated Price: ${predicted_price:,.2f}')
