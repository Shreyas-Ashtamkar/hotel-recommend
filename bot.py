
#Imports for the Chat Bot
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
bot = Flask(__name__)

#Imports for the recommender
from recommender import main as predict
from questionnaire import User

form = ""
with open('homepage.html', 'r') as page:
	form = page.read()

#Keep Track of Currently Active Users
activeUsers = {}
def selectUser(phNo):
	global activeUsers

	if phNo not in activeUsers:
		activeUsers[phNo] = User()

	return activeUsers[phNo]

@bot.route('/', methods = ['GET','POST'])
def homePage():
	userPhone   = request.form.get('from')
	userMessage = request.form.get('body')
	
	if userMessage == None:
		return form
	else:
		resp = "WORKING"
		# resp = predict(userMessage)"WORKING"
		return resp

	
@bot.route('/whatsapp/', methods = ['POST'])
def whatsapp():
	msg = request.form.get('Body')

	if msg not in [None,'']:
		resp = "Working"
		# resp = predict(msg.strip())
	else:
		resp = "Invalid input"
	msg =  MessagingResponse()
	msg.message(resp)
	return str(msg)

# print(output)

if __name__ == "__predict__": 
	userDetails = {
		"user_id"        : 'user12',        # 1 - 50
		"trip_type"		 : 'business',      # business vs leisure
		"companion"		 : 'couple',        # couple | family | friend | solo
		"destination"	 : 'singapore'      # singapore | tokyo | bankok
	}

	output = predict(
		userDetails['destination'], 
		userDetails['user_id'], 
		userDetails['trip_type'], 
		userDetails['companion']
	)
	print(output)

	# bot.run(debug = True)

