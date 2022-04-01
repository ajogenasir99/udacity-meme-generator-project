"""Creates class that will be used to draw over images."""

from curses import wrapper
from email.mime import image
from PIL import Image, ImageDraw, ImageFont
import PIL
import os
import random
import textwrap


class MemeEngine():
    """Meme generator Class."""

    def __init__(self, output_dir):
        """Check for output directory & creates path if it does not exist."""
        self.output_dir = output_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Write on an image to create a meme."""
        outfile = os.path.join(
            self.output_dir,
            f"meme-{random.randint(0,10000000)}.jpg"
        )

        try:
            with Image.open(img_path) as img:
                if width is not None:
                    img_width, img_height = img.size
                    ratio = width/float(img_width)
                    height = int(img_height * ratio)
                    if img_width > 500:
                        new_image = img.resize((width, height), Image.NEAREST)
                    else:
                        new_image = img

                full_quote = f"{text}\n - {author}"
                wrapper = textwrap.TextWrapper(width=40)
                quote_text = full_quote
                quote_text = wrapper.fill(text=quote_text)

                stroke_fill = 'black'
                fnt = ImageFont.truetype(
                    "./_data/Fonts/LilitaOne-Regular.ttf", 20)
                text_pos = random.randint(35, height - 50)
                d = ImageDraw.Draw(new_image)

                d.text((10, text_pos), quote_text, font=fnt,
                       stroke_fill=stroke_fill, fill='white')

            new_image.save(outfile, "JPEG")

            return outfile

        except PIL.UnidentifiedImageError:
            print('Path Invalid Unable to open Image')
            img = Image.new('RGB', (500, 300), color=(73, 109, 137))
            d = ImageDraw.Draw(img)
            d.text((10, 10), "Invalid Image Url", fill=(255, 255, 0))
            img.save(outfile, 'JPEG')
            return outfile
