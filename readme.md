# all endpoints

Note : To access all endpoints you must have to send with Basic Authentication Creadentials (username,password).

# Instructor Perform

Instructor register:

```Post: /api/register/student/
    json_data = {
    "username":"username",
    "password":"password",
    "password2":"password"}
```

Create Course:

```POST : /api/
    json_data = {
        "title":"course_title",
        "description":"course_description",
        "active":true/false
    }
```

Allcourses:

```GET : /api/

```

Single Course:

```GET : /api/<course_id>/

```

Course update:

```PUT : /api/<course_id>/
    json_data = {
        "title":"blabla update",
    }
```

Course Delete:

```Delete: /api/<course_id>/

```

Profile and created_course:

````Get : /api/profile/


# Instructor and Student both can perform



# Student Perform

register:
```Post: /api/register/student/
    json_data = {
    "username":"username",
    "password":"password",
    "password2":"password"
    }
````

Allcourses:

```
Get : /api/
```

Single Course:

```
Get : /api/<course_id>/
```

Course Enroll:

```Get : /api/<course_id>/enroll/

```

Profile and enrolled courses:

```Get : /api/profile/

```
