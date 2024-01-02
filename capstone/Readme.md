This project is a Student Management software built with Html, CSS and Javscript frontend with a Django Frontend, it can be used by lecturers/teacheers of an institution to view each course they teach, add new schedules for lectures and also send notices out to students. Students can also check class times and see the notice sent out y lecturers.In this project only lecturer need to do authentication while it isnt neededfor students as lecturers are the only ones who are able to add new schedulesor notices.
Complexity and Distinctiveness:
    One of the features of this project that sets it apart from the others is the factsthat it has 2 different apps which handles the lecturer and student part individually this is because in my program i aim to have different windows to handle both sets of people. This web application consists of multiple models for the Lecturer app,namely;The lecturer model(this handes registering the lecturers), the course model (this handles the courses), the course schedule(this is to store all schedules  for each course) and the notice model(this is to handle all the notices  by each lecturer), while the Student app consists of a single model which is the student model which handles storing student information. This application akso makes use of javascript in the front end to send alerts whenever a particular course schedule or noitce has been created or updated successfully. In this project a new user starts at the defualt route and is thenoffered two widgets to click on to take them to the appropriate page wether they are either a lecturer or a student.
File Content:
    In my web applications there are two different apps;
    1. Lecturer app: This contains;
       i. Static folder: this contains the Css files and the images files
       iI. Templates: this contains the Html files 
    2. Student App: this contains;
        This contains the templates file which hass the html files
How To Run:
    All that is needed is to run "py manage.py runserver" to activate the server and then visit http://localhost:8000 in your browser.
