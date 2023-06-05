import torch
import pandas as pd
from torch.utils.data import Dataset

class econNewsDataset(Dataset):

  def __init__(self, econDataPath, newsDataPath):
    self.econData = pd.read_csv(econDataPath)
    self.newsData = pd.read_csv(newsDataPath)