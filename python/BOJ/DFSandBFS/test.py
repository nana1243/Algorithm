from collections import Counter

dataSource=[
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]

tags=["t1", "t2", "t3"]

for i in range(len(dataSource)):
    datatag = dataSource[i][1:]
    print(datatag)
    print(Counter(datatag))
