#This program counts each character
import pprint
message  = "It's a wondeeeeeeeeeeeeeerful day."
counter = {}
for i in message:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1
pprint.pprint(counter)
nums = list(counter.values())
nums.sort()
for name, freq in counter.items():
    if freq == nums[-1]:
        print("maximum:"+ name)
