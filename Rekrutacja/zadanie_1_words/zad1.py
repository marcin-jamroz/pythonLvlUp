from collections import Counter
from operator import itemgetter

counter = Counter()

for i in range(30):
    with open("word_{}.txt".format(i), "r") as file:
        line = file.readline().lower()
        cnt = Counter(line)
        counter.update(line)
    
        #print(cnt)

sortedCounter = list(counter.items())
sortedCounter.sort(key=itemgetter(0))

final = ""

for item in sortedCounter:
    final = "{}{}{}".format(final, item[0], item[1])

print(final)