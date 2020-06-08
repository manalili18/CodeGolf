import sys
i=int(sys.argv[1])
s=['Tecpatl','Calli','Tochtli','Acatl']
print(str((i+2)%13+1)+' '+str(s[i%4]))
