from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
import os,face_recognition,numpy as np,cv2,datetime,csv
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
def process():
    path="media/profile_pic/"
    images = []
    classNames = []
    myList = os.listdir(path)
    for cl in myList:
        currImg = cv2.imread(f'{path}/{cl}')
        images.append(currImg)
        classNames.append(os.path.splitext(cl)[0])
    # print(classNames)
    return images,classNames
global known, classNames    
images,classNames=process()
known = findEncodings(images)

def BASE(request):
    return render(request, 'base.html')
def landing(request):
    return render(request,'landing.html')
def markAttendance(name):   
    head=[name,datetime.datetime.now()]
    with open('employee_management_system/Attendance.csv','a') as f:
        writer=csv.writer(f)
        writer.writerow(head)

def LOGIN(request):
    return render(request, 'login.html')

def BLANK(request):
    return render(request,'blank.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'), )

        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('head_home')
            elif user_type == '2':
                return redirect('employee_home')
            else:
                messages.error(request, 'Email and Password are invalid!')
                return redirect('login')
        else:
            messages.error(request, 'Email and Password are invalid!')
            return redirect('login')

def camera(req):
    encodeListKnown = known
    cap = cv2.VideoCapture(0)
    result=True
    while(result):
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        # print("IMGS")
        # print(imgS)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                
                print(name)
                # return(render(req,'login.html'))
                return redirect('login')
            else:
                cv2.imshow('Webcam',img)
                cv2.waitKey(1)
                cv2.destroyAllWindows()
                return(render(req,'test.html',{'text':"Authentication Failed, Try Again"}))
def attendance(req):
    encodeListKnown = known
    cap = cv2.VideoCapture(0)
    result=True
    while(result):
        
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        # print("IMGS")
        # print(imgS)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                markAttendance(name)
                print(name)
                print("Attendance Taken Sucessfully...")
                cv2.destroyAllWindows()
                return(render(req,'test.html',{'text':"Attendance Taken Successfully..."}))
                
            else:
                cv2.imshow('Webcam',img)
                cv2.waitKey(1)
                cv2.destroyAllWindows()
                return(render(req,'test.html',{'text':"Authentication Failed, Try Again"}))
                
def doLogout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if password != None and password != "":
                customuser.set_password(password)

            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic

            customuser.save()
            messages.success(request, 'Your Profile is Updated Successfully!')
            return redirect('profile')
        except:
            messages.error(request, 'FAILED to Update your Profile')

    return render(request, 'profile.html')
