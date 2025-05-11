'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order'''
nums = [12, 2, 4, 2 ,3,1,20, 40, 51,  9]
target = 13
'''nums = [3,3]
target = 6'''
dict1 = dict()
i = 0
for num in nums:
    dict1[i] = num
    i += 1

for key in dict1:
    print(f"{key}",end='')
    print(f" :{dict1[key]}")
odict = dict()
alldict = dict()
allsum = dict()
for key in dict1:

    print(f"key: {key} : dict1[key]:{dict1[key]}")
    new = target - dict1[key]
    
    if new in odict.values():
        print("success")
        print(f"{new}:new | nums: {nums} | target: {target} | dict[key]: {dict1[key]}")
        answer = [new, dict1[key]]
        print(answer)
        print(f"{new} + {dict1[key]} = {target}")
        allsum[new] = dict1[key]
        for keys in dict1:
            if new == dict1[keys] and new + dict1[key] == target and new != keys:
                print(f"{keys}::{new}")
                print(f"{keys}:{key}")
                answer = [keys, key]
                print(answer)
                print('the answer is tis bro, right above here')
                if keys in odict:
                    print('hello')
                    print(f"keys : {keys}")
                    print(f"key : {key}")
                    answer2 = [keys, key]
                    print(f"this is the real answer right here! {answer2}")
                    alldict[keys] = key

    odict[key] = dict1[key]
    print('adding to second search dictionary....')
    print(odict)
    print(alldict)
    print(allsum)
    for key in allsum:
        print(f"{key} + {allsum[key]} = {target}")
