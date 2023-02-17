import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))
st.title('Laptop Price Prediction')

# brand
company = st.selectbox('Brand',df['Company'].unique())
#type
type = st.selectbox('Type',df['TypeName'].unique())
#Ram
ram = st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32])
#Weight
weight = st.number_input('Enter the weight of the laptop: ')
#TouchScreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])
#IPS
ips = st.selectbox('IPS',['No','Yes'])

#screen size
screen_size = st.number_input('Screen Size')

#Resolution
resolution = st.selectbox('Screen Resolution',['1920x100','1920x1080','1366x768','1600x900','3200x1800','2880x1800','2560x1440','2304x1440'])

#CPU
cpu = st.selectbox('CPU',df['CPU Brand'].unique())

#HDD
hdd = st.selectbox('Hdd(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('ssd(in GB)',[0,128,256,512,1024,2048])

#GPU
gpu = st.selectbox('GPU',df['Gpu brand'].unique())

#OS
os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    ppi = None
    if touchscreen == 'yes':
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == 'yes':
        ips = 1
    else:
        ips = 0
    X_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))