#================================================================
#
#   File name   : join.py
#   Author      : Bostame Md Bayazid
#   Purpose      : For research module of masters course
#   Description : object detection image and video example
#
#================================================================
import os
from PIL import Image

def get_offsets(file):
	return [int(dimension[1:]) for dimension in file.split('.')[2:4]]

# Get the list of files
files = [file for file in sorted(os.listdir('.')) if file.startswith('Train.')]

if not files:
	print("No input files found")
else:
	print(str(len(files))+" input files found")
	lastFile = files[-1]
	outfile = lastFile[len('Train.'):].split('.')[0]+'_new.jpg'

	# The width and height of the original image can be determined from the last tile
	with Image.open(lastFile) as lastIm:
		w, h = lastIm.size
	x, y = get_offsets(lastFile)
	w += x
	h = 4000
	print("Combined image should be "+str(w)+" by "+str(h))
	
	# Create the new image
	im_out = Image.new(lastIm.mode, (w, h))
	for file in files:
		x, y = get_offsets(file)
		
		# Paste each tile
		with Image.open(file) as im:
			im_out.paste(im, (x, y))
	im_out.save(outfile)
	print("Image saved as "+outfile)
