import streamlit as st
import pandas as pd
from joblib import load
prediction_model = load('aqi_models.joblib')


# Load your data
df = pd.read_csv('AQI and Lat Long of Countries.csv')

# Load your model
prediction_model = load('aqi_models.joblib')

# Define prediction function
def predict_aqi(CO, Ozone, NO2, PM2_5):
    prediction = prediction_model.predict([[CO, Ozone, NO2, PM2_5]])
    return prediction

# Define main application
def main():
    st.title("AQI Predictor")
    st.header("Here you will get the Air Quality Index and suggestions regarding air category")
    
    CO = st.number_input("Enter CO [Carbon Monoxide] Value")
    Ozone = st.number_input("Enter O3 [Ozone] value")
    NO2 = st.number_input("Enter NO2 [Nitrogen Dioxide] value")
    PM2_5 = st.number_input("Enter PM2.5 value")
    
    if st.button("Predict"):
        result = predict_aqi(CO, Ozone, NO2, PM2_5)
        st.success('The predicted AQI is {}'.format(result))
        
        # Display AQI category and advice
        if result <= 50:
            st.subheader(":blue[_GOOD_] :innocent:")
            st.write("The air quality is ideal for most individuals; enjoy your normal outdoor activities.")
            
            st.subheader("Environmental Protection")
            st.markdown("""
            - Keep up with practices that reduce emissions, like using public transport or carpooling, even though air quality is good.
            - Educate others on sustainable practices to maintain a healthy environment.
            """)
            
            st.subheader("Personal hygiene")
            st.write(":tshirt: **Wear:** Regular clothing is fine. Enjoy outdoor activities without restrictions.")
            st.write(":apple: **Eat:** No special dietary requirements, but a balanced diet with fruits, vegetables, and hydration is always beneficial.")
            st.write(":selfie: **Body Care:** Engage in outdoor activities freely. Exercise outdoors to make the most of the fresh air.")
            st.write(":sparkles: **Products:** Regular sunscreen if it's sunny. General skincare routine is sufficient.")
        
        elif result > 50 and result <= 100:
            st.subheader(":green[_MODERATE_] :sunglasses:")
            st.write("The air quality is generally acceptable for most individuals. However, sensitive groups may experience minor to moderate symptoms from long-term exposure.")
            
            st.subheader("Environmental Protection")
            st.markdown("""
            - Limit the use of fireplaces or open burning.
            - Avoid idling your vehicle, and consider using energy-efficient appliances.
            """)
            
            st.subheader("Personal hygiene")
            st.write(":tshirt: **Wear:** Light, breathable fabrics; if exercising, choose moisture-wicking materials.")
            st.write(":apple: **Eat:** Antioxidant-rich foods like berries, nuts, and green tea to support lung health.")
            st.write(":selfie: **Body Care:** Mild exercise is fine. If you have respiratory sensitivities, consider shorter outdoor sessions.")
            st.write(":sparkles: **Products:** Regular sunscreen; if you have sensitive skin or lungs, apply a barrier cream to keep pollutants from settling on the skin.")
            
        elif result > 100 and result <= 150:
            st.subheader(":orange[_UNHEALTHY FOR SENSITIVE GROUPS_] :pensive:")
            st.write("The air has reached a high level of pollution and is unhealthy for sensitive groups. Reduce time spent outside if you are feeling symptoms such as difficulty breathing or throat irritation.")
            
            st.subheader("Environmental Protection")
            st.markdown("""
            - Encourage the use of air purifiers indoors to reduce exposure to indoor pollution.
            - Advocate for reduced industrial emissions in your area and participate in community clean-up events.
            """)
            
            st.subheader("Personal hygiene")
            st.write(":mask: **Wear:** If you have sensitivities, consider wearing a lightweight mask, especially if you’ll be outdoors for a while.")
            st.write(":apple: **Eat:** Anti-inflammatory foods such as turmeric, ginger, and leafy greens. Increase hydration to help the body flush out toxins.")
            st.write(":selfie: **Body Care:** Limit intense outdoor exercise. Opt for indoor workouts if you feel discomfort.")
            st.write(":sparkles: **Products:** Use a heavier moisturizer to act as a barrier for pollutants. Sunscreen is still recommended.")
        
        elif result > 150 and result <= 200:
            st.subheader(":red[_UNHEALTHY_] :mask:")
            st.write("Health effects can be immediately felt by sensitive groups. Healthy individuals may experience difficulty breathing and throat irritation with prolonged exposure. Limit outdoor activity.")
            
            st.subheader("Environmental Protection")
            st.markdown("""
            - Avoid outdoor burning, and reduce vehicle use where possible.
            - Encourage friends and family to avoid unnecessary travel and use alternative modes of transport.
            - Plant indoor and outdoor plants known to improve air quality, like spider plants or snake plants.
            """)
            
            st.subheader("Personal hygiene")
            st.write(":mask: **Wear:** Wear a high-quality mask (N95 or similar) if you need to be outdoors. Choose clothing that covers most of your skin.")
            st.write(":apple: **Eat:** Foods rich in omega-3 fatty acids (e.g., fish, flaxseeds) to reduce inflammation. Drink plenty of water to support detoxification.")
            st.write(":selfie: **Body Care:** Avoid outdoor activities, especially strenuous ones. Spend time in air-conditioned or purified indoor environments.")
            st.write(":sparkles: **Products:** Apply a protective moisturizer to keep pollutants from penetrating the skin barrier. Sunscreen with antioxidants is beneficial.")
        
        elif result > 200 and result <= 300:
            st.subheader(":red[_VERY UNHEALTHY_] :mask:")
            st.write("Health effects can be immediately felt by sensitive groups. Healthy individuals may experience difficulty breathing and throat irritation with prolonged exposure. Limit outdoor activity.")
            
            st.subheader("Environmental Protection")
            st.markdown("""
            - Minimize use of electricity and gas to reduce emissions.
            - Spread awareness and encourage the community to take collective action, such as carpooling, cycling, and avoiding use of wood-burning stoves.
            """)
            
            st.subheader("Personal hygiene")
            st.write(":mask: **Wear:** An N95 or similar mask when stepping outside is essential. Cover exposed skin with long sleeves and pants.")
            st.write(":apple: **Eat:** Detoxifying foods like citrus fruits, garlic, and cruciferous vegetables. Increase your intake of vitamins C and E to combat oxidative stress.")
            st.write(":selfie: **Body Care:** Stay indoors as much as possible. Use a humidifier or air purifier to maintain air quality indoors. Avoid outdoor exercise.")
            st.write(":sparkles: **Products:** Use barrier creams or lotions to protect the skin. Antioxidant-enriched skincare products and sunscreen with pollution-blocking properties are recommended.")
        
        else:
            st.subheader(":violet[HAZARDOUS] :dizzy_face:")
            st.write("Health effects will be immediately felt by sensitive groups and should avoid outdoor activity. Healthy individuals are likely to experience difficulty breathing and throat irritation; consider staying indoors and rescheduling outdoor activities.")
            
            st.subheader("Environmental Protection")
            st.markdown("""
            - Stay informed on air quality advisories and share information with your community.
            - Advocate for policies that support clean energy and stricter regulations on industrial emissions.
            - Encourage the community to reduce waste and recycle to lessen environmental impact.
            """)
            
            st.subheader("Personal hygiene")
            st.write(":mask: **Wear:** Stay indoors as much as possible. If you must go out, wear a certified air-filtering mask (N95 or P100). Cover your skin with long clothing to minimize exposure.")
            st.write(":apple: **Eat:** Focus on detoxifying and immune-boosting foods, such as leafy greens, vitamin C-rich fruits, and herbal teas like ginger or turmeric. Drink lots of water.")
            st.write(":selfie: **Body Care:** Avoid all outdoor activities. Seal windows and use air purifiers indoors. Take breaks from screens to avoid eye strain, as indoor air pollution can still irritate the eyes. Shower immediately after returning indoors to remove pollutants from skin and hair.")
            st.write(":sparkles: **Products:** Use heavy-duty moisturizers with antioxidants and anti-pollution properties. Apply a broad-spectrum sunscreen indoors, as UV rays can still penetrate windows.")

if __name__ == '__main__':
    main()

