data=input()
dataup=data.upper()
text=dataup[::-1]
if dataup==text : 
	print(data+" is a palindrome.")
else:
	print(data+" is NOT a palindrome.")