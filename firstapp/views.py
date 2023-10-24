from django.shortcuts import render,redirect,HttpResponse
from . models import student,present
from . forms import student_form
import face_recognition
import cv2
import numpy as np
from django.db.models import *
from openpyxl import Workbook
import pytz
from django.core.mail import send_mail
# Create your views here.

def home(request):
    profiles = student.objects.all().order_by('first_name').values()
    profile_present = student.objects.filter(present=1).order_by('first_name').values()
    profile_absent = student.objects.filter(present=0).order_by('first_name').values()
    context={
        'profiles':profiles,
        'pres':profile_present,
        'abs':profile_absent
        }
    return render(request,'index.html',context)
def profiles(request):
    profiles = student.objects.all()
    return render(request,'profiles.html',{'profiles':profiles})
def register(request):
    form = student_form
    if request.method == 'POST':
        form = student_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'register.html',{'form':form})
def deleteprofile(request,id):
    profiles = student.objects.get(id=id)
    profiles.delete()
    return redirect('profiles')
def modifyprofile(request,id):
    person = student.objects.get(id=id)
    form = student_form(instance=person)
    if request.method =='POST':
        form = student_form(request.POST,request.FILES,instance=person)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    return render(request,'register.html',{'form':form})


#use the below scan for accuracy and this scan for speed recognition But not Accurate

# def scan(request):

#     global last_face
#     known_face_encodings = []
#     known_face_names = []

#     profiles = student.objects.all()
#     for profile in profiles:
#         person = profile.image
#         image_of_person = face_recognition.load_image_file(f'{person}')
#         person_face_encoding = face_recognition.face_encodings(image_of_person)[0]
#         known_face_encodings.append(person_face_encoding)
#         known_face_names.append(f'{person}'[:-4])


#     video_capture = cv2.VideoCapture(0)

#     face_locations = []
#     face_encodings = []
#     face_names = []
#     process_this_frame = True

#     while True:

#         ret, frame = video_capture.read()
        

#         if process_this_frame:
#             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#             rgb_small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
#             face_locations = face_recognition.face_locations(rgb_small_frame)
#             face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#             face_names = []
#             for face_encoding in face_encodings:
#                 matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                 name="Unknown"
#                 face_distances = face_recognition.face_distance( known_face_encodings, face_encoding)
#                 best_match_index = np.argmin(face_distances)
#                 if matches[best_match_index]:
#                     name = known_face_names[best_match_index]

#                     # profile = student.objects.get(Q(image__icontains=name)) not working if 2 persons have same like image names
#                     profile = student.objects.filter(Q(image__contains=name)).first()
#                     if profile.present == True:
#                         pass
#                     else:
#                         profile.present = True
#                         profile.save()

#                     # if last_face != name:
#                     #     last_face = LastFace(last_face=name)
#                     #     last_face.save()
#                     #     last_face = name
#                     #     winsound.PlaySound(sound, winsound.SND_ASYNC)
#                     # else:
#                     #     pass

#                 face_names.append(name)

#         # process_this_frame = not process_this_frame

#         for (top, right, bottom, left), name in zip(face_locations, face_names):
#             top *= 4
#             right *= 4
#             bottom *= 4
#             left *= 4

#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#             cv2.rectangle(frame, (left, bottom - 35),(right, bottom), (0, 0, 255), cv2.FILLED)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(frame, name, (left + 6, bottom - 6),font, 0.5, (255, 255, 255), 1)

#         cv2.imshow('Video', frame)

#         if cv2.waitKey(1) & 0xFF == 13:
#             break

#     video_capture.release()
#     cv2.destroyAllWindows()
#     return redirect('index')
    
    
def reset1(request):
    profile = student.objects.filter(present=1).update(present=0)
    temp = present.objects.all()
    temp.delete()
    return redirect('index')
def save1(request):
    table1=student.objects.filter(present=1)
    for table in table1:
        first_name=table.first_name
        last_name=table.last_name
        name=first_name+" "+last_name
        table2=present.objects.create(name=name)
        table2.save()
    temp=present.objects.all()

    workbook = Workbook()
    sheet = workbook.active
    ist = pytz.timezone('Asia/Kolkata')
    i=3
    for t in temp:
        dtf = t.time
        dtf_ist = dtf.astimezone(ist)
        date = dtf_ist.strftime('%Y-%m-%d')
        time = dtf_ist.strftime('%I:%M:%S %p')  #this is 12 hour format of ist
        # time = dtf_ist.strftime('%H:%M:%S')  this line is 24 hours format of ist
        # date = str(dtf)[:10]
        # time = str(dtf)[11:19]               these 2 lines use utc timezone
        sheet["A1"]="NAME"
        sheet["B1"]="DATE"
        sheet["C1"]="TIME"
        a="A"+str(i)
        b="B"+str(i)
        c="C"+str(i)
        sheet[a] = t.name
        sheet[b] = str(date)
        sheet[c] = str(time)
        i=i+1
    workbook.save(filename="attendence.xlsx")
    return render(request,'saved_table.html',{'profiles':temp})

def send_email(request):
    email_from = "BilalProjectTesting@gmail.com"
    persons=student.objects.filter(present=1)
    for person in persons:
        subject = 'You Are Present Today'
        message = f'Hi, {person.first_name} {person.last_name} , Roll Number : {person.rollno}, We Have Been Successfully Marked Your Attendence today.'
        recipient = [person.email]
        send_mail( subject, message, email_from, recipient,fail_silently=False)
    return redirect('index')

def attendence(request):
    profiles = student.objects.all()
    return render(request,'attendence.html',{'profiles':profiles})

def profilepresent(request,id):
    profile = student.objects.filter(id=id).update(present=1)
    return redirect('attendence')

def profileabsent(request,id):
    profile = student.objects.filter(id=id).update(present=0)
    return redirect('attendence')


#use the below scan for accuracy and above scan for speed recognition But not Accurate

def scan(request):

# Define a dictionary to store known face encodings and their corresponding profiles
    known_face_encodings = {}
    known_face_names = {}

    # Load the profiles and their face encodings
    profiles = student.objects.all()
    for profile in profiles:
        person = profile.image
        image_of_person = face_recognition.load_image_file(f'{person}')
        person_face_encoding = face_recognition.face_encodings(image_of_person)[0]
        known_face_encodings[profile.id] = person_face_encoding
        name=profile.first_name + profile.last_name
        known_face_names[profile.id] = name

    # Initialize the video capture
    video_capture = cv2.VideoCapture(0)

    # Initialize variables for face detection
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()

        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(list(known_face_encodings.values()), face_encoding, tolerance=0.5)
                name = "Unknown"

                face_distances = face_recognition.face_distance(list(known_face_encodings.values()), face_encoding)
                best_match_id = np.argmin(face_distances)

                if matches[best_match_id]:
                    profile_id = list(known_face_encodings.keys())[best_match_id]
                    name = known_face_names[profile_id]

                    profile = student.objects.get(id=profile_id)
                    if profile.present:
                        pass
                    else:
                        profile.present = True
                        profile.save()

                face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == 13:
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return redirect('index')