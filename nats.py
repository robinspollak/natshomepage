from flask import Flask, url_for, render_template
import time as t
nats = Flask(__name__)

gamenum=0
f = open('natsschedule.txt') #file containing information
listofgames = []
for line in f:
	listofgames.append(line)
splitlist = []
for game in listofgames: 
	splitlist.append(game.split('|'))
dayofgame = (t.strftime("%m/%d/%y")==game)
#print splitlist[0]
#print t.strftime("%m/%d/%y")
#print splitlist[0][0]
#print (t.strftime("%m/%d/%y") == splitlist[0][0])

@nats.route('/')
def index():
	return render_template('indexpage.html')


#with nats.test_request_context():
#	print url_for('static', filename=cats)
	
		
if __name__=='__main__':
	nats.debug=True
	nats.run()




