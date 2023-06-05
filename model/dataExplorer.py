import pandas as pd
from dateutil import parser

df = pd.read_csv('../news.csv')

currentYear = None
currentMonth = None

print("Year\tMonth\trow#")
for index, row in df.iterrows():
  date = parser.parse(row['Time'])
  if currentYear is None or date.year != currentYear or date.month != currentMonth:
    currentYear = date.year
    currentMonth = date.month
    print(f"{currentYear}\t{currentMonth}\t{index}")
