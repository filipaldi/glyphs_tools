# encoding: utf-8

###########################################################################################################
#
#   Glyphs SVG Importer
#   Advanced batch importing and distribution to glyphs
#   
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from user_interface import showLTTRSVGImporterWindow

class LTTRSVGImporter(GeneralPlugin):

    @objc.python_method
    def settings(self):
        self.name = Glyphs.localize({
            'en': 'SVG Importer',
            'de': 'SVG Importer',
            'fr': 'SVG Importer',
            'es': 'SVG Importer',
            'pt': 'SVG Importer',
        })

    @objc.python_method
    def start(self):
        newMenuItem = NSMenuItem(self.name, self.showWindow_)
        Glyphs.menu[EDIT_MENU].append(newMenuItem)

    def showWindow_(self, sender):
        showLTTRSVGImporterWindow()

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
