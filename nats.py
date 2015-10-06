from flask import Flask, url_for, render_template
from datetime import datetime as t
import sys
import logging
nats = Flask(__name__)
nats.logger.addHandler(logging.StreamHandler(sys.stdout))
nats.logger.setLevel(logging.ERROR)

def getGameNumber():
	for i in range(162):
		date = datelist[i]
		if (t.today().day<=date.day and t.today().month<=date.month):
			return i
		else:
			return 999
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

@nats.route('/')
def index():
	gamenum=getGameNumber()
	gameToday = (datelist[gamenum].day==t.today().day)
	if gamenum == 999:
		return render_template('seasonover.html')
	elif gameToday:
		return render_template('gameday.html', gameNumber=gamenum+1, opponent=(splitlist[gamenum][2]), gametime=(splitlist[gamenum][1]))
	else:
		timetilgame = datelist[gamenum]-t.today()
		if timetilgame.days==0:
			return render_template('gametomorrow.html', gameNumber=gamenum, opponent=(splitlist[gamenum][2]), gametime=(splitlist[gamenum][1]))
		return render_template('nogame.html', days=timetilgame.days)	
		
if __name__=='__main__':
	nats.debug=True
	nats.run()




