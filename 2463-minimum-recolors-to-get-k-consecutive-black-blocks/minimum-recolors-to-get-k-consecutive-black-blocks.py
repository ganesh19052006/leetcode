class Solution(object):
    def minimumRecolors(self, blocks, k):
        # Count white blocks in the first window
        white = 0
        for i in range(k):
            if blocks[i] == 'W':
                white += 1

        minimum = white

        # Slide the window
        for i in range(k, len(blocks)):
            # Remove left character
            if blocks[i - k] == 'W':
                white -= 1

            # Add right character
            if blocks[i] == 'W':
                white += 1

            minimum = min(minimum, white)

        return minimum