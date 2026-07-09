class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += (str(len(s)) + "#" + s)

        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            decoded_strs.append(s[j+1:j+1+length])
            i = j + length + 1
            

        return decoded_strs