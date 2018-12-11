import os, slackclient

VALET_SLACK_NAME = os.environ.get('SLACK_BOT_NAME')
VALET_SLACK_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
# initialize slack client
valet_slack_client = slackclient.SlackClient(VALET_SLACK_TOKEN)
# check if everything is alright
print(VALET_SLACK_NAME)
print(VALET_SLACK_TOKEN)
is_ok = valet_slack_client.api_call("users.list").get('ok')
print(is_ok)

print ("hello world")

