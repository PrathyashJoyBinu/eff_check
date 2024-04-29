import streamlit as st

from components.data_loader import DataOperator


data_operator = DataOperator()

def DataView():
    st.subheader("Edit Data")
    df = data_operator.data_view()
    edited_df = st.data_editor(df)
    
    if st.button("Save Data"):
        edited_df.to_csv("output/data.csv")
        st.success("Successfully saved")
    
    
DataView()