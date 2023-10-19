n = int(input("input n: "))
s = str(n) 
l = len(s)
for i in range(l//2):
    if s[i] != s[-1-i]: 
       print("It's not palindrome")
       break
else:
    print("It's palindrome")
