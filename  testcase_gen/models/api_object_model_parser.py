from textwrap import dedent

from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers.pydantic import T


class ApiObjectModelParser(PydanticOutputParser):

    def get_format_instructions(self) -> str:
        prompt = super().get_format_instructions()

        # todo
        po_prompt = dedent(f"""
         以上是一段yapi导出的接口文档，基于上述接口文档，请编写接口的测试用例，并通过如下格式返回给我：
         以上是一段yapi导出的接口文档，基于上述接口文档，请编写接口的测试用例，并通过如下格式返回给我：
         name:声明接口的名称,
         uri: 接口请求的url路径,
         header: 接口请求header,
         paramers: 接口的请求参数,
         api_result: 接口预期返回的结果
         
        {prompt}
         """)
        return po_prompt
