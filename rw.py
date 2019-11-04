
music = []
def open_to_list(filename,music):
    try:
        data = open("/home/mate/Asztal/python/music.library/{}".format(filename), "r")
        for line in data:
            music.append(line.split())
        return(music)
        data.close()
    except FileNotFoundError:
        print("File not found!")
    
open_to_list("text_albums_data.txt",music)
print(music)