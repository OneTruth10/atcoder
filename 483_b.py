N, Q = map(int, input().split())
K_list = list(map(int, input().split()))

deck = [{"id": i, "face_up": True} for i in range(1, N + 1)]

for k in K_list:
  top_cards = deck[:k]
  top_cards.reverse()
  for card in top_cards:
    card["face_up"] = not card["face_up"]
  deck[:k] = top_cards

for card in deck:
  if card["face_up"]:
    print(card["id"])
  else:
    print(-card["id"])