import random
import string
import time

colorString = '\033['+str(32)+'m'

width = 194

previousRow = [' ']*width


def get_random_unicode(length):

    try:
        get_char = unichr
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        (0x0021, 0x0021),
        (0x0023, 0x0026),
        (0x0028, 0x007E),
        (0x00A1, 0x00AC),
        (0x00AE, 0x00FF),
        (0x0100, 0x017F),
        (0x0180, 0x024F),
        (0x2C60, 0x2C7F),
        (0x16A0, 0x16F0),
        (0x0370, 0x0377),
        (0x037A, 0x037E),
        (0x0384, 0x038A),
        (0x038C, 0x038C),
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
        for code_point in range(current_range[0], current_range[1] + 1)
    ]
    return ''.join(random.choice(alphabet) for i in range(length))


while True:
    text = ""

    for i in range(width):
        if previousRow[i] == ' ':
            skip = random.randint(0, 50)
        else:
            skip = random.randint(0, 7) == False

        if not skip:
            # randomChar = (random.choice(string.ascii_uppercase +
            #                            string.digits) for _ in range(1))

            randomChar = get_random_unicode(1)

            text += ''.join(randomChar)
            previousRow[i] = randomChar
        else:
            text += ' '
            previousRow[i] = ' '

    time.sleep(0.03)
    print(colorString + text)
