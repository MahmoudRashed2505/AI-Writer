# Import base streamlit dependency
import streamlit as st

# Import subprocess to run tiktok script from command line
from subprocess import call

# Import time
import time


# Set page width to wide
st.set_page_config(layout='wide')

# Set Page title
st.title('AI Writer by Voomo')

#Create sidebar
st.sidebar.markdown("<div><img src='https://upload.wikimedia.org/wikipedia/en/9/95/IA_Writer_Logo.png' width=100 /><br><h1 style='display:inline-block'>Ai Writer</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to type some text and number of charcters and it auto generate text for you using Python and Streamlit.")
st.sidebar.markdown("To get started <ol><li>Enter the <i>breif</i> you wish to use</li> <li>Enter the <i>Number of charchters </i> you wish to use</li> <li>Hit <i>Generate Text</i>.</li> <li>Get your Ai Generatet Text</li></ol>",unsafe_allow_html=True)


breif = st.text_input('Add breif text here', value="")
no_of_characters = st.text_input('Add number of characters here', value="")

if st.button('AI Write'):
    call(['python', 'instagram.py', breif,no_of_characters])
    with st.spinner('Wait for it...'):
        time.sleep(30)
    st.success('Done!')

    with open('gpttext.txt', 'r') as f:
        text = f.read()

    st.write('Number of characters: ',no_of_characters)
    st.write('Breif: ',breif)
    st.write('Generated Text: ',text)

    
    
