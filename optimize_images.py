import os
from PIL import Image

def optimize_image(input_path, output_path, max_width):
    try:
        if not os.path.exists(input_path):
            print(f"Error: {input_path} does not exist.")
            return

        with Image.open(input_path) as img:
            width, height = img.size
            if width > max_width:
                new_height = int((max_width / width) * height)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                print(f"Resized {input_path} to {max_width}x{new_height}")
            
            img.save(output_path, optimize=True, quality=85)
            print(f"Saved optimized image to {output_path}")

    except Exception as e:
        print(f"Failed to optimize {input_path}: {e}")

# Paths
base_dir = r"c:\Users\monks\Documents\GitHub\hellomnks.github.io\img"
logo_in = os.path.join(base_dir, "logo", "logo oficial.png")
logo_out = os.path.join(base_dir, "logo", "logo_optimized.png")

submerso_in = os.path.join(base_dir, "submerso", "submerso cover.png")
submerso_out = os.path.join(base_dir, "submerso", "submerso_cover_optimized.png")

# Optimize
optimize_image(logo_in, logo_out, 300)
optimize_image(submerso_in, submerso_out, 800)
