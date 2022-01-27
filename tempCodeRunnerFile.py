    for directory in dirs: 
        if GetWindowText(GetForegroundWindow()) == directory:
            os.chdir(f'{path}{directory}')

            with open(f'{directory}_contents.txt', 'w', encoding="utf-8") as f:
                f.seek(0)
                #TITLE
                f.write(f'##{directory.upper()}##\n')

                #for item in i.e downlods...
                for item in os.listdir(f'{path}{directory}'):
                    if os.path.isdir(item):
                        s = os.listdir(f'{path}{directory}/{item}')   
                        f.write(f'\n<#{item}#>')
                        f.writelines('\n    >>'.join(s))
                    if os.path.isfile(item):
                        print(item)
                        f.write(f'\n>{item}\n')
                