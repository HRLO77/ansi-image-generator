# ansi-image-generator

An ANSI image generator, to start it run:
`python generator.py`

Arguments are
`<path> [--resize int int] [--reduce int] [--pickle]`
`<path>` is a string, the path to the image file.
`--resize` is a tuple of integers, when passed, it resizes the image to the width and height passed.
`--reduce` reduces the quality of the image by the factor provided.
`--pickle` stores the ANSI string of the image in a pickle file in the current directory.

For example.

`$ /User/Images/rickroll.png --reduce 3 --pickle`
