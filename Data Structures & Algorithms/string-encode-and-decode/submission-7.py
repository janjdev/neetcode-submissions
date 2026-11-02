class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        Input: list of strings
        Output: string
        Edge case: list is empty, list has empyt strings
        Plan: let -1 as a string represent an empty list,
            join words using the "|" as a delimiter
            let a single ',' represent an empty string -> 97|,|98 -> ["a", "", "b"]
            Iterate over the list, for each word, iterate over each letter
            convert each letter to its ASCII
        '''
        code = ""
        for index in range(len(strs)):
            if strs[index] == "":
                code += ',' 
            for char_idx, char in enumerate(strs[index]):
                if char == "":
                    code += ','
                else:
                    code += str(ord(char))
                if char_idx < len(strs[index]) -1:
                    code += '-'
            if index < len(strs) -1:
                code += '|'
        print(code)
        return code

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        code = s.split('|')
        letter = ""
        decode = []
        for string in code:
            word = ""
            for index, char in enumerate(string):
                if char != "-" and char != ',':
                    letter += char
                else:
                    if letter.isdecimal():
                        word += chr(int(letter))
                        letter = ""
                if index == len(string) - 1 and letter.isdecimal():
                    word += chr(int(letter))
                    letter = ""
            decode.append(word)
        print(s)
        return decode        
        


