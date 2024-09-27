nickname = input()
if nickname[0] == '@' and 5 <= len(nickname) <= 15 and nickname[1:].isalnum() and ((nickname + 'a').islower()):
    print('Correct')
else:
    print('Incorrect')
