import os, slackclient, time
import random

# delay in seconds before checking for new events 
SOCKET_DELAY = 1
# slackbot environment variables
VALET_SLACK_NAME = os.environ.get('VALET_SLACK_NAME')
VALET_SLACK_TOKEN = os.environ.get('VALET_SLACK_TOKEN')
VALET_SLACK_ID = os.environ.get('VALET_SLACK_ID')
valet_slack_client = slackclient.SlackClient(VALET_SLACK_TOKEN)
def is_for_me(event):
    # TODO Implement later
    return True
def handle_message(message, user, channel):
    # TODO Implement later
    post_message(message='Hello', channel=channel)
def post_message(message, channel):
    valet_slack_client.api_call('chat.postMessage', channel=channel,
                          text=message, as_user=True)
def run():
    if valet_slack_client.rtm_connect():
        print('[.] Valet de Machin is ON...')
        while True:
            event_list = valet_slack_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print(event)
                    if is_for_me(event):
                        handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
            time.sleep(SOCKET_DELAY)
    else:
        print('[!] Connection to Slack failed.')

if __name__=='__main__':
    run()
