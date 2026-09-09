# First Non-Repeating Character – Code Explanation
def non_repeating_character(S):
    n = len(S)
     
    for i in range(n):
          found = False

          for j in range(n):
                if i != j and S[i] == S[j]:
                       found = True
                       break

          if not found:              
               return S[i]

                
    return "No non-repeating character found"

print("Enter a string:")
S = input()

print("The first non-repeating character is:", non_repeating_character(S))

print("Enter a string:")
S = input()

print("The first non-repeating character is:", non_repeating_character(S))

print("Enter a string:")
S = input()

print("The first non-repeating character is:", non_repeating_character(S))






