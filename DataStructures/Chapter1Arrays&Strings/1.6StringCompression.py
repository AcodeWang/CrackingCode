# O(n)
# O(n^2) string concatenation without StringBuilder

import unittest


# Bad algorithm
# Because String concatenation is O(n^2) time
# Use StringBuilder to fix the problem

def string_compression_bad(str_test:str):

    s = ""

    count = 1
    for i in range(len(str_test) - 1):
        if str_test[i] == str_test[i+1]:
            count += 1
            continue
        else:
            s += str_test[i] + str(count)
            count = 1

    s += str_test[len(str_test) - 1] + str(count)

    if len(s) < len(str_test):
        return s
    else:
        return str_test


def string_compression(string):

    # list.append StringBuilder in Python
    compressed = []
    counter = 0

    for i in range(1, len(string)):
        counter += 1
        if string[i] != string[i-1]:
            compressed.append(string[i-1] + str(counter))
            counter = 0

    # list[-1] last item in list
    compressed.append(string[-1] + str(counter + 1))

    # Python a ? b : c -> b if a else c
    # list has no len(), use ''.join(list) instead
    return min(string, ''.join(compressed), key=len)
    #return compressed if len(''.join(compressed)) < len(str) else str




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()