while True:
    name = input('What is your name? : ').lower()

    def girl(gname, glooking):
        print(f'{name.capitalize()} your girlfriend is {gname} and she is {glooking}. {name} already lost him. so sad :)')

    if 'stop' in name:
        print('Okay Sir! Stoping Program.')
        break

    elif name in 'foyez ahammad machum masum':
        girl('Salma Akter Mishu', 'Perfect')
        print('Sir! alwayes Fill him! Love hime! Miss him!')

    elif name in 'abdul kader':
        girl('Shakira', 'Chikna Chamili')

    elif name in 'nahidul islam rafi':
        girl('Raha', 'Preety Good')

    else:
        print('Your information does not exist!')
