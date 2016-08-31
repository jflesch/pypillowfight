import tempfile
import unittest

import PIL.Image

from pypillowfight import sobel


class TestSobel(unittest.TestCase):
    def test_sobel(self):
        with tempfile.NamedTemporaryFile(suffix='.jpg') as tmpfile:
            in_img = PIL.Image.open("tests/data/crappy_background.jpg")
            out_img = sobel.sobel(in_img)
            in_img.close()

            # beware of JPG compression
            out_img.save(tmpfile.name)
            out_img.close()
            out_img = PIL.Image.open(tmpfile.name)

        expected_img = PIL.Image.open(
            "tests/data/crappy_background_sobel.jpg"
        )
        self.assertEqual(out_img.tobytes(), expected_img.tobytes())
        expected_img.close()
