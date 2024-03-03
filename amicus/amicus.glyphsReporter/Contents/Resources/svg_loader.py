import os
import xml.etree.ElementTree as ET

class SVGLoader:
    def __init__(self):
        self.svg_directory = ""
        self.svg_data = []

    def load_svgs(self):
        # Prompt for the directory path dynamically
        self.svg_directory = input("Please enter the path to the directory with SVG files: ")
        for filename in os.listdir(self.svg_directory):
            if filename.endswith("_refined.svg"):  # Only load refined SVG files
                svg_path = os.path.join(self.svg_directory, filename)
                self.parse_svg(svg_path, filename)

    def parse_svg(self, svg_path, filename):
        tree = ET.parse(svg_path)
        root = tree.getroot()
        paths = root.findall('.//{http://www.w3.org/2000/svg}path')
        path_data = [path.attrib['d'] for path in paths]
        
        # Extract the character index from the filename
        char_index = filename.split('_')[1]  # Assuming the naming convention holds
        
        self.svg_data.append({'file': svg_path, 'char_index': char_index, 'paths': path_data})

    def get_svg_data(self):
        return self.svg_data

# Example usage
if __name__ == "__main__":
    svg_loader = SVGLoader()
    svg_loader.load_svgs()
    svg_data = svg_loader.get_svg_data()
    print(svg_data)