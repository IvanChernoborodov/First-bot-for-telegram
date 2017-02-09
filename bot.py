
import requests
import tok
import json
from birge import get_btc
# ______________________________________________GLOBAL___________________________________________
token=tok.token
URL = 'https://api.telegram.org/bot' + token + '/'
variance_function = ['getupdates', 'sendmessage?chat_id={}&text={}']
# _______________________________________________________________________________________________

def get_updates():
	url = URL + variance_function[0]
	response = requests.get(url)
	return response.json()
	
def save_json():
	content = get_updates()
	with open('content.json', 'w') as f:
		json.dump(content , f, indent=3)
	
def get_message():
	data = get_updates()
	proshe = data['result']
	chat_id = proshe[-1]['message']['from']['id']
	text = proshe[-1]['message']['text']
	message = {"chat_id": chat_id,
			 "text":text}
	return message	

def send_message(chat_id, text='Default text'):
		url = URL + variance_function[1].format(chat_id, text)
		requests.get(url)
		

def main():
	answer =get_message()
	chat_id = answer['chat_id']
	text = answer['text']
	if text == '/btc':
		send_message(chat_id, get_btc())

if __name__ == '__main__':
	main()