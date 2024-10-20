
def longest_common_prefix(string):
    if not string:
        return ""
    
    prefix = string[0]
    
    for string in string[1:]:
     
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1] 
        if not prefix:
            break 

    return prefix

strings = ['car','carpenter','cargo']
print(longest_common_prefix(strings))