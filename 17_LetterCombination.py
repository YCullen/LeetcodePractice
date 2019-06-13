import ipdb 

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}

    def backtrack(combinations,digits):
        if (len(digits)==0):
            output.append(combinations)

        else:
            for letter in phone[digits[0]]:
                backtrack(combinations + letter,digits[1:])

    output = []
    if digits:
        backtrack("",digits)
    
    return output


if __name__=="__main__":
    digits = "23"
    output = letterCombinations(digits)
    print(output)


