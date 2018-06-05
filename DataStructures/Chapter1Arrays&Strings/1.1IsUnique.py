#O(n)

# If its ASCII or Unicode ?

#ASCII has 128 characters
#extended ASCII (EASCII) has 256 characters

import unittest

def isUnique(str):
    if str.__len__() > 128:
        return False

    char_set = [False for _ in range(128)]

    for c in str:
        if char_set[ord(c)]:
            return False
        else:
            char_set[ord(c)] = True

    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_isUnique(self):
        for test_string in self.dataT:
            result = isUnique(test_string)
            self.assertTrue(result)

        for test_string in self.dataF:
            result = isUnique(test_string)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()