import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=3,
    border=4,
)

qr.add_data('http://www.gepca.fr/')
qr.make(fit=True)

img = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 0))
img.save('qrcodeGEPCA.png')