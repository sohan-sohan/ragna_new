
import streamlit as st
import requests

base_url = 'http://localhost:8000'

st.title('Ragna')

st.write('### Upload a file')

uploaded_file = st.file_uploader('Choose a file', type=['pdf'])

st.write('### Enter a question')

question = st.text_input('Start typing...')

st.info('Press submit once you have uploaded a file and entered a question', icon=':material/info:')

if st.button('Submit'):
    # process file

    # process question and get response from backend
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

    with st.spinner('Processing file...'):
        response = requests.post(url=f'{base_url}/processfile', files=files)
        st.success('File Processed')

    with st.spinner('Answering Question...'):
        answer = requests.post(url=f'{base_url}/question', json={"question_text": question})

    st.write('### Answer')
    with st.container(border=True):

        st.write(answer.json()['message'])

    st.write('### Relevant Chunks')
    with st.container(border=True):
        for chunk in answer.json()['rel_chunks']:
            st.write(chunk + '\n\n----------------------------')
