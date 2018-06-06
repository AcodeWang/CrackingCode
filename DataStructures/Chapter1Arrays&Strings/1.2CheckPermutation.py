# O(n)
# Consider whitespace, case sensitive

import unittest

# in Python collections Counter dose the job
from collections import Counter

def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False

    # counter = Counter()
    #
    # for c in s1:
    #     counter[c] += 1
    #
    # for c in s2:
    #     if counter[c] == 0:
    #         return False
    #     counter[c] -= 1
    #
    # return True
    # #Because the length of strings is the same, no need to check if the counter is all 0

    val_set = [0 for _ in range(128)]

    for c in s1 :
        val_set[ord(c)] += 1

    # We can exit the checking in 2nd for loop
    for c in s2 :
        val_set[ord(c)] -= 1
        if(val_set[ord(c)] < 0):
            return False
    #
    # for val in val_set :
    #     if val != 0 :
    #         return False
    return True

class Test(unittest.TestCase):
    dataT = (
        ('aabcd', 'abacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_checkPermutation(self):
        for test_string in self.dataT:
            result = checkPermutation(*test_string)
            self.assertTrue(result)

        for test_string in self.dataF:

            result = checkPermutation(*test_string)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
