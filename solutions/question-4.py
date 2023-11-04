# Method - 1
boxes = {1:0, 2:0, 3:0, 4:0, 5:0}
coins = input()

for i in range(len(coins)):
    box = (i % 5) + 1
    boxes[box] += int(coins[i])

max = 0
max_box = 0

for box in boxes:
    if boxes[box] > max:
        max = boxes[box]
        max_box = box
        
print(max_box)

# Method - 2
def max_coins(coin_sequence):
  box_coins = [0] * 5
  max_coins = 0
  max_coins_box = 0
  current_box = 0

  for coin in coin_sequence:
    current_coins = int(coin)
    box_coins[current_box] += current_coins

    if box_coins[current_box] > max_coins:
        max_coins = box_coins[current_box]
        max_coins_box = current_box
    elif box_coins[current_box] == max_coins and current_box < max_coins_box:
        max_coins_box = current_box

    current_box = (current_box + 1) % 5

    return max_coins_box + 1