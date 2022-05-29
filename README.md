## Face Verification Based Login, Attendance Employee Management System
## About
In this Attendance System the attendance for Employees is marked using Face verification. The Faculty has the permission to take Attendance, add a employee, modify employee details. The head can also send notifications to employees, and emplyees can also send feedback/requests to head which will be approved by Head . The head can also download the attendance sheet of the emplyees present<br>
The credentials for the Head are provided who has access to the whole database. Only the superuser can update the attendance of a employee.<br>
**Django** web framework was used for the development of the whole web app. **OpenCv and face_recognition Library** were used for the development of Face Recognizer. The Face Recognizer can detect faces and mark their attendance into Database.<br>
**Note: The dlib package required for installation of face_recognition api .**<br>
To run the web app on your local computer, install the required libraries([requirements.txt](https://github.com/ss1208/Employee_Management_System/blob/main/requirements.txt)) using the command:<br>
```python
pip3 install -r requirements.txt
``` 
<br>and run the following command in the command prompt:<br>
```python
python manage.py runserver
``` 

**For more details please refer to the video tutorial...**<br/>

<br/>
