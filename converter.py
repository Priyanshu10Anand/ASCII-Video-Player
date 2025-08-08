from PIL import Image
import os

ASCII_CHARS = "@%#*+=-:. "

def frame_to_ascii(image_path, width = 300):
    img = Image.open(image_path)

    # CROP black borders: adjust crop as needed
    w, h = img.size
    top_crop = int(h * 0.25)
    bottom_crop = int(h * 0.75)
    img = img.crop((0, top_crop, w, bottom_crop))

    # Resize and convert to grayscale
    new_h = int((bottom_crop - top_crop) / w / 1.65 * width)
    img = img.resize((width, new_h)).convert("L")

    # Convert to ASCII
    pixels = img.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels)
    return "\n".join(ascii_str[i:i+width] for i in range(0, len(ascii_str), width))

def convert_all_frames(input_folder = "frames", output_folder = "ascii_frames"):
    os.makedirs(output_folder, exist_ok = True)
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".png"):
            ascii_art = frame_to_ascii(os.path.join(input_folder, filename))
            with open(os.path.join(output_folder, filename.replace(".png", ".txt")), "w", encoding = "utf-8") as f:
                f.write(ascii_art)

if __name__ == "__main__":
    convert_all_frames()