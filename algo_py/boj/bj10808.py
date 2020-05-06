st = input()
print(' '.join(map(str, [(st.count(chr(i))) for i in range(97, 123)])))
