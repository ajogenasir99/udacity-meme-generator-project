"""Creates class that will be used to draw
over images"""

from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine():
    """Meme generator Class"""

    def __init__(self, output_dir):
        """Check for output directory & creates path if it does not exist"""
        self.output_dir = output_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Writes on an image to create a meme"""
        img = Image.open(img_path)
        outfile = os.path.join(
            self.output_dir,
            f"meme-{random.randint(0,10000000)}.jpg"
        )

        img_width, img_height = img.size
        ratio = width/float(img_width)
        height = int(img_height * ratio)

        fnt = ImageFont.truetype("./_data/Fonts/LilitaOne-Regular.ttf", 20)
        text_pos = random.randint(35, height - 50)
        d = ImageDraw.Draw(img)

        d.text((10, text_pos), text, font=fnt, fill='white')
        d.text((20, text_pos + 20), f"- {author}", font=fnt, fill="white")
        img.save(outfile, "JPEG")
        return outfile
