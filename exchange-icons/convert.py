import os


def rename_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith((".png", ".jpeg", ".gif", ".bmp", ".tiff")):
            new_filename = (os.path.splitext(filename)[0]).upper() + ".jpg"
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, new_filename),
            )
            print(f"Renamed: {filename} to {new_filename}")


rename_images("./")
