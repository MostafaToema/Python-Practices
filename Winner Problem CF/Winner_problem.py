#no of round
n = int(input())
l_winner = []
arr_name = []
index_name = 0

#enter the list of winners (name and score)
for each_list in range(n):
	l_winner.append(input().split())
	if (l_winner[index_name][0]) not in arr_name:
		arr_name.append(l_winner[index_name][0])
	index_name += 1
len_names = len(arr_name)
l_score = []
max_score = 0

#find sum of scores
for each_name in arr_name:
	sum_score = 0
	for	each_round in l_winner:
		if(each_round[0] == each_name):
			sum_score += int(each_round[1])
	l_score.append(sum_score)

#prepare to find the winner and find least of sum = max_score
max_score = max(l_score)
l_least_index = [1001]*len_names
for index_each_score in range(len_names):
	index_round = 0
	sum_score = 0
	if (l_score[index_each_score] == max_score):
		for	each_round in l_winner:
			if(each_round[0] == arr_name[index_each_score]):
				sum_score += int(each_round[1])
				if(sum_score >= max_score):
					l_least_index[index_each_score] = index_round
					break
			index_round += 1

#find the winner and printed
min_least_index = min(l_least_index)
for counter_score_index in range(len_names):
		if (l_score[counter_score_index] == max_score and l_least_index[counter_score_index] == min_least_index):
				print(arr_name[counter_score_index])
				break
