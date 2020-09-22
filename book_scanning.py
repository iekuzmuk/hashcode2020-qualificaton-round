import sys
from collections import namedtuple

Book = namedtuple('Book','id,days,bk_shp,bks')

B,L,D = (int(x) for x in sys.stdin.readline().rstrip().split())
scores = [int(x) for x in sys.stdin.readline().rstrip().split()]
libraries = []
for i in range(L):
    N,T,M = (int(x) for x in sys.stdin.readline().rstrip().split())
    bks = [int(x) for x in sys.stdin.readline().rstrip().split()]
    libraries.append(Book(i,T,M,bks))



# sort by check time - bk_shp
libraries.sort(key=(lambda x: (x.days,-x.bk_shp)))

print(L)
for l in libraries:
    print(l.id, len(l.bks))
    bks = sorted(l.bks, key=(lambda x: (-scores[x])))
    print(' '.join([str(x) for x in bks]))

#print(B,L,D)
#print(scores)
#print([(x.days,x.bk_shp) for x in libraries])
