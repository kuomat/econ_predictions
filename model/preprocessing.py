#%%
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
#%%

#https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

#%%

headlines = pd.read_csv('../news.csv')


#%%

embeddings = model.encode(headlines["Headlines"]) # type: ignore

#%%
newData = pd.DataFrame(embeddings) # type: ignore

newData.rename(columns=lambda x: f"embedding_{x}", inplace=True)

newData['Time'] = headlines['Time']

#%%

newData.to_csv('../newsEmbeddings.csv', index=False)