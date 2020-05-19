def minKBitFlips(A, K):
    N = len(A)
    hint = [0] * N
    ans = flip = 0

    # When we flip a subarray like A[i], A[i+1], ..., A[i+K-1]
    # we can instead flip our current writing state, and put a hint at
    # position i+K to flip back our writing state.
    for i, x in enumerate(A):
        flip ^= hint[i]
        if x ^ flip == 0:  # If we must flip the subarray starting here...
            ans += 1  # We're flipping the subarray from A[i] to A[i+K-1]
            if i+K > N:
                return -1  # If we can't flip the entire subarray, its impossible
            flip ^= 1
            if i+K < N:
                hint[i + K] ^= 1

    return ans


a = [0, 0, 0, 0]
k = 3
print(minKBitFlips(a, k))
