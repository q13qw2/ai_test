from textwrap import dedent

from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers.pydantic import T

class PageObjectModelParser(PydanticOutputParser):

    def get_format_instructions(self) -> str:
         prompt = super().get_format_instructions()

         #todo 把每个对象模型的字段丰富到这里，比如element是啥
         po_prompt = dedent(f"""
         以上是一段html代码，代表了某个网页。基于上述代码，请创建一个自动化测试的Page Object类(Java)
         
        {prompt}
         """)
         return  po_prompt
