import qrcode
#import qrcode.image.svg
import os

def create_qrcode(url, filepath):
    img = qrcode.make(url)#, image_factory=qrcode.image.svg.SvgImage)

    # Save to svg and png
    with open(filepath, 'wb') as qr:
        img.save(qr)
    print(f"open {filepath}")
    return

if __name__ == "__main__":
    sites = {
        "https://sebastiandres.github.io/pyschool_2025/": os.path.join("images", "qr_pyschool_site.svg"),
        "https://github.com/sebastiandres/pyschool_2025": os.path.join("images", "qr_poster_repo.svg"),
        "https://github.com/sebastiandres/pyschool_2025": os.path.join("images", "qr_poster_pdf.svg"),
        "https://sebastiandres.xyz": os.path.join("images", "qr_sebastiandres.svg"),
    }


    for url, filepath in sites.items():
        create_qrcode(url, filepath)
