# user_interface.py
from GlyphsApp import Glyphs, GetOpenFile, GetFolder
from vanilla import Window, Button, TextBox, EditText
from config import DEFAULT_SCALE_X, DEFAULT_SCALE_Y, DEFAULT_MOVE_X, DEFAULT_MOVE_Y, load_external_config

class AmicusWindow:
    def __init__(self):
        self.w = Window((400, 490), "Amicus SVG Importer")

        self.w.text = TextBox((15, 12, -15, 17), "Choose import option:", sizeStyle='small')
        self.w.selectiveImportButton = Button((15, 40, 180, 20), "Selective Import", callback=self.selectiveImportCallback)
        self.w.batchImportButton = Button((15, 70, 180, 20), "Batch Import", callback=self.batchImportCallback)
        self.w.htmlImportButton = Button((15, 100, 180, 20), "HTML Import", callback=self.htmlImportCallback)
        self.w.batchHtmlImportButton = Button((15, 130, 180, 20), "Batch HTML Import", callback=self.batchHtmlImportCallback)

        self.w.postProcessText = TextBox((15, 160, -15, 17), "Choose post-process option:", sizeStyle='small')
        self.w.postProcessButton = Button((15, 180, 180, 20), "Post Process Paths", callback=self.postProcessCallback)
        self.w.renameGlyphsButton = Button((15, 210, 180, 20), "Rename Glyphs", callback=self.renameGlyphsCallback)

        self.w.scaleXText = TextBox((15, 240, -15, 17), "Scale X (%):", sizeStyle='small')
        self.w.scaleXInput = EditText((100, 240, 60, 20), str(DEFAULT_SCALE_X))

        self.w.scaleYText = TextBox((15, 270, -15, 17), "Scale Y (%):", sizeStyle='small')
        self.w.scaleYInput = EditText((100, 270, 60, 20), str(DEFAULT_SCALE_Y))

        self.w.moveXText = TextBox((15, 300, -15, 17), "Move X:", sizeStyle='small')
        self.w.moveXInput = EditText((100, 300, 60, 20), str(DEFAULT_MOVE_X))

        self.w.moveYText = TextBox((15, 330, -15, 17), "Move Y:", sizeStyle='small')
        self.w.moveYInput = EditText((100, 330, 60, 20), str(DEFAULT_MOVE_Y))

        self.w.adjustPathsButton = Button((15, 360, 180, 50), "Adjust Paths", callback=self.adjustPathsCallback)
        self.w.revertPathsButton = Button((15, 420, 180, 20), "Revert Paths", callback=self.revertPathsCallback)

        self.w.cancelButton = Button((15, 450, 180, 20), "Cancel", callback=self.closeWindow)
        self.w.open()

    def selectiveImportCallback(self, sender):
        load_external_config(Glyphs.font.filepath)
        filePath = GetOpenFile("Select an SVG file")
        if filePath:
            from svg_import import selective_import
            selective_import(filePath)

    def batchImportCallback(self, sender):
        load_external_config(Glyphs.font.filepath)
        folderPath = GetFolder("Select a folder containing SVG files")
        if folderPath:
            from svg_import import batch_import
            batch_import(folderPath)

    def htmlImportCallback(self, sender):
        load_external_config(Glyphs.font.filepath)
        filePath = GetOpenFile("Select an HTML file")
        if filePath:
            from svg_import import html_import
            html_import(filePath)

    def batchHtmlImportCallback(self, sender):
        load_external_config(Glyphs.font.filepath)
        directory = GetFolder("Select a directory containing HTML files")
        if directory:
            from svg_import import batch_html_import
            batch_html_import(directory)

    def postProcessCallback(self, sender):
        load_external_config(Glyphs.font.filepath)
        from post_process import run_post_processing
        run_post_processing()

    def renameGlyphsCallback(self, sender):
        load_external_config(Glyphs.font.filepath)
        from post_names_conversion import run_name_conversion
        run_name_conversion()

    def adjustPathsCallback(self, sender):
        load_external_config(Glyphs.font.filepath)
        scaleX = float(self.w.scaleXInput.get()) / 100.0
        scaleY = float(self.w.scaleYInput.get()) / 100.0
        moveX = float(self.w.moveXInput.get())
        moveY = float(self.w.moveYInput.get())
        from post_adjust_paths import adjust_paths
        adjust_paths(scaleX, scaleY, moveX, moveY)

    def revertPathsCallback(self, sender):
        load_external_config(Glyphs.font.filepath)
        from post_adjust_paths import revert_adjust_paths
        revert_adjust_paths()

    def closeWindow(self, sender):
        self.w.close()

def showLTTRSVGImporterWindow():
    AmicusWindow()
