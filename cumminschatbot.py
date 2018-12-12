import os, slackclient, time
import random

# delay in seconds before checking for new events
SOCKET_DELAY = 1
# slackbot environment variables
VALET_SLACK_NAME = os.environ.get('SLACK_BOT_NAME')
VALET_SLACK_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
VALET_SLACK_ID = os.environ.get('SLACK_BOT_ID')
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
def is_private(event):
    """Checks if private slack channel"""
    return event.get('channel').startswith('D')
# how the bot is mentioned on slack
def get_mention(user):
    return '<@{user}>'.format(user=user)

valet_slack_mention = get_mention(VALET_SLACK_ID)

def is_for_me(event):
    """Know if the message is dedicated to me"""
    # check if not my own event
    type = event.get('type')
    if type and type == 'message' and not(event.get('user')==VALET_SLACK_ID):
        # in case it is a private message return true
        if is_private(event):
            return True
        # in case it is not a private message check mention
        text = event.get('text')
        channel = event.get('channel')
        if valet_slack_mention in text.strip().split():
            return True


def is_hi(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any(g in tokens
               for g in ['hello', 'bonjour', 'hey', 'hi', 'sup', 'morning', 'hola', 'ohai', 'yo'])


def is_bye(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any(g in tokens
               for g in ['bye', 'goodbye', 'revoir', 'adios', 'later', 'cya'])

def is_start(message1):
    if(message1 in ['Help', 'Get Started', 'Start']):
        return message1

def say_hi(user_mention):
    """Say Hi to a user by formatting their mention"""
    response_template = random.choice(['Sup, {mention}...',
                                       'Yo!',
                                       'Hola {mention}',
                                       'Bonjour!'])
    return response_template.format(mention=user_mention)


def say_bye(user_mention):
    """Say Goodbye to a user"""
    response_template = random.choice(['see you later, alligator...',
                                       'adios amigo',
                                       'Bye {mention}!',
                                       'Au revoir!'])
    return response_template.format(mention=user_mention)

def say_getHelp(user_mention):
    """Say Start to a user"""
    response_template = 'Let us get you started. Ask me any question about Cummins. #digitalTransformation'
    return response_template.format(mention=user_mention)

def is_whoareyou(message1):
    if(message1 in ['who are you', 'Who are you?', 'who are you?']):
        return message1

def say_whoareyou(user_mention):
    """Say Who are you to a user"""
    response_template = 'I am a Slack ChatBot. I try to answer questions. Sometimes I get them right, other times I need human help. I am designed to get smarter over time. How may I help you today?'
    return response_template.format(mention=user_mention)

def say_apologize(user_mention):
    """Apologize to a user"""
    response_template = 'My apologies. I did not understand the question. Please try again with one keyword and let me see if I can answer that for you.'
    return response_template.format(mention=user_mention)

def is_report(message3):
    if(message3 in ['How do I obtain copies of the Annual report for Cummins']):
        return message3

def say_report(user_mention):
    """Annual Report"""
    response_template = 'Go to investor.cummins.com and then on the left-hand navigation menu, under Contact Information click on Information Request, complete and submit the electronic form to have a copy of the Annual Report mailed to you promptly, or click on Annual Reports for an electronic copy.'
    return response_template.format(mention=user_mention)

def is_quarterly(message5):
    if(message5 in ['Does Cummins publish quarterly reports?']):
        return message5

def say_quarterly(user_mention):
    """Say Who are you to a user"""
    response_template = 'You can view our recent quarterly filings on our website http://investor.cummins.com/phoenix.zhtml?c=112916&p=irol-sec. Please click on this link.'
    return response_template.format(mention=user_mention)

def is_stock(message1):
    if(message1 in ['Does Cummins provide a direct stock purchase plan?']):
        return message1

def say_stock(user_mention):
    """Say Who are you to a user"""
    response_template = 'No, Cummins does not have a direct stock purchase plan. However, shareholders of record who participate in the Dividend Reinvestment Plan may elect to purchase additional shares of Cummins stock through an automatic monthly transfer of funds. See Dividend Reinvestment Plan.'
    return response_template.format(mention=user_mention)

def is_cust(message1):
    if(message1 in ['Who are Cummins’ largest customers?']):
        return message1

def say_cust(user_mention):
    """Say Who are you to a user"""
    response_template = 'We have thousands of customers around the world and have developed long-standing business relationships with many of them. We have long-term heavy-duty engine supply agreements with PACCAR, Navistar International, Volvo Trucks North America. We have long-term mid-range supply agreements with PACCAR, as well as with Daimler Trucks North America, Navistar, Ford and MAN. We also have an agreement with Chrysler for supplying the engine for use in Dodge Ram trucks. In our off-highway markets, Cummins has various engine and component supply agreements ranging across our midrange and high-horsepower businesses with Komatsu Ltd., as well as various joint ventures and other license agreements in our Engine, Component and Distribution segments.'
    return response_template.format(mention=user_mention)


def handle_message(message, user, channel):
    if is_hi(message):
        user_mention = get_mention(user)
        post_message(message=say_hi(user_mention), channel=channel)
    elif is_bye(message):
        user_mention = get_mention(user)
        post_message(message=say_bye(user_mention), channel=channel)
    elif is_whoareyou(message):
        user_mention = get_mention(user)
        post_message(message=say_whoareyou(user_mention), channel=channel)
    elif is_quarterly(message):
        user_mention = get_mention(user)
        post_message(message=say_quarterly(user_mention), channel=channel)
    elif is_stock(message):
        user_mention = get_mention(user)
        post_message(message=say_stock(user_mention), channel=channel)
    elif is_report(message):
        user_mention = get_mention(user)
        post_message(message=say_report(user_mention), channel=channel)
    elif is_start(message):
        user_mention = get_mention(user)
        post_message(message=say_getHelp(user_mention), channel=channel)
    elif is_cust(message):
        user_mention = get_mention(user)
        post_message(message=say_cust(user_mention), channel=channel)
    else:
        user_mention = get_mention(user)
        post_message(message=say_apologize(user_mention), channel=channel)

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
