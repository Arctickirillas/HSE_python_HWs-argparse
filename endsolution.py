import argparse

parser = argparse.ArgumentParser(description = 'print our inputs')
parser.add_argument('--gender', choices=['male', 'female', None])
parser.add_argument('height', type = int)
parser.add_argument('weight', type = int)
parser.add_argument('height', type = int)
parser.add_argument('sleep', type = int)
parser.add_argument('daily_meals', type = int)
parser.add_argument('fruits_veg', type = int)
parser.add_argument('steps', type = int)
parser.add_argument('health_mon', choices=['Not', 'Yes', None])
parser.add_argument('mood', choices=['Good', 'Neutral', 'Bad'])
parser.add_argument('happiness', choices=['During the week', 'During the month', 'During the year'])

args = parser.parse_args()
count = 0
if 7 <= args.sleep <= 8:
    count +=1
if 4 <= args.daily_meals <= 5:
    count += 1
if 500 <= args.fruits_veg:
    count += 1
if 10 <= args.steps:
    count += 1
if args.health_mon == 'Yes':
    count += 1
if args.mood == 'Good':
    count += 1
if args.happiness == 'During the week' or args.happiness == 'During the month':
    count += 1
BMI = int(args.weight / args.height * args.height)
if 18.5 <= BMI * 10000 <= 24.9:
    count += 1

if count == 8:
    print('Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')
elif 5<= count <= 7:
    print('Your health index is [5-7]/8, which means that you are on the right track!')
else:
    print('Your healthy lifestyle index is [0-4]/8 🤢, you need to rethink your healthy lifestyle!')
