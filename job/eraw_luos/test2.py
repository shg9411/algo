import random
import string


def makeString(length):
    intCount = random.randint(1, length)
    charCount = length-intCount
    text = ''.join(map(str, (random.randint(0, 9) for _ in range(intCount))))

    for _ in range(charCount):
        text += random.choice(string.ascii_letters)

    print(''.join(random.sample(text, len(text))))


makeString(12)
