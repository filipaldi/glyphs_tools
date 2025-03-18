# svg_import_parser.py
import os

def parse_glyph_name(svg_file_path):
    file_name = os.path.basename(svg_file_path)
    parts = file_name.split('_')
    if len(parts) >= 3 and parts[1].isdigit() and parts[2].isdigit():
        glyph_name = '_'.join(parts[:2])
        return glyph_name
    else:
        return os.path.splitext(file_name)[0]

def parse_layer_name(svg_file_path):
    file_name = os.path.basename(svg_file_path)
    parts = file_name.split('_')
    if len(parts) >= 3 and parts[1].isdigit() and parts[2].isdigit():
        layer_name = parts[2]
        return layer_name
    else:
        return os.path.splitext(file_name)[0]

def parse_name_mappings(raw_content):
    name_mappings = {}
    lines = raw_content.strip().split('\n')
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 2:
            key, value = parts[0].strip(), parts[1].strip()
            name_mappings[key] = value
        else:
            sys.stdout.write(f"Skipping invalid line in name mappings: {line}\n")
            sys.stdout.flush()
    sys.stdout.write(f"[svg_import_parser] Parsed name mappings: {name_mappings}\n")
    sys.stdout.flush()
    return name_mappings

# Move the parse_html_file_path function here
def parse_html_file_path(html_file_path):
    path_parts = html_file_path.split('/')
    start_index = None

    for i, part in enumerate(path_parts):
        if 'model_' in part or 'epochos_' in part or 'results_' in part:
            start_index = i
            break

    if start_index is not None:
        relevant_path = path_parts[start_index:]
        model_part = relevant_path[0]
        model_name_part = model_part.split('-')

        model_name = None
        epochs = None
        results_no = None
        
        for part in model_name_part:
            if part.startswith('model_'):
                model_name = part.replace('model_', '')
            elif part.startswith('epochos_'):
                epochs = part.replace('epochos_', '')
            elif part.startswith('results_'):
                results_no = part.replace('results_', '')

        font_id = next((part for part in relevant_path[1:] if part.isdigit()), None)
    else:
        model_name = epochs = results_no = font_id = None

    html_name = os.path.basename(html_file_path).replace('.html', '')

    return model_name, epochs, results_no, font_id, html_name
