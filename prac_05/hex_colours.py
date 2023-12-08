COLORS = {"Absolutezero": "#0048ba", "Acidgreen": "#b0bf1a", "Aliceblue": "#f0f8ff", "Alizarincrimson": "#e32636",
          "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Antiquewhite": "#faebd7",
          "Apricot": "#fbceb1"}
print(COLORS)
while True:
    try:
        color_name = input("Type your color>>> ").title().replace(" ", "")
        if color_name == "":
            break
        color_code = COLORS[color_name]
        print(f"Color code for {color_name} is {color_code}")
    except KeyError:
        print("Invalid")
