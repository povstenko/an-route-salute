def solution(s):
    cntr = 0
    for i, char in enumerate(s):
        # print(i, char)
        if char == ">":
            for el in s[i:]:
                if el == "<":
                    cntr += 2
    
    return cntr

print(solution(">----<"))
print(solution("<<>><"))
print(solution("<<->>-<"))