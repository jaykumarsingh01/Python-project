import smtplib as s

ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()

