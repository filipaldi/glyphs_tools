# svg_import_html.py
import os
import sys
from config import EXTRACTION_LIMIT, FILE_NAME_DIGITS

def log(message):
    sys.stdout.write(f"[svg_import_html] {message}\n")
    sys.stdout.flush()

def svg_import_load_html(html_file_path):
    log(f"Loading HTML file: {html_file_path}")
    temp_dir = os.path.join(os.path.dirname(html_file_path), "extracted_svgs")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    svg_import_extract_svg_files(html_content, temp_dir)
    return temp_dir

def svg_import_extract_svg_files(html_content, temp_dir):
    svgs = extract_svgs_from_html(html_content)
    
    for i, svg in enumerate(svgs[:EXTRACTION_LIMIT]):
        svg_file_name = f"{i+1:0{FILE_NAME_DIGITS}}.svg"
        svg_file_path = os.path.join(temp_dir, svg_file_name)
        with open(svg_file_path, 'w', encoding='utf-8') as svg_file:
            svg_file.write(svg)

def extract_svgs_from_html(html_content):
    svgs = []
    pos = 0
    
    while pos < len(html_content):
        start_tag = html_content.find('<svg', pos)
        if start_tag == -1:
            break
        
        end_tag = html_content.find('</svg>', start_tag)
        if end_tag == -1:
            break
        
        end_tag += len('</svg>')
        
        svg_content = html_content[start_tag:end_tag]
        svgs.append(svg_content)
        
        pos = end_tag
    
    return svgs
