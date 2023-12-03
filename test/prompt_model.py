# LangChain相关模块的导入
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

key = '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'
# 创建OpenAI调用实例
# temperature用来设置大模型返回数据的随机性和创造性，较低的数值返回的数据就更贴近现实。
chat = ChatOpenAI(temperature=0.0, openai_api_key=key)

# 可复用的模板字符串，注意不要使用 f字符串 ，LangChain会在运行时自动替换
template_str = """我的身份是{role}，需要你完成以下任务：将三个反引号内的文本内容转换成{style}风格的文本```{text}```"""
# 创建一个针对模板字符串的prompt模板实例
prompt_template = ChatPromptTemplate.from_template(template_str)
# 用prompt模板实例+参数，生成具体的请求消息列表
custom_message = prompt_template.format_messages(
    role = "老师",
    style="英语",
    text="我爱吃苹果"
    )
# 调用chat发送消息，从ChatGPT中获取相应信息
customer_res = chat(custom_message)
# 相应信息中的content是具体的返回消息体
print(customer_res.content)