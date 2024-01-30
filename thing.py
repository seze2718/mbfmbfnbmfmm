import string

alphabet = tuple(string.ascii_lowercase) 
def checkPos(pos, jump, index, maxBarrier):
    for jumpNode in range(jump):
        if index == 0: pos = True
        if index == maxBarrier: pos = False

        if pos: index += 1
        else: index -= 1
    return index, pos

def shuffleStr(name: str, platform: str) -> tuple:
    count, tailoredStr, pos, plat = len(name), list(name), False, platform.upper()
    for letter, i in tuple(zip(plat, range(len(plat)))):
        tailoredStr.insert(count, letter)
        count += 1
        if i == len(plat) - 1:
            break
        count, pos = checkPos(pos, 2, count, len(tailoredStr))
    return "".join(tailoredStr)[:10], count, pos 

def insertNum(target: str, index: int, sign: bool) -> str:
    count, pos, tailoredStr = index, sign, list(target)
    rfafrm5 = alphabet.index(target[0].lower())+1-alphabet.index(target[0].lower())//5*5
    for num in range(5):
        if num + 1 == rfafrm5: tailoredStr.insert(count, "#")
        else: tailoredStr.insert(count, str(num + 1))
        count += 1
        count, pos = checkPos(pos, rfafrm5, count, len(tailoredStr))
    return "".join(tailoredStr)

shuffled = shuffleStr(input("string1: "),input("string2: "))
print(insertNum(shuffled[0], shuffled[1], shuffled[2]))

#print(shuffleStr(input(), input())[0])
