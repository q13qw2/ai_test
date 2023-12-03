import os

from util.log import log
from transformers import AutoTokenizer, AutoModel
import torch


tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)

model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)
log.log(model)

# models.float()
model.cuda()

model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
log.log(response)
response, history = model.chat(tokenizer, "中国的首都在哪里?", history=history)
log.log(response)
response, history = model.chat(tokenizer, "你对人力资源领域了解有多少，对于人力TOB端的项目了解有多少", history=history)
log.log(response)
response, history = model.chat(tokenizer, "如何学好人工智能并在测试领域落地 ", history=history)
log.log(response)