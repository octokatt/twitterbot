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
  return tweet


def shuffle_quotes(quotes):
  shuffled = quotes.iloc[1:]
  shuffled.append(quotes.iloc[0])
  shuffled.reset_index()
  return shuffled

def update_quotes(new_file):
  new_file.to_csv('quotes_shuffed.csv', index=False)

def update_quotes_file():
  new_csv = shuffle_quotes()
  update_quotes(new_csv)
