# 1. The output value is computed as a list of integers. Use Python's print(...) to print it.
# 2. Negative integers and ZERO are allowed in the input.
# 3. Use python's spilt(...) function to process the input string
txt=str(input())
lst=txt.split(",")
for i in range(len(lst)):
	lst[i]=int(lst[i])*2
print(lst)