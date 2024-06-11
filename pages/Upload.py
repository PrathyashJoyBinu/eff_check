import os
import streamlit as st

def file_upload_page():
    st.title(" 📉 Upload Logs")

    uploaded_file = st.file_uploader(" 📑 Please upload the measurement log files for analysis", type=["csv"])

    if uploaded_file is not None:
        destination_folder = st.text_input("src/data", value="output")
        if st.button("Save File"):
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            with open(os.path.join(destination_folder, uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getvalue())
            st.success(f"File saved to {destination_folder}/{uploaded_file.name}")

def main():
    file_upload_page()

if __name__ == "__main__":
    main()
