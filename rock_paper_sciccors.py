player1 = input("Enter player one name:\n")
player2 = input("Enter player two name:\n")

num1 = int(input(player1 + " enter a number 0, 1, or 2:\n"))
num2 = int(input(player2 + " enter a number 0, 1, or 2:\n"))

if num1 == 0 and num2 == 1:
	print(player2, "won", player1+"!!!")

if num1 == 0 and num2 == 2:
	print(player1, "won", player2+"!!!")

if num1 == 0 and num2 == 0:
	print("The match is a draw!!!")
	
if num1 == 1 and num2 == 1: 
	print("The match is a draw!!!")

if num1 == 1 and num2 == 0:
	print(player1, "won", player2+"!!!")

if num1 == 1 and num2 == 2:
	print(player2, "won", player1+"!!!")

if num1 == 2 and num2 == 1:
	print(player1, "won", player2+"!!!")

if num1 == 2 and num2 == 0:
	print(player2, "won", player1+"!!!")

if num1 == 2 and num2 == 2:
	print("The match is a draw!!!")