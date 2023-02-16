# invertir numero de 4 digitos

# input

A = int(input("se ingresa numero de 4 digitos: "))

# processing


c4 = (A%10) * 1000
pe A//10
c3 = (A%10) * 100
pe A//10
c2 = (A%10) * 10
c1 = pe//10

nj = c1 + c2 + c3 + c4

# output

print("-------------------------------")
print("---------resultado-------------")
print("-------------------------------")

print("el numero invertido es: " + str(nj))
