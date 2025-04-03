# Simple to generate the Qr code 

import qrcode as qr
img= qr.make("https://www.youtube.com/watch?v=btGd40yV47A")
img.save("jay_kumar_singh_QR.png")

# user can decide


import qrcode  

qr_code = qrcode.QRCode(  
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4,  
)  
qr_code.add_data("https://www.youtube.com/watch?v=btGd40yV47A")  
qr_code.make(fit=True)  

img = qr_code.make_image(fill="black", back_color="white")  
img.save("Sonal_kumar_singh_QR.png")  