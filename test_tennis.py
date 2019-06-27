import unittest
from tennis import tennis_score


class TennisTest(unittest.TestCase):
	def assert_tennis_score(self, expected_score, player1_points, player2_points):
		self.assertEqual(expected_score, tennis_score(player1_points, player2_points))
	"""
	#testing with custm assert
	def assert_tennis_score(self, expected_score, player1_points, player2_points):
		self.assertEqual(expected_score, tennis_score(player1_points, player2_points))

	def test_even_scores_early_game(self):
		self.assert_tennis_score('love-All', 0, 0)
		self.assert_tennis_score('fifteen-All', 1, 1)
		self.assert_tennis_score('thirty-All', 2, 2)
		
	def test_uneven_scores_early_game(self):
		self.assert_tennis_score('love-fifteen', 0, 1)
		self.assert_tennis_score('fifteen-love', 1, 0)
		self.assert_tennis_score('love-thirty', 0, 2)
		self.assert_tennis_score('forty-thirty', 3, 2)
	"""
	
	
#test with param data
test_case_data={'even_scores':[('love-All', 0, 0), ('fifteen-All', 1, 1), ('thirty-All', 2, 2)], 
				'uneven_scores_early_game':[('love-fifteen', 0, 1), ('fifteen-love', 1, 0), ('love-thirty', 0, 2), ('forty-thirty', 3, 2)]}
				
def tennis_test_template(*args):
	def temp(self):
		self.assert_tennis_score(*args)
	return temp
	
for behaviour, test_cases in test_case_data.items():
	for tennis_test_case_data in test_cases:
		exp_output, player1_score, player2_score=tennis_test_case_data
		test_name='test_{0}_{1}_{2}'.format(behaviour, player1_score, player2_score)
		tennis_test_case=tennis_test_template(*tennis_test_case_data)
		setattr(TennisTest, test_name, tennis_test_case)


#test
if __name__=='__main__':
	unittest.main() 