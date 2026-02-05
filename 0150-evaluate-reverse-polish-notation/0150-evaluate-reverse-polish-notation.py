class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0 
        first, second = 0, 0 
        cal = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operators:
                cal.append(int(token))
            else:
                second = cal.pop()
                first = cal.pop()
                print(first)
                print(second)
                if token == "+":
                    res = (first + second)
                elif token == "-":
                    res = (first - second)
                    print(res)
                elif token == "*":
                    res = (first * second)
                else:
                    res = int(first / second)
                cal.append(res)
            
        return cal[0]