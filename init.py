import libraries
import json
words = []
classes = []
documents = []
ignore_words = ['?', '!']
intents = json.loads(open('intents.json').read())
kaggle_intents = json.loads(open('kaggle_intent.json').read())
c_intents = json.loads(open('complete_intents.json').read())