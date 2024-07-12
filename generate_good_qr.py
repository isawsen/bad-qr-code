import qrcode

# Use the customized Bitly short URL
short_url = "https://bit.ly/Valtech-secure-redirect"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(short_url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("good_qr_code.png")
