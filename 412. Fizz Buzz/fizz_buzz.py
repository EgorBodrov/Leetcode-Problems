class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(x) for x in range(1, n+1)]
        for i in range(1, n+1):
            tmp = ''
            if i % 3 == 0:
                tmp += 'Fizz'
            if i % 5 == 0:
                tmp += 'Buzz'
            answer[i - 1] = tmp if tmp != '' else answer[i - 1]
        
        return answer
