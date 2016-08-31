from loremipsum import Generator
import unicodedata
import re

class TextGenerator(object):
	generator = None

	def __init__(self):
		file = 'Wiseau.txt'

		with open(file, 'r') as sample_file:
			sample = sample_file.read().decode('utf-8')

		dictionary = self.buildDict(file)
		self.generator = Generator(sample, dictionary)

	def encodeAsAscii(self, text):
		normalizedText = unicodedata.normalize('NFKD', text)
		encodedText = normalizedText.encode('ascii', 'ignore')
		return encodedText

	def parseTextAsDict(self, text):
		symbols = "\"\';:.,?!@#$%^&*()-_=+][\{\}\\|<>`~"
		text = text.lower()
		return re.findall(r"[\w']+", text)

	def buildDict(self, file):
		with open(file, 'r') as dictionary_file:
			dictionaryText = dictionary_file.read()
			parsedDict = self.parseTextAsDict(dictionaryText)

		return list(set(parsedDict))

	def generate(self, text):
		#Indices 0 and 1 are simply statistical info, ignore them
		generatedText = self.generator.generate_sentence()[2]
		return self.encodeAsAscii(generatedText)
