if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    a=list(arr)
    a.sort(reverse=True)
    m = max(a)
    for i in a:
        if i != m:
            print(i)
            break
