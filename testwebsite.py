import streamlit as st

# Regular page content
st.title('Main Page')
st.write('This is the main content')

# Sidebar content
st.sidebar.title('Sidebar')
st.sidebar.write('This is in the sidebar!')

# Sidebar inputs
name = st.sidebar.text_input('Enter your name')
age = st.sidebar.slider('Age', 0, 100, 25)
option = st.sidebar.selectbox('Choose option', ['Option 1', 'Option 2', 'Option 3'])

# Use the sidebar inputs on main page
if st.sidebar.button('Submit'):
    st.write(f'Hello {name}, you are {age} years old')
    st.write(f'You selected: {option}')