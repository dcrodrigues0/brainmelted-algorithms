#  Leet Code 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        # todo
        


    def getValue(self,symbol: chr) -> int:
        match symbol:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case 'L':
                return 50
            case 'C':
                return 100
            case 'D':
                return 500
            case 'M':
                return 1000