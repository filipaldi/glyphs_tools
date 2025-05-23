"""
This script allows you to export a lot of font files without creating instances.
Use "CONFIGURATION" to set how many instances to export.
"""

from GlyphsApp import GSInstance, GSFont, PLAIN, WOFF, WOFF2
import time
import os


# ===== CONFIGURATION =====

"""
AXIS_RANGES:
Rename the axis tags and set their ranges according to the font.
Remove the axes that are not needed.

"""

AXIS_RANGES = {
    'wght': (0, 100),
    'wdth': (0, 100),
    'slnt': (0, 100),
    'ital': (0, 100),
    'opsz': (0, 100),
}

"""
NUM_STEPS:
Is a number of steps per axis to set the export.
For instance if set to 5, the export will be 5x5x5 = 125 files.
"""
NUM_STEPS = 5


"""
EXPORT_PATH:
Set the path where to export the files.
The directory will be created if it doesn't exist.
"""
EXPORT_PATH = os.path.expanduser("~/Desktop/lttrface-export-woff2")


"""
EXPORT_FORMATS:
Set the formats to export.
Valid options: "OTF", "TTF", "WOFF", "WOFF2"
You can set multiple formats for instance: ["WOFF2", "TTF"]
"""
EXPORT_FORMATS = ["WOFF2"]


"""
BATCH_SIZE, PAUSE_AFTER_INSTANCE, PAUSE_AFTER_BATCH:
This helps to avoid memory issues and to export the files faster.
"""
BATCH_SIZE = 6 # Number of instances to process in each batch
PAUSE_AFTER_INSTANCE = 0.5  # Seconds to pause after exporting each instance
PAUSE_AFTER_BATCH = 3  # Seconds to pause after each batch




def export_font_files(font, axis_ranges, num_steps, export_path, export_formats=["OTF"], 
                      batch_size=10, pause_after_instance=0.5, pause_after_batch=5):
    if not os.path.exists(export_path):
        os.makedirs(export_path)
        print(f"Created export directory: {export_path}")
    
    format_choice = export_formats[0]
    containers = []
    
    if format_choice in ["WOFF", "WOFF2"]:
        base_format = "OTF"  
        
        if format_choice == "WOFF":
            containers = [WOFF]
            print(f"Will generate WOFF format")
        else:  
            containers = [WOFF2]
            print(f"Will generate WOFF2 format")
    else:
        base_format = format_choice
        containers = [PLAIN]
        print(f"Will generate {base_format} format")
    
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
    
    batch_count = 0
    processed_count = 0
    
    for i in range(0, total_combinations, batch_size):
        batch = min(batch_size, total_combinations - i)
        print(f"Processing batch {batch_count + 1}: {batch} fonts")
        
        for b in range(batch):
            temp_instance = GSInstance()
            instance_name = []
            instance_position = i + b
            
            for axis_index, axis in enumerate(axes):
                axis_step_index = (instance_position // (num_steps ** axis_index)) % num_steps
                axis_value = steps[axis][axis_step_index]
                instance_name.append(f"{int(axis_value):03d}")
                temp_instance.setAxisValueValue_forId_(axis_value, font.axes[axis_index].axisId)
            
            instance_name_str = ' '.join(instance_name)
            temp_instance.name = instance_name_str
            
            print(f"Preparing to export font: {temp_instance.name}")
            
            temp_instance.font = font
            
            try:
                filename = f"{font.familyName}-{temp_instance.name.replace(' ', '')}"
                
                print(f"Exporting to: {export_path}/{filename}.{format_choice.lower()}")
                
                result = temp_instance.generate(
                    format=base_format, 
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

font = Glyphs.font
export_font_files(font, AXIS_RANGES, NUM_STEPS, EXPORT_PATH, EXPORT_FORMATS, 
                  BATCH_SIZE, PAUSE_AFTER_INSTANCE, PAUSE_AFTER_BATCH)