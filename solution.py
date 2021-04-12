def solution(s):
    cntr = 0
    prev = s[0]
    for char in s:
        if prev != char:
            cntr += 1
            print(char)
        prev = char
    return cntr

print(solution("<<->>-<"))