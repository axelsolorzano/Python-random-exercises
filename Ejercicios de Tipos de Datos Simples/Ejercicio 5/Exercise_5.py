#Escribir un programa que pregunte al usuario por el número de horas trabajadas 
#y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
hours = int(input("How many hours do you work?"));
cash = int(input("how many cash pay for hour?"));
total = hours * cash;
print("you get:",total,"of Cash");
