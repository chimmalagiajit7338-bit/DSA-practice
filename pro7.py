def min_window(s, p):
    # Step 1: store frequency of characters in p
    need = {}
    for ch in p:
        if ch in need:
            need[ch] += 1
        else:
            need[ch] = 1

    window = {}   # current window character count
    left = 0
    matched = 0   # how many characters matched
    min_len = float('inf')
    result = ""

    # Step 2: expand window using right pointer
    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        # check if this character satisfies need
        if ch in need and window[ch] <= need[ch]:
            matched += 1

        # Step 3: shrink window when all characters matched
        while matched == len(p):
            # update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right+1]

            # remove left character
            left_char = s[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                matched -= 1

            left += 1

    return result
print(min_window("timetopractice", "toc"))  # toprac
print(min_window("zoomlazapzo", "oza"))     # apzo