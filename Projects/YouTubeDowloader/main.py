import yt_dlp

url = input("Video URL'sini girin: ")

ydl_opts = {
    # 1. En iyi video ve en iyi sesi ayrı ayrı seç
    'format': 'bestvideo+bestaudio/best',
    
    # 2. İkisini MP4 kapsayıcısında birleştir
    'merge_output_format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s',
    
    # 3. İstemci olarak iOS veya Android VR dene (SABR / PO Token engellerini en iyi aşan istemciler)
    'extractor_args': {
        'youtube': {
            'player_client': ['ios', 'android']
        }
    }
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])