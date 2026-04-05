from PIL import Image

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ""
    for char in chars:
        if char == '11111111':
            break
        message += chr(int(char, 2))
    return message

def decode_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary_data = ""
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)

    hidden_message = binary_to_text(binary_data)
    print("🔓 Hidden Message:", hidden_message)

# ---- RUN HERE ----
decode_image("stego.png")
