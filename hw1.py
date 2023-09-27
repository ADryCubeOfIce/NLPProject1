"""This is a sample file for hw1. 
It contains the function that should be submitted,
except all it does is output a random value out of the
possible values that are allowed. type2B, type2C, type2D, type2E, type2F
- Dr. Licato"""

import random
import re
import sys
import os

#[a|an]?
def problem1():
	hypernyms = set(['dogs', 'cats', 'mammals', 'living things']) 
	sentence1 = """All mammals, such as dogs and cats, eat to survive. Mammals are living things, aren't they?"""
	sentence2 = "Some animals, including cats, are considered. But it is NOT true that dogs are animals; I refuse to accept it."
	sentence3 = "Hemingway was an author of many classics. But also, Hemingway was a bibliophile, having read the works of every other famous American author, such as William Faulkner and Mark Twain."
	#for i in range(len(NPs)-1):
	#	hypernyms.add( (NPs[i], NPs[i+1]) ) #fill the set of hypernyms

	testingRegex = re.compile(r'(\w+) are ([\w\s*]+)')
	type1A = re.compile(r'(?![it])(\w+) (?:[is|are|was]) ([\w\s*]+)')
	type1B = re.compile(r'(\w+) is a type of (\w+)')
	type1C = re.compile(r'(\w+) is a kind of (\w+)')
	#type1D = re.compile(r'(\w+) was [a|an]* (\w+)')
	type1E = re.compile(r'(\w+) was a type of (\w+)')
	type1F = re.compile(r'(\w+) was a kind of (\w+)')
	#type1G = re.compile(r'(\w+) are ([\w\s*]+)')
	type1H = re.compile(r'(\w+) are a type of (\w+)')
	type1I = re.compile(r'(\w+) are a kind of (\w+)')
	type2A = re.compile(r'(\w+), [including|such as]+ ([\w\s*]+) and ([\w\s*]+)')
	type2B = re.compile(r'(\w+), including (\w+)')
	#type2C = re.compile(r'(\w+), including [(\w+), ]+, or (\w+)')
	#type2D = re.compile(r'(\w+), such as (\w+)')
	#type2E = re.compile(r'(\w+), such as [(\w+), ]+, and (\w+)')
	#type2F = re.compile(r'(\w+), such as [(\w+), ]+, or (\w+)')

	regexes = set([type1A, type1B, type1C, type1E, type1F, type1H, type1I, type2A, type2B])
	for regex in regexes:
		mo = regex.findall(sentence1)
		print(mo)
	return hypernyms


def problem2(s1, s2):
	# if len(s1) > len(s2):
	# 	difference = len(s1) - len(s2)
	# 	s1[:difference]

	# elif len(s2) > len(s1):
	# 	difference = len(s2) - len(s1)
	# 	s2[:difference]

	# else:
	# 	difference = 0

	# for i in range(len(s1)):
	# 	if s1[i] != s2[i]:
	# 		difference += 1

	# return difference
	if len(s1) < len(s2):
		return problem2(s2, s1)

	# len(s1) >= len(s2)
	if len(s2) == 0:
		return len(s1)

	previous_row = range(len(s2) + 1)
	for i, c1 in enumerate(s1):
		current_row = [i + 1]
		for j, c2 in enumerate(s2):
			insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
			deletions = current_row[j] + 1       # than s2
			substitutions = previous_row[j] + (c1 != c2)
			current_row.append(min(insertions, deletions, substitutions))
		previous_row = current_row

	return previous_row[-1]


print(problem2("""Don't let your dreams be dreams\nYesterday you said tomorrow\nSo just do it\nMake your dreams come true\nJust do it""",
		"""Some people dream of success\nWhile you're gonna wake up and work hard at it\nNothing is impossible"""))