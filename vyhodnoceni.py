rightAnswers = ["matka", "otec", "babicka"]
answers = ["MAtka", "Otec", "Babick"]
count = 0

for i in range(len(rightAnswers)):
    if rightAnswers[i] == answers[i].lower().strip():
        count += 1

print(f"Spravne je {count} z {len(rightAnswers)}, uspesnost: {round(count / (len(rightAnswers) / 100), 1)}%")