# svg_import.py
import sys
from GlyphsApp import Glyphs
from svg_import_single import svg_import_single
from svg_import_batch import svg_import_batch_load_directory, svg_import_batch_process
from svg_import_html import svg_import_load_html
from svg_import_batch_html import load_html_files, generate_master_name, create_new_master, svg_import_batch_html_process, set_font_axes, set_axes_values_for_master, load_name_mappings
from svg_import_parser import parse_name_mappings, parse_glyph_name, parse_layer_name, parse_html_file_path 
from svg_import_distributor import distribute_data, convert_svg_to_glyphs_layer
from config import NAME_MAPPINGS_MODELS

def log(message):
    sys.stdout.write(f"[svg_import] {message}\n")
    sys.stdout.flush()

def selective_import(file_path):
    svg_file_path = svg_import_single(file_path)
    if svg_file_path:
        glyph_name = parse_glyph_name(svg_file_path)
        layer_name = parse_layer_name(svg_file_path)
        distribute_data(svg_file_path, glyph_name, layer_name)

def batch_import(folder_path):
    svg_files_paths = svg_import_batch_load_directory(folder_path)
    for svg_file_path in svg_import_batch_process(svg_files_paths):
        glyph_name = parse_glyph_name(svg_file_path)
        layer_name = parse_layer_name(svg_file_path)
        distribute_data(svg_file_path, glyph_name, layer_name)

def html_import(html_file_path):
    temp_dir = svg_import_load_html(html_file_path)
    svg_files_paths = svg_import_batch_load_directory(temp_dir)
    for svg_file_path in svg_import_batch_process(svg_files_paths):
        glyph_name = parse_glyph_name(svg_file_path)
        layer_name = parse_layer_name(svg_file_path)
        distribute_data(svg_file_path, glyph_name, layer_name)

def batch_html_import(directory):
    font = Glyphs.font
    set_font_axes(font)
    name_mappings = load_name_mappings()
    html_files = load_html_files(directory)
    for html_file_path in svg_import_batch_html_process(html_files):
        model_name, epochs, results_no, font_id, html_name = parse_html_file_path(html_file_path)
        master_name = generate_master_name(model_name, epochs, results_no, font_id, html_name)
        new_master = create_new_master(master_name)
        set_axes_values_for_master(new_master, model_name, epochs, results_no, font_id, name_mappings)
        temp_dir = svg_import_load_html(html_file_path)
        svg_files_paths = svg_import_batch_load_directory(temp_dir)
        for svg_file_path in svg_import_batch_process(svg_files_paths):
            glyph_name = parse_glyph_name(svg_file_path)
            layer_name = new_master.name
            distribute_data(svg_file_path, glyph_name, layer_name, master_name=new_master.name)
