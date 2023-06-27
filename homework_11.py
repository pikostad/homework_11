import argparse

with open('poem.txt', mode='w', encoding='utf-8') as poem_file:  
#I create a new poem.txt file filled with some random text here, so the user doesn't need to do it manually
    poem_file.write(
'''
My grandfather's clock was too large for the shelf,
So it stood ninety years on the floor.
It was taller by half than the old man himself,
Though it weighed not a pennyweight more.
It was bought on the morn of the day that he was born,
And was always his treasure and pride;
But it stopped short — never to go again —
When the old man died.''')


parser = argparse.ArgumentParser(description='working with date in files')
parser.add_argument("input_file", default=None, help=("Input file to read"))
parser.add_argument("output_file", default=None, help=("Output file to put the results into."))
parser.add_argument('-n', '--number', help='character to be replaced with this number', default= 0, type=int)
parser.add_argument('-c', '--character', help='a charecter to be replaced to a certain number', default='o', type=str)
parser.add_argument("--upper", action="store_true",default=False, help=("every word will start with uppercase"))


args = parser.parse_args()

def uppercase_first(str):
    return str.title()


def replace_char(line, char, number):
    numb_srt = str(number)
    return line.replace(char, numb_srt)

def modify_text_file(input_file, output_file, number, character, upper):
    '''the main function in this homework: opens an input and an output file and makes some changes inside :
    1.if the flag "upper" is true, then it makes every first character in every word uppercased 
    2. replace a character with a given number.'''
    with open(input_file, encoding='utf-8') as opened_input_file:
        with open(output_file, mode = 'w', encoding='utf-8') as opened_output_file:
            for line in opened_input_file:
                if upper:
                    line = uppercase_first(line)
                print(replace_char(line, character, number), end='', file = opened_output_file)


        

modify_text_file(args.input_file, args.output_file, args.number, args.character, args.upper)
