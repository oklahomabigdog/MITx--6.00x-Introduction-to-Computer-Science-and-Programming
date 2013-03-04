def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False
    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False
    # Strings not equal in length can not be semordnilap
    if len(str1) != len(str2):
        return False

    return semordnilap(str1, str2)


def semordnilap(str1, str2):
    count = len(str1)
    string1 = 0
    string2 = -1
    while count > 0:
        if str1[string1] != str2[string2]:
            return False
        else:
            if count == 1:
                count -=1
                return True
            else:
                count -= 1
                string1 += 1
                string2 += -1




print semordnilapWrapper("DOANE", "ENAOD")


