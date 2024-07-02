# from transformers import BertTokenizerFast, BertModel
# import torch
# import numpy as np

# 예시
# model_name = "kykim/bert-kor-base"
# tokenizer = BertTokenizerFast.from_pretrained(model_name)
# model = BertModel.from_pretrained(model_name)

def get_embedding(symtom):
    dummy = [0, 0, 0]
    return dummy
#     inputs = tokenizer(text, return_tensors="pt")
#     outputs = model(**inputs)
#     embeddings = torch.mean(outputs.last_hidden_state, dim=1)
#     return embeddings.detach().numpy()
