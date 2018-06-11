# O(n)
# Boundary of list length 0 and 1, be careful with s[i+1]

import unittest


def one_away(s1, s2):
    if abs(len(s1)-len(s2)) > 1:
        return False

    if len(s1) == 0 or len(s2) == 0:
        return True

    if len(s1) == 1 and len(s2) == 1:
        return True

    i = 0
    j = 0
    if len(s1) > len(s2):
        while i < len(s2):
            if s1[i + j] != s2[i]:
                j += 1
                if not s1[i + j] == s2[i]:
                    return False
            i += 1
        return True
    elif len(s1) < len(s2):
        while i < len(s1):
            if s1[i] != s2[i+j]:
                j += 1
                if not s1[i] == s2[i+j]:
                    return False
            i += 1
        return True
    else:
        diff = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                diff += 1
            i += 1
        if diff > 1:
            return False
        else:
            return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()