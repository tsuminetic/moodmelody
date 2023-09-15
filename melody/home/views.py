from django.shortcuts import render

def home(request):
    
    return render(request, 'home/home.html')

def genre_happy(request):
    audio_url = '/static/home/audio/happy.mp3'  # Replace with the actual path to your audio file
    return render(request, 'home/genre_details.html', {'genre_name': 'happy','audio_url': audio_url})

def genre_lofi(request):
    audio_url = '/static/home/audio/lofi.mp3'  # Replace with the actual path to your audio file
    return render(request, 'home/genre_details.html', {'genre_name': 'lofi','audio_url': audio_url})

def genre_romantic(request):
    audio_url = '/static/home/audio/romantic.mp3'  # Replace with the actual path to your audio file
    return render(request, 'home/genre_details.html', {'genre_name': 'romantic','audio_url': audio_url})