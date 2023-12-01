import os

formats = ["mp3", "mp4"]

print("yt-mdl -> the youtube mass downloader")

with open("config/userdata.txt", "a+"):
    print("userdata.txt loaded.")
with open("config/cookies.txt", "a+"):
    print("cookies.txt loaded.")
with open("config/urls.txt", "a+"):
    print("urls.txt loaded.")

with open("config/userdata.txt") as userdata_file:
    userdata = userdata_file.read().splitlines()

    if len(userdata) == 2:
        username = userdata[0]
        password = userdata[1]
    else:
        username = spoof
        password = idsoft

with open("config/urls.txt") as urls_file:
    urls = urls_file.read().splitlines()

ext = input("Format: ")
if ext in formats:
    match ext:
        case "mp3":
            ext = f"ba -x --audio-format {ext}"
        case "mp4":
            ext = f"bv*+ba/b -x --audio-format {ext}"
else:
    quit()

for url in urls:
    os.system(f"python3 yt-dlp -f {ext} --no-warnings -u {username} -p {password} --cookies config/cookies.txt {url} -o 'files/%(title)s.%(ext)s'")

for file in os.listdir("files"):
    if os.path.isfile(file):
        os.system(f"ffmpeg -i {file} -map_metadata -1 {file}")

print("Completed.")
