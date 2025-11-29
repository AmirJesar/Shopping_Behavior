# pages/1_📊_Overview.py
import streamlit as st
from app import filtered_df, df  # Import from app.py if needed (or reload data)

st.title("📊 Dataset Overview")

st.write("### Raw Data Preview")
st.dataframe(filtered_df.head(10))

st.write("### Summary Statistics")
st.dataframe(filtered_df.describe())

st.write("### Data Info")
buffer = pd.DataFrame(filtered_df.dtypes, columns=["Data Type"])
buffer["Missing Values"] = filtered_df.isnull().sum()
st.dataframe(buffer)

st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name="filtered_shopping_data.csv",
    mime="text/csv"
)
