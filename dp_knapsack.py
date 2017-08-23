#!/usr/bin/python
masks=[]
memo={}
def iSize(i): return i[0]
def iValue(i): return i[1]
def iName(i): return i[2]
example=[(3, 3, 'A'),
         (4,1,'B'),
         (8,3,'C'),
         (10,4,'D'),
         (15,3,'E'),
	 (20,6,'F')] 
sackSize = 32
def knapsack(items, sizeLimit):
	P={}
	for n in range (len(items)+1):
		for lim in range(sizeLimit+1):
			if n == 0:
				P[n,lim] = 0
			elif iSize(items[n-1])>lim:
				P[n,lim] = P[n-1,lim]
			else:
				P[n,lim] = max(P[n-1, lim], P[n-1,lim-iSize(items[n-1])]+ iValue(items[n-1]))

	
	print P
	L=[]
	nItems = len(items)

	lim = sizeLimit
	while nItems > 0:
		if P[nItems, lim] == P[nItems-1, lim]:
			nItems = nItems - 1
		else: 	
			nItems = nItems - 1
			L.append(iName(items[nItems]))
			lim -= iSize(items[nItems])

	L.reverse()
	return L
	
	          

def main():
  	print (example)
	print (iSize(example[2]))
	print knapsack(example, sackSize)
         		  
if __name__ == "__main__":
	main()
	
    
