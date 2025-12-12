def largest_increasing_subsequence(arr):
    n = len(arr)
    best_seq = []


    def backtrack(start_idx, current_seq, last_val):
        nonlocal best_seq


        if len(current_seq) > len(best_seq):
            best_seq = current_seq.copy()


        for i in range(start_idx, n):
            if arr[i] > last_val:
                current_seq.append(arr[i])
                backtrack(i + 1, current_seq, arr[i])
                current_seq.pop()


    backtrack(0, [], float("-inf"))
    return best_seq




if __name__ == "__main__":
    data = list(map(int, input("Masukkan deret bilangan (pisah spasi): ").split()))


    lmis = largest_increasing_subsequence(data)
    print("Deret awal        :", data)
    print("Subsequence naik terpanjang:", lmis)
    print("Panjang           :", len(lmis))
