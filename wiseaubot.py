import sopel.module
import markovgen

losers = []
file_ = open('Wiseau.txt')
markov = markovgen.Markov(file_)

@sopel.module.nickname_commands('pontificate')
def pontificate(bot, trigger):
	print "Generating sentence..."
	bot.say(markov.generate_markov_text(10))

@sopel.module.nickname_commands('losers')
def printLosers(bot, trigger):
	print "Printing losers..."
	for loser in losers:
		bot.say(loser)

@sopel.module.rule('.+ is a loser$')
def addLoser(bot, trigger):
	print "Adding a loser..."
	nickLen = len(bot.nick)
	lowerBound = nickLen+2
	trigLen = len(trigger)
	upperBound = trigLen-11
	losers.append(trigger[lowerBound:upperBound])
