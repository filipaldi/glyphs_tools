"""
Export font files in batches using a grid of values from axis ranges.
"""

from GlyphsApp import GSInstance, GSFont, PLAIN, WOFF, WOFF2
import time
import os

def export_font_files(font, axis_ranges, num_steps, export_path, export_formats=["OTF"], 
                      batch_size=10, pause_after_instance=0.5, pause_after_batch=5):
    """
    Export font files directly without creating instances in the Glyphs file.
    Uses the same grid logic as instance_manager.py to create temporary instances.
    """
    if not os.path.exists(export_path):
        os.makedirs(export_path)
        print(f"Created export directory: {export_path}")
    
    # Setup format configurations
    primary_format = "OTF"  
    containers = [PLAIN]
    
    web_formats = []
    for fmt in export_formats:
        if fmt in ["OTF", "TTF"]:
            primary_format = fmt
        elif fmt in ["WOFF", "WOFF2"]:
            web_formats.append(fmt)
    
    format_map = {"WOFF": WOFF, "WOFF2": WOFF2}
    for fmt in web_formats:
        if fmt in format_map:
            containers.append(format_map[fmt])
            print(f"Will generate {fmt} format")
    
    # Calculate all possible combinations
    axes = list(axis_ranges.keys())
    steps = {axis: [(axis_ranges[axis][1] - axis_ranges[axis][0]) / (num_steps - 1) * step + axis_ranges[axis][0] 
             for step in range(num_steps)] for axis in axes}
    
    total_combinations = 1
    for axis in axes:
        total_combinations *= num_steps
    
    print(f"Total fonts to generate: {total_combinations}")
    print(f"Formats to export: {', '.join(export_formats)}")
    print(f"Export directory: {export_path}")
    
    # Process in batches
    batch_count = 0
    processed_count = 0
    
    for i in range(0, total_combinations, batch_size):
        batch = min(batch_size, total_combinations - i)
        print(f"Processing batch {batch_count + 1}: {batch} fonts")
        
        for b in range(batch):
            # Create a temporary instance (won't be added to the font)
            temp_instance = GSInstance()
            instance_name = []
            instance_position = i + b
            
            # Configure instance axis values
            for axis_index, axis in enumerate(axes):
                axis_step_index = (instance_position // (num_steps ** axis_index)) % num_steps
                axis_value = steps[axis][axis_step_index]
                instance_name.append(f"{int(axis_value):03d}")
                temp_instance.setAxisValueValue_forId_(axis_value, font.axes[axis_index].axisId)
            
            # Set instance name
            instance_name_str = ' '.join(instance_name)
            temp_instance.name = instance_name_str
            
            # Prepare to export this instance
            print(f"Preparing to export font: {temp_instance.name}")
            
            # Set the temporary instance in the font
            temp_instance.font = font
            
            # Export the font file directly
            try:
                filename = f"{font.familyName}-{temp_instance.name.replace(' ', '')}"
                
                print(f"Exporting to: {export_path}/{filename}.{primary_format.lower()}")
                
                result = temp_instance.generate(
                    format=primary_format, 
                    fontPath=export_path, 
                    autoHint=True, 
                    removeOverlap=True,
                    useSubroutines=True,
                    useProductionNames=True,
                    containers=containers
                )
                
                if result is True:
                    processed_count += 1
                    print(f"✅ Successfully exported: {filename}")
                    print(f"   Formats: {', '.join(export_formats)}")
                else:
                    print(f"❌ Failed to export: {filename}")
                    if isinstance(result, list):
                        for error in result:
                            print(f"  Error: {error}")
            except Exception as e:
                print(f"❌ Error exporting {temp_instance.name}: {str(e)}")
            
            time.sleep(pause_after_instance)
        
        batch_count += 1
        print(f"Batch {batch_count} completed. Waiting for Glyphs to process...")
        print(f"{processed_count}/{i+batch} fonts processed so far.")
        time.sleep(pause_after_batch)
    
    print(f"Font generation completed. Successfully exported {processed_count} of {total_combinations} fonts.")
    print(f"Fonts are saved in: {export_path}")

# ===== CONFIGURATION =====
# Edit these settings as needed

# Axes to interpolate (axis_name: (min_value, max_value))
AXIS_RANGES = {
    '001': (0, 100),
    '002': (0, 100),
    'SWGT': (20, 100),
    'TCON': (0, 100),
    'TTIL': (30, 150),
}

# Number of steps per axis
NUM_STEPS = 9  # Small number for testing, increase as needed

# Export settings
EXPORT_PATH = os.path.expanduser("~/Desktop/lttrface-export-woff2")

# Font formats to export
# First OTF/TTF in the list will be used as the primary format
# Valid options: "OTF", "TTF", "WOFF", "WOFF2"
EXPORT_FORMATS = ["WOFF2"]

# Batch processing settings
BATCH_SIZE = 6  # Number of instances to process in each batch
PAUSE_AFTER_INSTANCE = 0.5  # Seconds to pause after exporting each instance
PAUSE_AFTER_BATCH = 5  # Seconds to pause after each batch

# ===== RUN SCRIPT =====
font = Glyphs.font
export_font_files(font, AXIS_RANGES, NUM_STEPS, EXPORT_PATH, EXPORT_FORMATS, 
                  BATCH_SIZE, PAUSE_AFTER_INSTANCE, PAUSE_AFTER_BATCH)