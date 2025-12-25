import qrcode

url = input("Enter the URL: ").strip()

file_path = r"D:\Python\qrcode.png"   # raw string is safer

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)   # ✅ IMPORTANT

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print("QR Code was generated successfully")
print(f"Saved at:{file_path}")



