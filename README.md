# KritaPy
Python utilities for working with Krita .kra files. In particular,
reading them, because Krita's command-line performance leaves
something to be desired.

At the moment, all this does is extract the merged image from the KRA file, but more
features may come eventually. Since ImageMagick doesn't support KRA yet,
this is probably the fastest way to get image data out of a KRA without opening Krita.

## Command line

Usage:
`python KritaPy.py MyKraFile.kra MyKraOutput.png`

Optional arguments:

`--mode` Specify a different [color mode](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes) for the output file. By default the merged image is RGBA, so you may need to specify a different mode if
your output format doesn't support that. JPG, for example, requires conversion to 'RGB'.

## As import
You can also import the KRA-reading function like so, if you need to be able to access 
the merged image from another script:
```
import KritaPy
image = KritaPy.extractMergedImageFromKRA('myfile.kra')
```
Returns a PIL Image object.





