# A function that takes a grade by input and shows the final grade
def main():
    mid=float(input("Enter grade on midterm:"))
    final=float(input("Enter grade on final exam:"))
    print("Semester Grade: {}".format(semesterGrade(mid,final)))
# A function that calculates grades and classifies them as 'ABCDF'
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
# A function that rounds up the calculated results
def ceil(ave):
    ave2=int(-(-ave//1))
    return ave2
main()


