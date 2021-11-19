import pandas as pd

def get_quote():
  # Pull a quote from the csv
  quotes = pd.read_csv('quotes.csv')

  my_quote = quotes.iloc[0]
  quote = my_quote[0]
  author = my_quote[1]

  # # Shuffle the csv and put it back
  # quotes = quotes.drop(quotes.index[0])
  # quotes.iloc[-1] = my_quote
  # quotes.reset_index()
  # quotes.to_csv('quotes.csv')

  return quote, author


def create_tweet(quote, author):
  return "{}  -- {}".format(quote, author)

# tweet = create_tweet(get_quote())

def assemble():
  quote, author = get_quote()
  tweet = create_tweet(quote, author)
  return tweet

sample = assemble()
print(sample)


