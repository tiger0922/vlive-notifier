import requests

def telegram_bot_send_text(bot_message):

    bot_token = 'TOKEN'
    bot_chatID = 'CHATID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

test = telegram_bot_send_text('Message from Earth.')
print(test)
