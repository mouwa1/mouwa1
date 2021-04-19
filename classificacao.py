id = input("entre com idade: ")
if id <= 0:
    print "erro"
else:
    if id <= 3:
        print "bebe"
    else:
        if id <= 11:
            print "crianca"
        else:
            if id <= 17:
                print "teen"
            else:
                if id <= 30:
                    print "jovem"
                else:
                    if id <= 64:
                        print "adulto"
                    else:
                        print "senior"
                
