import streamlit as st

# Add elements to the sidebar
st.sidebar.title("Welcome to CyberIntelai")
# st.sidebar.write("This is developed by Sathish Sivaprakash - Please Note : This is under development - Thanks for Understanding.")

st.markdown(
     """
     <style>
     body {
     background-color: #333;
     color: #fff;
     padding: 2rem;
     }
     </style>
     """,
     unsafe_allow_html=True
)

# Add elements to the main app area
st.write("Welcome to the main app area")

# Set the title of the app
st.title('Welcome to CyberIntelai')

# Display some text on the front-end
st.write('We will help you to provide the maximum information')

# Type of Attack input field
attack_option = st.selectbox(
    'Select Type of Attack:',
    ('Ransomware', 'Malware', 'Threat Actor Campaign','Phishing Campiagn','DDOS')
)

# year of Attack input field
year_option = st.selectbox(
    'Select Year of Attack:',
    ('2020', '2021', '2022','2023','2024')
)
