
font = Glyphs.font

if len(font.masters) > 0:
    del font.masters[0]
    print("First master removed successfully.")
else:
    print("No masters available to remove.")
