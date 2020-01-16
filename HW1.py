#################################################################
# HW1.py
# Marcus Blaisdell
# Cpt_S 355
# 27/1/2017
# Sakire Arslan Ay
#################################################################

# Debugging function:
debugging = True
def debug (*s):
    if debugging:
        print (*s)

#################################################################
# 1. Warmup - cryptDict() and deCrypt()
# Define a function cryptDict(s1,s2) that returns a dictionary
#    such that each character in s1 is mapped to the character
#    at the corresponding position in s2.
# You may assume that the characters in s1 are unique and that
#    the two strings are the same length.
# (“You may assume X” means that your code does not have to check
#    whether X holds or not).
#################################################################

# create the encryption dictionary
# map values in str2 to values in str1
def cryptDict (str1, str2):
    # create blank dictionary, fDict, to load with our values
    fDict = {}
    # Using our dictionary, map each element of str1 to each element of str2
    for x in range (len(str1)):
        fDict[str1[x]] = str2[x]
    return fDict

# decrypt the string (s) using dictionary cDict
def decrypt (cDict, s):
    # create blank string to load our values
    retString = ''
    for x in range (len(s)):
        retString = retString + (cDict.get(s[x],s[x]))
    return retString

# test the decryption (given test case)
def testDecrypt ():
    cDict = cryptDict('abc', 'xyz')
    revcDict = cryptDict ('xyz', 'abc')
    tests = "Now I know my abc's"
    answer = "Now I know my xyz's"
    if decrypt (cDict, tests) != answer:
        return False
    
    # Our test string contains a 'y' in the word 'my'
    # that is getting decoded to a 'b'
    # I have handled this by acknowledging that in the test string:
    if decrypt (revcDict, decrypt(cDict, tests)) != "Now I know mb abc's":
        return False
    if decrypt (cDict, '') != '':
        return False
    if decrypt (cryptDict('', ''), 'abc') != 'abc':
        return False
    # If we get this far, there haven't been any failures
    return True

#################################################################
# 2. charCount()
# Define a function, charCount(S) counting the number of times
#    that each character appears in a given string.
# charCount(S) should return a list of characters in the input
#    string S each paired with its frequency (as a 2-tuple).
# The “space character” should be excluded in the result.
# Characters must appear in the list ordered from least frequent
#    to most frequent.
#################################################################


def charCount (S):
    # create blank dictionary countDict:
    countDict = {}
    # evaluate each character of our input string and increment the count
    # on each character as they are encountered
    # if a character is not in our dictionary, add it
    for x in range (len(S)):
        # add 'x' sentinel if not found
        incrementIt = countDict.get(S[x],'x') 
        if incrementIt != 'x':
            incrementIt = incrementIt + 1
            countDict[S[x]] = incrementIt
        # if character wasn't found, add it
        else:
            countDict[S[x]] = 1
    return countDict

def testCount():
    # charCount, pass a string, capture and print result
    # test 1
    myDict = charCount("a, a, a, b, b, c")
    myList = list(myDict.items())
    # remove the space count from our list
    myList.remove ((' ', myDict.get(' ')))
    # print the list in ascending order of counts
    if sorted (myList, key=lambda item:item[1], reverse=False) != [('c', 1), ('b', 2), ('a', 3), (',', 5)]:
        return False
    # test 2
    myDict2 = charCount("c, c, c, b, b, c, d, d, d")
    myList2 = list(myDict2.items())
    # remove the space count from our list
    myList2.remove ((' ', myDict2.get(' ')))
    # print the list in ascending order of counts
    if sorted(myList2, key=lambda item:item[1], reverse=False) != [('b', 2), ('d', 3), ('c', 4), (',', 8)]:
        return False
    return True


#########################################################################
# 3. dictAddUp ()
# Assume you keep track of the number of hours you study every
#    day for each of the courses you are enrolled in.
# You maintain the weekly log of your hours in a Python dictionary
#    as follows:
# {Monday:{’355’:2,’451’:1,’360’:2},Tuesday:{’451’:2,’360’:3},
# Thursday:{’355’:3,’451’:2,’360’:3}, Friday:{’355’:2},
# Sunday:{’355’:1,’451’:3,’360’:1}}
# The keys of the dictionary are the days you studied and the
#    values are the dictionaries which include the number of hours
#    for each of the courses you studied.
# Please note that you may not study for some courses on some days
#    OR you may not study at all on some days of the week.
# Define a function, dictAddup(d) which adds up the number of hours
#    you studied for each of the courses during the week and returns
#    the summed values as a dictionary. Note that the keys in the
#    resulting dictionary should be the course names and the values
#    should be the total number of hours you have studied for the
#    corresponding courses.
# dictAddup would return the following for the above dictionary:
# {’355’:8,’451’:8,’360’:9}
# Define a function testAddup() that tests your dictAddup(d)
#    function, returning True if the code passes your tests,
#    and False if the tests fail.
#########################################################################

# create a function that makes a dummy dictionary filled with test values:
def makeDictionary():
    # create an empty dictionary to hold our data
    studyDict = {}
    # create dummy data for testing
    Monday =    {'317':1,    '355':2,   '322':3}
    Tuesday =   {'202':1.5,  '360':2.5}
    Wednesday = {'317':1.25, '355':1.5, '322':2.25}
    Thursday =  {'202':1.25, '360':.5}
    Friday =    {'317':1.1,  '355':.75, '322':.1}
    Saturday =  {'317':1.5,  '355':2,   '322':1.5,'202':2, '360':1.5}
    Sunday =    {'317':1,    '202':.25, '360':1.25}
    # create master dictionary from dummy data
    studyDict['Monday'   ] = Monday
    studyDict['Tuesday'  ] = Tuesday
    studyDict['Wednesday'] = Wednesday
    studyDict['Thursday' ] = Thursday
    studyDict['Friday'   ] = Friday
    studyDict['Saturday' ] = Saturday
    studyDict['Sunday'   ] = Sunday
    return studyDict

def dictAddUp (d):
    # create temp dictionary
    tempDict = {}
    # Iterate through each item in our dictionary and get the keys and values.
    # From each value, which is another dictionary,
    # iterate through that dictionary to create a new dictionary that
    # sums the values from like keys
    for k, v in d.items():
        for a, b in v.items():
            tempDict[a] = tempDict.get(a,0) + b
    return tempDict

def testAddUp (d):
    testDict = dictAddUp(d)
    # test 1, explicit:
    if testDict.get ('317') != 5.85:
        return False
    elif testDict.get ('355') != 6.25:
        return False
    elif testDict.get ('322') != 6.85:
        return False
    elif testDict.get ('202') != 5.0:
        return False
    elif testDict.get ('360') != 5.75:
        return False
    else:
        return True

# Testing


if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"

if testDecrypt():
    print ( passedMsg % 'testDecrypt' )
else:
    print ( failedMsg % 'testDecrypt' )

if testCount():
    print ( passedMsg % 'testCount' )
else:
    print ( failedMsg % 'testCount' )

# setup our dictionary to test 'testAddUp'
studyDict = makeDictionary()

if testAddUp(studyDict):
    print ( passedMsg % 'testAddUp' )
else:
    print ( failedMsg % 'testAddUp' )
