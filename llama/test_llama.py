import sys
sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\ai_test')

from llama_cpp import Llama
from util.log import log

if __name__ == '__main__':
  # llm = Llama(model_path="D:\AI\projects\llama.cpp\models\llama-2-7b-chat.Q4_0.gguf")
  # output = llm("Q: 中国的首都在哪里? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
  # log.log(output)

  llm = Llama(
    model_path="D:\AI\projects\llama.cpp\models\llama-2-7b-chat.Q4_0.gguf",
    temperature=0.1,
    max_tokens=32,
    top_p=1
  )
  output = llm("Q: 你会说中文吗? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
  log.log(output)

