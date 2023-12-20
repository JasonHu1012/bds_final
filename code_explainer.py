import streamlit as st
import streamlit_ace as st_ace
from openai import OpenAI
import json


class Code_explainer():
    def __init__(self, code_language, openai_api_key):
        self.code_language = code_language
        self.client = OpenAI(
            api_key=openai_api_key
        )
        self.code = ''
        self.overview = {
            'explanation': '',
            'improvement': ''}

    def submit_code(self, code):
        prompt = f'''我將會給你一段{self.code_language}程式碼，請你解釋這段程式在做什麼，以及可以怎麼改善它。
【以下為程式碼】
{code}
【以上為程式碼】

條件限制：
【程式碼說明】: 解釋程式的流程和用途，使用繁體中文 
【程式改進建議】:  說明程式寫不好的地方，提供相關改進建議，使用繁體中文

回傳格式：
以json格式回傳，如{{"explanation":程式碼說明,"improvement":程式改進建議}}'''

        completion = self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
        message = json.loads(completion['choices'][0]['message']['content'])

        self.code = code
        self.overview['explanation'] = message['explanation']
        self.overview['improvement'] = message['improvement']

    def get_explanation(self):
        return self.overview['explanation']

    def get_improvement(self):
        return self.overview['improvement']


def main():
    st.title('GPT code explainer')

    code_languages = st_ace.LANGUAGES
    code_language = st.selectbox('language', code_languages)

    code = st_ace.st_ace(
        placeholder='type your code here',
        language=code_language)

    if code == '':
        return

    with open('api_key') as f:
        code_explainer = Code_explainer(code_language, f.read())

    code_explainer.submit_code(code)

    st.header('Code Explaination')
    st.write(code_explainer.get_explanation())

    st.header('How to Improve')
    st.write(code_explainer.get_improvement())


if __name__ == '__main__':
    main()
