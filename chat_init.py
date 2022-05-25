import init
from libraries import pickle
from tensorflow.keras.models import load_model
import json
import random

#Load Model here
model = load_model('bi_chatbot_model.h5')


kaggle_intents = json.loads(open('kaggle_intent.json').read())
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
c_intents = json.loads(open('complete_intents.json').read())


#list = []
#list.extend(kaggle_intents['intents'])
#list.extend(intents['intents'])
#c_intents = dict()
#c_intents['intents'] = list


#save words and classes
#with open('words.pkl', 'wb') as f:
    #pickle.dump(words, f)
#with open('classes.pkl','wb') as f:
    #pickle.dump(classes, f)
    
#write complete_intents to json file
#with open('complete_intents.json', 'w') as outfile:
    #json.dump(c_intents, outfile)
