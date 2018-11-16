from PIL import Image
import numpy as np

class Image_manager(object):

    def load_image(self,infilename):
        img = Image.open(infilename)
        img.load()
        data = np.asarray(img, dtype="int32")
        return data


    def save_image(self,npdata, outfilename):
        img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"), "RGB")
        img.save(outfilename)