def lca(A, B, C):
    if (A.val > B and A.val > C):
        return lca(A.left, B, C)

    if (A.val < B and A.val < C):
        return lca(A.right, B, C)

    return A.val
