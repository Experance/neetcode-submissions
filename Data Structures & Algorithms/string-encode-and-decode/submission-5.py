class Solution:

    def encode(self, strs: List[str]) -> str:
        # separate each individual list with the num of chars that string is
        if len(strs) == 0:
            return ""


        encoded = "" + str(len(strs)) + "#"
        
        for i, s in enumerate(strs):
            encoded = encoded + str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        decoded = []

        index_of_pound = s.find("#")  # find first instance of #
        num_of_strings = int(s[0:index_of_pound])
        s = s[index_of_pound + 1:]
        
        for i in range(num_of_strings):
            # from start of first string (skipping the num) to the end of string amount
            index_of_pound = s.find("#")
            str_length = int(s[0:s.find("#")])
            decoded.append(s[index_of_pound + 1:index_of_pound + 1 + str_length])
            s = s[index_of_pound + 1 + str_length:] # adjust the string

        return decoded
        