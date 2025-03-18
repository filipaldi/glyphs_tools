# post_process.py
from GlyphsApp import Glyphs

def run_post_processing():
    font = Glyphs.font
    from post_close_open_paths import close_open_paths
    from post_clean_up import clean_up_paths
    from post_correct_paths_directions import correct_paths_directions
    
    # Step 1: Close open paths
    close_open_paths(font)
    
    # Step 2: Clean up paths
    clean_up_paths(font)
    
    # Step 3: Correct paths directions
    correct_paths_directions(font)
    
    # Save the file
    font.save()
