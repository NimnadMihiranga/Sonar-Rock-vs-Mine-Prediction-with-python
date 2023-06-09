import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

model = data['model']
sensor_data = data['Sensor Data']


def show_predict_page():
    st.titile("Mine vs Rock Predicor")

    st.write("This will predict Sensor data is Mine or a Rock")
