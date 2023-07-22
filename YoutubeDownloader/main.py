import pytube


url = input("Enter Video URL: ")

path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path)