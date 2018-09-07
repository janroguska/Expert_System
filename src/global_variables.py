# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    globals.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jroguszk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/05 16:19:22 by jroguszk          #+#    #+#              #
#    Updated: 2018/09/05 16:19:24 by jroguszk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

statement_dict = {
	"to_find": [],
	"A": None,
	"B": None,
	"C": None,
	"D": None,
	"E": None,
	"F": None,
	"G": None,
	"H": None,
	"I": None,
	"J": None,
	"K": None,
	"L": None,
	"M": None,
	"N": None,
	"O": None,
	"P": None,
	"Q": None,
	"R": None,
	"S": None,
	"T": None,
	"U": None,
	"V": None,
	"W": None,
	"X": None,
	"Y": None,
	"Z": None
}

class factObject:
	value = []
	rules = []
	negated = []
	truth = "F"

class OrNode:
	values = []
	negated = []

class AndNode:
	values = []
	negated = []

class XorNode:
	values = []
	negated = []

class BracketsNode:
	rules = []
	negated = 0