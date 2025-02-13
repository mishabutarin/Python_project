import streamlit as st
import pandas as pd
import plotly.express as px


# Load data
df=pd.read_csv("vehicles_us.csv")

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

# Ensure filtering works dynamically
df_filtered = df.copy()

# Additional checkbox to filter by model year
filter_recent = st.checkbox("Show only recent cars (model year > 2015)")
if filter_recent:
    df_filtered = df_filtered[df_filtered['model_year'] > 2015]

# New scatter plot: Price vs Model Year
st.subheader("Price vs Model Year")
fig_year = px.scatter(df_filtered, x='model_year', y='price', title='Price vs Model Year', trendline='ols')
st.plotly_chart(fig_year)