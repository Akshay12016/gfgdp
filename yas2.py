def minFlips(s):
     if "0" not in s:      return 0  # all 1s, no flip needed
     if s in ("00","000"): return 1  # last flip for whole string
     
     def flip(n): # flip 1st n bits
          return s[:n].translate({48:49,49:48})+s[n:]
     
     result = [float('inf')] # track minimum flips
     if s.startswith("0"):   # must flip if starting with a zero
         if len(s)>2:        # first 2 + recursion
             result.append(1+minFlips(flip(2)[1:])) 
         if len(s)>3:        # first 3 + recursion
             result.append(1+minFlips(flip(3)[1:])) 
     else: # starts with "1"
         result.append(minFlips(s[1:])) # 0 flip + recursion
         if "0" in s[:2]: # can flip zero at 2nd position
             result.append(1+minFlips(flip(2))) # first 2 + recursion
         if "0" in s[:3]: # can flip zero at 2nd or 3rd position
             result.append(1+minFlips(flip(3))) # first 3 + recursion
     return min(result)

print(minFlips("10"))       # 2
print(minFlips("1111"))      # 1
print(minFlips("1001101"))