for i in range(1, 10, 1):
    for j in range(i):
        print(i, end='')   # 設定end參數讓print()不要換行

    print()   # 每印完一個數字要換行


# =====================
print([str(i) for i in range(4)])