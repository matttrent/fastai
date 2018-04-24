import pathlib
import fire

import numpy as np

import skimage
import skimage.io
import skimage.color

from skimage.filters import (threshold_otsu, threshold_local, threshold_sauvola)


class ImageThresholder(object):

    def __init__(self, window_size=None):
        self.indir = None
        self.outdir = None
        self.window_size = window_size

    def _read_image(self, fn):
        img = skimage.io.imread(fn)
        img = skimage.color.rgb2grey(img)
        return img

    def _save_image(self, fn, img):
        skimage.io.imsave(fn, img)

    def _process_image(self, img):
        binary_global = img > threshold_otsu(img)
        binary_global = binary_global.astype(np.float32)

        ws = self.window_size
        if not ws:
            ws = int(.5 * min(img.shape[:2]))
            if ws % 2 == 0: ws += 1

        thresh_local = threshold_local(img, block_size=ws)
        binary_local = img > thresh_local
        binary_local = binary_local.astype(np.float32)

        combo_image = (binary_global + binary_local) / 2.

        return binary_global, binary_local, combo_image

    def process(self, indir, outdir):
        self.indir = pathlib.Path(indir).expanduser()
        self.outdir = pathlib.Path(outdir).expanduser()

        bg_dir = self.outdir / 'global_thresh'
        bs_dir = self.outdir / 'sauvola_thresh'
        bc_dir = self.outdir / 'combo_thresh'

        bg_dir.mkdir(parents=True, exist_ok=True)
        bs_dir.mkdir(parents=True, exist_ok=True)
        bc_dir.mkdir(parents=True, exist_ok=True)

        for fn in self.indir.glob('*.jpg'):
            print(fn.name)
            img = self._read_image(fn)
            bg, bs, bc = self._process_image(img)

            self._save_image(bg_dir / fn.name, bg)
            self._save_image(bs_dir / fn.name, bs)
            self._save_image(bc_dir / fn.name, bc)


if __name__ == '__main__':
    fire.Fire(ImageThresholder)
