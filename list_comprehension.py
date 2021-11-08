scores = []
count = 0

entry = input(" Enter a number of scores: ")
print("Entering", entry, "scores.")

for i in range(0, int(entry)):
    score = int(input(" Enter a score: " ))
    scores.append(score)
    count = count + score
print("Scores entered: ")

print(scores)
original = scores.copy()
average = float(count)/int (entry)
print("Average Score: %.2f " % average)
    
scores.sort()
print("Score from lowest to highest: ")
print(scores)

scores.reverse()
print("Score from highest to lowest: ")
print(scores)

highest = scores[0]
lowest = scores[-1]

lowIndex = original.index(lowest)
highIndex = original.index(highest)


print("Lowest score: " + str(lowest))
print(str(lowest) + " appears in the list at index " + str(lowIndex))
print("Highest score: " + str(highest))
print(str(highest) + " appears in the list at index " + str(highIndex))

remove_scores = scores.copy()


print("List with low score removed: ")
low = [score for score in remove_scores if score != lowest]
print(low)

print("List with high score removed: ")
high = [score for score in remove_scores if score != highest]
print(high)

print("List with low and high score removed: ")
both = [score for score in remove_scores if score != lowest and score != highest]
print(both)