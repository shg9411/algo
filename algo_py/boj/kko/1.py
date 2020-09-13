def solution(new_id):
    ans = ''
    for char in new_id:
        if char.isalpha():
            ans += char.lower()
        elif char in '0123456789-_.':
            ans += char
    aans = ans[0]
    for char in ans[1:]:
        if aans[-1] == '.' and char == '.':
            continue
        aans += char
    ans = aans
    if ans and ans[0] == '.':
        ans = ans[1:]
    if ans and ans[-1] == '.':
        ans = ans[:-1]
    if not ans:
        ans = 'a'
    ans = ans[:15]
    if ans[-1] == '.':
        ans = ans[:-1]
    l = len(ans)
    while l < 3:
        ans += ans[-1]
        l += 1
    return ans


print(solution("."))
# ok
