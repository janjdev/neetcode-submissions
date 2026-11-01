class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a signature for each word, store that signature as a key
        # in a dict and the words that match stored in an array that is the value
        ana_group = {}

        for word in strs:
            sig = [0] * 26 #create an array to hold the signature (must be 26 elements because a word could have any of the 26 letter in the alphabet)
            for char in word:
                sig[ord(char) -97] += 1 #gets the letter as an integer representation (0-25, 0=a, 1=b... and increments the frequency of that letter in the array. ie sig[0] is the letter a, sig[0] = 1 means the letter is seen one time in the word and gets 1 in the signature)
            signature = tuple(sig) # converts the signature array of elements to a tuple 
            if signature in ana_group:
                ana_group[signature].append(word)
            else: ana_group[signature] = [word] # creates a key value pair where the tuple(signature) is the key and an array is the value. Any word whose signature matches the key is added to the array value
        return list(ana_group.values())
