from collections import Counter

random  = 'sselirjalijrlaijrliawenrlinvlaidlivjawlijer'
crand=Counter(random)

print(crand)

## counter한것을 list로 변환
## list(random)= list(Counter(random).elements())
print(list(crand.elements()))
print(crand.most_common(2))
