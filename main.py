train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]
def count_moods(data):
  h=0
  s=0
  for i in data:
    if i[1]=="Happy":
      h+=1
    else:
      s+=1
  return h,s
print(count_moods(train_data))
happy_words=["full","won","surprise","tasty","excited","selected","learned","favourite","finally","great"]
sad_words=["lost","failed","moving","another ","cancelled","missed","upset","stopped","lonely"]
def guess_mood(sentence):
  sentence=sentence.lower()
  word=sentence.split()
  h=0
  for w in word:
    w=w.strip(".?!@,;:")
    if w in happy_words:
      return "Happy"
    elif w in sad_words:
      return "Sad"
for sentence,j  in train_data:
  print(sentence," - ",guess_mood(sentence))
practice_data = [ ("I won a medal in the sports meet", "Happy"),
                 ("I lost my notebook before the exam", "Sad"), 
                 ("My friends gave me a lovely surprise", "Happy"),
                 ("The train was late and I felt upset", "Sad"), 
                 ("Today was a great day","Happy")]
f=0
for sentence,g in practice_data:
  p=guess_mood(sentence)
  print(sentence," - ",p)
  if p==g:
    f+=1
accuracy=(f/len(practice_data))*100
print(accuracy,"%")
   
    
      
    
  
