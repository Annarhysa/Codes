MAX, MIN = 1000, -1000
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
	if (depth == 3):
	    return values[nodeIndex]
	
	if maximizingPlayer:
	
		best = MIN

		# Recur for left and right children
		for i in range(0, 2):
			
			val = minimax(depth + 1, nodeIndex * 2 + i,
						False, values, alpha, beta)
			best = max(best, val)
			alpha = max(alpha, best)

			# Alpha Beta Pruning
			if beta <= alpha:
				break
		
		return best
	
	else:
		best = MAX

		# Recur for left and
		# right children
		for i in range(0, 2):
		
			val = minimax(depth + 1, nodeIndex * 2 + i,
							True, values, alpha, beta)
			best = min(best, val)
			beta = min(beta, best)

			# Alpha Beta Pruning
			if beta <= alpha:
				break
		
	return best

if __name__ == "__main__":
	
	arr = []
	n = int(input("Enter how many elements you want:"))
	print ('Enter numbers in array: ')
	for i in range(int(n)):
	    a = input("Num :")
	    arr.append(int(a))

print("The optimal value is :", minimax(0, 0, True, arr, MIN, MAX))
	
