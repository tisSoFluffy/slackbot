import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    #say(f"Hey there <@{message['user']}>!")
    view ={
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Employee Starting Date."
			},
			"accessory": {
				"type": "datepicker",
				"initial_date": "2022-01-01",
				"placeholder": {
					"type": "plain_text",
					"text": "Starting Date"
				},
				"action_id": "datepicker-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This is a section block with checkboxes."
			},
			"accessory": {
				"type": "checkboxes",
				"options": [
					{
						"text": {
							"type": "mrkdwn",
							"text": "Active Directory"
						},
						"description": {
							"type": "mrkdwn",
							"text": "Needs Accounting Updated"
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "mrkdwn",
							"text": "Accounting"
						},
						"description": {
							"type": "mrkdwn",
							"text": "*this is mrkdwn text*"
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "mrkdwn",
							"text": "*More stuff*"
						},
						"description": {
							"type": "mrkdwn",
							"text": "*this is mrkdwn text*"
						},
						"value": "value-2"
					}
				],
				"action_id": "checkboxes-action"
			}
		}
	]
}
    say(view)

@app.command('/hello-socket-mode')
def hello_command(ack, body):
    user_id = body['user_id']
    ack(f'Hi, <@{user_id}>!')

@app.event('app_mention')
def event_test(say):
    say('hi there')

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
    #SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()