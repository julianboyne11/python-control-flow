# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
phrase = input("Please enter a word or phrase: ")
#      Please enter a word or phrase: 
# 2. Print the following message:


while phrase != "quit":
  phrase = input("Please enter a word or phrase: ")
  print(len(phrase))
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

