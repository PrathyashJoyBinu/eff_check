import streamlit as st
import pandas as pd


from components.data_loader import DataOperator


data_operator = DataOperator()

def Home():
    
    st.title("Dashboard.")
    st.subheader("")
    df=data_operator.display_chart()
    anomalyCount= data_operator.threshold_breaker()
    leng =df.shape[0]


# Create two columns
    col1, col2 = st.columns(2)

    # Add items to the first column
    with col1:
        st.subheader(" ❗ Anomaly Detected : "+ str(anomalyCount))
 
     

    # Add items to the second column
    with col2:
        st.subheader(" 📆 Days : "+ str(leng))
      

    st.subheader("")
    st.write("Air Flow Vs Production")
    

    
    
    
    # Draw line chart
    df.set_index('date', inplace=True)

    st.line_chart(df.head(10))
    
    st.write("Percentage Increase")
    st.bar_chart(df['percentage'].tail(25))
    

    
    
    
Home()
