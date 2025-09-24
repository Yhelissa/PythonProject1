import os
print(os.getcwd())

current_year=int(2025)

course_file = open ("vgsales.txt","r")
lines_in_file = course_file.readlines()
for line in lines_in_file[1:]:
    line=line.strip()
    split_line=line.split("\t")
    name=split_line[1]
    year=float(split_line[3])
    na_sales=float(split_line[6])
    eur_sales=float(split_line[7])
    jp_sales=float(split_line[8])
    other_sales=split_line[9]
    global_sales=float(split_line[10])
    years_since_release = int(current_year - year)
    avg_sales=(na_sales + eur_sales + jp_sales * years_since_release)/3
    formatted_avg_sales=f"{avg_sales:.2f}"
    print("the video game:\n ", name ,"sold: ",formatted_avg_sales ," millions of copies on average since its release")
print("all done")