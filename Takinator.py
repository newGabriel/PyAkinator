import akinator as ak

from os import system, name


def cls():
	if name == 'nt':
		system('cls')
	else:
		system('clear')


aki = ak.Akinator()

q = aki.start_game(language='pt')


while aki.progression <= 80:
	cls()
	print(q,"\n")
	print("y - sim")
	print("n - não")
	print("i - não sei")
	print("p - provavelmente sim")
	print("pn - provavelmente não")

	print("b - corrigir")

	a = input("Resposta: ")

	cls()
	print("Processando...")

	if a == 'b':
		try:
			q = aki.back()
		except ak.CantGoBackAnyFurther:
			pass
	else:
		try:
			q = aki.answer(a)
		except ak.exceptions.InvalidAnswerError:
			pass
	
aki.win()
c = input(f"Você pensou no(a) {aki.first_guess['name']} ({aki.first_guess['description']})? S/n\n")
if c.lower()=='s':
	print("Eu sou mesmo um genio :-)")
else:
	print("Você me venceu :-(")
	
