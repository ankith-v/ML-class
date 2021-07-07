from textblob import TextBlob


words = ["Machne", "Learnin", "Deta"]

corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i)) 

print(corrected_words)
print("All words :", words)



print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")

