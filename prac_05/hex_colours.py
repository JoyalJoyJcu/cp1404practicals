COLOR_CODE = {"Absolute Zero": "#0048ba",
              "Acid Green": "#b0bf1a",
              "AliceBlue": "#f0f8ff",
              "Alizarin crimson": "#e32636",
              "Amaranth": "#e52b50",
              "Amber": "#ffbf00",
              "Amethyst": "#9966cc",
              "AntiqueWhite": "#faebd7",
              "AntiqueWhite1": "#ffefdb",
              "AntiqueWhite2": "#eedfcc"}
print(COLOR_CODE)

color_name = input("Enter a color name: ")
while color_name != "":
    if color_name in COLOR_CODE:
        print(color_name, "is", COLOR_CODE[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter a color name: ")
