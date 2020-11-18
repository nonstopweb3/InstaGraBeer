import numpy as np

before_sale = [60,51,61,52,56,53,68,57,60,70,72,68,70,78]
after_sale = [58,70,64,56,60,62,70,64,75,82,65,64,76,73]

def midle(arr):
	a = 0
	b = 0
	for price in arr:
		a += price
		b += 1

	return a/b

def mediana(arr):
	a = len(arr)
	if a % 2:
		b = a//2
		return(arr[b])
	else:
		b = a//2
		c = arr[b-1]+arr[b]
		return(c/2)

def despers(arr):
	a = 0
	b = 0
	for price in arr:
		a += price
		b += 1

	min_max = a/b
	arg = 0
	for x in arr:
		diya = x - min_max
		suma = diya**2
		arg += suma

	final = arg / (b-1)
	return final

def rozmax(arr):
	final = max(arr) - min(arr)
	return final

def standear_move(arr):
	return np.std(arr)

text = """\
\t\tПРОДАЖ ТОВАРУ
\tДО АКЦІЇ      ПІСЛЯ АКЦІЇ\n
"""
for a in zip(before_sale, after_sale):  
	text += f"\t\t  {a[0]}    |   {a[1]}\n"

text += f"""\
				|
Середнє\t{round(midle(before_sale), 2)}   |  {round(midle(after_sale), 2)} 
				|
Медіана\t{mediana(before_sale)}    |  {mediana(after_sale)}
				|
Диспер. {round(despers(before_sale), 2)}   |  {round(despers(after_sale), 2)} 
				|
Розмах\t{rozmax(before_sale)}      |  {rozmax(after_sale)}
\t\tАкція була успішною
"""

print(text)
