# Import the necessary custom modules for each step of the process
from svg_loader import SVGLoader
# from metric_calculator import MetricCalculator  # Uncomment if metric calculations are implemented
from glyphs_assembly import create_glyphs_from_svg_data

def main():
    # Step 1: Load SVG files and extract path data
    svg_loader = SVGLoader()
    svg_loader.load_svgs()  # Assumes that svg_loader prompts for the directory path
    svg_data = svg_loader.get_svg_data()
    
    # Step 2: Calculate metrics for each glyph (if metric_calculator.py is implemented)
    # This step would be necessary if metrics need to be dynamically calculated based on SVG paths
    # metric_calculator = MetricCalculator(svg_data)
    # glyph_metrics = metric_calculator.calculate_metrics()
    # For the purpose of this example, assume that metrics can be directly used or are manually set
    
    # Step 3: Assemble glyphs in the Glyphs font project
    create_glyphs_from_svg_data(svg_data)
    
    print("Glyphs assembly completed successfully.")

if __name__ == "__main__":
    main()
