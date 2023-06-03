#%%
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import time

#%%

device = "cuda:4"

#https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2
model = SentenceTransformer('paraphrase-MiniLM-L6-v2').to(device)

#%%

headlines = pd.read_csv('../news.csv')


#%%
start_time = time.time()
embeddings = model.encode(headlines["Headlines"], convert_to_tensor=True, device=device)
print(f"Model took {time.time() - start_time} to encode")

#%%
newData = pd.DataFrame(embeddings.cpu().numpy())

newData.rename(columns=lambda x: f"embedding_{x}", inplace=True)

newData['Time'] = headlines['Time']

#%%

newData.to_csv('../newsEmbeddings.csv', index=False)
