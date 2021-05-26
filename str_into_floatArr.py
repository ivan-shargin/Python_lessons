def str_into_floatArr(s, size):
    """ Function splits and turns string 's' into array of floats.

        The number of floats is limited by the argument 'size'.
        It only ingnores spaces and '\n' at the end of string, so
        if there are another symbols except spaces and decimals,
        it will throw exception.
        Returns the array of floats.
    """

    floatArr = [0] * size

    for i in range(size):
        #strips spaces at the begining of s
        #so the begining of float is s[0]
        s = s.lstrip(' ')
        end_of_float = min(s.find(' '), len(s))
        # if s.find(' ') != -1 and s.find('\n') != -1:
        #     end_of_float = min(s.find(' '), s.find('\n'))
        # elif s.find(' ') == -1 and s.find('\n') != -1:
        #     end_of_float = s.find('\n')
        # elif s.find(' ') != -1 and s.find('\n') == -1:
        #     end_of_float = s.find(' ')
        # else:
        #     print("INCORRECT FORMAT!")
        #     return floatArr

        try:
            floatArr[i] = float(s[0:end_of_float])
        except ValueError:
            print("The format of value: '" + s[0:end_of_float] + "' is incorrect")

        s = s[end_of_float:]

    return floatArr
