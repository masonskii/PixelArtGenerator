from django.shortcuts import render
from django.http import JsonResponse


def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # Здесь вы можете выполнить обработку изображения
        # Например, сохранить его на сервере или обработать его с помощью сторонней библиотеки
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def submit_rgb(request):
    if request.method == 'POST':
        red = request.POST.get('red', 0)
        green = request.POST.get('green', 0)
        blue = request.POST.get('blue', 0)

        print(red, green, blue)

        return JsonResponse({'success': True, 'message': f'RGB values submitted successfully.{red}, {green}, {blue}'})
    else:
        return JsonResponse({'success': False, 'error': 'Failed to submit RGB values.'})
def index(request):
    return render(request, 'index.html')
