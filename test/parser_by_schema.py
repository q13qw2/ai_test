# LangChain相关模块的导入
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

key = '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'
# 创建OpenAI调用实例
# temperature用来设置大模型返回数据的随机性和创造性，较低的数值返回的数据就更贴近现实。
chat = ChatOpenAI(temperature=0.0, openai_api_key=key)

# 针对prompt中的每个想要提取的属性，创建ResponseSchema记录字段名称和描述，用于后续解析返回数据
time_schema = ResponseSchema(name="时间", description="事件发生的准确时间")
location_schema = ResponseSchema(name="地点", description="事情发生时，讲述人所处的城市名称")
event_schema = ResponseSchema(name="事件", description="文中主要讲述的具体事件是发生了什么事件")
situation_schema = ResponseSchema(name="现象",description="列举出事件发生时，出现的每个现象，每个现象作为列表中的单独一项")

response_schemas = [time_schema, location_schema, event_schema, situation_schema]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
# 根据schema格式定义，自动生成一个支持格式化输出的prompt
format_instructions = output_parser.get_format_instructions()

# 可复用的模板字符串，注意不要使用 f字符串 ，LangChain会在运行时自动替换
template_str = """\
text: {text}
{format_instructions}
"""

prompt_template = ChatPromptTemplate.from_template(template_str)
custom_message = prompt_template.format_messages(
    text="2023年10月24日下午18：19分，我在高途工位上忽悠两下，感觉到了地震，房子在晃动两下，窗帘在动，厨房灯在抖动，我连忙打开手机发现北京周边在地震，而我们是余震，可吓死我了",
    format_instructions=format_instructions
)

customer_res = chat(custom_message)
final_res = output_parser.parse(customer_res.content)
print(final_res)