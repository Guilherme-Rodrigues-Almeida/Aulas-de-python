# Operadores aritiméticos
# ** = potencia; // = divisão inteira; % = resto da divisão

#ordem de precedência: 1º (); 2º **;  3º *,/,//,% ;  4º +,-;

#Raiz quadrada de um número(n) = n**0.5 ou n**(1/2)
#Raiz cúbica n**(1/3)

n = 81
print(n**(1/2))
print(n**(1/3))

print("ola" * 20)
print("")
print("")

nome = input("Qual o seu nome?: ")
print("Prazer em te conhecer {:=^20}!".format(nome))

print("")
print("")

n1 = int(input("Um valor: "))
n2= int(input("Segundo valor: "))

print(f"A soma vale: {n1 + n2}, \no produto é: {n1 * n2}, \na divisão é: {n1 / n2}", end = ", ")
print(f"\ndivisão inteira é: {n1 // n2} \ne a potência é: {n1 ** n2}")