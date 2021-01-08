items=[n for n in input("Type the words with hyphen saprated: " ).split('-')]
items.sort()
print('-'.join(items))
