def str_into_floatArr(s, size):
    """ This function splits and turns string 's'
        into array of floats. The number of floats
        is limited by the argument 'size'.
        It only ingnores spaces, if there are another symbols
        except spaces and decimals, it will end with error
        and print about it.
        Returns the array of floats.
    """
    floatArr = [0] * size
    s = s.split(' ')

    """ If there were more that one space in a row in data file,
        then after split there will be some empty elements ''
        in array s.
        For example, the split(' ') for 3 spaces '   ' is ['', '']
        The block below ignores those empty elements ''.
    """
    k = 0
    for i in range(size):
        while s[k] == '':
            k += 1
        else:
            floatArr[i] = float(s[k])

    return floatArr

    # floatArr = [0] * size
    # tack = s.find(' ')
    # floatArr[0] = float(s[0:tack])
    # tack += 1
    # s = s[tack:]


    # for i in range(size):
    #     while s[0] == ' ':
    #         s = s[1:]
    #     else:
    #         s.find

    #         floatArr[i] = float(s[0:tack])
