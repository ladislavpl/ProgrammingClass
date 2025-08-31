rightanswers = ["matka", "otec", "babicka"]
answers = ["MAtka", "Otec", "Babick"]
count = 0

for i in range(len(rightanswers)):
    if rightanswers[i] == answers[i].lower().strip():
        count += 1

print(f"""Spravne je {count} z {len(rightanswers)}
      Uspesnost: {round(count / (len(rightanswers) / 100), 1)}%""")
