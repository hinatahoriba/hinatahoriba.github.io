import yt_dlp

def download_audio_as_mp3(video_url, save_path='music/'):
    ydl_opts = {
        'format': 'bestaudio/best',  # Select best audio quality
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Output file template
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'mp3',  # Convert to MP3 format
            'preferredquality': '0',  # Best quality
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Example usage:
video_url = "https://www.youtube.com/watch?v=TWg9QxEqzrc"
download_audio_as_mp3(video_url)