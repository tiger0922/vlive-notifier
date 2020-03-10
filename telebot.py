import requests

f = open('token_file.txt', 'r')
List = []
for line in f.readlines():
    for word in line.split():
        List.append(word)
bot_token = List[1]
bot_chatID = List[3]

def send_text(bot_message):

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


