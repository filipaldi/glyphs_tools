# post_clean_up.py
def clean_up_paths(font):
    for glyph in font.glyphs:
        for layer in glyph.layers:
            for path in layer.paths:
                layer.cleanUpPaths()
