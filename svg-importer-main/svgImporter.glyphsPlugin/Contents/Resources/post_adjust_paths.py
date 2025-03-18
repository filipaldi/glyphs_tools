# post_adjust_paths.py

from GlyphsApp import Glyphs

last_transformations = {}

def adjust_paths(scaleX, scaleY, moveX, moveY):
    font = Glyphs.font

    for glyph in font.glyphs:
        for layer in glyph.layers:
            layer_id = (glyph.name, layer.layerId)

            current_transform = [
                [scaleX, 0, 0, scaleY, moveX, moveY]
            ]

            layer.applyTransform([
                scaleX, 0, 0,
                scaleY, 0, 0
            ])

            layer.applyTransform([
                1, 0, 0,
                1, moveX, moveY
            ])

            inverse_scale = [1/scaleX, 0, 0, 1/scaleY, 0, 0]
            inverse_move = [1, 0, 0, 1, -moveX, -moveY]
            last_transformations[layer_id] = (inverse_scale, inverse_move)

    font.save()

def revert_adjust_paths():
    font = Glyphs.font

    for glyph in font.glyphs:
        for layer in glyph.layers:
            layer_id = (glyph.name, layer.layerId)

            if layer_id in last_transformations:
                inverse_scale, inverse_move = last_transformations[layer_id]

                layer.applyTransform(inverse_move)
                layer.applyTransform(inverse_scale)

                del last_transformations[layer_id]

    font.save()
