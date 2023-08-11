import random
from PIL import Image

"""
def generate_pixel_art(width, height):
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pixels[x, y] = (r, g, b)

    return img


# Пример использования
pixel_art = generate_pixel_art(1000, 1000)
pixel_art.show()
pixel_art.save("pixel_art.png")
"""
"""

def average_color(pixels):
    r, g, b = zip(*pixels)
    avg_r = sum(r) // len(r)
    avg_g = sum(g) // len(g)
    avg_b = sum(b) // len(b)
    return (avg_r, avg_g, avg_b)


def downscale_image(image):
    width, height = image.size
    new_width = width // 2
    new_height = height // 2
    downscaled_image = Image.new("RGB", (new_width, new_height))

    for x in range(0, new_width, 2):
        for y in range(0, new_height, 2):
            pixels = [
                image.getpixel((x, y)),
                image.getpixel((x + 1, y)),
                image.getpixel((x, y + 1)),
                image.getpixel((x + 1, y + 1))
            ]
            new_pixel = average_color(pixels)
            downscaled_image.putpixel((x // 2, y // 2), new_pixel)

    return downscaled_image


# Load the original image
original_image = Image.open("1.jpg")

# Downscale the image
downscaled_image = downscale_image(original_image)

# Save the downscaled image
downscaled_image.save("downscaled_image.jpg")
"""
"""
# Загрузка изображения
image = Image.open('1.jpg')

# Определение размеров пиксель-арта
pixel_size = 10
width, height = image.size
new_width = width // pixel_size
new_height = height // pixel_size

# Масштабирование исходного изображения для создания пиксель-арта
resized_image = image.resize((new_width, new_height))

# Создание пустого холста для пиксель-арта
pixel_art = Image.new('RGB', (width, height))

# Заполнение пиксель-арта с использованием цветов из масштабированного изображения
for x in range(new_width):
    for y in range(new_height):
        rgb_values = resized_image.getpixel((x, y))
        pixel_art.paste(rgb_values, (x * pixel_size, y * pixel_size,
                        (x + 1) * pixel_size, (y + 1) * pixel_size))

# Сохранение полученного пиксель-арта
pixel_art.save('pixel_art.jpg')
"""

main_image = Image.open('2.jpg')
# Масштабирование пиксель-арта до нужных размеров
width, height = main_image.size


def generate_pixel_art(width, height):
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r = random.randint(100, 124)
            g = random.randint(20, 120)
            b = random.randint(80, 111)
            pixels[x, y] = (r, g, b)
    return img


# Пример использования
pixel_art = generate_pixel_art(width, height)
pixel_art.save("pixel_art.png")
# Загрузка основного фото и пиксель-арта
pixel_art = Image.open('pixel_art.png')


pixel_art = pixel_art.resize((width, height))

# Создание прозрачной версии пиксель-арта
pixel_art_with_alpha = pixel_art.copy()
# Изменение значения прозрачности (0 - полностью прозрачно, 255 - полностью непрозрачно)
pixel_art_with_alpha.putalpha(115)  # 70

# Наложение пиксель-арта на основное фото
result = Image.alpha_composite(
    main_image.convert('RGBA'), pixel_art_with_alpha)

# Сохранение результата
result.save('result_image.png')
