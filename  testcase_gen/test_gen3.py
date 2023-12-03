from gc import set_debug
from pathlib import Path

import yaml

from server.MyChatLLM import MyChatLLM
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from models.page_object_model import PageObjectModel
from models.page_object_model_parser import PageObjectModelParser


set_debug(True)
def test_gen3():

    web_html = (Path().parent / 'web.html').read_text(encoding='utf-8')
    chat_llm = MyChatLLM()

    # Set up a parser + inject instructions into the prompt template.
    # parser = PydanticOutputParser(pydantic_object=PageObjectModel)
    parser = PageObjectModelParser(pydantic_object=PageObjectModel)

    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "{web_html}"),
            # ("human", "{query} {format_instructions}"),
            ("human", "{format_instructions}"),
        ]
    )

    chain = chat_template | chat_llm

    output = chain.invoke({
        'name':'宋兆军',
        # 'query':'以上是一段html代码，代表了某个网页。基于上述代码，请创建一个自动化测试的Page Object类(Java)',
        'web_html':web_html,
        'format_instructions': parser.get_format_instructions()
    })

    r=parser.parse(output.content)

    print(r.__class__)
    print(r)

    with open('po.yaml','w') as f:
        yaml.dump(r,f,allow_unicode=True)

if __name__ == '__main__':
    test_gen3()