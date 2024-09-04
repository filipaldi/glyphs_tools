#!/usr/bin/env python
# encoding: utf-8
"""
glyphs_exporter_script.py

"""

import os
from Glyphs import Glyphs, currentDocument, RunScript
from Foundation import NSURL


def exportAllInstances():
	'''
	This will export all instances of the font at 'path' as TrueType fonts.
	'''
	path = os.path.expanduser("~/Desktop/test/file.glyphs")
	doc = Glyphs.openDocumentWithContentsOfFile_display_(path, False)
	print("Exporting:", doc.displayName())
	font = doc.font()
	for instance in font.instances():
		print("Instance:", instance)
		instance.generate_({
			'ExportFormat': "TTF",
			'ExportContainer': "woff",
			'Destination': NSURL.fileURLWithPath_(os.path.expanduser("~/Desktop/test/"))
		})

	'''
	possible keys:
		ExportContainer: "woff", "woff2", "eot"
		Destination: NSURL
		autoHint: bool (default = true)
		removeOverlap: bool (default = true)
		useSubroutines: bool (default = true)
		useProductionNames: bool (default = true)
	'''

	doc.close()
	print("Ready!")


if __name__ == '__main__':
	# exportAllInstances()
	accessLayers()