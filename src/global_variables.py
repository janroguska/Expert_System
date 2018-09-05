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
	"defined_values": [],
	"to_find": [],
	"statements": []
}

class statementObject:
	rule = ""
	connective = ""
	then = ""
