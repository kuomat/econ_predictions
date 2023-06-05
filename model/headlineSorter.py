from dateutil import parser
import csv

outputFiles = [[open(f"../newsEmbeddings/headlines{month}_{year}.csv","w") for month in range (1,13)] for year in range(2017,2024)]

counts = [[0 for month in range (1,13)] for year in range(2017,2024)]


with open("../newsEmbeddings.csv",encoding="utf-8") as f:

  header = f.readline()

  for year in outputFiles:
    for monthFile in year:
      monthFile.write(header)

  nextLine = f.readline()

  while nextLine != None and nextLine != "":

    segments = csv.reader([nextLine]).__next__()

    date = parser.parse(segments[-1])

    if(date.year < 2017 or date.year > 2023):

      print(f"Error on line: {nextLine}")

      print(f"Date: {date.year}")

    try:

      outputFiles[date.year-2017][date.month-1].write(nextLine)

      counts[date.year-2017][date.month-1] += 1

    except IndexError as e:

      print(f"Error on line: {nextLine}")

      print(f"Date: {date.month} {date.year}")


    nextLine = f.readline()


for year in outputFiles:
  for f in year:
    f.close()


print("year\tJan\tFeb\tMarch\tApril\tMay\tJune\tJuly\tAug\tSept\tOct\tNov\tDec")
for index,year in enumerate(counts):
  print(f"{index+2017}\t",end="")
  for month in year:
    print(f"{month}\t",end="")
  print()