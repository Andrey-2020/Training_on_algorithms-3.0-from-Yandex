if (__name__ == "__main__"):
    stdin = open("input.txt", "r")
    N = int(stdin.readline().rstrip())
    prices = stdin.readline().rstrip().split(" ")
    stdin.close()
    stack = []
    for i, price_str in enumerate(prices):
        price = int(price_str)
        if (not len(stack)):
            stack.append([i, price])
        elif (len(stack) and price >= stack[-1][1]):
            stack.append([i, price])
        elif (len(stack) and price < stack[-1][1]):
            while len(stack) and price < stack[-1][1]:
                price_end = stack.pop()
                prices[price_end[0]] = str(i)
            stack.append([i, price])
    if (len(stack)):
        for price in stack:
            prices[price[0]] = str(-1)
    print(" ".join(prices))
