# InstaGen Script for Glyphs 3+
from GlyphsApp import GSInstance, GSAxis, GSFont

def generate_instances(font, axis_ranges, num_steps, batch_size):
    axes = list(axis_ranges.keys())
    steps = {axis: [(axis_ranges[axis][1] - axis_ranges[axis][0]) / (num_steps - 1) * step + axis_ranges[axis][0] for step in range(num_steps)] for axis in axes}
    
    total_combinations = 1
    for axis in axes:
        total_combinations *= num_steps
    
    print("Total combinations to generate:", total_combinations)
    
    batch_count = 0
    for i in range(0, total_combinations, batch_size):
        batch = min(batch_size, total_combinations - i)
        print(f"Processing batch {batch_count + 1}: {batch} instances")
        
        for b in range(batch):
            instance = GSInstance()
            instance_name = []
            instance_position = i + b
            for axis_index, axis in enumerate(axes):
                axis_step_index = (instance_position // (num_steps ** axis_index)) % num_steps
                axis_value = steps[axis][axis_step_index]
                instance_name.append(f"{axis}{int(axis_value):03d}")
                instance.setAxisValueValue_forId_(axis_value, font.axes[axis_index].axisId)
            
            instance.name = ''.join(instance_name)
            font.instances.append(instance)
        
        batch_count += 1
        if batch_count % batch_size == 0 or i + batch == total_combinations:
            print(f"Batch {batch_count}/{(total_combinations // batch_size) + (1 if total_combinations % batch_size else 0)} completed.")
            font.save() # Save the `.glyphs` file after processing each batch
    
    print("Instance generation completed.")

# Script parameters
axis_ranges = {
    'shap': (-100, 100),
    'tilt': (0, 100),
    'wght': (0, 150),
}
num_steps = 10  # Define the number of steps per axis
batch_size = 5  # Define the number of instances to process in each batch

# Get the current font
font = Glyphs.font

# Call the function to generate instances
generate_instances(font, axis_ranges, num_steps, batch_size)
