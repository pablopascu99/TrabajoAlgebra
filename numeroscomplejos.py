#####################################################################
###---------------------NUMEROS COMPLEJOS-------------------------###
#####################################################################

a=int(input("Introduce el valor real del complejo 1: "))
b=int(input("Introduce el valor imaginario del complejo 1: "))
c=int(input("Introduce el valor real del complejo 2: "))
d=int(input("Introduce el valor imaginario del complejo 2: "))
n=int(input("Introduce el valor del escalar para calcular el producto: "))
m=int(input("Introduce el valor de la potencia para los complejos: "))

c1=complex(a,b)
c2=complex(c,d)

print("Complejo 1: ",c1)
print("Complejo 2: ",c2)

print("***-----------------IGUALDAD-------------------***")
print("¿Es igual?: ",c1==c2)

print("***----------------ESCOMPLEJO------------------***")
print("Tipo de c1: ",type(c1))
print("Tipo de c2: ",type(c2))

print("***---------PARTE REAL E IMAGINARIA------------***")
print("Parte real de c1: ",c1.real)
print("Parte imaginaria de c1: ",c1.imag)
print("Parte real de c2: ",c2.real)
print("Parte imaginaria de c2: ",c2.imag)

print("***-------------VALOR ABSOLUTO-----------------***")
print("Valor absoluto de c1: ",abs(c1))
print("Valor absoluto de c2: ",abs(c2))

print("***-------------------SUMA---------------------***")
print("c1+c2=",c1+c2)

print("***-------------------RESTA--------------------***")
print("c1-c2=",c1-c2)

print("***--------------PRODUCTO ESCALAR--------------***")
print("c1^n=",c1*n)
print("c2^n=",c2*n)

print("***-----------------CONJUGADO------------------***")
print("Conjugado de c: ",c1.conjugate())
print("Conjugado de c: ",c2.conjugate())

print("***---------------MULTIPLICACIÓN---------------***")
print("c1*c2=",c1*c2)

print("***-----------------DIVISIÓN-------------------***")
print("c1/c2=",c1/c2)

print("***-----------------POTENCIA-------------------***")
print("c1^n=",c1**m)
print("c2^n=",c2**m)




