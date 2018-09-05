# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jroguszk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/05 09:29:38 by jroguszk          #+#    #+#              #
#    Updated: 2018/09/05 09:29:40 by jroguszk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, parse_file, tools

def main(av):
	if len(av) != 2:
		tools.error("incorrect number of arguments")
	parse_file.parseFile(av[1])

main(sys.argv)