
string= input("Enter string: " )
print (string[ : : -1])
vowels=0
index=-1

user_Input=input("String Please: ")
for i in user_Input:
      index=index+1
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
          print("Index:", index)
          print("vowel is:", i)
          vowels=vowels+1
          
