class color:
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'
    
def wrongInputMessage(error, caller=None):
    print("taskmaster.py: invalid input -- '{}'".format(error))
    extraString = ''
    if caller is not None:
        extraString = " or 'taskmaster.py {} help'".format(caller)
    print("Try 'taskmaster.py --help'{} for more information".format(extraString))

def helpMessage():
    title =       '                                       TASKMASTER                                       '
    explanation = '                          A cli app to help organize your days                          '
    usage =       'Usage: taskmaster.py [OPTION] [FURTHER ARGS]                                            '
    tip =         'All options can be given FURTHER ARGS but will exit if input is invalid:                '
    command0 =    '  -h, --help                 outputs this help message and exit\n'
    command1 =    '  -c, --create               creates a task, if no FURTHER ARGS are given prompts       \n'
    more1    =    '                             accordingly, use "taskmaster.py -c help" for info     \n'
    command2 =    '  -s, --say, -p              say/print a day\'s, week\'s schedule or all recurring tasks\n'
    more2    =    '                             currently registered, use "taskmaster.py -s help" for info\n'
    command3 =    '  -d, --delete               delete a task by name, use "taskmaster.py -d help" for info\n'
    command4 =    '  -o, --options, --conf      prompts to change the given option, or all if not specified\n'
    more4    =    '                             use "taskmaster.py -o help" for info'
    ctrld    =    'press Ctrl-D to exit from text input prompts'
    splittingLine='----------------------------------------------------------------------------------------'
    examplesString=     'Examples:'
    examples = ''
    print('')
    print(color.bold+title+color.end)
    print(color.bold+splittingLine+color.end)
    print(explanation)
    print('')
    print(usage)
    print(tip)
    print(command0+command1+more1+command2+more2+command3+command4)
    print(ctrld)
    print(color.bold+splittingLine+color.end)
    print(examplesString)
    print(examples)
    print(color.bold+splittingLine+color.end)
    print('Me: Orfeas Zografos')
    print('orfeas.zografos@gmail.com for if you find I f\'ed something up too much')
    print('or to tell me how cool this is(\'nt)')