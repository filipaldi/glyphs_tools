# config.py
import os
import importlib.util

BATCH_LIMIT = 10
EXTRACTION_LIMIT = 52
FILE_NAME_DIGITS = 4
BATCH_LIMIT_HTML = 1

MAPPINGS_ORIG = "Mapping a"
MAPPINGS_NEW = "Name"
NAME_MAPPINGS_GLYPHS = "name_mappings_glyphs.csv"
NAME_MAPPINGS_MODELS = "name_mappings_models.csv"


DEFAULT_SCALE_X = 91
DEFAULT_SCALE_Y = 91
DEFAULT_MOVE_X = 0
DEFAULT_MOVE_Y = -15

# Default vertical metrics
DEFAULT_ASCENDER = 800
DEFAULT_CAPHEIGHT = 700
DEFAULT_XHEIGHT = 500
DEFAULT_DESCENDER = -200

# Default overshoots
ASCENDER_OVERSHOOT = 20
CAPHEIGHT_OVERSHOOT = 20
XHEIGHT_OVERSHOOT = 20
DESCENDER_OVERSHOOT = -20
BASELINE_OVERSHOOT = -20


def update_config(external_config):
    globals().update({k: v for k, v in external_config.items() if k in globals()})

def load_external_config(font_path):
    config_dir = os.path.dirname(font_path)
    external_config_path = os.path.join(config_dir, 'config.py')

    if os.path.exists(external_config_path):
        spec = importlib.util.spec_from_file_location("external_config", external_config_path)
        external_config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(external_config)
        update_config(external_config.__dict__)
