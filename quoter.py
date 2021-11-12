import csv
import pandas as pd

with open('quotes.csv') as quotes_csv:
  quotes = csv.reader(quotes_csv, dialect='excel')
  header = next(quotes)
  quote = next(quotes)

  print(quote)


# print(quote)