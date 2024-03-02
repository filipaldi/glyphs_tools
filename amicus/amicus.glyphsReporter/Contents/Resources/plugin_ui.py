import vanilla

class AmicusPlugin(GSReporterPlugin):
    def settings(self):
        self.menuName = 'Amicus Batch Importer'

    def start(self):
        pass

    def __file__(self):
        """Please set this path to where your script is in your system."""
        return "/path/to/your/plugin/AmicusPlugin.py"

    def showBatchImportDialog(self):
        self.w = vanilla.FloatingWindow((400, 110), "Batch Import SVG", minSize=(400, 110), maxSize=(600, 110), autosaveName="com.yourname.AmicusPlugin.mainwindow")

        self.w.text_description = vanilla.TextBox((15, 12, -10, 14), "Select the directory containing SVG files:", sizeStyle='small')
        self.w.directoryPath = vanilla.EditText((15, 30, 270, 22), placeholder="No directory selected", sizeStyle='small', readOnly=True)
        self.w.selectDirectoryButton = vanilla.Button((290, 30, 100, 20), "Select Directory", sizeStyle='small', callback=self.selectDirectory)
        
        self.w.importButton = vanilla.Button((15, 70, -10, 20), "Start Batch Import", sizeStyle='small', callback=self.startImport)

        self.w.setDefaultButton(self.w.importButton)

        self.w.open()

    def selectDirectory(self, sender):
        directoryPath = vanilla.dialogs.getFolder("Select a directory containing SVG files")
        if directoryPath:
            self.directoryPath = directoryPath
            self.w.directoryPath.set(self.directoryPath)
        else:
            self.directoryPath = None
            self.w.directoryPath.set("No directory selected")

    def startImport(self, sender):
        if self.directoryPath:
            self.performBatchImport(self.directoryPath)
        else:
            vanilla.dialogs.message("Directory not selected", "Please select a directory containing SVG files before starting the import.")

    def performBatchImport(self, directoryPath):
        # Placeholder for import logic
        print(f"Importing SVGs from {directoryPath}")

# Don't forget to replace 'AmicusPlugin' with the actual name of your class
# To load your plugin in Glyphs, instantiate it and call the showBatchImportDialog method when appropriate
if __name__ == "__main__":
    Glyphs.clearLog() # Clears Macro window log
    plugin = AmicusPlugin()
    plugin.showBatchImportDialog()
