# pages/2_🔍_Exploration.py
import streamlit as st
import plotly.express as px
from app import filtered_df

st.title("🔍 Data Exploration & Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Purchase Amount Distribution")
    fig = px.histogram(filtered_df, x="Purchase Amount (USD)", color="Gender", nbins=20, title="Purchase Amounts by Gender")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Age vs. Purchase Amount")
    fig = px.scatter(filtered_df, x="Age", y="Purchase Amount (USD)", color="Category", size="Previous Purchases", title="Age vs. Purchase (Sized by Previous Purchases)")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Category Breakdown")
fig = px.pie(filtered_df, names="Category", values="Purchase Amount (USD)", title="Total Purchases by Category")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Top Locations by Purchases")
top_locations = filtered_df.groupby("Location")["Purchase Amount (USD)"].sum().nlargest(10).reset_index()
fig = px.bar(top_locations, x="Location", y="Purchase Amount (USD)", title="Top 10 Locations by Total Purchases")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Correlation Heatmap")
corr = filtered_df.select_dtypes(include=['float64', 'int64']).corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
