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
	temp_object = global_variables.statementObject()
	for index, elem in enumerate(string):
		if elem == "=>" or elem == "<=>":
			temp_object.connective = elem
			if checkStatementValidity(string[index + 1:], string[:index]) == False:
				tools.error("syntax error")
			temp_object.then = string[index + 1:]
			temp_object.rule = string[:index]
			print temp_object.rule
			global_variables.statement_dict["statements"].append(temp_object)
			return
		if ((elem.isalpha() == False or elem.isupper() == False or len(elem) > 1) and elem != "|" and elem != "+"
			and elem != "^" and elem != "^" and elem.startswith("!")
				== False and elem.startswith("(") == False and
					elem.endswith(")") == False or len(elem) > 2):
			tools.error("syntax error")
	tools.error("syntax error")

def addToDefinedValues(statement):
	string = statement[1:-1]
	for i in string:
		if i.isalpha() and i.isupper():
			global_variables.statement_dict["defined_values"].append(i)
		else:
			tools.error("syntax error")

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