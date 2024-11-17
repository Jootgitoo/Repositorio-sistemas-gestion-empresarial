PYTHON_EXISTS = "python"
#Exercise 1

name = input("Whats your name?: ")
sales = input("How many sales have you done?: ")

comission = (float)(float(sales) * 13)/100

print(name+" your comission is "+str(comission))

#Exercise 2
text = input("Put the text: ")
letra1 = input("Insert the first letter: ")
letra2 = input("Insert the second letter: ")
letra3 = input("Insert the third letter: ")

cont1 =0
cont2 =0
cont3 =0

text = text.upper()
for i in range (0,len(text)):
    if text[i] == letra1.upper():
        cont1+=1
    elif text[i] == letra2.upper():
        cont2+=1
    elif text[i] == letra3.upper():
        cont3+=1

print("The letter "+letra1+" appears "+str(cont1)+" times in the text")
print("The letter "+letra2+" appears "+str(cont2)+" times in the text")
print("The letter "+letra3+" appears "+str(cont3)+" times in the text")

print("Words in the text: "+str(len(text.split())))

print("First letter: "+str(text[0])+"\nLast letter: "+str(text[len(text)-1]))

print(text[::-1])

def lookForPython(text):
    return PYTHON_EXISTS in text.lower()

def estaOno(text):
    answers = {
        "yes": "The word PYTHON appears in the text",
        "no": "The word PYTHON doesn't appear in the text"
    }
    if lookForPython(text):
        return answers["yes"]
    else:
        return answers["no"]

print(estaOno(text))