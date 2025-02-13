import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('//Users/misabutarin/Documents/GitHub/Python_project/vehicles_us.csv')

# Clean data
df=df.drop_duplicates()
df.replace("", pd.NA, inplace=True)
df.replace(" ", pd.NA, inplace=True)

# Convert numerical columns (handling potential NaN values)
num_cols = ['price', 'odometer', 'model_year']
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop NaN values in price and odometer to avoid plotting issues
df = df.dropna(subset=['price', 'odometer'])

# Streamlit App
st.title("🚗 Vehicle Data Dashboard")
st.header("Overview of Vehicle Prices and Mileage")

# Histogram of car prices
st.subheader("Distribution of Car Prices")
fig_price = px.histogram(df, x='price', nbins=50, title='Distribution of Car Prices')
st.plotly_chart(fig_price)

# Scatter plot: Price vs Mileage
st.subheader("Price vs Mileage")
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Mileage', trendline='ols')
st.plotly_chart(fig_scatter)

# Checkbox to show filtered data
if st.checkbox("Show only expensive cars (price > 50,000)"):
    df_filtered = df[df['price'] > 50000].sort_values(by='price', ascending=False)
    st.write(df_filtered[['model', 'price', 'odometer', 'condition']].reset_index())
