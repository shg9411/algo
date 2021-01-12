n = int(input())
arr = ["" for _ in range(8)] #수의 길이가 최대 8이므로 길이 8짜리 리스트를 만듬(리스트의 인덱스에 대한 설명 : index 7->1의 자리, 6->10의 자리 .... 0->1000만의자리)
result = {} #알파벳과 숫자를 키와 값으로 대응시킬 딕셔너리
sum = 0
for _ in range(n):
  word = input()
  #리스트arr의 마지막 방과 현재 입력받은 단어의 마지막 알파벳을 일치시키며 단어의 뒤에서부터 앞쪽으로 리스트arr에 넣어준다. 즉, 알파벳들이 그 자리수에 맞게 arr에 차곡차곡 쌓이게 된다.
  for i in range(len(word)): 
    arr[7-i]+=word[len(word)-1-i]
print(arr)
i = 9 
for k in range(len(arr)):
  if arr[k]: #arr[k]가 비어있지 않다면
    for alpha in arr[k]: 

      if alpha not in result: #딕셔너리에 현재 계산하려고하는 알파벳이 없는 상태라면
        result[alpha] = i
        i-=1
      sum+=(10**(7-k))*result[alpha] #딕셔너리에서 해당 알파벳에 대응하는 숫자를 찾아내어 자릿수와 곱하여 sum에 누적.
print(sum)