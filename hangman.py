import random
import string
from image import IMaGES
z=string.ascii_lowercase
print("_______hello welcome to hangman GaMe.________")
print("level of game.'easy','medium','hard' ")
user=input()
# if user=="e":
print('aviliale Words.',z)
if user=="e":
	b=['ankur','vishal','raj','abhishek','love']
	a=random.choice(b)
elif user=="m":
	c=['apple','dogs','boy','Ordered']
	a=random.choice(c)
elif user=="h":
	d=['qazxswed','cdeswassd','ertyhnfv','sxdwswqasd']
	a=random.choice(d)
# else:
# 	print('invilid choice')
print(a)
words=a
print("length of secreat_words:-",len(words))
Guess_words=""
lives=0
# zz=""
save_live=8
emp_list=[]
words_list=list(words)
for i in range(len(words)):
	emp_list.append('_')
	aa=' '.join(emp_list)
print(aa)

while True:		
	user=input('Guess a letter.\n')
	if len(user)==1:
		if user in words:
			for t in range(len(words_list)):
				if user==words_list[t]:
					emp_list[t]=user
			print('good guessed.')
			print(' '.join(emp_list))

			print("aviliale Words.",z.replace(user , ""))
			
			if emp_list==words_list:
				print(' Ooo \n you win !!\n')
				break
		else:
			print('incorrect guessed')
			print(IMaGES[lives])
			print(aa)
			lives+=1
		if lives==save_live:
			print('you lose.!')
			break 
		else:
			d=save_live-lives
			print("you have lives:",d)
	else:
		print('invilid choice')