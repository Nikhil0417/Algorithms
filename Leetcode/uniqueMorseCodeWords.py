class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        morsedict = set() #dict()
        for word in words:
            morsecode = ""
            for i in word:
                if i in alphabet:
                    morsecode += alphabet[i]
            morsedict.add(morsecode)
            # if morsecode not in morsedict:
            #     morsedict[morsecode] = 1
            # else:
            #     morsedict[morsecode] += 1
        return len(morsedict)
