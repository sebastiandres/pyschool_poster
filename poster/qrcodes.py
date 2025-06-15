# scaled_qrcode.py

import segno
import os

qr_dict = {
    "https://sebastiandres.github.io/pyschool_2025/": "qr_pyschool_site.png",
    "https://github.com/sebastiandres/pyschool_2025": "qr_poster_repo.png",
    "https://github.com/sebastiandres/pyschool_2025/blob/main/pyschool-poster.pdf?raw=true": "qr_poster_pdf.png",
    "https://sebastiandres.xyz": "qr_sebastiandres.png",
}

for url, qr_filename in qr_dict.items():
    qrcode = segno.make(url)
    qr_filepath = os.path.join("images", qr_filename)
    qrcode.save(qr_filepath, scale=5)
    print(f"open {qr_filepath}")
