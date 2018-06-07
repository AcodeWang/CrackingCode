# O(n)
# ASCII 65:A 90:Z 97:a 122:z

# Python list to string ''.join(list)
# Python if 0 = False

import unittest

def is_palindrome_permutation(string:str):

    lower = string.lower()

    count_odd = 0

    alpha_set = [0 for _ in range(26)]
    for c in lower:
        if ord('a') <= ord(c) <= ord('z'):
            # alpha_set[ord(c) - 97] += 1
            alpha_set[ord(c) - 97] += 1
            if alpha_set[ord(c) - 97] % 2:
                count_odd += 1
            else:
                count_odd -= 1
    if count_odd <= 1:
        return True
    else:
        return False


    # chance = 1
    #
    # for i in alpha_set:
    #     if i % 2 != 0:
    #         chance -= 1
    #
    #     if chance < 0:
    #         return False
    #
    # return True


class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_palindrome(self):
        for [phrase, expected] in self.data:
            result = is_palindrome_permutation(phrase)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()