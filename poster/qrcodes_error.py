import qrcode
from cairosvg import svg2png
#import qrcode.image.svg
import os

def create_qrcode(url, png_filepath):
    img = qrcode.make(url)#, image_factory=qrcode.image.svg.SvgImage)
    # Save to svg and png
    svg_filepath = png_filepath.replace(".png", ".svg")
    with open(svg_filepath, 'wb') as qr:
        img.save(qr)
    #print(f"open {svg_filepath}")
    # Convert from svg to png using inkscape
    svg2png(url=svg_filepath, write_to=png_filepath)
    print(f"open {png_filepath}")
    return

if __name__ == "__main__":
    """
    sites = {
        "https://sebastiandres.github.io/pyschool_2025/": os.path.join("images", "qr_pyschool_site.png"),
        "https://github.com/sebastiandres/pyschool_2025": os.path.join("images", "qr_poster_repo.png"),
        "https://github.com/sebastiandres/pyschool_2025/blob/main/pyschool-poster.pdf?raw=true": os.path.join("images", "qr_poster_pdf.png"),
        "https://sebastiandres.xyz": os.path.join("images", "qr_sebastiandres.png"),
    }
    for url, filepath in sites.items():
        create_qrcode(url, filepath)
    """
    svg2png(url="images/qr.svg", write_to="images/qr.png")
    print(f"open images/qr.png")