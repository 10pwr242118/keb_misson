# ex 6.2
guess_me = 5
number = 0

for number in range (10):
        if number > guess_me:
                print('too high')
                break
        if number < guess_me:
                print('too low')
                continue
        else:
                print('thats right')
                break