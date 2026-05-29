'''
Student add & Marks input করা -done
GPA calculate -done
Result save করা (results.txt)
Topper show করা
'''
def gpa_calculate(x):
    main_dict = {}
    for i,j in x.items():
        total = 0
        num = 0
        for k in j:
            k  = int(k)
            total += k
            num += 1
        avg = round(total / num)
        if avg >= 0 and avg <= 33:
            result = '1.0'
        elif avg >= 34 and avg <= 39:
            result = '2.0'
        elif avg >= 40 and avg <= 69:
            result = '3.0'
        elif avg >= 70 and avg <= 79:
            result = '4.0'
        elif avg >= 80 and avg <= 100:
            result = '5.0'
        main_dict[i] = result
    return main_dict




student = {
    'student_1': [50, 60, 80],
    'student_2': [10, 15, 22],
    'student_3': [20, 30, 60],
    'student_4': [20, 100, 90],
}

operation = int(input('1.Add Student\n2.GPA Calculate\n3.Save Result\n4.Show Topper\nEnter number what do you want to do?\n'))

#Add student & his/her marks
if operation == 1:
    add_student = input('Enter the name of the student:\n')
    bangla = int(input('How much number got in Bangla\n'))
    english = int(input('How much number got in English\n'))
    math = int(input('How much number got in Math\n'))
    student[add_student] = [bangla,english,math]
    print(student)

#Calculate GPA by function
elif operation == 2:
    result = gpa_calculate(student)
    for i, j in result.items():
        print(f'{i} accquired {j}')

#Save Result:
elif operation == 3:
    with open('result.txt', 'w') as x:
        result = gpa_calculate(student)
        for i, j in result.items():
            x.write(f'{i} accquired {j}\n')

elif operation == 4:
    result_list = gpa_calculate(student)
    x = max(result_list.values())
    for i, j in result_list.items():
        if j == x:
            print(f'{i} is the Topper')


