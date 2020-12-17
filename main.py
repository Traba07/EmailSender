import smtplib

print("############### LOGIN ###############")
mail = input("email: ")
password = input("password: ")
print("############### SEND MAIL ###############")
utente = input ("mail: ")
o1 = input ("Subject: ")
contenuto = input ("Content: ")
emittente = mail

o2 = "Subject: "
o3 = "\n\n"

oggetto = o2 + o1 + o3

messaggio = oggetto + contenuto

email = smtplib.SMTP("smtp.gmail.com", 587)

email.ehlo()

email.starttls()

email.login(emittente, password)
email.sendmail(emittente,utente,messaggio)

print("send to", utente)
email.quit()