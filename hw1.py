import os
print(os.getcwd())

course_file = open ("vgsales.txt","r")
lines_in_file = course_file.readlines()
for line in lines_in_file[1:]:
    line=line.strip()
    split_line=line.split("\t")
    name=split_line[1]
    year=int(split_line[3])
    na_sales=split_line[6]
    eur_sales=split_line[7]
    jp_sales=split_line[8]
    other_sales=split_line[9]
    global_sales=float(split_line[10])
    avg_sales=(global_sales)/4
    print("the video game ", name ,"had an average yearly sale of:",avg_sales ," copies sold")
print("all done")