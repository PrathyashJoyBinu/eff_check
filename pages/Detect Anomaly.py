import streamlit as st

from components.math_converter import MathConverter


converter=MathConverter()

def Detect():
    
    st.title(" ⚠ Detect Anomaly")
    st.write("Please enter todays's measurements in given form")
    
    st.title("")
# Display two text input fields
    air_Flow = st.text_input("Enter Air Flow (m3)")
    production = st.text_input("Enter Production (Kg)")

    # Display a calendar for date selection
    selected_date = st.date_input("Select a date")

    # Center the button horizontally
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    # Add a button
    button_clicked = st.button("Detect Anomaly")

    st.markdown("</div>", unsafe_allow_html=True)

    # Print the selected date and text inputs when the button is clicked
    if button_clicked:
        status = converter.math_operations(air_Flow, production,selected_date)
        print (status)
        if status.get("st"):
             st.success("System Normal")
        else:
            st.error("Your compressor system has an excess air leakage. Please check it out. Percentage increase is about "+str(status.get("val")))
        

Detect()
