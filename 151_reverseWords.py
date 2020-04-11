
def reverseWords(s):
    s_list = s.split(' ')
    rs = ''
    for i in range(len(s_list)):
        if s_list[-i-1]!='':
            rs = rs + s_list[-i-1] + ' '
    return rs.strip()

if __name__=="__main__":
    aString = "the sky is blue"
    print(reverseWords(aString))
