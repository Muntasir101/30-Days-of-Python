"""
create a QR code for sharing WiFi password
"""

import qrcode

# WiFi credentials
ssid = "Muntasir_2.4G"
password = "25258586"
security = "WPA"   # Security type (WEP, WPA, etc.)

# Generate WiFi QR code
wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(wifi_config)
qr.make(fit=True)

# Save QR code as an image file
img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_qr.png")
