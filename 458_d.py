import sys
import heapq

input = sys.stdin.readline

x = int(input())
q = int(input())

bigger = []
smaller = []

# 【ポイント】最初の中央値 x も、まずは bigger に入れておきます
heapq.heappush(bigger, x)

dup = {}
result = []

for i in range(q):
    a, b = map(int, input().split())
    
    # 登場した数はすべて dup でカウントし、一旦ヒープに振り分ける
    dup[a] = dup.get(a, 0) + 1
    dup[b] = dup.get(b, 0) + 1
    
    # x を基準に、まずは単純にヒープへ追加する（moveの計算は不要になります！）
    if a >= x: heapq.heappush(bigger, a)
    else:      heapq.heappush(smaller, -a)
        
    if b >= x: heapq.heappush(bigger, b)
    else:      heapq.heappush(smaller, -b)
    
    # 常に「現在の黒板にある総数」から、中央値が位置すべきインデックス（左から数えて何番目か）を計算
    # クエリ i (0始まり) のとき、全体の要素数は 2*i + 3 個になります。
    # その中央値のインデックスは (全体の要素数 // 2) + 1 番目です。
    target_smaller_size = (2 * i + 3) // 2
    
    # 【左右のスライド処理】
    # smaller の有効な要素数が、目標の数になるまで中央値を調整します
    while True:
        # 1. 両方のヒープの先頭にある「すでに消費されたゴミデータ」を掃除する
        while bigger and dup.get(bigger[0], 0) == 0:
            heapq.heappop(bigger)
        while smaller and dup.get(-smaller[0], 0) == 0:
            heapq.heappop(smaller)
            
        # 2. 現時点で、smaller に入っている「本物の要素数」が目標より少ない場合、
        # bigger の一番小さい値を smaller に移す
        if len(smaller) < target_smaller_size:
            # もし、biggerの先頭がゴミなら上で消えているはずですが、
            # 万が一のバグ防止のために再度チェックしてpop
            val = heapq.heappop(bigger)
            heapq.heappush(smaller, -val)
        else:
            break

    # 3. 調整が終わったら、本物のデータが残るまでさらに smaller を掃除
    while smaller and dup.get(-smaller[0], 0) == 0:
        heapq.heappop(smaller)
        
    # smaller の一番大きい値（＝左半分の最大値）が、常に「現在の中央値」になります！
    x = -smaller[0]
    result.append(x)
    
    # 【重要】中央値として1個確定させて出力に回すので、この瞬間だけ dup を1減らす
    # これにより、次のクエリでの「ゴミ掃除」の対象になり、二重カウントを防げます
    dup[x] -= 1

print("\n".join(map(str, result)))