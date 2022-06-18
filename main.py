#pip isntall pytube
import pytube

link = input('Enter Youtube Video URL')
yt = pytube.Youtube(link)
yt.streams.first().download()
print('dowloaded', link)