idade = input("idade: ")
if idade <= 0:
    print "erro", idade
elif idade <= 3:
    print "bebe", idade
elif idade <= 11:
    print "crianca", idade
elif idade <= 17:
    print "teen", idade
elif idade <= 30:
    print "jovem", idade
elif idade <= 64:
    print "adulto", idade
else:
    print "senior", idade
