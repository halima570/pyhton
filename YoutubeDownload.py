from pytube import YouTube
def Download(link):
    youtubeObject=YouTube(link)
    youtubeObject.streams.filter(file_extension='mp4')
    youtubeObject =youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download("C:/Users/LENOVO/Desktop/python")
    except:
        print("error")
        print("download not complited")

link=input("entrez URL")
Download(link)
