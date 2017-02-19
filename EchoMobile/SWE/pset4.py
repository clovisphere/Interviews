def foo(stock):
	best_day_to_buy = stock.index(min(stock))
	# to get the best day to sell, we need to count days
	# from the day we purchased a stock
	temp = stock[best_day_to_buy:]
	best_day_to_sell = stock.index(max(temp))
	# add 1 to each day since lists are 0-based
	return [best_day_to_buy + 1, best_day_to_sell + 1]

# for testing purposes
if __name__ == '__main__':
	P = [30, 20, 10, 15, 17, 25, 20, 23]
	days = foo(P)
	print('(B) - {}\n(S) - {}'.format(days[0], days[1]))