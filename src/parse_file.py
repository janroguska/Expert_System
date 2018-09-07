# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse_file.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jroguszk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/05 16:13:34 by jroguszk          #+#    #+#              #
#    Updated: 2018/09/05 16:13:36 by jroguszk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import global_variables, tools

def populateNode(value, rule, obj, connective, i):
	global_variables.statement_dict[value].rules.append(obj)
	j = len(global_variables.statement_dict[value].rules) - 1
	print (global_variables.statement_dict[value].rules)
	for index, elem in enumerate(rule[i:]):
		if (elem.isalpha() == False and elem != connective and
			elem.startswith("!") == False):
			break
		if elem.isalpha() or elem.startswith("!"):
			if elem.startswith("!"):
				global_variables.statement_dict[value].rules[j].values.append(rule[i:][index])
				global_variables.statement_dict[value].rules[j].negated.append(0)
			elif elem.isalpha():
				global_variables.statement_dict[value].rules[j].values.append(elem)
				global_variables.statement_dict[value].rules[j].negated.append(1)
	return len(global_variables.statement_dict[value].rules[j].values)	

def populateDict(rule, fact, i):
	if global_variables.statement_dict[fact[i].replace("!", "")] == None:
		temp_object = global_variables.factObject()
		temp_object.value = fact[i].replace("!", "")
		if fact[i].startswith("!"):
			temp_object.negated = 0
		else:
			temp_object.negated = 1
		global_variables.statement_dict[fact[i].replace("!", "")] = temp_object
		if (i < len(fact) - 1):
			i += 2
			populateDict(rule, fact, i)
			return
	x = 0
	while x < len(rule):
		if rule[x] == "+":
			y = populateNode(fact[i].replace("!", ""), rule, global_variables.AndNode(), "+", x - 1)
			x += y
		elif rule[x] == "|":
			y = populateNode(fact[i].replace("!", ""), rule, global_variables.OrNode(), "|", x - 1)
			x += y
		elif rule[x] == "^":
			y = populateNode(fact[i].replace("!", ""), rule, global_variables.XorNode(), "^", x - 1)
			x += y
		else:
			x += 1

def checkStatementValidity(conclusion, rule):
	for index, elem in enumerate(conclusion):
		if ((elem.isalpha() and elem.isupper() and index % 2 == 1)
			or (elem.isalpha == False and index % 2 == 0)
				or (elem == "=>" or elem == "<=>")):
			return False
	for index, elem in enumerate(rule):
		if ((elem.isalpha() and elem.isupper() and index % 2 == 1)
			or (elem.isalpha == False and index % 2 == 0)):
			return False
	return True

def addToStatements(statement):
	string = statement.split()
	for index, elem in enumerate(string):
		if elem == "=>" or elem == "<=>":
			if checkStatementValidity(string[index + 1:], string[:index]) == False:
				tools.error("syntax error")
			populateDict(string[:index], string[index + 1:], 0)
			return
		if (((elem.isalpha() == False or elem.isupper() == False or len(elem) > 1)
			and elem != "|" and elem != "+"
				and elem != "^" and elem != "^" and elem.startswith("!")
					== False and elem.startswith("(") == False and
						elem.endswith(")") == False or len(elem) > 2)
							and (elem.startswith("(!") == False
								and elem.startswith("!(") == False or len(elem) > 3)):
			tools.error("syntax error")
	tools.error("syntax error")

def addToDefinedValues(statement):
	pass
	# string = statement[1:-1]
	# for i in string:
	# 	if i.isalpha() and i.isupper():
	# 		global_variables.statement_dict["defined_values"].append(i)
	# 	else:
	# 		tools.error("syntax error")

def addToToFind(statement):
	string = statement[1:-1]
	for i in string:
		if i.isalpha():
			global_variables.statement_dict["to_find"].append(i)
		else:
			tools.error("syntax error")

def getCorrectFunction(statement):
	string = statement.split()
	for elem in string:
		if elem.isalpha() or elem.startswith("("):
			return addToStatements
		elif elem.startswith("="):
			return addToDefinedValues
		elif elem.startswith("?"):
			return addToToFind
		else:
			tools.error("syntax error")

def parseFile(file):
	try:
		fd = open(file, "r")
	except IOError:
		tools.error("not a valid file")
	for line in fd:
		string = line.split("#")
		if len(string[0]) > 0:
			func = getCorrectFunction(string[0])
			func(string[0])