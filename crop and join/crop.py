import PIL
from PIL import Image

infile = 'DSC04124.JPG'
chopsize = 512
img = Image.open(infile)
width, height = img.size

for x0 in range(0, width, chopsize):
    for y0 in range(0, height, chopsize):
        box = (x0, y0,x0+chopsize if x0+chopsize <  width else  width - 1, y0+chopsize if y0+chopsize < height else height - 1)
        print('%s %s' % (infile, box))
        img.crop(box).save('Train.%s.x%03d.y%03d.JPG' % (infile.replace('.JPG',''), x0, y0))