import pandas as pd

def pull_quotes():
  quotes = pd.read_csv('quotes.csv')
  return quotes

def get_quote():
  quotes = pull_quotes()

  my_quote = quotes.iloc[0]
  quote = my_quote[0]
  author = my_quote[1]

  return quote, author

def create_tweet(quote, author):
  return "{}  -- {}".format(quote, author)

def assemble():
  quote, author = get_quote()
  tweet = create_tweet(quote, author)
  update_quotes_file()
  return tweet


def shuffle_quotes(quotes):
  used_quote = quotes.iloc[0]
  shuffled = quotes.iloc[1:]
  updated = shuffled.append(used_quote)
  return updated

def update_quotes_file():
  current_csv = pull_quotes()
  new_csv = shuffle_quotes(current_csv)
  new_csv.to_csv('quotes.csv', index=False)