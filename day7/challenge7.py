import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + "\input.txt"
INPUTS = []
with open(__location__) as raw_input:
    for line in raw_input.read().strip().split("\n"):
        target, input = line.split(":")
        input = input.strip().split(" ")
        input.append(target)
        INPUTS.append(input)
def backtrack(index, curr_value,target,inp):
    if curr_value > target:
        return False
    if index == len(inp) - 1:
        if curr_value == target:
            return True
        return False
    # prt2
    if backtrack(index + 1, int(str(curr_value) + inp[index]),target,inp): return True
    if backtrack(index + 1, curr_value + int(inp[index]), target, inp): return True
    if backtrack(index+1,curr_value * int(inp[index]),target, inp): return True
    return False 
ans = 0
for inp in INPUTS:
    target = int(inp[-1])
    no_of_spaces = len(inp) - 2
    if backtrack(0, 0,target,inp):
        print("yo", target)
        ans += target
print(ans)
        
    