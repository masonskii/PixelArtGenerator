import io
import json
import os
import re
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import numpy as np
import random
from PIL import Image
from django.http import FileResponse
def generate_pixel_art(width, height, rgb):
    img = Image.new("RGB", (width, height))
    pixels = img.load()
    for x in range(width):
        for y in range(height):
            r = int(rgb[0])
            g = int(rgb[1])
            b = int(rgb[2])
            pixels[x, y] = (r, g, b)
    return img

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        r = request.POST.get('r')
        g = request.POST.get('g')
        b = request.POST.get('b')
        color = [int(r), int(g), int(b)]
        image = request.FILES['image']
        main_image = Image.open(image)
        width, height = main_image.size
        pixel_art = generate_pixel_art(width, height,color)
        pixel_art.save("pixel_art.png")
        pixel_art = Image.open("pixel_art.png")
        pixel_art = pixel_art.resize((width, height))
        pixel_art_with_alpha = pixel_art.copy()
        # Изменение значения прозрачности (0 - полностью прозрачно, 255 - полностью непрозрачно)
        pixel_art_with_alpha.putalpha(123)  
        result = Image.alpha_composite(
        main_image.convert('RGBA'), pixel_art_with_alpha)
        result.save('result.png')

        # Конвертируем изображения в байты
        image_path ='C:\\Users\\user37\\Desktop\\VSCodeProject\\project2\\pixelArtDeveloping\\result.png'
        with open(image_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/png')
            response['Content-Disposition'] = 'inline; filename=result.png'
            return response
    return JsonResponse({'success': False})

def submit_rgb(request):
    if request.method == 'POST':
        color_data = request.POST.get('color')

        if color_data is not None:
            color = json.loads(color_data)

            red = color.get('r', 0)
            green = color.get('g', 0)
            blue = color.get('b', 0)

            # Process the RGB values as needed
            # Your logic here
            print
            return JsonResponse({'success': True, 'message': 'RGB values submitted successfully.'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid color data.'})

    return JsonResponse({'success': False, 'error': 'Failed to submit RGB values.'})
def index(request):
    return render(request, 'index.html')
