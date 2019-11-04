from class_music import music
album = []
def open_to_list(filename,music1):
    try:
        data = open("/home/mate/Asztal/python/music.library/{}".format(filename), "r")
        for line in data:
            music1.append(line.split(","))
        return(music1)
        data.close()
    except FileNotFoundError:
        print("File not found!")
    
def put_in_class(music1):
    for i in range(len(music1)):
        album.append(music(music1[i][0],music1[i][1],music1[i][2],music1[i][3],music1[i][4][:-1])
    return(album)


