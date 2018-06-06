# String problem sometimes is easier from end to begin

# two-scan approach

# Python list to string ''.join(list1)

import unittest


def urlify(str, trueLength):

    spaceCount = 0

    for i in range(trueLength):
        if str[i] == ' ':
            spaceCount += 1

    outputLength = trueLength + spaceCount * 2

    newStr = ['' for _ in range(outputLength)]

    offset = 0

    for i in range(trueLength):
        if str[i] != ' ':
            newStr[i + offset] = str[i]
        else:
            newStr[i + offset] = '%'
            newStr[i + offset + 1] = '2'
            newStr[i + offset + 2] = '0'
            offset += 2
    return ''.join(newStr)


class Test(unittest.TestCase):
    data = [
        # (list('much ado about nothing      '), 22,
        #  list('much%20ado%20about%20nothing')),
        ("Mr John Smith    ", 13, "Mr%20John%20Smith")]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
