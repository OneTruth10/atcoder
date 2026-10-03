def isPrime(number):  
   prime=True
   if number<2:
      return False
   for i in range(2,int(number**0.5)+1):  
      if number % i ==0:  
         prime=False  
         break  
   return prime 

S = input()
temp = "1"*len(S)
#while temp[0]!="0":
    