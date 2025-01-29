#!/usr/bin/env python
# encoding: utf-8

"""
glyphs_exporter_script.py


Example of use:
python "glyphs_exporter_script.py" "/path/to/source.glyphs" "/path/to/export/directory/"
"""

# /usr/local/bin/python3 
# /Users/flp/Desktop/git/glyphs-tools/exporter_script/glyphs_exporter_script.py 
# /Users/flp/Library/CloudStorage/OneDrive-Letterinks.r.o/_LTTR_CORP/01\ Fonts\ Development/01\ AI\ Fonts/_lttr_24_base.glyphs 
# /Users/flp/Desktop/lttr_testing_20_samples/lttr_24_base/_exports




import os
import time
from Foundation import NSURL, NSObject, NSConnection

# Establish connection to the Glyphs app using PyObjC
def application(appName="Glyphs", port=None):
    if port is None:
        port = "com.GeorgSeifert.Glyphs3"  # Default port for Glyphs 3
    conn = None
    tries = 0

    while ((conn is None) and (tries < 10)):
        conn = NSConnection.connectionWithRegisteredName_host_(port, None)
        tries += 1
        if not conn:
            time.sleep(1)

    if not conn:
        print(f"Could not find a JSTalk connection to {appName}")
        return None

    return conn.rootProxy()

# Connect to Glyphs
Glyphs = application()

def exportAllInstances():
	'''
	This will export all instances of the font at 'path' as TrueType fonts.
	'''
	path = os.path.expanduser("/Users/flp/Library/CloudStorage/OneDrive-Letterinks.r.o/_LTTR_CORP/01_Fonts_Development/01_AI_Fonts/_lttr_24_base.glyphs")
	doc = Glyphs.openDocumentWithContentsOfFile_display_(path, False)
	print("Exporting:", doc.displayName())
	font = doc.font()
	for instance in font.instances():
		print("Instance:", instance)
		instance.generate_({
			'ExportFormat': "woff2",
			'ExportContainer': "woff2",
			'Destination': NSURL.fileURLWithPath_(os.path.expanduser("/Users/flp/Desktop/lttr_testing_20_samples/lttr_24_base/_exports"))
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
	exportAllInstances()