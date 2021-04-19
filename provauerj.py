n1 = input("entre com n1: ")
n2 = input("entre com n2: ")
nf = (n1+n2) / float(2)
if nf>=7:
    print "aprovado ", nf
else:
    if nf >=4:
        print "prova final ", nf
    else:
        print "reprovado ", nf
