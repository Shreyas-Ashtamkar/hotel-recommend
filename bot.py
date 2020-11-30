
#Imports for the Chat Bot
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
bot = Flask(__name__)

#Imports for the recommender
from recommender import main

form = ""

with open('homepage.html', 'r') as page:
	form = page.read()

@bot.route('/', methods = ['GET','POST'])
def homePage():
	msg = request.form.get('body')
	
	if msg == None:
		return form
	else:
		# resp = predict(msg)
		# return resp
		return "WORKING"

	
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
	# userDetails = {
	# 	"user_id"                            : 'user12',        # 1 - 50
	# 	"trip_type"							 : 'business',     # business vs leisure
	# 	"companion"						  : 'couple',        # couple | family | friend | solo
	# 	"destination"						: 'singapore'    # singapore | tokyo | bankok
	# }

	# output = main(
	# 	userDetails['destination'], 
	# 	userDetails['user_id'], 
	# 	userDetails['trip_type'], 
	# 	userDetails['companion']
	# )

	bot.run(debug = True)

