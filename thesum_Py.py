import sys

f = open("sum.dat", "r")
#print f
#sys.exit(0)

if not f:
    print "File inesistente, il valore di partenza e' 0"

else:
    print "Lettura da sum.dat in corso ..."
    line = f.readline()
    num = int(line)
    print "Valore attuale in sum.dat: ", num
    f.close

num_input = input("Digita un valore da sommare: ")

somma = num + num_input

print "Nuovo valore: ", somma
print "Salvataggio in sum.dat in corso ..."
f = open("sum.dat", "w")
f.write(str(somma))

f.close()


