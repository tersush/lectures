name: str = "Name"
for i in range(5):
    print(f"Hello {name} {4.6875494:4f}")
    
my_range: range = range(5)
print(my_range)

sentence: str = "Hello, dear, meow!"
print(sentence.split())
splitted_sentence: list[str]=sentence.split()
print(
    splitted_sentence
)
for i in range(len(splitted_sentence)):
    print(splitted_sentence[i])
    
# or we can do
#for value in splitted_sentence: итерироваться по копии листа, а не по нему самому!!!
    #print(value) 