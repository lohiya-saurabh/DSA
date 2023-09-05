def last_word_len(A):

    # @param A : string
    # @return an integer
    vecs = A.split(" ")[::-1]
    for vec in vecs:
        if len(vec):
            return len(vec)
    return 0


print(last_word_len("   "))
