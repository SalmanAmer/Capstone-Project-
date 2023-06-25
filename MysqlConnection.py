
import sqlite3
import smtplib
import ssl
from email.message import EmailMessage
import sql
import cv2
import numpy as np
from io import BytesIO
import base64
from kivy.uix.image import Image



conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def get_Theme():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Theme FROM Themes")
    result = cursor.fetchall()
    print(result)
    return result[0][0]








# def get_Theme():
#     sqlstmt = f"""SELECT Theme FROM CapstoneDB.Themes"""
#     cursor = conn.cursor()
#     cursor.execute(sqlstmt)
#     list = cursor.fetchall()
#     return list[0][0]


# print(get_Theme())


# def set_Theme(flag):
#     value = 1 if flag else 0
#     opposite_value = int(not value)
#     print(f"{value},{opposite_value}")
#     sqlstmt = """UPDATE CapstoneDB.Themes SET Theme = %s WHERE Theme = %s"""
#     cursor = conn.cursor()
#     cursor.execute(sqlstmt, (value, opposite_value))
#     conn.commit()



def set_Theme(flag):
    # Convert flag to 1 or 0
    value = 1 if flag else 0
    opposite_value = int(not value)

    # Execute the SQL statement
    sqlstmt = "UPDATE Themes SET Theme = ? WHERE Theme = ?"
    cursor.execute(sqlstmt, (value, opposite_value))
    conn.commit()


    # Close the connection





# set_Theme(True)
# print("theme has been set")
# print(get_Theme())


# def get_progress(userid):

#     sqlstmt = f"""SELECT idProgress,ProgressName FROM CapstoneDB.Progress WHERE UserId ='{userid}'"""
#     cursor = conn.cursor()
#     cursor.execute(sqlstmt)
#     list = cursor.fetchall()
#     print(list)
#     return list





def get_progresses(userid,LW):
    if LW == "ALL"or LW=="Graph":
        sqlstmt = f"SELECT idProgress, ProgressName, Language, Level, LorW FROM Progress WHERE UserId = '{userid}'"
        cursor.execute(sqlstmt)
        result = cursor.fetchall()
    else:
        sqlstmt = f"SELECT idProgress, ProgressName, Language, Level, LorW FROM Progress WHERE UserId = '{userid}' AND LorW= '{LW}'"
        cursor.execute(sqlstmt)
        result = cursor.fetchall()


    # Close the connection


    return result




def get_progress_by_name(userid,progname):
    sqlstmt = f"SELECT idProgress, ProgressName, Language, Level, LorW FROM Progress WHERE UserId = '{userid}' AND ProgressName= '{progname}'"
    cursor.execute(sqlstmt)
    result = cursor.fetchall()
    return result[0]


#print(get_progress(1))


# def get_Actions_by_id(progressid):

#     sqlstmt = f"""SELECT Image,LW,Feedback,idActions FROM CapstoneDB.Actions WHERE idProgress ='{progressid}'"""
#     cursor = conn.cursor()
#     cursor.execute(sqlstmt)
#     list = cursor.fetchall()

#     return list


def get_Actions_by_id(progressid):

    # Execute the SQL statement
    sqlstmt = f"SELECT Image, LW, Feedback, idActions FROM Actions WHERE idProgress = '{progressid}'"
    cursor.execute(sqlstmt)
    result = cursor.fetchall()

    # Close the connection


    return result



# print(get_Actions_by_id(1))


# def create_account(username, password, mail):
#     cursor = conn.cursor()
#     check_query = "SELECT COUNT(*) FROM CapstoneDB.Users WHERE Username = %s"
#     cursor.execute(check_query, (username,))
#     result = cursor.fetchone()

#     if result[0] == 0:
#         sqlstmt = """INSERT INTO CapstoneDB.Users (Username, Password, Mail) VALUES (%s, %s, %s)"""
#         values = (username, password, mail)
#         cursor.execute(sqlstmt, values)
#         conn.commit()


def create_account(username, password, mail):
    # Check if the username already exists
    check_query = "SELECT COUNT(*) FROM Users WHERE Username = ?"
    cursor.execute(check_query, (username,))
    result = cursor.fetchone()

    if result[0] == 0:
        # Insert the new account details into the table
        sqlstmt = "INSERT INTO Users (Username, Password, Mail) VALUES (?, ?, ?)"
        values = (username, password, mail)
        cursor.execute(sqlstmt, values)
        conn.commit()
        return "ok"
    return "Username already exists"

    # Close the connection





# def create_progress(userid, name, lang, lvl):
#     cursor = conn.cursor()
#     check_query = "SELECT COUNT(*) FROM CapstoneDB.Progress WHERE (UserId, ProgressName) = (%s,%s)"
#     cursor.execute(check_query, (userid,name))
#     result = cursor.fetchone()

#     if result[0] == 0:
#         sqlstmt = """INSERT INTO CapstoneDB.Progress (UserId, ProgressName, Language, Level) VALUES (%s, %s, %s, %s)"""
#         values = (userid, name, lang, lvl)
#         cursor.execute(sqlstmt, values)
#         conn.commit()



def create_progress(userid, name, lang, lvl,LorW):
   

    # Check if the progress already exists for the given userid and name
    check_query = "SELECT COUNT(*) FROM Progress WHERE UserId = ? AND ProgressName = ?"
    cursor.execute(check_query, (userid, name))
    result = cursor.fetchone()

    if result[0] == 0:
        # Insert the new progress details into the table
        sqlstmt = "INSERT INTO Progress (UserId, ProgressName, Language, Level, LorW) VALUES (?, ?, ?, ?, ?)"
        values = (userid, name, lang, lvl, LorW)
        cursor.execute(sqlstmt, values)
        conn.commit()
    else:
        return "Progress with this name already exist"    

    # Close the connection











# def add_action_to_progress(progressid, LW, image, feedback):
#     sqlstmt = """INSERT INTO CapstoneDB.Actions (Image, LW, Feedback, idProgress) VALUES (%s,%s,%s,%s) """
#     values = (image, LW, feedback, progressid)
#     cursor = conn.cursor()
#     cursor.execute(sqlstmt, values)
#     conn.commit()




def add_action_to_progress(progressid, LW, image, feedback,progname):
    # Insert the new action details into the table
    sqlstmt = "INSERT INTO Actions (Image, LW, Feedback,ProgressName, idProgress) VALUES (?, ?, ?, ?, ?)"
    values = (image, LW, feedback,progname, progressid)
    cursor.execute(sqlstmt, values)
    conn.commit()
    

def Counter_INC(progressid):
    sqlstmt = f"""UPDATE Progress
                SET Counter = Counter + 1
                WHERE idProgress = {progressid}"""
    cursor.execute(sqlstmt)
    conn.commit()    


def create_quiz(progressid,level,Group):
    sqlstmt = "INSERT INTO Quiz (progressid, level, GroupNum) VALUES (?, ?, ?)"
    values = (progressid,level,Group)
    cursor.execute(sqlstmt, values)
    conn.commit()
    last_row_id = cursor.lastrowid
    return last_row_id

  
def save_quiz_grade(quizid,Grade):
    sqlstmt = f"""UPDATE Quiz
                SET Grade = ? , Date = CURRENT_DATE
                WHERE quizid = {quizid}"""
    cursor.execute(sqlstmt,[Grade])
    conn.commit() 
    




def add_action_to_quiz(progressid, quizid, LW, image, feedback):
    # Insert the new action details into the table
    sqlstmt = "INSERT INTO ActionInQuiz (quizid,progressid,Image, LW, Feedback) VALUES (?, ?, ?, ?, ?)"
    values = (quizid,progressid,image, LW, feedback)
    cursor.execute(sqlstmt, values)
    conn.commit()


def get_progress_quizes(progressid):
    sqlstmt = f"SELECT * FROM Quiz WHERE progressid = '{progressid}'"
    cursor.execute(sqlstmt)
    result = cursor.fetchall()
    return result

def get_Quiz_Actions(progressid):
    sqlstmt = f"SELECT idAction,quizid,progressid,LW,FeedBack FROM ActionInQuiz WHERE progressid = '{progressid}'"
    cursor.execute(sqlstmt)
    result = cursor.fetchall()
    return result

def get_Quiz_Actions_imgs(progressid):
    conn.text_factory=bytes
    sqlstmt = f"SELECT Image FROM ActionInQuiz WHERE progressid = '{progressid}'"
    cursor.execute(sqlstmt)
    result = cursor.fetchall()
    conn.text_factory=str

    return result


def get_progress_quiz_dates(progressid):
    sqlstmt = f"SELECT Grade, Date FROM Quiz WHERE progressid = '{progressid}'"
    cursor.execute(sqlstmt)
    result = cursor.fetchall()
    return result


    # Close the connection

def get_counter(progressid):
    sqlstmt = f"SELECT Counter FROM Progress WHERE idProgress = '{progressid}'"
    cursor.execute(sqlstmt)
    result = cursor.fetchall()
    print(result)
    return int(result[0][0])







def read_blob_and_convert_to_image():
    conn.text_factory=bytes
    # Read the blob from the database
    cursor.execute(f"SELECT Image FROM image")
    blob = cursor.fetchone()[0]

    # Convert the blob to a numpy array
    np_array = np.frombuffer(blob, np.uint8)

    # Decode the numpy array to an image using cv2
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # Save the image to a file
    conn.text_factory=str
    return image
    # Close the database connection

def read_blob_and_convert_to_graph():
    conn.text_factory=bytes
    # Read the blob from the database
    cursor.execute(f"SELECT Graph FROM image")
    blob = cursor.fetchone()[0]

    # Convert the blob to a numpy array

    # Convert the Blob data to a BytesIO object
    blob = BytesIO(blob)

    # Create a base64 encoded string from the BytesIO data
    base64_data = base64.b64encode(blob.getvalue()).decode()

    # Create a Kivy Image widget and set the source to the base64 data
    graph = Image(source='data:image/png;base64,' + base64_data)

    # Save the image to a file
    conn.text_factory=str
    return graph
    # Close the database connection    






def read_all_letters():


    # Retrieve all the letters from the table
    cursor.execute(f"SELECT letter FROM Letters")
    rows = cursor.fetchall()

    # Initialize a list to store the letter images
    letters = []

    # Iterate through the rows and convert the blobs to images
    for row in rows:
        # Convert the blob to a numpy array
        np_array = np.frombuffer(row[0], np.uint8)

        # Decode the numpy array to an image using cv2
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        # Append the image to the list
        letters.append(image)

    # Close the database connection
    return letters



def delete_all_letters():


    # Delete all the letters from the table
    cursor.execute("DELETE FROM Letters")

    # Commit the transaction and close the database connection
    conn.commit()

def delete_incomplete_quizes(quizid):
    sqlstmt = f"DELETE FROM Quiz WHERE Grade = -1 AND quizid = '{quizid}'"

    cursor.execute(sqlstmt)
    conn.commit()
    sqlstmt = f"DELETE FROM ActionInQuiz WHERE quizid = '{quizid}'"
    cursor.execute(sqlstmt)
    conn.commit()


def Log_in_DB(username, password):

    sqlstmt = "SELECT * FROM Users WHERE Username = ? AND Password = ?"
    values = (username, password)
    cursor.execute(sqlstmt, values)
    result = cursor.fetchall()

    # Close the connection


    return result



def write_image_to_blob(image,column):
    # Read the image using cv2


    # Encode the image as a byte array
    _, encoded_image = cv2.imencode(".png", image)

    # Convert the byte array to a blob
    blob = encoded_image.tobytes()

    # Connect to the SQLite database


    # Insert the blob into the database
    cursor.execute(f"UPDATE Image SET {column} = ?", (blob,))


    # Commit the transaction and close the database connection
    conn.commit()


def insert_letter(image):
    # Read the image using cv2


    # Encode the image as a byte array
    _, encoded_image = cv2.imencode(".png", image)

    # Convert the byte array to a blob
    blob = encoded_image.tobytes()

    # Connect to the SQLite database


    # Insert the blob into the database
    cursor.execute(f"INSERT INTO Letters (letter) VALUES (?)", (blob,))


    # Commit the transaction and close the database connection
    conn.commit()

# print(Log_in_DB("salman", 'amer'))


def update_last_inserted_blob(image):
    # Read the image using cv2


    # Encode the image as a byte array
    _, encoded_image = cv2.imencode(".png", image)

    # Convert the byte array to a blob
    blob = encoded_image.tobytes()

    # Connect to the SQLite database


    # Get the last inserted row using the ROWID
    cursor.execute(f"SELECT MAX(ROWID) FROM Letters")
    rowid = cursor.fetchone()[0]

    if rowid is not None:
        # Update the blob in the last inserted row
        cursor.execute(f"UPDATE Letters SET letter = ? WHERE ROWID = ?", (blob, rowid))

        # Commit the transaction and close the database connection
        conn.commit()
        
    else:
        print("No rows found in the table.")




def forgot_Pass(username):
    sqlstmt = f"""SELECT * FROM Users WHERE Username=?"""
    values = (username)
    cursor.execute(sqlstmt, values)
    result = cursor.fetchall()
    print(list)
    email = list[0][3]
    password = list[0][2]
    name = list[0][1]

    # Create a text/plain message


# me == the sender's email address
# you == the recipient's email address
    email_sender = 'Salmana3335@gmail.com'
    email_password = 'uhbxmfuhviomtoec'
    email_receiver = email

    # Set the subject and body of the email
    subject = 'kivy password'
    body = f"""
Your Kivy Password is: {password}
    """
    try:
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    except Exception as e:
        print("An error occurred while sending the email:", str(e))




# Define email sender and receiver
