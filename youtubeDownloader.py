import pytube
import sys

link = str(sys.argv[1])
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
