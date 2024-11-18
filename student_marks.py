# we can cheak grade of students
import time
from sty import fg,rs,ef
print(f"{fg.blue}{ef.b}_______WellCome to Student marks______{rs.all}")
name=input(f"{fg.grey}{ef.b}{ef.u}Insert Your Name :{rs.all}")
age=int(input(f"{fg.grey}{ef.b}{ef.u}Enter your age:{rs.all}"))
if age>=18:
    print(f"{fg.blue}{ef.i}_____{ef.u}WellCome {name} to Screen{ef.rs}____{rs.all}")
else:
    print(f"{fg.blue}{ef.b}{ef.u}You can't play.{rs.all}")
    quit()
def student(marks):
    if marks>=90 and marks<=100:
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(3)
        print(f"{fg.blue}{ef.i}{ef.u}Your Grade is A+{rs.all}")
    elif marks>=75 and marks<=89:
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(3)
        print(f"{fg.blue}{ef.i}{ef.u}Your Grade is B+{rs.all}")
    elif marks>=50 and marks<=74:
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(3)
        print(f"{fg.blue}{ef.i}{ef.u}Your Grade is C{rs.all}")
    elif marks>=40 and marks<=49:
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(3)
        print(f"{fg.blue}{ef.i}{ef.u}Your Grade is D{rs.all}")
    elif marks>=30 and marks<=39:
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(3)
        print(f"{fg.blue}{ef.i}{ef.u}Your Grade is E{rs.all}")
    elif marks>=0 and marks<=29:
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(3)
        print(f"{fg.blue}{ef.i}{ef.u}Your Grade is F{rs.all}")
        print(f"{fg.red}{ef.i}{ef.u}Fail...{rs.all}")
    else:
        print(f"{fg.blue}{ef.b}Invalid{rs.all}")
try:
    while True:
        marks=float(input(f"{fg.green}{ef.b}Enter marks of one subject for cheacking Grade\n type 0 for Quit : {rs.all}"))
        if marks==0:
            print(f"{fg.blue}{ef.blink}{ef.u}Done!{rs.all}")
            quit()
        else:
            
            print("ok")
            student(marks)
except ValueError:
    print(f"{fg.red}{ef.b}Invalid!{rs.all}")