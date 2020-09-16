import argparse
parser = argparse.ArgumentParser(description='Testing healthy lifestyle index')
parser.add_argument('--Name')
parser.add_argument('--Gender', choices=['male', 'female', 'other'])
parser.add_argument('Weight', type=int)
parser.add_argument('Height', type=int)
parser.add_argument('Sleep_Hours', help='How much do you usually sleep?',
                    choices=['<7', '7-8', '>8'])
parser.add_argument('Meals', help='How many meals does your daily diet include?',
                    choices=['1', '2-3', '4-5'])
parser.add_argument('Fruits', help='How many fresh fruits and vegetables do you eat during the day?',
                    choices=['no', '<500g', '>500g'])
parser.add_argument('Steps', help='How many steps do you walk on average per day?',
                    choices=['<5k', '5k-10k', '>10k'])
parser.add_argument('Health', help='Do you monitor your health?',
                    choices=['Not', 'Yes', '3y', 'No_Doctor'])
parser.add_argument('Mood', help='What is your mood today?',
                    choices=['Good', 'Neutral', 'Bad'])
parser.add_argument('Happiness', help='When was the last time you had a state of happiness?',
                    choices=['Week', 'Month', 'Year'])
args = parser.parse_args()
points = 0
BMI = int(args.Weight)/(int(args.Height)**2)
if args.Sleep_Hours == '7-8':
    points += 1
if args.Meals == '4-5':
    points += 1
if args.Fruits == '>500g':
    points += 1
if args.Steps == '>10k':
    points += 1
if args.Health == '3y':
    points += 1
if args.Mood == 'Good':
    points += 1
if args.Happiness == 'Week' or args.Happinness == 'Month':
    points += 1
if 18.5 <= BMI * 10000 <= 24.9:
    points += 1

if points == 8:
    print('Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')
elif 5 <= points <= 7:
    print('Your health index is {0}/8, which means that you are on the right track!'.format(points))
else:
    print('points Your healthy lifestyle index is {0}/8 🤢, you need to rethink your healthy lifestyle!'.format(points))