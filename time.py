# Python DataTime
import datetime
# tim = datetime.datetime.now()
# print(tim)
# print(tim.year)
# print(tim.strftime("%A"))
# tm = datetime.datetime(2021, 4, 10)
# print(tm)
# print(tm.month)
# tm = datetime.datetime(2021, 4, 10, 12, 30, 20,8)
# print(tm)
# strftime() method - use to format datetime object into readable string
# print(tm.strftime("%Z"))
# # strftime format codes
# %a : returns weekday in short version eg wed
# %A : returns weekday in full version eg wednesday
# %w : returns weekday in number version from 0-6 where 0 means sunday eg web is 3 
# %d : returns day of the month in number version from 01-31
# %b : returns month name in short version eg Dec
# %B : returns month name in full version eg December
# %m : returns month in number formart from 01-12 
# %y : returns year in short version eg 2021 is 21
# %Y : returns year in full version eg 2021
# %H : returns hour in 24hrs format from 00-23
# %I : returns hour in 12hrs format from 00-12
# %p : returns AM or PM of time
# %M : returns minute of time from 00-59
# %S : returns seconds of time from 00-59
# %f : returns microseconds of time form 000000-999999
# %Z : for timezone
# %j : days number of the year from 001-366
# %U : return week number of the year from 00-54 
import vlc
import time
# print(help(vlc.AudioSetVolumeCb))
# print(help(vlc.MediaPlayer))

# while True:
#     time.sleep(5)
#     tm = datetime.datetime.now()
#     if tm.strftime("%I") == "9" or tm.strftime("%M") == "56" or tm.strftime("%S") == "04" and tm.strftime("%p") == "AM":
        # if tm.strftime("%M") == "51":  
        # print("it's time for break")
        # break
        # p = vlc.MediaPlayer("01 Merciful God.mp3")
        # p.play()
        # time.sleep(170)
        # p.stop()
        # break
    # else:
    #     print("lecture continues") 
        # p = vlc.MediaPlayer("01 Merciful God.mp3")
        # p.play()
        # time.sleep(170)
        # p.stop()
        # break      
        
        

# import datetime
# check = int(datetime.datetime.now().strftime("%M")) 
# # print(check)
# rang =[]
# [rang.append(rn) for rn in range(0,60)]
# while True:
#     time =datetime.datetime.now() 
#     nexttime = time.strftime('%M')
#     # print(nexttime)
#     if int(nexttime) in rang and check == int(nexttime):   
#         for i in range(1):
#             print("i am going for class today")
#     check = int(nexttime )+ 1

# hour = hour[0]+str(int(hour[1]) + 2)
# print(hour)

# Python Math class
# import math
# print(help(math.ceil))
# l = [2, 4, 5, 7, 3]
# print(min(l))
# print(max(l))
# print(abs(-5.34))
# print(pow(3, 3))
# print(math.sqrt(9))
# print(math.ceil(8.3492))
# print(math.floor(5.6732))
# print(math.pi)
# print(math.pi * 1000 + 25)

# personal_info ={}
# for i in range(1,4):
#     name =input("Enter your name>")
#     level =input("Enter your level>")
#     email =input("Enter your email>")
#     person ={"name":name,"level":level,"email":email}
#     personal_info[name]=person
    
# print(personal_info)
# print("_________________________________")


    # if statement

# name = "paul"
# age = [12,13,14,15]
# if 12 not in age:
#     print(name)
# elif age == age:
#     if 12 not in age:
#         print("12 is not in age")
#     else:
#         print("welcom")
# else:
#     print("none of the above")



phone = input("Enter your percentage of your phone here>")
nepa = False
light = True
gen = "have petrol"

if phone <= "20" or phone <= "30":    
    if nepa == True:
        if light == False:
            print("i will off my phone") 
        elif light == True:
            print("i will change my phone")
        else:
            print("i will sleep")

    elif nepa != False:
        if gen == "have petrol":
            print("i will on Genetator and charge my phone") 
        elif gen != "have petrol":
            print("i will go and buy petrol and on the generator")
        else:
            print("i don't have money and i will go and watch man-u football")
    else:
        print("Nigeria is  a good country")

elif phone > "30" and phone <= "70":
    if nepa == False:
        if light != False:
            print("i will off my phone") 
        elif light == False:
            print("i will change my phone")
        else:
            print("i will sleep")

    elif nepa != False:
        if gen == "have petrol":
            print("i will on Genetator and charge my phone") 
        elif gen != "have petrol":
            print("i will go and buy petrol and on the generator")
        else:
            print("i don't have money and i will go and watch man-u football")
    else:
        print("Nigeria is not a good country")

else:
    print("I will buy new phone")


# name ="paul"
# age =[10,12,13,14]
# if 12 in age:
#     print(name)
# else:
#     print("paul is not in name")

# phone = "20"
# light =True
# if (light !=True )and (phone == "30"):
#     print("i will not charge my phone")
# elif (light == True) or (phone == "40"):
#     print("i will charge my phone")
# else:
#     print("i will off my phone")








