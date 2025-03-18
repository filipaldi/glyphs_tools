# svg_import_distributor.py
import GlyphsApp
from GlyphsApp import Glyphs, GSGlyph, GSLayer
from Foundation import NSURL, NSClassFromString

GSSVGtoPath = NSClassFromString("GSSVGtoPath")

def convert_svg_to_glyphs_layer(svg_file_path):
    layer = GSLayer()
    svg_to_path = GSSVGtoPath.alloc().init()
    url = NSURL.fileURLWithPath_(svg_file_path)

    bounds = None
    error = None
    
    success = svg_to_path.readFile_toLayer_bounds_error_(url, layer, bounds, error)
    if success:
        # print(f"SVG converted successfully for {svg_file_path}")
        return layer
    else:
        if error:
            print(f"Error during SVG conversion for {svg_file_path}: {error.localizedDescription()}")
        else:
            print(f"Error during SVG conversion for {svg_file_path}, but no error details were provided.")
        return None

def distribute_data(svg_file_path, glyph_name, layer_name, master_name=None):
    font = Glyphs.font
    
    glyph = font.glyphs[glyph_name]
    if not glyph:
        glyph = GSGlyph(glyph_name)
        glyph.name = glyph_name
        font.glyphs.append(glyph)
    
    new_layer = convert_svg_to_glyphs_layer(svg_file_path)

    if new_layer:
        if master_name:
            master = None
            for m in font.masters:
                if m.name == master_name:
                    master = m
                    break
            if master:
                masterLayer = glyph.layers[master.id]
                new_layer.associatedMasterId = master.id
            else:
                masterLayer = glyph.layers[0]
        else:
            masterLayer = glyph.layers[0]

        if not masterLayer.shapes:
            masterLayer.shapes.extend(new_layer.shapes)
            masterLayer.name = layer_name
        else:
            newLayer = GSLayer()
            newLayer.associatedMasterId = masterLayer.associatedMasterId
            newLayer.name = layer_name
            newLayer.shapes.extend(new_layer.shapes)
            glyph.layers.append(newLayer)
