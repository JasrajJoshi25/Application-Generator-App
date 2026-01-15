# import area
from customtkinter import *
from tkinter import messagebox as msg
from tkcalendar import DateEntry
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch
import os
import random as rand
import sys


# def area

def write_application_to_file(application_text):
    filename = f"Application_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Times-Roman"
    style.fontSize = 12
    style.leading = 18  # line spacing

    text_width = width - 2 * inch
    x = inch
    y = height - inch

    for para in application_text.strip().split("\n\n"):
        p = Paragraph(para.replace("\n", "<br/>"), style)
        w, h = p.wrap(text_width, y)
        if y - h < inch:
            c.showPage()
            y = height - inch
        p.drawOn(c, x, y - h)
        y -= h + 12

    c.save()
    os.startfile(filename)

def generateSick():
    name= studentNameVar.get()
    college= collegeNameVar.get()
    classs= classVar.get()
    enrollment= enrollmentVar.get()
    reason= reasonVar.get()
    from_date_value = from_date.get()
    to_date_value = to_date.get()
    # Validation
    if not name or not college or not classs or not enrollment or not reason:
        msg.showerror("Input Error", "Please fill in all the fields.")
    elif from_date_value > to_date_value:
        msg.showerror("Input Error", "From Date cannot be later than To Date.")
    else:
        # Generate the sick leave application
        application_text = f"""
To
The Counsellor
{college}

Subject: Application for Sick Leave

Respected Sir,

I am writing to respectfully inform you that I am suffering from {reason}
and have been advised to rest by the doctor. Due to my current health condition, I am unable to
attend college and participate in academic activities for the mentioned period.

My illness has made it difficult for me to concentrate and perform my duties effectively.
Therefore, I kindly request you to grant me sick leave from {from_date_value} 
to {to_date_value} so that I may recover properly and return to college with full efficiency.
I assure you that I will cover all the missed lectures and academic work once I resume my classes.

I shall be very grateful to you for your kind consideration and support.

Thanking you.

Yours sincerely,
{name}
{classs}
{enrollment}
        """

        # Display the generated application
        msg.showinfo("Sick Leave Application", "Application generated successfully!")
        # write_application_to_file(application_text)
        write_application_to_file(application_text)

def sick():
    #title frame
    clear(mainScreenFrame)
    titleFrame= CTkFrame(mainScreenFrame, width=585,fg_color="#2B2C33")
    titleFrame.pack(side="top", fill="x", padx=10, pady=10)

    #dataframe
    dataFrame= CTkFrame(mainScreenFrame, width=585,fg_color="#2B2C33")
    dataFrame.pack(side="top", fill="both", padx=10, pady=10)

    global studentNameVar
    global collegeNameVar
    global classVar
    global enrollmentVar
    global reasonVar

    studentNameVar = StringVar()
    collegeNameVar = StringVar()
    classVar = StringVar()
    enrollmentVar = StringVar()
    reasonVar = StringVar()

    CTkLabel(titleFrame, text="Sick Leave Application", font=("Arial", 40),width= 585,text_color="#EBF4DD").pack(pady=20)

    CTkLabel(dataFrame, text="Student Name:", font=("Arial", 20)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    CTkEntry(dataFrame, textvariable=studentNameVar, width=300, font=("Arial", 20)).grid(row=0, column=1, padx=10, pady=10)

    CTkLabel(dataFrame, text="College Name:", font=("Arial", 20)).grid(row=1, column=0, padx=10, pady=10, sticky="w")

    CTkEntry(dataFrame, textvariable=collegeNameVar, width=300, font=("Arial", 20)).grid(row=1, column=1, padx=10, pady=10)

    CTkLabel(dataFrame, text="Class:", font=("Arial", 20)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    CTkEntry(dataFrame, textvariable=classVar, width=300, font=("Arial", 20)).grid(row=2, column=1, padx=10, pady=10)

    CTkLabel(dataFrame, text="Enrollment Number:", font=("Arial", 20)).grid(row=3, column=0, padx=10, pady=10, sticky="w")

    CTkEntry(dataFrame, textvariable=enrollmentVar, width=300, font=("Arial", 20)).grid(row=3, column=1, padx=10, pady=10)

    CTkLabel(dataFrame, text="Reason for Sick Leave:", font=("Arial", 20)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
    CTkEntry(dataFrame, textvariable=reasonVar, width=300, font=("Arial", 20)).grid(row=4, column=1, padx=10, pady=10)

    CTkLabel(dataFrame, text="From Date").grid(row=5, column=0, padx=10, pady=10, sticky="w")
    global from_date
    global to_date
    from_date = DateEntry(
        dataFrame,
        date_pattern="dd-mm-yyyy",
        background="darkblue",
        foreground="darkblue",
        borderwidth=2,width=20,font=("Arial", 19)
        
    )
    from_date.grid(row=5, column=1, padx=10, pady=10)
    
    CTkLabel(dataFrame, text="To Date").grid(row=6, column=0, padx=10, pady=10, sticky="w")
    to_date = DateEntry(
        dataFrame,
        date_pattern="dd-mm-yyyy",
        background="darkblue",
        foreground="white",
        borderwidth=2,width=20,font=("Arial", 19)
    )
    to_date.grid(row=6, column=1, padx=10, pady=10)
    

    CTkButton(dataFrame, text="Submit", width=300, height=50, font=("Arial", 20),fg_color="#121212",command=generateSick).grid(row=7, column=1, padx=10, pady=10)

def generateCasual():
    name = studentNameVar.get()
    college = collegeNameVar.get()
    classs = classVar.get()
    enrollment = enrollmentVar.get()
    reason = reasonVar.get()
    from_date_value = from_date.get()
    to_date_value = to_date.get()

    if not name or not college or not classs or not enrollment or not reason:
        msg.showerror("Input Error", "Please fill in all the fields.")
    elif from_date_value > to_date_value:
        msg.showerror("Input Error", "From Date cannot be later than To Date.")
    else:
        application_text = f"""
To
The Counsellor
{college}

Subject: Application for Casual Leave

Respected Sir,

I would like to respectfully inform you that due to {reason}, I will not be able to attend college during the period mentioned below.

I kindly request you to grant me casual leave from {from_date_value} to {to_date_value}. I assure you that I will complete all academic responsibilities and maintain regular attendance thereafter.

Thanking you for your kind consideration.

Yours sincerely,
{name}
{classs}
{enrollment}
        """

        msg.showinfo("Casual Leave", "Application generated successfully!")
        write_application_to_file(application_text)


def casual():
    clear(mainScreenFrame)

    titleFrame = CTkFrame(mainScreenFrame, width=585, fg_color="#2B2C33")
    titleFrame.pack(side="top", fill="x", padx=10, pady=10)

    dataFrame = CTkFrame(mainScreenFrame, width=585, fg_color="#2B2C33")
    dataFrame.pack(side="top", fill="both", padx=10, pady=10)

    global studentNameVar, collegeNameVar, classVar, enrollmentVar, reasonVar
    global from_date, to_date

    studentNameVar = StringVar()
    collegeNameVar = StringVar()
    classVar = StringVar()
    enrollmentVar = StringVar()
    reasonVar = StringVar()

    CTkLabel(titleFrame, text="Casual Leave Application", font=("Arial", 40), text_color="#EBF4DD").pack(pady=20)

    labels = ["Student Name:", "College Name:", "Class:", "Enrollment Number:", "Reason:"]
    vars = [studentNameVar, collegeNameVar, classVar, enrollmentVar, reasonVar]

    for i, (label, var) in enumerate(zip(labels, vars)):
        CTkLabel(dataFrame, text=label, font=("Arial", 20)).grid(row=i, column=0, sticky="w", padx=10, pady=10)
        CTkEntry(dataFrame, textvariable=var, width=300, font=("Arial", 20)).grid(row=i, column=1, padx=10, pady=10)

    CTkLabel(dataFrame, text="From Date:", font=("Arial", 20)).grid(row=5, column=0, sticky="w", padx=10, pady=10)
    from_date = DateEntry(dataFrame, date_pattern="dd-mm-yyyy", width=20, font=("Arial", 19))
    from_date.grid(row=5, column=1, padx=10, pady=10)

    CTkLabel(dataFrame, text="To Date:", font=("Arial", 20)).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    to_date = DateEntry(dataFrame, date_pattern="dd-mm-yyyy", width=20, font=("Arial", 19))
    to_date.grid(row=6, column=1, padx=10, pady=10)

    CTkButton(
        dataFrame,
        text="Submit",
        width=300,
        height=50,
        font=("Arial", 20),
        fg_color="#121212",
        command=generateCasual
    ).grid(row=7, column=1, pady=20)

    
def generateBonafide():
    name = studentNameVar.get()
    college = collegeNameVar.get()
    classs = classVar.get()
    enrollment = enrollmentVar.get()
    purpose = purposeVar.get()

    if not name or not college or not classs or not enrollment or not purpose:
        msg.showerror("Input Error", "Please fill in all the fields.")
    else:
        application_text = f"""
To
The Counsellor
{college}

Subject: Request for Bonafide Certificate

Respected Sir,

I am a bonafide student of your institution currently studying in {classs}.
I kindly request you to issue me a Bonafide Certificate for the purpose of {purpose}.

I shall be very grateful to you for your support.

Thanking you.

Yours sincerely,
{name}
{classs}
{enrollment}
        """

        msg.showinfo("Bonafide", "Application generated successfully!")
        write_application_to_file(application_text)


def bonafied():
    clear(mainScreenFrame)

    titleFrame = CTkFrame(mainScreenFrame, fg_color="#2B2C33")
    titleFrame.pack(fill="x", padx=10, pady=10)

    dataFrame = CTkFrame(mainScreenFrame, fg_color="#2B2C33")
    dataFrame.pack(fill="both", padx=10, pady=10)

    global studentNameVar, collegeNameVar, classVar, enrollmentVar, purposeVar
    studentNameVar = StringVar()
    collegeNameVar = StringVar()
    classVar = StringVar()
    enrollmentVar = StringVar()
    purposeVar = StringVar()

    CTkLabel(titleFrame, text="Bonafide Certificate Application", font=("Arial", 40),text_color="#EBF4DD").pack(pady=20)

    labels = ["Student Name", "College Name", "Class", "Enrollment Number", "Purpose"]
    vars = [studentNameVar, collegeNameVar, classVar, enrollmentVar, purposeVar]

    for i, (label, var) in enumerate(zip(labels, vars)):
        CTkLabel(dataFrame, text=label + ":", font=("Arial", 20)).grid(row=i, column=0, sticky="w", padx=10, pady=10)
        CTkEntry(dataFrame, textvariable=var, width=300, font=("Arial", 20)).grid(row=i, column=1)

    CTkButton(dataFrame, text="Submit", width=300, height=50, font=("Arial", 20),
              fg_color="#121212", command=generateBonafide).grid(row=6, column=1, pady=20)

    
def generateApology():
    name = studentNameVar.get()
    college = collegeNameVar.get()
    classs = classVar.get()
    enrollment = enrollmentVar.get()
    mistake = reasonVar.get()

    if not name or not college or not classs or not enrollment or not mistake:
        msg.showerror("Input Error", "Please fill in all the fields.")
    else:
        application_text = f"""
To
The Counsellor
{college}

Subject: Letter of Apology

Respected Sir,

I am {name}, a student of {classs} with enrollment number {enrollment}

I sincerely apologize for {mistake}. I deeply regret my actions and take full responsibility for the inconvenience caused.

I assure you that such a mistake will not be repeated in the future and I will strictly follow all rules and regulations.

Kindly forgive me for this unintentional mistake.

Yours sincerely,
{name}
{classs}
{enrollment}
        """

        msg.showinfo("Apology", "Application generated successfully!")
        write_application_to_file(application_text)


def apology():
    clear(mainScreenFrame)

    # title frame (fixed width)
    titleFrame = CTkFrame(
        mainScreenFrame,
        width=585,
        fg_color="#2B2C33"
    )
    titleFrame.pack(side="top", fill="x", padx=10, pady=10)

    # data frame (fixed width)
    dataFrame = CTkFrame(
        mainScreenFrame,
        width=585,
        fg_color="#2B2C33"
    )
    dataFrame.pack(side="top", fill="both", padx=10, pady=10)

    global studentNameVar, collegeNameVar, classVar, enrollmentVar, reasonVar
    studentNameVar = StringVar()
    collegeNameVar = StringVar()
    classVar = StringVar()
    enrollmentVar = StringVar()
    reasonVar = StringVar()

    CTkLabel(
        titleFrame,
        text="Apology Letter",
        font=("Arial", 40),
        width=585,
        text_color="#EBF4DD"
    ).pack(pady=20)

    fields = [
        "Student Name",
        "College Name",
        "Class",
        "Enrollment Number",
        "Reason for Apology"
    ]
    vars = [
        studentNameVar,
        collegeNameVar,
        classVar,
        enrollmentVar,
        reasonVar
    ]

    for i, (field, var) in enumerate(zip(fields, vars)):
        CTkLabel(
            dataFrame,
            text=field + ":",
            font=("Arial", 20)
        ).grid(row=i, column=0, sticky="w", padx=10, pady=10)

        CTkEntry(
            dataFrame,
            textvariable=var,
            width=300,
            font=("Arial", 20)
        ).grid(row=i, column=1, padx=10, pady=10)

    CTkButton(
        dataFrame,
        text="Submit",
        width=300,
        height=50,
        font=("Arial", 20),
        fg_color="#121212",
        command=generateApology
    ).grid(row=6, column=1, pady=20)

    
def about():
    clear(mainScreenFrame)
    titleFrame= CTkFrame(mainScreenFrame, width=585,fg_color="#2B2C33")
    titleFrame.pack(side="top", fill="x", padx=10, pady=10)

    #dataframe
    dataFrame= CTkFrame(mainScreenFrame, width=585,fg_color="#2B2C33")
    dataFrame.pack(side="top", fill="both", padx=10, pady=10)

    CTkLabel(titleFrame, text="About", font=("Arial", 40),width= 585,text_color="#EBF4DD").pack(pady=20)
    about_text = """This Application Generator is designed to help students create various types of applications easily and efficiently. Whether you need to request sick leave, casual leave, a bonafide certificate, or write an apology letter, this tool simplifies the process by generating well-structured documents based on your input."""

    madeBY = """\n\n Made by: Jasraj Joshi
    For More Information or Quesries Contact at Email: 25amtics285@gmail.com
    If there are any issues please report it to the email provided.
    Next update will include more features and types of applications.
    """

    updates= """
    Updates > Version 1.2:
    - Improved PDF formatting for better readability.
    - Fixed Bugs in Date Selection for Applications.
    - Enhanced User Interface.
    - Added Apology Letter Generation Feature.
    Rest Updates and bug fixes will be provided in Next Version 1.3"""

    CTkLabel(dataFrame, text=about_text, font=("Arial", 15), wraplength=500).pack(pady=20)
    CTkLabel(dataFrame, text=updates, font=("Arial", 15), wraplength=500).pack(pady=10)
    CTkLabel(dataFrame, text=madeBY, font=("Arial", 15,"bold"), wraplength=500,text_color="#9AA0A6").pack(pady=10)

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

root = CTk()
set_appearance_mode("dark")
root.minsize(950,600)
root.maxsize(950,600)
root.title("Application Generator")

#sidebar frame
sideBarFrame= CTkFrame(root, width=322, corner_radius=15)
sideBarFrame.pack(side="left", fill="y",padx=10, pady=10)

#main screen frame
mainScreenFrame= CTkFrame(root, width=585, corner_radius=15, fg_color="#22232A") 
mainScreenFrame.pack(side="right", fill="both", padx=10, pady=10)

#sidebar Code
# these are the buttons of the sidebar to navigate through
CTkButton(sideBarFrame, text="Sick Leave", width=300, height=70, corner_radius=20, fg_color="#1E1E1E", text_color="white", font=("Arial", 22),hover_color="#7AE06B",command=sick).pack(pady=10, padx=10)

CTkButton(sideBarFrame, text="Casual Leave", width=300, height=70, corner_radius=20, fg_color="#1E1E1E", text_color="white", font=("Arial", 22),hover_color="#7AE06B",command=casual).pack(pady=10, padx=10)

CTkButton(sideBarFrame, text="Bonafied", width=300, height=70, corner_radius=20, fg_color="#1E1E1E", text_color="white", font=("Arial", 22),hover_color="#7AE06B",command=bonafied).pack(pady=10, padx=10)

CTkButton(sideBarFrame, text="Apology Letter", width=300, height=70, corner_radius=20, fg_color="#1E1E1E", text_color="white", font=("Arial", 22),hover_color="#7AE06B",command=apology).pack(pady=10, padx=10)

CTkButton(sideBarFrame, text="About", width=300, height=70, corner_radius=20, fg_color="#1E1E1E", text_color="white", font=("Arial", 22),hover_color="#7AE06B",command=about).pack(pady=10, padx=10)

CTkButton(sideBarFrame, text="Quit", width=300, height=90, corner_radius=20, fg_color="#1E1E1E", text_color="white", font=("Arial", 22),hover_color="#CD3434",command=root.destroy).pack(pady=10, padx=10)

home= ["Are You Sick Today?","Need a Leave?","Need a Bonafied Certificate?","Want to Apologize?","We got you covered!","What wrong you did Today?","Make it Right with an Apology Letter!","Your One-Stop Application Generator!","Which Application do you need Today?"]

random_home= rand.choice(home)
titleFrame= CTkFrame(mainScreenFrame, width=585,fg_color="#2B2C33")
titleFrame.pack(side="top", fill="x", padx=10, pady=10)

#dataframe
dataFrame= CTkFrame(mainScreenFrame, width=585,fg_color="#2B2C33")
dataFrame.pack(side="top", fill="both", padx=10, pady=10)

CTkLabel(titleFrame, text="Welcome to Application Generator", font=("Arial", 35),width= 585,text_color="#EBF4DD").pack(pady=20)
CTkLabel(dataFrame, text=random_home, font=("Arial", 30),text_color="#F1E6C9").pack(pady=180)
CTkLabel(dataFrame, text="**--Made By JJ--**", font=("Arial", 15),text_color="#9AA0A6").pack(side="bottom", pady=10)

root.mainloop()

# Code Ends here