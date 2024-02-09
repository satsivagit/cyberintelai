import streamlit as st

# Create a layout with a sidebar
st.beta_set_page_config(layout="wide")

# Add elements to the sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar")

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

# Create a text input field
user_input = st.text_input("Enter some text:")

# Display the user input back to the front-end
st.write("You entered:", user_input)

# Create a slider
slider_value = st.slider('Select a number:', 0, 100, 50)

# Display the slider value on the front-end
st.write("You selected:", slider_value)

# Create a checkbox
if st.checkbox('Show/hide some text'):
    st.write('This is some hidden text that appears when the checkbox is checked.')
