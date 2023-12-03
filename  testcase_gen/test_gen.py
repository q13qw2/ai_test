from doctest import debug
from pathlib import Path
from textwrap import dedent

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

def test_gen():
    key = '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'
    web_html=(Path().parent / 'web.html').read_text()

    template=PromptTemplate.from_template(
        dedent('''
        {web_html}
        
        {query}

        ''')
    )

    llm = ChatOpenAI(temperature=0.0, openai_api_key=key)

    chain=template | llm
    output=chain.invoke({'query':'以上是一段html代码，代表了某个网页。基于上述代码，请创建一个自动化测试的Page Object类',
                  'web_html':web_html})

    debug(output)