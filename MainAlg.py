import Alg1
import Alg2
import image_spliter
import random
import os
import cv2
import MysqlConnection
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
# import Demo
Levels={"Beginner":0,"Intermediate":40,"Advancd":60}

def Empty_Letters():
    for filename in os.listdir("Letters"):
        os.remove("Letters/"+filename)

def extract_sift_features(image,threshold):
    # Create SIFT object
    image = gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()

    # Detect keypoints and compute descriptors
    keypoints, descriptors = sift.detectAndCompute(image, None)

    num_keypoints = len(keypoints)
    return num_keypoints>=threshold



min_percentage=[4,3,4,7,4,2,4,4,2,3,4,3,3,2,3,3,6,6,6,4,3,3,3,3,5,3]
def correct_mistake(mistake):
    corrections = {
        'Slant': [
            "Please ensure the letters are properly aligned before shearing.",
            "Try adjusting the shearing angle for better letter preservation.",
            "Make sure the letters are evenly positioned before shearing."
        ],
        'Incomplete': [
            "Check if all the required letter fields have been filled.",
            "Make sure you haven't missed any steps in letter completion.",
            "Try completing the letter again from the beginning."
        ],
        'Incompatable': [
            "Ensure that the letter parts are compatible with each other.",
            "Check if the letter sizes and styles meet the requirements."
           
        ]
    }
    correction_list = corrections[mistake]
    correction = random.choice(correction_list)
    return correction


# Example usage

def Classify_Algorithm(image,word,level):
    image_spliter.Image_splite(image)
   
    letters=MysqlConnection.read_all_letters()
    num_letters=len(letters)
    response=[]
    if(len(word)!=num_letters):
        response.append("Please write the full word!")
        MysqlConnection.delete_all_letters()
        return response
    for i in range(len(letters)):

        if word[i].islower():
            ch='a'
            letter_from_image,per=Alg1.Read_Letter(letters[i])
            letter_from_image=letter_from_image.lower()
        else:
            ch='A'
            letter_from_image,per=Alg1.Read_Letter(letters[i])

        
        print(letter_from_image)
        print(word[i])
        
        if letter_from_image!=word[i]:
            if word[i]=='e'and (letter_from_image=='c'):
                response.append("try making the circle of the letter e bigger")
                break
            if (word[i]=='l')and letter_from_image=='l':
                response.append("Good job! No letter mistakes found.")     
                break
            if (word[i]=='m' or word[i]=='M')and (letter_from_image=='N' or letter_from_image=='n'):
                response.append("try adjusting the gap size of letter m it seems like you wrote n")
                break
            if (word[i]=='t')and letter_from_image=='l':
                response.append("try making the ascender stroke in letter t bigger")
                break
            if (word[i]=='G')and letter_from_image=='O':
                response.append("try making the gap of the letter G bigger")
                break  
            if (word[i]=='b' or word[i]=='d')and letter_from_image=='o':
                response.append("make the stick bigger")
                break
            if (word[i]=='D')and letter_from_image=='O':
                response.append("try making the letter less round")
                break
            if (word[i]=='V' or word[i]=='v')and (letter_from_image=='U' or letter_from_image=='u'):
                response.append("try making the letter more pointy")
                break
            if (word[i]=='K' or word[i]=='k')and (letter_from_image=='X' or letter_from_image=='x'):
                response.append("try preventing the lines of the K to not pass the vertical line so it does not look like X")
                break
            if (word[i]=='i')and letter_from_image=='l':
                response.append("Try to make the point further from the line")
                break
            if (word[i]=='q')and letter_from_image=='g':
                response.append("Try to make the stroke at the end of the letter q go more to the right") 
                break
            if (word[i]=='h')and letter_from_image=='n':
                response.append("make the stick bigger") 
                break
            if (word[i]=='R')and letter_from_image=='P':
                response.append("Try to make the stroke at the end of the letter R go more to the right") 
                break
            if (word[i]=='E')and (letter_from_image=='F' or letter_from_image=='T' ):
                response.append("Try to make the three strokes of the letter bigger") 
                break
            if (word[i]=='W' or word[i]=='w')and (letter_from_image=='V' or letter_from_image=='v'):
                response.append("try adjusting the gap size of letter W it seems like you wrote V")  
                break             
            if word[i]=='Q'and (letter_from_image=='A'or letter_from_image=='O'):
                if extract_sift_features(letters[i],min_percentage[ord(word[i])-ord(ch)]) and per>Levels[level]:
                    response.append("Good job! No letter mistakes found.")
                
                else:
                    response.append(correct_mistake(Alg2.Classify_Mistake(letters[i])))
            else:
                response.append("you wrote a wrong letter")

        else:
            if extract_sift_features(letters[i],min_percentage[ord(word[i])-ord(ch)]) and per>Levels[level]:
                response.append("Good job! No letter mistakes found.")
                
            else:
                 feedback=Alg2.Classify_Mistake(letters[i])
                 if feedback=='Slant' and (word[i]=='O'or word[i]=='o'):
                     response.append("Good job! No letter mistakes found.")
                 else:
                    response.append(correct_mistake(feedback))
        

    MysqlConnection.delete_all_letters()
           
    return response		 	

#print(correct_mistake(Alg2.Classify_Mistake("Letters/ROI_0.png")))


def Make_Charts(progressid,progressname):
    list=MysqlConnection.get_progress_quiz_dates(progressid)
    
    Grades = [item[0] for item in list]
    dates = [item[1] for item in list]

    Dates=[]
    
    for date in dates:
        Date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        Dates.append(Date)
    if not Dates:
        return False     
    Dates=sorted(Dates)
    indexes=range(1,len(Grades)+1)
# Convert the dates to matplotlib format
    matplotlib_dates = mdates.date2num(Dates)


    # Create a line plot with time on the x-axis
    plt.plot(indexes, Grades,linewidth=5)

    # Set the x-axis format as dates


    # Set labels and title
    plt.xlabel('Quiz Number')
    plt.ylabel('Score')
    plt.title(progressname)

    # Rotate x-axis labels for better readability


    # Display the plot
    #plt.tight_layout()

    plt.savefig("chart.jpg")
    MysqlConnection.write_image_to_blob(cv2.imread("chart.jpg"),"Graph")
    plt.close('all')
    return True
    #

    
#Make_Charts(17,"prog")

