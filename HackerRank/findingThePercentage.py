if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        res = sum(scores)/len(scores)
        student_marks[name] = res
    query_name = input()
    #z = str(round(student_marks[query_name],2))
    #print(z)
    print("{:0.2f}".format(student_marks[query_name]))
