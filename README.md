# Svg2Png Converter
This is a simple tool that I've written to convert svg files to png with python3. You can convert a single svg file or a whole folder with svg files.

## Prerequisites

* python3
* [cairosvg](https://cairosvg.org/)  
```sh
pip3 install cairosvg
```

## How to use

* Run it with two arguments
* Argument 1
	* SVG Filename or
	* Directory with **only** SVG Files
* Argument 2
	* Output Directory

### Examples

**Single File**  
```sh
./svg2png_converter.py svg_file.svg converted
```

**Directory with SVG Files**  
```sh
./svg2png_converter.py Desktop/svg_files/ converted
```


