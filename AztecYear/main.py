import sys
i=int(sys.argv[1])
s=['Tochtli','Acatl','Tecpatl','Calli']
print(str((i+2)%13+1)+' '+str(s[(i+2)%4]))
