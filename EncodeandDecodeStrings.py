"""
271. Encode and Decode Strings - Explanation

Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

vector<string> decode(string s) {
    //... your code
    return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.



Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:

Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);



Example 2:
Input: dummy_input = [""]
Output: [""]



Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
"""


class Solution:
    def encoder(self, listStr):
        res = ''
        for s in listStr:
            res += str(len(s)) + '#' + s
        return res

    def decoder(self, strs):
        res = []
        i = 0

        while i < len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            length = int(strs[i:j])
            i = j + 1
            j = i + length
            res.append(strs[i:j])
            i = j
        
        return res

dummy_input = ["Hello","Worldlylife"]
output = ["Hello","World"]

s = Solution()

en = s.encoder(dummy_input)
de = s.decoder(en)
print(en)
print(de)