d={"Lion":0,"Tiger":0}
for _ in range(9):
    d[input()]+=1
if d["Lion"]>=5:
    print("Lion")
else:
    print("Tiger")