def palindrom_1(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 * (i + 1)]:
            return False
    else:
        return True


print(palindrom_1("수박이박수"))
print(palindrom_1("박수박수"))
print(palindrom_1('다시합창합시다'))

