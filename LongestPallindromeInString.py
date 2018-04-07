def longest_pallindrome(s):
    if s == s[::-1]:
        return len(s), s

    else:
        if len(s) > 2:
            left = longest_pallindrome(s[:-1])
            right = longest_pallindrome(s[1:])

            if left[0] > right[0]:
                return left
            else:
                return right
        else:
            return [0,0]

# s = "asdfghjklqwekasdfghjklkjhgfdsaqweewq"
# s = "asaabcd"
s = "babkanakbc"
test = longest_pallindrome(s)
print(test)
