from PIL import Image, ImageOps, ImageDraw
import os

def load_flags(flag_names, flag_folder='flags'):
    flags = []
    for flag_name in flag_names:
        flag_path = os.path.join(flag_folder, f'{flag_name}.png')
        if os.path.exists(flag_path):
            flag_image = Image.open(flag_path).convert("RGBA")
            flags.append(flag_image)
        else:
            print(f"Flag '{flag_name}' not found.")
    return flags

def create_overlay_image(base_image_path, flag_names, scale_percentage, output_path='output_image.png'):
    # можно изменить по желанию
    final_size = (640, 640)
    
    # загруз-очка
    base_image = Image.open(base_image_path).convert("RGBA")
    if base_image_path.lower().endswith('.png'):
        base_image = Image.open(base_image_path).convert("RGBA")
    elif base_image_path.lower().endswith('.jpg') or base_image_path.lower().endswith('.jpeg'):
        base_image = Image.open(base_image_path).convert("RGB").convert("RGBA")
    else:
        raise ValueError("Unsupported file format. Please use .png or .jpg files.")
    
    # новый размер основываясь на процентеееессс
    new_width = base_image.width * scale_percentage // 100
    new_height = base_image.height * scale_percentage // 100
    base_image = base_image.resize((new_width, new_height))
    
    # закгругление
    mask = Image.new("L", base_image.size, 0) # LLLLL
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + base_image.size, fill=255)
    rounded_base_image = ImageOps.fit(base_image, mask.size, centering=(0.5, 0.5))
    rounded_base_image.putalpha(mask)

    final_image = Image.new("RGBA", final_size, (255, 255, 255, 0))
    
    # флажки :3
    flags = load_flags(flag_names)
    
    if not flags:
        print("No valid flags selected.")
        return

    # конец флажков :(

    overlay = Image.new("RGBA", final_size, (255, 255, 255, 0))
    
    if len(flags) == 1:
        flag_resized = flags[0].resize(final_size)
        overlay = Image.alpha_composite(overlay, flag_resized)
    elif len(flags) == 2:
        flag1, flag2 = flags
        flag1_resized = flag1.resize((final_size[0] // 2, final_size[1]))
        flag2_resized = flag2.resize((final_size[0] // 2, final_size[1]))
        
        combined_flag = Image.new("RGBA", final_size)
        combined_flag.paste(flag1_resized, (0, 0))
        combined_flag.paste(flag2_resized, (final_size[0] // 2, 0))
        
        overlay = Image.alpha_composite(overlay, combined_flag)
    else:
        for flag in flags:
            flag_resized = flag.resize(final_size)
            overlay = Image.alpha_composite(overlay, flag_resized)

    x = (final_size[0] - rounded_base_image.width) // 2
    y = (final_size[1] - rounded_base_image.height) // 2
    final_image = Image.alpha_composite(overlay, final_image)
    final_image.paste(rounded_base_image, (x, y), rounded_base_image)

    # сохранение ^^
    final_image.save(output_path)
    print(f"Overlay image saved to {output_path}")

def main():
    base_image_path = 'image.png'
    flag_folder = 'flags'
    
    # вопрос 1
    num_flags = int(input("How many flags to overlay: "))

    # вопрос 2
    flag_names = []
    for i in range(num_flags):
        flag_name = input(f"Enter flag name {i + 1}: ")
        flag_names.append(flag_name)

    # вопрос 3
    scale_percentage = int(input("Enter the percentage to scale the avatar (90 is nice): "))

    # генерация -w-
    create_overlay_image(base_image_path, flag_names, scale_percentage)

main()
# made by zhevonez       ///////            in 100 lines!
