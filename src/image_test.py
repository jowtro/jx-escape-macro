from python_imagesearch.imagesearch import imagesearch

pos = imagesearch("./assets/rune_ore_chest.png")
if pos[0] != -1:
    print("position : ", pos[0], pos[1])
else:
    print("image not found")