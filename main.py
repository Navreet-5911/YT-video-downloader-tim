from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from urllib.parse import urlparse, parse_qs

def clean_youtube_url(url):
    parsed = urlparse(url)
    video_id = parse_qs(parsed.query).get("v")
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id[0]}"
    return url

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        highest_res_stream = yt.streams.get_highest_resolution()

        if highest_res_stream:
            print(f"Downloading: {yt.title}")
            highest_res_stream.download(output_path=save_path)
            print("Video downloaded successfully!")
        else:
            print("No downloadable stream found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    clean_url = clean_youtube_url(video_url)

    save_dir = open_file_dialog()

    if save_dir:
        print("Starting download...")
        download_video(clean_url, save_dir)
    else:
        print("Invalid save location.")