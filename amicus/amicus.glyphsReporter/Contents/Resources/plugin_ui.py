import vanilla
from GlyphsApp import Glyphs

class AmicusPluginUI:
    def __init__(self):
        self.w = vanilla.FloatingWindow((400, 240), "Amicus Batch Importer")

        # Directory Selection
        self.w.text_description = vanilla.TextBox((15, 12, -10, 14), "Select the directory containing SVG files:", sizeStyle='small')
        self.w.directoryPath = vanilla.EditText((15, 30, 270, 22), placeholder="No directory selected", sizeStyle='small', readOnly=True)
        self.w.selectDirectoryButton = vanilla.Button((290, 30, 100, 20), "Select", callback=self.selectDirectory)

        # Progress and Status Feedback
        self.w.progressBar = vanilla.ProgressBar((15, 70, -15, 12))
        self.w.statusLabel = vanilla.TextBox((15, 90, -15, 14), "", sizeStyle='small')

        # Batch Import Customization (Optional UI elements for future implementation)
        # self.w.customOptionCheckBox = vanilla.CheckBox((15, 114, -15, 20), "Custom Option", callback=self.toggleCustomOption, value=True)

        # Import Button
        self.w.importButton = vanilla.Button((15, 200, -15, 20), "Start Batch Import", callback=self.startImport)
        self.w.setDefaultButton(self.w.importButton)

        self.w.open()

    def selectDirectory(self, sender):
        try:
            directoryPath = vanilla.dialogs.getFolder("Select a directory containing SVG files")
            if directoryPath:
                self.directoryPath = directoryPath
                self.w.directoryPath.set(self.directoryPath)
                self.updateStatus("Directory selected successfully.")
            else:
                self.directoryPath = None
                self.w.directoryPath.set("No directory selected")
                self.updateStatus("Directory selection cancelled.")
        except Exception as e:
            Glyphs.showMacroWindow()
            print("Error selecting directory: {}".format(e))
            self.updateStatus("Failed to select directory.")

    def startImport(self, sender):
        if not self.directoryPath:
            self.updateStatus("No directory selected. Please select a directory first.")
            return

        # Placeholder for validation and import logic
        self.updateStatus("Starting import...")
        # Implement the validation and import logic here
        # Update progress bar as necessary
        # self.w.progressBar.set(0.5) # Example progress update

        self.updateStatus("Import completed successfully.")

    def updateStatus(self, message):
        self.w.statusLabel.set(message)

    def performBatchImport(self, directoryPath):
        # Placeholder for batch import logic
        print(f"Importing SVGs from {directoryPath}")
        # Update UI based on import progress and results

if __name__ == "__main__":
    Glyphs.clearLog()  # Clears Macro window log
    pluginUI = AmicusPluginUI()