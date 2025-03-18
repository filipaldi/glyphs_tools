# svg_import_single.py
import sys
import os

loaded_files = []
name_mappings_content = ""

def log(message):
    sys.stdout.write(f"[svg_import_single] {message}\n")
    sys.stdout.flush()

def svg_import_single(file_path):
    global loaded_files
    log(f"Attempting to load single SVG: {file_path}")
    if file_path.endswith(".svg"):
        loaded_files.append(file_path)
        log(f"Successfully loaded: {file_path}")
        return file_path
    else:
        log("Selected file is not an SVG.")
        return None

def load_name_mappings(folder_path):
    global name_mappings_content
    log(f"Loading name mappings from folder: {folder_path}")
    mappings_file_path = os.path.join(folder_path, "_name_mappings.txt")
    try:
        with open(mappings_file_path, 'r') as file:
            name_mappings_content = file.read()
    except FileNotFoundError:
        log(f"Name mappings file not found at {mappings_file_path}. Using default names.")
    except Exception as e:
        log(f"Error loading name mappings: {e}. Using default names.")

    log(f"Name mappings content: {name_mappings_content}")
    return name_mappings_content
