def longest_word(words):
 max_length=0
 for word in words:
    if len(word)>max_length:
        max_length=len(word)
 return max_length
words=input("enter words seperated by space:").split()
result=longest_word(words)
print("length of longest word",result)
