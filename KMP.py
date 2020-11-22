def KMPsearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create LPS array to hold longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0 # index for pat[]

    # run preprocessing method to generate LPS array
    computeLPSarray(pat, M, lps)

    i = 0 # index for txt[]
    while i < N and pat[j] != txt[i]:
        if j != 0:
            j = lps[j-1]
        else:
            i += 1


def computeLPSarray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix

    lps[0] # lps[0] is always 0, so start i at 1
    i = 1

    # loop calculates lps[i] for i = 1 to M - 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1
    print(f"LPS array is: {lps}")


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(KMPsearch(pat, txt))