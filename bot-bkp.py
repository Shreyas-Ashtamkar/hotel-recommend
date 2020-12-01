
#Imports for the Chat Bot
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
bot = Flask(__name__)

#Imports for the recommender
from recommender import main

form = ""
with open('homepage.html', 'r') as page:
	form = page.read()

#Initialised with Some random defaults.
activeUsers = []

userDetails = {
	"user_id"		: 'user12'		,        # 1 - 50
	"trip_type"		: 'business'	,     # business vs leisure
	"companion"		: 'couple'		,        # couple | family | friend | solo
	"destination"	: 'singapore'    # singapore | tokyo | bankok
}

questions = [
	"Hii! What is your User ID ?",
	"What is the type of trip you have ? \n\n1. Business \n2. Leisure\n\nEnter your choice ? (1\\2)",
	"How are you travelling ? \n\n1. Couple\n2. Family\n3. Friend\n4. Solo\n\nEnter your choice ? (1\\2\\3\\4)",
	"What is your destination ? \n\n1. Singapore\n2. Tokyo\n3. Bankok\n\nEnter your choice ? (1\\2\\3)",
]

@bot.route('/', methods = ['GET','POST'])
def homePage():
	msg = request.form.get('body')
	
	if msg == None:
		return form
	else:
		resp = "WORKING"
		# resp = predict(msg)"WORKING"
		return resp

	
@bot.route('/whatsapp/', methods = ['POST'])
def whatsapp():
	msg = request.form.get('Body')

	if msg not in [None,'']:
		resp = "Working"
		# resp = predict(msg.strip()	)
	else:
		resp = "Invalid input"
	msg =  MessagingResponse()
	msg.message(resp)
	return str(msg)

# print(output)

if __name__ == "__main__": 
	userDetails = {
		"user_id"                            : 'user12',        # 1 - 50
		"trip_type"							 : 'business',     # business vs leisure
		"companion"						  : 'couple',        # couple | family | friend | solo
		"destination"						: 'singapore'    # singapore | tokyo | bankok
	}

	output = main(
		userDetails['destination'], 
		userDetails['user_id'], 
		userDetails['trip_type'], 
		userDetails['companion']
	)
	print(output)

	# bot.run(debug = True)

