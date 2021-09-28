# file handling
# open('filename', mode='r', 'a', 'w', 'x', encoding='t', 'b')
# 'r' read only and it is the default for open function. raise error if file do not exist 
# 'a' append new content to an existing file. create new file with the specific file.
# 'w'  open file for writing . create new file with specific name if not exist.
# 'x'  to create new file. raise error if file already exist


# with open("main.py", mode='r') as myFile:
#   for i in myFile:
#     print(myFile.readline())

#   print(myFile.read(10))
# with open("C:\\USER\\Documents\\python code.txt", mode='rt') as myFile:
#   print(myFile.read())

# myFile = open("C:\\USER\\Documents\\python code.txt", 'rt') 
# myFile = open("C:\\Users\\ASUS\\Documents\\vuework.txt", mode='r')
# print(myFile.read())
# print(myFile.read(20))
# print(myFile.readline())

# for i in range(20):
#   print(myFile.readline())

# for i in myFile:
#   print(i)

# myFile = open("text.txt", 'a') 
# myFile.write("\n this is new content to append to the old file")

# myFile = open("C:\\USER\\Documents\\PYTHON\\code.txt", 'rt') 
# print(myFile.read())
# myFile.close()



# myFile = open("code.txt", 'w') 
# myFile.write("\n this is cnew content to append to the old file")

# with open("code2.txt", 'w') as newFile:
#   newFile.write("here i am writing to new file")


# open("C:\\Users\\ASUS\\Documents\\vuwwork4.txt", 'x') 
# myFile = open("C:\\Users\\ASUS\\Documents\\vuwwork4.txt", 'a') 
# myFile.write("\n lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum")
# myFile = open("C:\\Users\\ASUS\\Documents\\vuwwork4.txt", 'r') 
# print(myFile.read())



# with open("C:\\USER\\Documents\\python code.txt", mode='rt') as myFile:
#   print(myFile.read())


# import os
# os.remove('newfile.txt') #raise error if not exist
# if os.path.exists('newfile.txt'):
#   os.remove('newfile.txt')
#   print("file deleted successfully")
# else:
#   print('file not available')


# if os.path.exists('newfile.txt'):
#   with open("newfile.txt", mode='rt') as myFile:
#     print(myFile.read())
# else:
#   print("file does not exist")

# if os.path.exists("code.txt"):
#   os.remove("code.txt")
#   print("file deleted successfully")
# else:
#   print("file not available")



# os.rmdir("new folder")
# os.mkdir("new folder")
# os.mkdir("another folder")
# os.mkdir("Documents")




# with open("bankOOP.py", 'rt') as myFile:
#   print(myFile.read())



# with open("Documents", mode='rt') as inFile:
#   for files in inFile:
#     os.remove(files)

# deleting file and folder in a system
# for root, dirs, files in os.walk("new folder"):
#   for file in files:
#     os.remove("new folder\\"+file)
# os.rmdir("new folder")


# deleting file in folder
# for root, dirs, files in os.walk("another folder"):
#   for fil in files:
#     os.remove("another folder\\"+fil)
# os.rmdir("another folder")

# searching for  path of a file
# print(os.path.dirname(os.path.abspath("text.txt")))




# with open("Documents", mode='rt') as inFile:
#   for files in inFile:
#     os.remove(files)


# code to get username of any system(pc)
# import os.path
# homedir = os.path.expanduser("~")
# print(homedir)
# code to get system environment
# import os
# homedir = os.environ["PATH"]
# print(homedir)

# code to get the path of a file on your device
# print(os.path.dirname(os.path.abspath("damilare.py")))




# code to get username of any system(pc)
# import os.path
# homedir = os.path.expanduser("~")
# homedir = os.environ["PATH"]
# print(homedir)





# pip install playsound
# import os
# with open
# import playsound from playsound
# playsound("01 Merciful God.mp3")


# wavfile =input("Enter a wav filename: ")
# playsound(wavfile)

# mp3file =input('Enter a mp3 filename: ')
# playsound(mp3file)

# how to insert sound in python
# import winsound
# winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

# from playsound import playsound
# playsound('audio_file_place/file name')


# code to play all sound in the document directry
import os
import vlc
import time
mp3 =[]
mp4 =[]
# C:\Users\D\Pictures\Screenshots
mik = os.path.dirname("C:\\Users\\D\\Documents\\")
for root, dirs, files in os.walk(mik):    
      for file in files:
          if file.endswith(".mp3"):
              mp3.append(root+file)
          elif file.endswith(".mp4"):
               mp4.append(file) 
print(mp4)       
                # p = vlc.MediaPlayer(file)
                # p.play()
                # time.sleep(10)
                # p.stop()