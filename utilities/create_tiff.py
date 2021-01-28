import tifffile as tiff
import numpy

data = numpy.random.randint(0, 255, (100, 100, 3), 'uint32')
tiff.imwrite('temp.tif', data, bigtiff=True, photometric='rgb')