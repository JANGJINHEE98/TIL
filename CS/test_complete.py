# case1

# import copy
# def solution(participant, completion):
#     cnt = copy.deepcopy(participant)
#     for person in cnt:
#         if person in completion: # 완주 했을 경우 
#             completion.remove(person)
#             participant.remove(person)
#     return participant[0]

# case2

def solution(participant, completion): 
    hashDict = {} 
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    for comp in completion:
        sumHash -= hash(comp)

    return hashDict[sumHash]



print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))

