import re

files = '''20200309_최종.png
20200309_최종_수정.png
20200309_최종_수정(1).png
20200309_최종_수정(2).png
20200309_최종_확정.png
20200309_최종_확정2.png'''.split()

directory = dict()  # java의 hashmap


# 기존 파일들 hashmap에 저장
for file in files:
    name, ext = file.split('.')
    if ext in directory:
        directory[ext].add(name)
    else:
        directory[ext] = set()
        directory[ext].add(name)


def fileName():
    print("파일명을 입력하세요.")
    while True:
        try:
            # 파일 이름 입력
            name, ext = input().split('.')
            break
        except:
            print("확장자까지 입력하세요.")
            continue

    if ext in directory.keys():
        if name in directory[ext]:
            regex = re.compile('.+\([\d]+\)')
            cnt = 1
            if (tmp := re.fullmatch(regex, name)):
                for file in directory[ext]:
                    if (match := re.match('.+(?=\([\d]+\))', file)):
                        idx = match.end()+1
                        cnt = max(cnt, int(file[idx:-1]))
                cnt += 1
                insertedName = ''.join(
                    tmp.group().split('(')[:-1])+"({})".format(cnt)
                directory[ext].add(insertedName)
            else:
                while True:
                    if name+"({})".format(cnt) in directory[ext]:
                        cnt += 1
                    else:
                        break
                insertedName = name+"({})".format(cnt)
                directory[ext].add(insertedName)
        else:
            insertedName = name
            directory[ext].add(insertedName)
    else:
        directory[ext] = set()
        insertedName = name
        directory[ext].add(insertedName)

    for key in directory.keys():
        for value in directory[key]:
            print(value+"."+key)

    print("추가된 이름은", insertedName+'.'+ext)


fileName()
