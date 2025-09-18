import csv
arq = open("dados.csv","w",newline="")
grav = csv.writer(arq)
grav.writerow(["Nome","Idade","Cidade"])
grav.writerow(["Alice","23","Mossoró"])
grav.writerow(["Bianca","22","Tibau"])
grav.writerow(["Carol","27","Barauna"])
arq.close()
print("Gravado com sucesso.")