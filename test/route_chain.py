from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate

# 加载个人的OpenAI Token
key = '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'
# temperature用来设置大模型返回数据的随机性和创造性，较低的数值返回的数据就更贴近现实。
llm = ChatOpenAI(temperature=0.0, openai_api_key=key)

# 2个角色prompt模板，作为请求处理的2个分支
physics_template = """你是一位非常聪明的物理学家，非常擅长回答物理相关的问题，\  
并且会以一种简洁易懂的方式对问题做出讲解。\  
当你无法回答问题的时候，就会主动承认无法回答问题。\  

以下是具体问题:  
{input}"""

math_template = """你是一位非常棒的数学家，非常擅长回答数学相关的问题。\  
你之所以这么棒，是因为你能够将难题拆解成它们的组成部分，\  
对组成部分分别作答后，再将它们组合起来最终成功的回答出最初的原始问题。 \  

以下是具体问题:  
{input}"""

# 将角色prompt模板和对应的描述、名称组装成列表，方便遍历
prompt_info = [
    {
        "name": "物理学家",
        "description": "擅长回答物理方面的问题",
        "prompt_template": physics_template
    },
    {
        "name": "数学家",
        "description": "擅长回答数学方面的问题",
        "prompt_template": math_template
    },
]

# 名称和大模型Chain映射关系的字典
destination_chains = {}
# 根据prompt_info中的信息，创建对应的LLMChain实例，并放入映射字典中
for p_info in prompt_info:
    # destination_chains最终的结构为: {name: 对应的LLMChain实例}
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    # 给每个角色创建一个自己的大模型Chain实例
    chain = LLMChain(llm=llm, prompt=prompt)
    # 组装成字典，方便router根据逻辑选择分支之后，能够找到分支对应调用的Chain实例
    destination_chains[name] = chain

# 生成destinations
destinations = [f"{p['name']}: {p['description']}" for p in prompt_info]
# 转换成多行字符串，每行一句对应关系
destinations_str = "\n".join(destinations)
# 真正实现 if 分支判断的地方
# 选择使用哪个人设模型进行处理的prompt模板
MULTI_PROMPT_ROUTER_TEMPLATE = """Given a raw text input to a \  
language models select the models prompt best suited for the input. \  
You will be given the names of the available prompts and a \  
description of what the prompt is best suited for. \  
You may also revise the original input if you think that revising\  
it will ultimately lead to a better response from the language models.  

<< FORMATTING >>  
Return a markdown code snippet with a JSON object formatted to look like:  
  ```json  {{{{    "destination": string \ name of the prompt to use or "DEFAULT"    "next_inputs": string \ a potentially modified version of the original input  }}}}  ```  
REMEMBER: "destination" MUST be one of the candidate prompt \  
names specified below OR it can be "DEFAULT" if the input is not\  
well suited for any of the candidate prompts.  
REMEMBER: "next_inputs" can just be the original input \  
if you don't think any modifications are needed.  

<< CANDIDATE PROMPTS >>  
{destinations}  

<< INPUT >>  
{{input}}  

<< OUTPUT (remember to include the ```json)>>"""

# 在router模版中先补充部分数据
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations=destinations_str
)
# 组装一个基础的prompt模板对象，通过更多的参数设置更多的信息
router_prompt = PromptTemplate(
    # 基础模板
    template=router_template,
    # 输入参数名称
    input_variables=["input"],
    # 输出数据解析器
    output_parser=RouterOutputParser(),
)
# 通过模板和大模型对象，生成LLMRouterChain，用于支持分支逻辑
router_chain = LLMRouterChain.from_llm(llm, router_prompt)

# 创建 else 场景
# 创建一个默认的LLMChain实例，作为上述匹配未命中时的默认调用目标，避免调用最终没有逻辑去处理的情况出现
# 上述的匹配规则可以看成一组if elif的逻辑匹配规则，default作为最后的else负责处理所有未命中的情况
default_prompt = ChatPromptTemplate.from_template("{input}")
default_chain = LLMChain(llm=llm, prompt=default_prompt)

# 把 分支、 else 的情况 以及 做if判断的语句结合到一起
# 将多个chain组装成完整的chain对象，完成带有逻辑的请求链
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True
)

# 提出一个物理问题
physics_res = chain.run("什么是黑体辐射?")
print(physics_res)
# 提出一个数学问题
math_res = chain.run("2的4次方是多少？")
print(math_res)
