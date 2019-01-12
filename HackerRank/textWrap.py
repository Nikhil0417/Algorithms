import textwrap

def wrap(string, max_width):
    s = ''
    for i in range(0,len(string),max_width):
        s += '\n' + (string[i:max_width+i])
    return s[1:]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
