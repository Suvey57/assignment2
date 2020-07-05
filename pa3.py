def Convert(string): 
    li = list(string.split(" ")) 
    return li 
  
a=input("enetr a paragraph in which anagrams is to be detected:")
b=Convert(a)
print(b)

anagram_list = []
for word_1 in b: 
    for word_2 in b: 
        if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
            anagram_list.append(word_1)
print(anagram_list)