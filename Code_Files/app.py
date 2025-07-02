import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    return sns.load_dataset("iris")

df = load_data()

# App title
#st.title("Iris Dataset Explorer")

# Show raw data checkbox
if st.checkbox("Show raw data"):
    st.write(df)

# Species filter
species = st.multiselect(
    "Select species to filter:",
    options=df['species'].unique(),
    default=df['species'].unique()
)

filtered_df = df[df['species'].isin(species)]

# Summary statistics
st.subheader("Summary Statistics")
st.write(filtered_df.describe())

# Histogram
st.subheader("Histogram")
col = st.selectbox("Choose column to plot", df.columns[:-1])
fig, ax = plt.subplots()
sns.histplot(filtered_df[col], kde=True, ax=ax)
st.pyplot(fig)

# Scatter plot
st.subheader("Scatter Plot")
x_axis = st.selectbox("X-axis", df.columns[:-1], index=0)
y_axis = st.selectbox("Y-axis", df.columns[:-1], index=1)
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x=x_axis, y=y_axis, hue="species", ax=ax2)
st.pyplot(fig2)
