
def small_straight(dice):
	"""
	Score the dice roll.
	Args:
		dice: sorted list of ints indicating the dice rolled
	Returns:
		an int score
		>>>small_straight([1,2,3,4,5])
		15
		>>>small_straight([1,2,3,4,4])
		0
		>>>small_straight({1,2,3,4,5})
		0
	"""
	if dice==[1,2,3,4,5]:
		return sum(dice)
	else:
		return 0