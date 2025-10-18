name: str = input()
def change_name(name: str):
    name=name.lower()
    list_name=list(name)
    for i in range(len(list_name)):
        if (i+1)%2==0:
            list_name[i]=list_name[i].upper()
        else: 
            list_name[i]=list_name[i]
    return ("".join(list_name))
change_name(name)

from rich import print as rprint
edited_name=change_name(name)
def fancy(edited_name):
    rprint(f'Привет, [bold purple]{edited_name}[/bold purple]!')
fancy(edited_name)