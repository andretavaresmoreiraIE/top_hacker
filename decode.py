alpha = " abcdefghijklmnopqrstuvwxyz"
vowel = list("aeiou")

fp = open("secret.txt")
decoded = ""  # this is your decoded message. It gets one letter per line of file decoded

#start adding code here

for each_line in fp:

    nr_vowel = 0

    for letter in each_line:
        if letter in vowel:
            nr_vowel = nr_vowel +1

    decoded = decoded + alpha[nr_vowel]
#end the code here
print(decoded)
fp.close()