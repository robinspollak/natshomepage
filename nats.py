from flask import Flask, url_for, render_template
from datetime import datetime as t
nats = Flask(__name__)

gamenum=0
gameToday = False
f = open('natsschedule.txt') #file containing information
listofgames = []
for line in f:
	listofgames.append(line)
splitlist = []
for game in listofgames: 
	splitlist.append(game.split('|'))
datelist = []
for game in splitlist:
	datelist.append(t.strptime(game[0],"%m/%d/%y"))
#dayofgame = (t.strftime("%m/%d/%y")==game)
#print splitlist[0]
#print t.strftime("%m/%d/%y")
#print splitlist[0][0]
#print (t.strftime("%m/%d/%y") == splitlist[0][0])

@nats.route('/')
def index():
	if gameToday and (t.today().day>currentdate.day or t.today().month>currentdate.month):
		gameToday = False
	if t.today()==datelist[gamenum]:
		gameToday = True
		currentdate = t.today()
		gamenum+=1
	return render_template('indexpage.html')


#with nats.test_request_context():
#	print url_for('static', filename=cats)
	
		
if __name__=='__main__':
	nats.debug=True
	nats.run()




