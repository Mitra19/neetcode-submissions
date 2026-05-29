class Solution:
    def reverseBits(self, n: int) -> int:
        n_in_bits = format(n,"b")
        
        len_n = len(n_in_bits)
        n_in_bits = "0"*(32-len_n)+n_in_bits
        
        return int(n_in_bits[::-1],2) 