import streamlit as st
import streamlit_ace as st_ace
import openai


class Code_explainer():
    def __init__(self, openai_api_key):
        self.code = ''
        self.overview = {
            'explaination': '',
            'improvement': ''}
        openai.api_key = openai_api_key

    def submit_code(self, code):
        self.code = code

    def get_explaination(self):
        return self.overview['explaination']

    def get_improvement(self):
        return self.overview['improvement']


def main():
    st.title('GPT code explainer')

    languages = st_ace.LANGUAGES
    language = st.selectbox('language', languages)

    code = st_ace.st_ace(
        placeholder='type your code here',
        language=language)

    if code == '':
        return

    code_explainer = Code_explainer('api_key')

    st.header('Code Explaination')
    st.write(code_explainer.get_explaination())

    st.header('How to Improve')
    st.write(code_explainer.get_improvement())


if __name__ == '__main__':
    main()
