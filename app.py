import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Median House Price:', 0, 500001, 20000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults


income_level = st.sidebar.radio(
    'Select Income Level:',('Low', 'Medium', 'High')
    )
# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")


# filter by population
df = df[df.median_house_value >= price_filter]

# filter by capital
df = df[df.ocean_proximity.isin(location_filter)]

if income_level == 'Low(<=2.5)':
    filtered_df = df[df['median_income']<= 2.5]
elif income_level =='Medium(>2.5&<4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df =df[df['median_income'] > 4.5]



# show on map
st.map(filtered_df)


st.subheader('Median House Value')
fig, ax = plt.subplots(figsize=(20, 20))
ax.hist(filtered_df['median_house_value'], bins = 30)

ax.set_title('Histogram of Median House Value', fontsize = 16)
ax.set_xlabel('Median House Value', fontsize = 12)
ax.set_ylabel('Frequency', fontsize = 12)


st.pyplot(fig)