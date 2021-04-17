
def main():
    mid=float(input("Enter grade on midterm:"))
    final=float(input("Enter grade on final exam:"))
    print("Semester Grade: {}".format(semesterGrade(mid,final)))

def semesterGrade(mid,final):
    ave=(mid+final*2)/3
    ave2=ceil(ave)
    if ave2>=90:
        return "A"
    elif ave2>=80:
        return "B"
    elif ave2>=70:
        return "C"
    elif ave2>=60:
        return "D"
    else:
        return "F"

def ceil(ave):
    ave2=round(ave)
    return ave2

# lambda eve:round(ave)

main()




