f = open("sum.dat", "r")

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


