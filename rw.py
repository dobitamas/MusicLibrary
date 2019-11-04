from class_music import music
album = []
music1 = []
def open_to_list(music1):
    try:
        data = open("Music.txt", "r")
        for line in data:
            music1.append(line.split(","))
        data.close()
        return(music1)
    except FileNotFoundError:
        print("File not found!")
    
def put_in_class(music1):
    for i in range(len(music1)):
        album.append(music(music1[i][0],music1[i][1],music1[i][2],music1[i][3],music1[i][4][:-1]))
    return(album)


def save_to_list(album,filename):
    writer = open(filename, "w")
    for sor in range(len(music1)):
        for elem in sor:
            writer.writelines(album[sor][elem])
    

open_to_list(music1)
put_in_class(music1)
save_to_list(album,"Music1.txt")