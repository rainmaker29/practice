
# Asked in hackwithinfy2020

import sys
n = int(sys.argv[1])

if n==3:
    print("B")
else:
    print("A")


# Actual Nim game

# Find the cumulative XOR
# If the XOR comes out 0 then the second player wins
# Otherwise the first one wins

# Also, Nimgame isn't affected if a concept of adding stones/blocks to piles is introduced
# Because, if a player adds X number of stones, the other player nullifies this move by removing those stones
