n = 3
ans = []


def backtrack(s="", left=0, right=0):
    if len(s) == n*2:
        ans.append(s)
    else:
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)

