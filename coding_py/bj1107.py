enable_btn_set = {str(x) for x in range(10)}

N = int(input())
break_button_num = int(input())
if(break_button_num == 0):
    pass
else:    
    break_button = set(input().split())
    enable_btn_set -= break_button
    
result = abs(N - 100)
for i in range(1000001):
    is_enable = True
    for div_num in str(i):
        if(div_num not in enable_btn_set):
            is_enable = False
    if(is_enable):
        result = min(result, abs(N - i) + len(str(i)))
        
print(result)