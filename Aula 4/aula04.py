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

n1 = float(input("Um valor: "))
n2= float(input("Segundo valor: "))

print(f"A soma vale: {n1 + n2:.3f}, \no produto é: {n1 * n2:.3f}, \na divisão é: {n1 / n2:.3f}", end = ", ")
print(f"\ndivisão inteira é: {n1 // n2:.3f} \ne a potência é: {n1 ** n2:.3f}")