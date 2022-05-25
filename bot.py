import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
from chat_functions import getResponse, predict_class
from chat_init import c_intents, model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'],
    '/slack/events',app)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

#client.chat_postMessage(channel='#test', text='Hello World!')
BOT_ID = client.api_call('auth.test')['user_id']


@slack_event_adapter.on('message')
def message(payload):
    event= payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    if BOT_ID != user_id:
        t = Tokenizer()
        input_size = model.layers[0].output_shape[1] #Gets the input size of the model. Add padding to this size
        tokens = t.texts_to_sequences([text])
        tokens = pad_sequences(tokens, maxlen = 2000)
        prediction = model.predict(np.array(tokens))
        pred = np.argmax(prediction)
        classes = ['Mulesoft','Customer Service Related','Tableau','Cloud Commerce']
        
        client.chat_postMessage(channel=channel_id, text=classes[pred])

#helper methods



if __name__ == '__main__':
    app.run(debug=True)