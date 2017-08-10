import getre

a = ["-","0","1","2","3","4","5","6","7","8","9"]
b = ["0","1","2","3","4","5","6","7","8","9"]

sd = open("./txts/Urls.txt","w+")
print("Generating Urls.txt...done.")
sd.close()

sd = open("./txts/hash.txt","w+")
print("Generating hash.txt...done.")
sd.close()

for i in a:
    for n in b:
        for asd in b:
            sd = open("./txts/%s/%s/%s.txt" % (i,n,asd),"w+")
            print(i+"/"+n+"/"+asd)
            sd.close()

#for i in open("hash.txt","r"):
#    [asd] = getre.get(r'(.+)\n',i)
#    temp = open("./txts/%s/%s/%s.txt" % (str(asd)[0],str(asd)[1],str(asd)[2]),"at")
#    temp.write("%s\n" % asd)
#    print("./txts/%s/%s/%s.txt||||||%s" % (str(asd)[0],str(asd)[1],str(asd)[2],asd))
#    temp.close()