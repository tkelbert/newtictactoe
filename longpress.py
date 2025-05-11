def isLongPressedName(name: str, typed: str) -> bool:
    i = 0
    for j in range(len(typed)):
        if i < len(name) and name[i] == typed[j]:
            i += 1
        elif j == 0 or typed[j] != typed[j - 1]:
            return False
    return i == len(name)

print(isLongPressedName("alex", "aaleex"))  # True
print(isLongPressedName("saeed", "ssaaedd"))  # False
print(isLongPressedName("leelee", "leeeleee"))  # True
print(isLongPressedName("laiden", "laideeeeennn"))  # True
print(isLongPressedName("alex", "aaleexx"))  # False