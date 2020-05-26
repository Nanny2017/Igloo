from random import choice
def initial():
		a = input("Please enter name of player 1 : ")
		print(a)
		b = input("Please enter name of player 2 : ")
		print(b)
		"""player list"""
		p = [a,b]
		"""a player shout the number that shown in input list"""
		i = [5,10,15,20]
		"""players instantly provide their number that shown in output list"""
		o = [0,5,10]
		start = choice(p)
		print("Who will start the game : "+start)
		shout = choice(i)
		print("Number that "+start+" shout : ",int(shout))
		"""number that actually shown by players as below"""
		ch_a = choice(o)
		print("Player 1 number: ",int(ch_a))
		ch_b = choice(o)
		print("Player 2 number: ",int(ch_b))
		"""sum of both numbers that chosen by players"""
		a_b = int(ch_a) + int(ch_b)
		if int(shout) != a_b:
			print("Numbers not match!")
		else:
			print(start+" win the game!")
		
		cont = input("Continue the game? Yes or No : ")
		print(cont)
		if cont == "No":
			print("End game!")
		else:
			return initial()
initial()