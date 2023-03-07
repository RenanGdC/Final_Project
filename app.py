import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

data = pd.read_csv('Data_bases/data_final_url.csv')

def recommender_2(performance, camera_q, battery_l, size): 
    result = data[(data["performance_c"] >= performance) & (data["cam_c"] >= camera_q) & 
                  (data["battery_t"] <= battery_l) & (data["size_c"] >= size)] 
    if len(result) == 0:
        return result
    else: 
        return result.sample(5) if len(result) >= 5 else result.sample(len(result))
    
image = Image.open('images/phonereco-low-resolution-logo-color-on-transparent-background.png')
st.image(image)

    
def app():
    st.title('PhoneRecom')

    in_perf = st.slider('How important is performance for you? [1-5]', min_value=1, max_value=5)
    in_cam = st.slider('How important is camera quality for you? [1-3]', min_value=1, max_value=3)
    in_size = st.slider('How important is size for you? [1-3]', min_value=1, max_value=3)
    in_battery = st.slider('How important is the battery duration for you? [1-5]', min_value=1, max_value=5)
    if st.button('Go!'):
        recommender_enter(in_perf, in_cam, in_battery, in_size)
    
def recommender_enter(in_perf, in_cam, in_battery, in_size):
    
    res = recommender_2(in_perf, in_cam, in_battery, in_size)


    if len(res) == 0:
        st.write('No phones meet the criteria.')
    else:
        res = res.sort_values(by="price")
        for i in range(len(res)):
            model = res.iloc[i]['model']
            brand = res.iloc[i]['brand']
            price = res.iloc[i]['price']
            url = res.iloc[i]['url']
            st.write(f'Recommendation {i+1}: {brand} {model} {price}€ {url}')
            
app()