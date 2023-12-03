# LangChain相关模块的导入
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

key = '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'

# 创建OpenAI调用实例
# temperature用来设置大模型返回数据的随机性和创造性，较低的数值返回的数据就更贴近现实。
chat = ChatOpenAI(temperature=0.0, openai_api_key=key)
# 可复用的模板字符串，注意不要使用 f字符串 ，LangChain会在运行时自动替换
template_str = """\
对于给出的text数据，从中提取出下列数据
时间: 事件发生的准确时间
地点: 事情发生时，讲述人所处的城市名称
事件: 文中主要讲述的具体事件是发生了什么事件
现象: 列举出事件发生时，出现的每个现象，每个现象作为单独的句子记录

将提取出的数据，按照json的格式显示出来，json的key分别为以下几个字段
时间
地点
事件
现象

text: {text}
"""
# 创建一个针对模板字符串的prompt模板实例
prompt_template = ChatPromptTemplate.from_template(template_str)
# 用prompt模板实例+参数，生成具体的请求消息列表
custom_message = prompt_template.format_messages(
    text="2023年10月24日下午18：19分，我在高途工位上忽悠两下，感觉到了地震，房子在晃动两下，窗帘在动，厨房灯在抖动，我连忙打开手机发现北京周边在地震，而我们是余震，可吓死我了"
)
# 调用chat发送消息，从ChatGPT中获取相应信息
customer_res = chat(custom_message)
# 相应信息中的content是具体的返回消息体
print(customer_res.content)
print(type(customer_res.content))
