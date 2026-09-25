def Anagram(str):
    group={}
    for word in str:
        key=''.join(sorted(word))
        
        if key not in group:
            group[key]=[]
        group[key].append(word)
        
    return list(group.values())

str=["eat", "tea", "tan", "ate", "nat", "bat"]
result=Anagram(str)
print(result)
            