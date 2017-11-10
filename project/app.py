from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
	"""Respond to incoming calls with a simple text msg."""
	# start pir TwiML response
	resp = MessagingResponse()

	# Add a message
	resp.message("Andie Sunwoo.. you are the love of my life <3. Stop working so hard!")

	return str(resp)

if __name__ == '__main__':
	app.run(debug=True)