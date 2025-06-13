import os, json

def main():

    position = os.getcwd()

    library_folder = input("Enter the path to your library folder: ")
    output_file = input("Enter the name of the output file (default: library.json): ")
    if output_file == "":
        output_file = "library.json"

    if output_file not in (file for file in os.listdir(os.getcwd()) if os.path.isfile(file)):

        os.chdir(library_folder)

        artists = []
        albums = []

        for artist in (folder for folder in os.listdir(os.getcwd()) if os.path.isdir(folder)):
            artists.append(artist)
            os.chdir(artist)
            albums.append([])
            for album in (folder for folder in os.listdir(os.getcwd()) if os.path.isdir(folder)):
                albums[-1].append(album)
            os.chdir("..")
        # print(albums)

        dict = {}
        for i in range(len(artists)):
            dict[artists[i]] = albums[i]
        print(dict)

        os.chdir(position)
        
        with open(output_file, mode="w", encoding="utf-8") as write_file:
            json.dump(dict, write_file, indent=4)
    else:
        print("Output file already exists. Please choose a different name.")


if __name__ == "__main__":
    main()

[]