class MetricCalculator:
    def __init__(self, svg_data):
        self.svg_data = svg_data  # This is a list of dictionaries with 'char_index' and 'paths'

    def calculate_metrics(self):
        glyph_metrics = []
        for glyph in self.svg_data:
            char_index = glyph['char_index']
            paths = glyph['paths']
            # Initialize min and max values for bounding box calculation
            min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')
            
            for path in paths:
                # Assuming a function here that extracts min and max x, y from a path's d attribute
                path_min_x, path_max_x, path_min_y, path_max_y = self.analyze_path(path)
                min_x, max_x = min(min_x, path_min_x), max(max_x, path_max_x)
                min_y, max_y = min(min_y, path_min_y), max(max_y, path_max_y)
            
            width, height = max_x - min_x, max_y - min_y
            glyph_metrics.append({
                'char_index': char_index,
                'width': width,
                'height': height,
                'bounding_box': {'min_x': min_x, 'max_x': max_x, 'min_y': min_y, 'max_y': max_y}
            })
        return glyph_metrics

    def analyze_path(self, path_d):
        # Placeholder for path analysis logic
        # You'd parse the path's d attribute and calculate min and max x, y values
        # This is a simplified example; actual implementation would need to parse SVG path commands
        return 0, 0, 0, 0  # Replace with actual calculation

# Example usage
if __name__ == "__main__":
    # Assume svg_data is loaded from svg_loader.py
    svg_data = [...]  # Placeholder for SVG data loaded from the SVGLoader
    metric_calculator = MetricCalculator(svg_data)
    glyph_metrics = metric_calculator.calculate_metrics()
    print(glyph_metrics)
