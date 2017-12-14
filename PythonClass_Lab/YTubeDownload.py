# Before starting this please install pytube -> pip3 install pytube==6.4.2

import pytube

print("Enter the Video Link")
link = input()

yt = pytube.YouTube(link)
videos = yt.get_videos()

s = 1
for v in videos:
	print(str(s)+". "+str(v))
	s += 1

print("Enter the number of the videos")
n = int(input())
vid = videos[n-1]

print("Enter the destination")
destination = input()
vid.download(destination)
print("Downloading your video......")

print(yt.filename+"\nDownloaded")

