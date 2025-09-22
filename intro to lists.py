'''
course_file = open ("course.txt","r")
lines_in_file = course_file.readlines()
for line in lines_in_file:
    line = line.strip()
    print(line)
    print("all done")
'''

course_file = open ("course.txt","r")
lines_in_file = course_file.readlines()
for line in lines_in_file:
    line=line.strip()
    split_line=line.split(":")
    course=split_line[0]
    credits= split_line[1]
    print(course, ": ", credits)
print("all done")

    

