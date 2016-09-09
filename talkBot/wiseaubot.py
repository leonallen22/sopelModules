import sopel.module
import random
from gen import Generator
from parse import Parser
from rnd import Rnd
from sql import Sql
from db import Db
import sqlite3


SENTENCE_SEPARATOR='.'
WORD_SEPARATOR=' '
DEFAULT_LENGTH=1
NAME='wiseau'

losers = []
insults = ["u idiot", "go home", "who even invited u", "delete ur account", "u nerd"]

#db = Db(sqlite3.connect(NAME + '.db'), Sql())
#db.setup(2)

#file_ = open('/home/adtran/.sopel/modules/Wiseau.txt')
#text = file_.read().decode('utf-8', 'ignore')
#Parser(NAME, db, SENTENCE_SEPARATOR, WORD_SEPARATOR).parse(text)
#markov = markovgen.Markov(file_)



def checkForOwner(trigger):
	ownerAliases = ["lallen", "leon", "allen", "harry", "sklooh"]
	trigger = trigger.lower()
	for alias in ownerAliases:
		if alias in trigger:
			return True
	else:
		return False

@sopel.module.nickname_commands('pontificate')
def pontificate(bot, trigger):
	print "Generating sentence..."
	markLen = [int(x) for x in trigger.split() if x.isdigit()]

	db = Db(sqlite3.connect(NAME+'.db'), Sql())
	gen = Generator(NAME, db, Rnd())

	for i in range(0,DEFAULT_LENGTH):
		bot.say(gen.generate(WORD_SEPARATOR))

@sopel.module.nickname_commands('losers')
def printLosers(bot, trigger):
	print "Printing losers..."
	for loser in losers:
		bot.say(loser)

@sopel.module.nickname_commands('clear')
def clearLosers(bot, trigger):
	print "Clearing losers list..."
	losers = ['alangham']

@sopel.module.rule('.+ is a loser$')
def addLoser(bot, trigger):
	print "Adding a loser..."
	tokens = trigger.split()

	if trigger.startswith("wiseaubot, "):
		newName = tokens[1]
		if not checkForOwner(trigger) and newName not in losers:
			losers.append(newName)
	else:
		newName = tokens[0]
		if not checkForOwner(trigger) and newName not in losers:
			losers.append(newName)

@sopel.module.rule('wiseaubot,.*get mad.*')
def insult(bot, trigger):
	print "Insulting..."
	numLosers = len(losers)
	numInsult = len(insults)
	randVict = random.randint(0,numLosers-1)
	randInsult = random.randint(0,numInsult-1)
	victim = losers[randVict]
	x = insults[randInsult]
	bot.say(victim + ' ' +x)
