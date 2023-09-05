def deserialize(A):
    ans = [
        ''.join([i for i in x if not i.isdigit()]) for x in A.split("~")
    ]
    n = len(ans)
    return ans[: n-1]


print(deserialize('tawpyuckm9~szrnndrxk9~vrgwdesum9~vfhsvtmht9~qqcjkaxai9~jyvepbblv9~mmbovpgln9~bbqwypicj9~fsazxkmgx9~'))
