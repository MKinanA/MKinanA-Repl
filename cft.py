"""                  Characters from Text                      
                       module by MKinanA
    chars:
        length(text): returns value of len(text)
        array(text): returns a list of every character in text
        dict(text): returns a dictionary of every character in text
        replace(text,tobereplaced, toreplace): returns a result of text with characters that match tobereplaced replaced with character from toreplace (multiple characters supported, characters in tobereplaced will be replaced with characters in toreplace in the same order)
        delete(text,todelete): returns a result of text with characters that match todelete removed (multiple characters supported)
        deldupes(text): returns a result of text with no 2 same characters in a row (text="abccdeefg", result="abcdefg")
        reverse(text): returns a result of text reversed (text="abc", result="cba")
        randomize(length,chartype): returns a text of randomized characters with length of length and characters of chartype (letters/number/mix)
        check: (result=True/False)
            ifcontains(text,tocheck): returns a result of test if text contains characters that match tocheck (multiple characters supported)
            ifstr(text): returns a result of test if text (must be str) contains another str (quotation marks)
            ifint(text): returns a result of test if text only contains int
    code:
        en(text): returns a code of encoded text
        de(text): returns a text of decoded text
    convert:
        dict:
            toarray(ledict): returns a list from converted ledict
            toarrayold(ledict): old version of toarray (Doesn't support '{}' in dict or dict in dict)
        array:
            totext(array): returns a result of text from converted array
            todict(array): returns a dictionary from converted array
            reverse: returns a list of reversed array
    about:
        credits(): returns "Characters from Text, a module by MKinanA"
"""

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
alphabetarray = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ',0,1,2,3,4,5,6,7,8,9,'.','?','!',',','(',')']
alphabetdict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'A', 28: 'B', 29: 'C', 30: 'D', 31: 'E', 32: 'F', 33: 'G', 34: 'H', 35: 'I', 36: 'J', 37: 'K', 38: 'L', 39: 'M', 40: 'N', 41: 'O', 42: 'P', 43: 'Q', 44: 'R', 45: 'S', 46: 'T', 47: 'U', 48: 'V', 49: 'W', 50: 'X', 51: 'Y', 52: 'Z', 53: ' ', 54: 0, 55: 1, 56: 2, 57: 3, 58: 4, 59: 5, 60: 6, 61: 7, 62: 8, 63: 9, 64: '.', 65: '?', 66: '!', 67: ',', 68: '(', 69: ')'}
alphabetdictrev = {'a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05', 'f': '06', 'g': '07', 'h': '08', 'i': '09', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26', 'A': '27', 'B': '28', 'C': '29', 'D': '30', 'E': '31', 'F': '32', 'G': '33', 'H': '34', 'I': '35', 'J': '36', 'K': '37', 'L': '38', 'M': '39', 'N': '40', 'O': '41', 'P': '42', 'Q': '43', 'R': '44', 'S': '45', 'T': '46', 'U': '47', 'V': '48', 'W': '49', 'X': '50', 'Y': '51', 'Z': '52', ' ': '53', 0: '54', 1: '55', 2: '56', 3: '57', 4: '58', 5: '59', 6: '60', 7: '61', 8: '62', 9: '63', '.': '64', '?': '65', '!': '66', ',': '67', '(': '68', ')': '69'}
alphabetarraycut = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',0,1,2,3,4,5,6,7,8,9]
onlyalphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
onlyalphabetup = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
onlynumbers = [0,1,2,3,4,5,6,7,8,9]

"""def e(ledict):
    dictalph = {}
    for x in range(len(ledict)) :
        print("x = " + str(x + 1))
        print("ledict[x + 1] = " + str(ledict[x + 1]))
        dictalph[ledict[x + 1]] = str(x + 1)
    return dictalph"""

def nothing(): pass

class chars :
    
    def length(text) :
        return str(len(text))
    
    def array(text) :
        result = []
        for char in text :
            result.append(char)
        return result

    def arraynum(start, end) :
        result = []
        isint = True
        try:
            int(start)
            int(end)
        except: isint = False
        if not isint: raise Exception("both arguments (start, end) must be int")
        for x in range(start, end):
            result.append(x)
        result.append(end)
        return result
    
    def dict(text) :
        result = {}
        for textlen in range(len(text)) : result["Character " + str(textlen + 1)] = text[textlen]
        return result
    
    def replace(text, tobereplaced, toreplace) :
        result = ""
        if len(tobereplaced) != len(toreplace) : raise Exception("tobereplaced (second argument) and toreplace (third argument) must have the same length")
        for char in text :
            for toreplen in range(len(tobereplaced)) :
                if char == tobereplaced[toreplen] :
                    char = toreplace[toreplen]
                    break
            result = str(result) + str(char)
        return result
    
    def delete(text, todelete) :
        result = ""
        for char in text :
            for todellen in range(len(todelete)) :
                if char == todelete[todellen] :
                    char = ""
                    break
            result = str(result) + str(char)
        return result

    def deldupes(text) :
        result = ""
        prevchar = ""
        for char in text :
            if not char == prevchar : result = result + str(char)
            prevchar = char
        return result

    """def dellinecontchar(text) :
        result = ""
        lechar = "\\"
        for char in text :
            if not char == lechar[0:1] : result = result + char
        return result"""

    def reverse(text) :
        result = ""
        for charlen in range(len(text)) : result = result + str(text[len(text) - (1 + charlen)])
        return result

    def randomize(length, chartype) :
        result = ""
        if not isinstance(length, int) : raise Exception("length (first argument) must be integer")
        if chartype == "mix" :
            for reslen in range(length) : result = result + random.choice(alphabet+numbers)
        elif chartype == "alphabet" or chartype == "letters" :
            for reslen in range(length) : result = result + random.choice(alphabet)
        elif chartype == "number" :
            for reslen in range(length) : result = result + random.choice(numbers)
        else : raise Exception("Invalid chartype (second argument) value")
        return result

    def fillen(text, tofillwith=" ", length=16, cut=True) :
        modtext = str(text)
        if cut:
            if len(str(text)) > int(length):
                modtext = str(text)[0:int(length)]
        return str(modtext) + (tofillwith*(length-len(str(modtext))))

    class check :

        def ifcontains(text, tocheck) :
            result = ""
            for textlen in range(len(str(text))) :
                for checklen in range(len(tocheck)) :
                    if str(text)[textlen] == tocheck[checklen] : return True
            return False

        def ifstr(text) :
            result = ""
            if not isinstance(text, str) : raise Exception("argument must be str, function will check if it contains another str (quotation marks)")
            checkpass = 0
            if text[0] == "'" or text[0] == '"' : checkpass = checkpass + 1
            if text[len(text)-1] == "'" or text[len(text)-1] == '"' : checkpass = checkpass + 1
            if checkpass == 2 : return True
            else : return False

        def ifint(text) :
            result = ""
            if not isinstance(text, str) : raise Exception("argument must be str, function will check if it only contains int")
            checkpass = 0
            checkpass2 = 0
            if not text[0] == "'" and not text[0] == '"' and not text[0] == "{" and not text[0] == "[" and not text[0] == "<" : checkpass = checkpass + 1
            if not text[len(text)-1] == "'" and not text[len(text)-1] == '"' and not text[len(text)-1] == "{" and not text[len(text)-1] == "[" and not text[len(text)-1] == "<" : checkpass = checkpass + 1
            for textlen in range(len(onlyalphabet + onlyalphabetup)) :
                if chars.check.ifcontains(text, onlyalphabet + onlyalphabetup) : checkpass2 = checkpass2 + 1
                if checkpass2 >= 1 : break
            try : int(text)
            except ValueError : checkpass2 = checkpass2 + 1
            if not checkpass2 >= 1 : checkpass = checkpass + 1
            if checkpass == 3 : return True
            else : return False

class code :

    def en(text) :
        result = ""
        for textlen in range(len(text)) :
            if text[textlen] in alphabetdictrev : result = result + str(alphabetdictrev[text[textlen]])
            else : raise Exception("Unsupported character: '" + str(text[textlen]) + "'")
        return result

    def de(text) :
        result = ""
        valueerror = False
        try : int(text)
        except ValueError : valueerror = True
        if valueerror : raise Exception("argument must be int")
        if isinstance(int(text), int) :
            text = str(text)
            if (len(text) % 2) == 0 :
                for codelen in range(len(text) // 2) : result = result + str(alphabetdict[int(text[(len(result)+codelen):(len(result)+codelen+2)])])
            else : raise Exception("text length is odd")
        else : raise Exception("text is not an integer")
        return result

class convert :

    class dict :

        """def toarray(ledict) :
            result = []
            resultword = []
            resultwordbreak = 0
            if not isinstance(ledict, dict) : raise Exception("argument must be dict")
            for num in range(len(str(ledict))) :
                print(str(ledict)[num])
                if str(ledict)[num] == "," or str(ledict)[num] == "}" :
                    for minnum in range(num) :
                        if not resultwordbreak == 2 :
                            if str(ledict)[num-(minnum+1)] == "'" : resultwordbreak = resultwordbreak + 1
                            else : resultword.append(str(ledict)[num-(minnum+1)])
                        else : break
                    result.append(convert.array.totext(convert.array.reverse(resultword)))
            return result"""#unsuccessful

        """def toarray(ledict) :
            result = []
            resultword = []
            resultwordstart = 0
            resultwordbreak = 0
            if not isinstance(ledict, dict) : raise Exception("argument must be dict")
            print(str(ledict))
            for num in range(len(str(ledict))) :
                print(str(ledict)[num])
                if resultwordstart == 1 :
                    for resultwordnum in range(len(str(ledict))-num) :
                        resultword.append(str(ledict)[resultwordnum])
                        if str(ledict)[resultwordnum] == "'" : 
                            resultwordbreak = resultwordbreak + 1
                            if resultwordbreak == 2 :
                                resultwordbreak = 0
                                resultwordstart = 0
                                print("resultwordbreak (2') at num = "+str(num + resultwordnum))
                                num = num + resultwordnum
                                break
                    result.append(convert.array.totext(resultword))
                if str(ledict)[num:num+1] == ":" :
                    print("resultwordstart (:) at num = "+str(num))
                    resultwordstart = 1
            return result"""#unsuccessful

        def toarray(ledict) :
            result = []
            resultword = []
            resultwordstart = 0
            resultwordbreak = 0
            if not isinstance(ledict, dict) : raise Exception("argument must be dict")
            if chars.check.ifcontains(str(ledict)[1:len(str(ledict))-1], "{}") : raise Exception("Doesn't support '{}' in dict or dict in dict")
            for num in range(len(str(ledict))) :
                if resultwordstart == 2 :
                    if str(ledict)[num:num+1] == "," or str(ledict)[num:num+1] == "}" : resultwordbreak = resultwordbreak + 1
                    else : resultword.append(str(ledict)[num])
                    if resultwordbreak == 1 :
                        resultword = convert.array.totext(resultword)
                        if chars.check.ifstr(resultword) : resultword = resultword[1:len(resultword)-1]
                        elif chars.check.ifint(resultword) : resultword = int(resultword)
                        result.append(resultword)
                        resultwordstart = 0
                        resultwordbreak = 0
                        resultword = []
                if resultwordstart == 1 : resultwordstart = resultwordstart + 1
                if str(ledict)[num:num+1] == ":" :
                    resultwordstart = 1
            return result

    class array :

        def totext(array) :
            result = ""
            for num in range(len(array)) : result = str(result) + str(array[num])
            return result

        def todict(array) :
            result = {}
            if not isinstance(array, list) : raise Exception("argument must be list (/ array)")
            for num in range(len(array)) : result[int(num + 1)] = array[num]
            return result

        def reverse(array) :
            result = []
            if not isinstance(array, list) : raise Exception("argument must be list (/ array)")
            for num in range(len(array)) : result.append(array[(len(array)-num)-1])
            return result

class about :
    
    def credits() :
        return "Characters from Text, a module by MKinanA"

if __name__ == "__main__" :
    print("Characters from Text, a module by MKinanA")
    
    #for cft.mkinana.repl.co, do not call this function
    def runwebapp():
        try:
            import webapp
            webapp.runapp()
        except:
            pass
   