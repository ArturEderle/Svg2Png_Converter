#!/usr/bin/python3
from cairosvg import svg2png
import os
import re
import sys

def exists(path):
	return os.path.exists(path)

def convert(file, output):
	filename = os.fsencode(file)
	base_filename = os.path.basename(filename.decode("utf-8"))
	new_filename = re.sub('.svg', '.png', base_filename)

	# create output directory
	if not exists(output):
		os.makedirs(output)

	svg_file = ""
	with open(filename, "rb") as f:
		svg_file = f.read()			

	print("converting: "+filename.decode("utf-8")+" to "+output+"/"+new_filename)
	return svg2png(bytestring=svg_file, write_to=output+"/"+new_filename)

def main():

	# 1st argument SVG File or Directory with SVG Files
	# 2nd argument PNG output directory

	if len(sys.argv) > 2:
		svg = sys.argv[1]
		png_output = sys.argv[2]
	else:
		print("Not enough arguments given!")
		return -1

	if exists(svg):
		if os.path.isfile(svg):
			svg_file = svg
		if os.path.isdir(svg):
			svg_directory = os.fsencode(svg)
	
	if 'svg_directory' in locals():
		for file in os.listdir(svg_directory):
			convert(svg_directory+file, png_output)

	if 'svg_file' in locals():
		convert(svg_file, png_output)

if __name__ == "__main__":
	main()

