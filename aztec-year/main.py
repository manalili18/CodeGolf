import sys
i=int(sys.argv[1])
s=['Tecpatl','Calli','Tochtli','Acatl']
print((i+2)%13+1,s[i%4])
