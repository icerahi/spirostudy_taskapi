Live_test : https://spirotask.pythonanywhere.com

## Local Installation

```
git clone https://github.com/icerahi/spirostudy_taskapi.git
cd spirostudy_taskapi
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## all endpoints Guide

Note : We have only two user role (instructor and student).Instructor and Student both can register,view own profile,visit other's courses,But Instructor can only create courses,update,delete and keep hide from others. Student can enroll those open courses.
After register,To access all endpoints you must have to send Basic Authentication Creadentials (username,password) with requests.

### Instructor Perform

Instructor register:

```
Post: /api/register/student/
    json_data = {
    "username":"username",
    "password":"password",
    "password2":"password"}
```

Create Course:

```
POST : /api/
    json_data = {
        "title":"course_title",
        "description":"course_description",
        "active":true/false
    }
```

Allcourses:

```
GET : /api/
```

Single Course:

```
GET : /api/<course_id>/
```

Course update:

```
PUT : /api/<course_id>/
    json_data = {
        "title":"blabla update",
        "description":"bla bla update",
        "active":true/false
    }
```

Course Delete:

```
Delete: /api/<course_id>/
```

Profile and created_course:

```
Get : /api/profile/
```

### Student Perform

register:

```
Post: /api/register/student/
    json_data = {
    "username":"username",
    "password":"password",
    "password2":"password"
    }
```

Allcourses:

```
Get : /api/
```

Single Course:

```
Get : /api/<course_id>/
```

Course Enroll:

```
Get : /api/<course_id>/enroll/
```

Profile and enrolled courses:

```
Get : /api/profile/
```
