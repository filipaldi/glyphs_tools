# post_set_vertical_metrics.py

font = Glyphs.font

metrics = {
    "ascender": {"position": 800, "overshoot": 20},
    "capHeight": {"position": 700, "overshoot": 20},
    "xHeight": {"position": 500, "overshoot": 20},
    "descender": {"position": -200, "overshoot": -20},
    "baseline": {"position": 0, "overshoot": -20}
}

metric_types = {
    "ascender": GSMetricsTypeAscender,
    "capHeight": GSMetricsTypeCapHeight,
    "xHeight": GSMetricsTypexHeight,
    "descender": GSMetricsTypeDescender,
    "baseline": GSMetricsTypeBaseline
}

for master in font.masters:
    for key, values in metrics.items():
        metric_type = metric_types[key]
        position = values["position"]
        overshoot = values["overshoot"]
        
        master.setMetricPosition_overshoot_type_name_filter_(
            position,
            overshoot,
            metric_type,
            None,
            None
        )
