import os, sys

#If contents file exists, execute writing to the file 
s = os.path.dirname(os.path.realpath(sys.argv[0]))
#print(path)
os.chdir(s)
path = os.getcwd()

#Function to write directory contents to file
def fill_cont():

    with open(f'{path[17:]}_contents.txt', 'w', encoding="utf-8") as f:
        f.seek(0)
        for item in os.listdir(path):
            if os.path.isdir(f'{path}\\{item}'):
                s = os.listdir(f'{path}\\{item}')   
                f.write(f'\n {item.upper()}: \n\n')
                f.writelines('\n'.join(s))
                f.write("\n ----------------------- ")
            else:
                f.writelines(item)
                f.write("\n ----------------------- ")
                
                
#If contents file exists, execute function
if os.path.exists(path):  
    fill_cont()     

#If contents file exists, execute function
else:
    #f = open(f'{path[17:]}_contents.txt', 'w')
    print("Created new contents file")
    #fill_cont()

