# pages/3_📈_Insights.py
import streamlit as st
from app import filtered_df

st.title("📈 Key Insights")

# Average metrics
avg_purchase = filtered_df['Purchase Amount (USD)'].mean()
avg_rating = filtered_df['Review Rating'].mean()
avg_previous = filtered_df['Previous Purchases'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Avg Purchase Amount", f"${avg_purchase:.2f}")
col2.metric("Avg Review Rating", f"{avg_rating:.1f}/5")
col3.metric("Avg Previous Purchases", f"{avg_previous:.1f}")

st.subheader("Trends")
st.write("- **Gender Differences**: Males tend to purchase more in certain categories—check the charts!")
st.write("- **Seasonal Patterns**: Winter sees higher spends on clothing; Summer on accessories.")
st.write("- **Subscription Impact**: Subscribers have higher previous purchases and ratings.")

st.subheader("Custom Query")
query = st.text_input("Enter a Pandas query (e.g., Age > 50 & Gender == 'Female')")
if query:
    try:
        result = filtered_df.query(query)
        st.dataframe(result)
    except:
        st.error("Invalid query—try again!")
