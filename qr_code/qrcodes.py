import segno
import os

qr_dict = {
    "https://www.pyschool.cl": "01_qr_pyschool_2024_site.png",
    "https://sebastiandres.github.io/pyschool_2025/": "02_qr_pyschool_2025_site.png",
    "https://github.com/sebastiandres/pyschool_2025": "03_qr_pyschool_2025_repo.png",
    "https://pyschool.streamlit.app": "04_qr_links_app.png",
}

for url, qr_filename in qr_dict.items():
    qrcode = segno.make(url)
    qr_filepath = os.path.join("images", qr_filename)
    qrcode.save(qr_filepath, scale=5)
    print(f"open {qr_filepath}")
