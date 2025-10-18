from rich import print as rprint
rprint('[bold blue]hello dear friend[/bold blue]')
rprint('[bold red]today we are[/bold red]')
decision: str = input('re u coming?[y/n]:')
if decision=='y':
    rprint('[bold red]Yay! Good![/bold red]')
elif decision=='n':
    print('bedolaga')
else: 
    print('Ну вот скажи, ты вообще не понимаешь, да, что нужно ставить n или y? Ну вообще не соображаешь?')
    answer: str = input()
    if answer.lower()=="да":
        print("Нет слов..")
    else: print("Не беси меня.")