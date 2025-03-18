# svg_import_batch_html.py
import os
import csv
from GlyphsApp import GSFont, GSAxis, GSFontMaster, Glyphs
from config import BATCH_LIMIT_HTML, NAME_MAPPINGS_MODELS
import math
import time
from svg_import_parser import parse_html_file_path

def load_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    html_files.sort()
    return html_files

def generate_master_name(model_name, epochs, results_no, font_id, html_name):
    if model_name and epochs and results_no and font_id:
        master_name = f"{model_name}-{epochs}-{results_no}-{font_id}"
    else:
        master_name = html_name or f"default-master-{int(time.time())}"
    return master_name

def create_new_master(master_name):
    new_master = GSFontMaster()
    new_master.name = master_name
    font = Glyphs.font
    font.masters.append(new_master)
    return new_master

def svg_import_batch_html_process(html_files_paths):
    batch_count = math.ceil(len(html_files_paths) / BATCH_LIMIT_HTML)
    for batch_index in range(batch_count):
        batch_start = batch_index * BATCH_LIMIT_HTML
        batch_end = batch_start + BATCH_LIMIT_HTML
        batch = html_files_paths[batch_start:batch_end]
        for html_file_path in batch:
            yield html_file_path

def load_name_mappings():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(script_dir, NAME_MAPPINGS_MODELS)

    name_mappings = {}
    try:
        with open(full_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                original_string = row["original string"].strip()
                integer_value = row["Integer"].strip()
                name_mappings[original_string] = int(integer_value)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise

    return name_mappings

def set_font_axes(font):
    required_axes = ['model', 'epochs', 'results', 'font']
    for axis_name in required_axes:
        if axis_name not in [axis.name for axis in font.axes]:
            new_axis = GSAxis()
            new_axis.name = axis_name
            new_axis.axisTag = axis_name[:4].ljust(4)
            font.axes.append(new_axis)

def set_axes_values_for_master(master, model_name, epochs, results_no, font_id, name_mappings):
    model_value = name_mappings.get(model_name, 0)
    epochs_value = int(epochs) if epochs else 0
    results_value = int(results_no) if results_no else 0
    font_id_value = int(font_id) if font_id else 0
    master.axes = [model_value, epochs_value, results_value, font_id_value]
