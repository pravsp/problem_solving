import math

class RevString:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid_point = math.ceil(len(s)/2)
        for i in range(mid_point):
            tmp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = tmp

if __name__ == '__main__':
    srcStr = ["h","e","l","l","o"]
    print(srcStr)
    RevString().reverseString(srcStr)
    print("Reversed sting:",srcStr)
