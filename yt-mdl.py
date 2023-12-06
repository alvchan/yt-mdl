import os
import sys

formats = ["mp3", "mp4"]

print("yt-mdl -> the youtube mass downloader")

with open("config/userdata.txt", "a+"):
    print("userdata.txt loaded.")
with open("config/cookies.txt", "a+"):
    print("cookies.txt loaded.")
with open("config/urls.txt", "a+"):
    print("urls.txt loaded.")

with open("config/userdata.txt") as f:
    userdata = f.read().splitlines()

    if len(userdata) == 2:
        username = userdata[0]
        password = userdata[1]
    else:
        username = spoof
        password = idsoft

with open("config/urls.txt") as f:
    urls = f.read().splitlines()

ext = input("Format: ")
if ext in formats:
    match ext:
        case "mp3":
            ext = f"ba -x --audio-format {ext}"
        case "mp4":
            ext = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
else:
    quit()

path = sys.executable  # maybe don't leave this exposed
if os.name == "posix":
    path = path[:path.rfind("/")] + "/yt-dlp"
elif os.name == "nt":
    path = path[:path.rfind("\\")] + "\yt-dlp"  # \ may be error prone

for url in urls:
    os.system(f"python3 {path} -f {ext} --no-warnings -u {username} -p {password} --cookies config/cookies.txt {url} -o 'files/%(title)s.%(ext)s'")

for file in os.listdir("files"):
    if os.path.isfile(file):
        os.system(f"ffmpeg -i {file} -map_metadata -1 {file}")

print("Completed.")
