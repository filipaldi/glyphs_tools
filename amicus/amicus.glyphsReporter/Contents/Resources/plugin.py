# encoding: utf-8

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class AmicusImporter(ReporterPlugin):

    @objc.python_method
    def settings(self):
        self.menuName = Glyphs.localize({'en': 'Amicus SVG Importer', 'de': 'Amicus SVG Importer'})
        self.keyboardShortcut = 'p'  # Example shortcut, change as needed
        self.keyboardShortcutModifier = NSControlKeyMask
        self.generalContextMenus = [
            {"name": Glyphs.localize({'en': "Layer info in Macro Window", 'de': "Layer-Info im Makro-Fenster"}), "action": self.printInfo},
        ]

    @objc.python_method
    def start(self):
        # Your initialization code goes here...
        pass

    @objc.python_method
    def foreground(self, layer):
        # Example: Draw a blue rectangle on top of the glyph's bounding box
        NSColor.blueColor().set()
        NSBezierPath.fillRect_(layer.bounds)

    @objc.python_method
    def background(self, layer):
        # Example: Draw a red rectangle behind the glyph's bounding box
        NSColor.redColor().set()
        NSBezierPath.fillRect_(layer.bounds)

    @objc.python_method
    def inactiveLayerForeground(self, layer):
        # Example: Drawing in inactive glyphs (the glyphs left and right of the active glyph)
        if layer.paths:
            NSColor.blueColor().set()
            layer.bezierPath.fill()

        if layer.components:
            NSColor.redColor().set()
            for component in layer.components:
                component.bezierPath.fill()

    @objc.python_method
    def conditionalContextMenus(self):
        contextMenus = []
        if Glyphs.font.selectedLayers:
            layer = Glyphs.font.selectedLayers[0]
            contextMenus.append({"name": Glyphs.localize({'en': 'Import SVG for Glyph', 'de': 'SVG für Glyph importieren'}), "action": self.importSVGForGlyph_})
        return contextMenus

    def importSVGForGlyph_(self, sender):
        print('Import SVG action triggered')
        # Implement the SVG import logic here

    def printInfo(self, sender=None):
        print("Layer info printed in Macro Window")
        # You can expand this method to print more useful information

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__