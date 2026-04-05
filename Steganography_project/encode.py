from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encode_image(image_path, secret_text, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    binary_text = text_to_binary(secret_text) + '1111111111111110'
    data_index = 0

    width, height = img.size

    for y in range(height):
        for x in range(width):
            if data_index < len(binary_text):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_text[data_index])
                pixels[x, y] = (r, g, b)
                data_index += 1

    img.save(output_path)
    print("✅ Message hidden successfully!")

# ---- RUN HERE ----
encode_image("input.png", "THIS IS FISA, close the container and leave its conents. unless you want to mess with the federal investigation " "stego.png")
