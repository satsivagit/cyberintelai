import streamlit as st

# Set the title of the app
st.title('Welcome to CyberIntelai')

# Display some text on the front-end
st.write('We will help you to provide the maximum information')

# Type of Attack input field
attack_option = st.selectbox(
    'Select an option:',
    ('Ransomware', 'Malware', 'Threat Actor Campaign','Phishing Campiagn','DDOS')
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
