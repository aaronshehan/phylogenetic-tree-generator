def lcs_length(str1, str2): 
    str1_len = len(str1) 
    str2_len = len(str2) 

    L = [[0] * (str2_len + 1) for _ in range(str1_len + 1)] 
  
    for i in range(str1_len + 1): 
        for j in range(str2_len + 1): 
            L[i][j] = 0 if i==0 or j==0 else(L[i-1][j-1]+1 if str1[i-1]==str2[j-1] else max(L[i-1][j], L[i][j-1]))

    return L[str1_len][str2_len] 

def main():
    b = lcs_length('hxbecqibzpyqhosszypghkdddykjfjcajnwfmtfhqcpavqrtoipocijrmqpgzoufkjkyurczxuhkcpehbhpsuieqgjcepuhbpronmlrcgvipvibhuyqndbjbrrzpqbdegmqgjliclcgahxoouqxqpujsyfwbdthteidvigudsuoznykkzskspjufgkhaxorbrdvgodlb', 'qnnprxqpnafnhekcxljyysobbpyhynvolgtrntqtjpxpchqwgtkpxxvmwwcohxplsailheuzhkbtayvmxnttycdkbdvryjkfhshulptkuarqwuidrnjsydftsyhuueebnrjvkfvhqmyrclehcwethsqzcyfvyohzskvgttggndmdvdgollryqoswviqurrqhiqrqtyrl')
    print(b)
    print(len('hxbbpyhogntqppcqgkxchpsieuhbncvpuqndbjqmclchqyfttdvgoysuhrrl'))
    


if __name__ == "__main__":
    main()
