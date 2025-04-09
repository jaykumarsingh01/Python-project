# You can send multiple email using python 
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Test Email with PDF Attachment'
msg['From'] = 'jaykumarsingh8117@gmail.com'
msg['To'] = ['225ucd001@gbu.ac.in']
msg.set_content('Hi,Please find the attached PDF.Regards,\nJay ,\n'
'My name is Jay, and I’m a passionate software engineer with a strong interest in coding, compiler design,'
' and full-stack development. I enjoy building practical solutions like attendance management systems,'
' using technologies like React, Node.js, and MongoDB. When I’m not coding, you’ll likely find me immersed in a good' 
' book like The Polyester Prince, competing in Free Fire, or spiking it on the volleyball court. '
'I’m always curious, always learning, and driven by the excitement of turning ideas into reality')

# file path
file_path = r"C:\Users\Dell\OneDrive\Desktop\Web_syllabus.pdf"

# Read and attach the PDF file
with open(file_path, 'rb') as f:
    file_data = f.read()
    file_name = 'Web_syllabus.pdf'
    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

# --- Attach Image ---
image_path = r"C:\Users\Dell\OneDrive\Desktop\images.png"
with open(image_path, 'rb') as f:
    image_data = f.read()
    msg.add_attachment(image_data, maintype='image', subtype='png', filename='images.png')

# SMTP send
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jaykumarsingh8117@gmail.com', 'your_16_char_app_password')
    smtp.send_message(msg)

print("Mail Sent Successfully!")

# ob.quit()


                                                #Jay Kumar Singh
