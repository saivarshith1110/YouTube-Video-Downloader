import yt_dlp 
import os

def download_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Download completed!")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_location = input("Enter folder path (or press Enter for current location): ")
    if not download_location:
        download_location = os.getcwd()

    download_video(video_url, download_location)
