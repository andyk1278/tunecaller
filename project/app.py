import spotify

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import urllib

from random import randint

client = Client('AC73040659450e04d2b11237f2be163bef', '71665748fae6613db44132fe6187c078')
app = Flask(__name__)

# A route to respoind to SMS msgs and kick off a phone call
@app.route('/sms', methods=['POST'])
def inbound_sms():
	response = MessagingResponse()
	response.message("Hey you, I'm searching for your song as we speak!"
					 "Hang tight, and I will call you shortly.")

	# Grab the song title from the body of the txt msg
	song_title = urllib.parse.quote(request.form['Body'])

	# Grab the relevant phone numbers
	from_number = frequest.form['From']
	to_number = request.form['To']

	# Create a phone call that uses the other route to play a song from Spotify
	client.api.account.calls.create(to=from_number, from_=to_number,
								url='http://sagnew.ngrok.op/call?track={}'.format(song_title))

	return str(response)

# A route to handle the logic for phone calls
@app.route('/call', methods=['POST'])
def oubound_call():
	song_title = request.args.get('track')
	track_url = spotify.get_track_url(song_title)

	response = MessagingResponse()
	response.play(track_url)
	return str(response)

# @app.route("/ball8", methods=['GET', 'POST'])
# def ball8_sms_reply():
# 	"""Respond to incoming sms msgs with a simple text msg."""
# 	responses = {
# 			 1: 'It is certain',
# 			 2: 'It is decidedly so',
# 			 3: 'Without a doubt',
# 			 4: 'Yes definitely',
# 			 5: 'You may rely on it',
# 			 6: 'As I see it, yes',
# 			 7: 'Most likely',
# 			 8: 'Outlook good',
# 			 9: 'Signs point to yes',
# 			 10: 'Reply hazy try again',
# 			 11: 'Ask again later',
# 			 12: 'Better not tell you now',
# 			 13: 'Cannot predict now',
# 			 14: 'Concentrate and ask again',
# 			 15: 'Don\'t count on it',
# 			 16: 'My reply is no',
# 			 17: 'My sources say no',
# 			 18: 'Outlook not so good',
# 			 19: 'Very doubtful',
# 	}

# 	response = responses[randint(1,19)]

# 	# start pir TwiML response
# 	resp = MessagingResponse()

# 	# Add a messag de
# 	resp.message(response)

# 	return str(resp)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)