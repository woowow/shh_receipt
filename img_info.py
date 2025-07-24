from PIL import Image, ExifTags

def print_image_info(image_path):
    img = Image.open(image_path)

    print(f"📂 File: {image_path}")
    print(f"🧩 Format: {img.format}")
    print(f"📏 Size (width x height): {img.size}")
    print(f"🎨 Mode: {img.mode}")
    print(f"🔍 DPI: {img.info.get('dpi', 'Not available')}")


    # 픽셀 샘플 출력 (좌상단)
    print(f"\n🧪 Sample Pixel at (0,0): {img.getpixel((0, 0))}")

# 사용 예시

img_path = 'C:/Users/SSAFY/Desktop/shh_receipt/image/receipt_etc_2.jpg'
print_image_info(img_path)

img_path2 = 'C:/Users/SSAFY/Desktop/shh_receipt/image/receipt_cu.jpg'
print_image_info(img_path2)