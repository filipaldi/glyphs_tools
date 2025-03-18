# svg_import_batch.py
import os
from config import BATCH_LIMIT
import math

def svg_import_batch_load_directory(folder_path):
    svg_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".svg"):
            full_path = os.path.join(folder_path, file_name)
            svg_files.append(full_path)
            # print(f"Loaded SVG file: {full_path}")
    svg_files.sort()
    if not svg_files:
        print(f"No SVG files found in {folder_path}.")
    return svg_files

def svg_import_batch_process(svg_files_paths):
    batch_count = math.ceil(len(svg_files_paths) / BATCH_LIMIT)
    for batch_index in range(batch_count):
        batch_start = batch_index * BATCH_LIMIT
        batch_end = batch_start + BATCH_LIMIT
        batch = svg_files_paths[batch_start:batch_end]
        # print(f"Processing batch {batch_index + 1}/{batch_count}")
        for svg_file_path in batch:
            # print(f"Processing SVG file: {svg_file_path}")
            yield svg_file_path
