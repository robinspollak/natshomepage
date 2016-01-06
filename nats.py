from flask import Flask, url_for, render_template
from datetime import datetime as t
import sys
import logging
nats = Flask(__name__)
nats.logger.addHandler(logging.StreamHandler(sys.stdout))
nats.logger.setLevel(logging.ERROR)

def getGameNumber():
	for i in range(162):
		date = listofgames[i]
		if (t.today().day<=date.day and t.today().month<=date.month and t.today().year<=date.year):
			return i
	return 999
f = open('natsschedule.txt') #file containing information
listofgames = []
for line in f:
	listofgames.append(line)
listofgames = map(lambda x: t.strptime(x[0],"%m/%d/%y"),\
	map(lambda x:x.split('|'),listofgames))

@nats.route('/')
def index():
	gamenum=getGameNumber()
	if gamenum != 999:
		gameToday = (listofgames[gamenum].day==t.today().day)
		if gameToday:
			return render_template('gameday.html', gameNumber=gamenum+1, opponent=(splitlist[gamenum][2]), gametime=(splitlist[gamenum][1]))
		else:
			timetilgame = listofgames[gamenum]-t.today()
			if timetilgame.days==0:
				return render_template('gametomorrow.html', gameNumber=gamenum, opponent=(splitlist[gamenum][2]), gametime=(splitlist[gamenum][1]))
			return render_template('nogame.html', days=timetilgame.days)	
	else:
		return render_template('seasonover.html')
		
if __name__=='__main__':
	nats.debug=True
	nats.run()




