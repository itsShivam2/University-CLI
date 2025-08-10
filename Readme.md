university-cli

v1.0
print("University Management System!")


v1.1
print("Welcome to the University Management System!")


v1.2
Code changes to save data to /student_data/students.json file


Tried to use volumes to persist data
Error - Gave wrong path to save file, data couldn't persist


v1.3
Removed the error encountered in the v1.2
Data persisted across containers using volumes


v2.0
Added multi stage builds, image size reduced by 12%.

What multi stage build did?
1. Install the build tools, pip caches, temp files and any other dependencies into /install folder in the build stage
2. Copies only the installed packages into a clean Python Alpine image in the run stage