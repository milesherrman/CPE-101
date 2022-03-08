# Lab 8
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

#Purpose: Given an encoded ppm file, decode it in a new file
def decode_image(orginal_image: str, decoded_image: str) -> None:

    image = open(orginal_image, "r")
    new_image = open(decoded_image, "w")

    new_image.write(image.readline())
    new_image.write(image.readline())
    new_image.write(image.readline())
    
    while True:
        r = image.readline()
        if r == "":
            break
        image.readline()
        image.readline()
        r_new = int(r)*10
        if r_new > 255:
            r_new = 255
        new_image.write(str(r_new) + '\n')
        new_image.write(str(r_new) + '\n')
        new_image.write(str(r_new)  + '\n')

    image.close()
    new_image.close()

#Purpose: pass files to decode image function
def main() -> None:
    decode_image("hidden.ppm", "discovered.ppm")

if __name__ == '__main__':
   main()