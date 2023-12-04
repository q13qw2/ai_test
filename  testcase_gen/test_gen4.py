from gc import set_debug
from pathlib import Path

import yaml

from server.MyChatLLM import MyChatLLM
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from models.service_object_model import ServiceObjectModel
from models.api_object_model_parser import ApiObjectModelParser


set_debug(True)
def test_gen4():

    api_files = (Path().parent / 'api.json').read_text(encoding='utf-8')
    chat_llm = MyChatLLM()

    parser = ApiObjectModelParser(pydantic_object=ServiceObjectModel)

    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "{api_files}"),
            # ("human", "{query} {format_instructions}"),
            ("human", "{format_instructions}"),
        ]
    )

    chain = chat_template | chat_llm

    output = chain.invoke({
        'name':'宋兆军',
        # 'query':'以上是一段html代码，代表了某个网页。基于上述代码，请创建一个自动化测试的Page Object类(Java)',
        'api_files':api_files,
        'format_instructions': parser.get_format_instructions()
    })

    r=parser.parse(output)
    print(r.__class__)
    print(r)

    with open('po4.yaml','w') as f:
        yaml.dump(r,f,allow_unicode=True)

if __name__ == '__main__':
    test_gen4()