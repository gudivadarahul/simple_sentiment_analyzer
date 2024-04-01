import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

def analyze(sentence):
  sia = SentimentIntensityAnalyzer()
  score = sia.polarity_scores(sentence)
  print(f"Sentiment Score: {score}")

if __name__ == "__main__":
    print("Type a sentence to analyze its sentiment ('exit' to quit):")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            break
        analyze(user_input)


