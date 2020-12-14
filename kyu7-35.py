def palindrome_chain_length(n) :

    s = str(n)
    count = 0

    while True :
        reverse_s = s[::-1]
        if s == reverse_s :
            return count
        else :
            count = count + 1
            s = str(int(s) + int(reverse_s))


print(palindrome_chain_length(87)) # 4
print(palindrome_chain_length(88)) # 0
print(palindrome_chain_length(89)) # 24
