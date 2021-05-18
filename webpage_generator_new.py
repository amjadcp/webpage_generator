'''
Author : Rijfas
Date   : 18/05/2021
Desc   : Just a simple version of webpage_generator
'''
from re import findall
from subprocess import call

# change to vim ( ͡❛ ͜ʖ ͡❛)
DEFAULT_INLINE_EDITOR = 'nano'

'''
function : print_error
    prints an error message to console
@param 
    message : str  
    warning : bool
@return None
'''
def print_error(message, warning=False):
    print(f'{"WARNING" if warning else "ERROR"}: {message}!')


'''
function : print_banner
    prints banner to console
@param None
@return None
'''
def print_banner():
    print('''
  █████   ███   █████          █████       █████████                     
░░███   ░███  ░░███          ░░███       ███░░░░░███                    
 ░███   ░███   ░███   ██████  ░███████  ███     ░░░   ██████  ████████  
 ░███   ░███   ░███  ███░░███ ░███░░███░███          ███░░███░░███░░███ 
 ░░███  █████  ███  ░███████  ░███ ░███░███    █████░███████  ░███ ░███ 
  ░░░█████░█████░   ░███░░░   ░███ ░███░░███  ░░███ ░███░░░   ░███ ░███ 
    ░░███ ░░███     ░░██████  ████████  ░░█████████ ░░██████  ████ █████
     ░░░   ░░░       ░░░░░░  ░░░░░░░░    ░░░░░░░░░   ░░░░░░  ░░░░ ░░░░░ 
                                                                        
    Simple WebPage Genrator
    Version : 0.1
    Contributers  : Amjad, r1jf45                                                               
    
    Enter a number based on your need 
    
    ==================================MENU============================
             
             1: SAMPLE PAGE WITH MINIMAL PERSONAL DATA
             2: SAMPLE FORM TO ACCESS MINIMAL PERSONAL DATA
             3: SAMPLE FRAME SET TO INCLUDE YOU ALREADY CREATED DATA ( only for 3 pages -- screen divition "cols = 25%,50%,25%" )''')


'''
function : write_html
        writes the html file with given keys
          @param 
              template_file_name : str  
              output_file_name   : str  
          @return None
          '''
def write_html(template_file_name, output_file_name, **kwargs):
    try:
        template_file = open(template_file_name, 'r')
        template = template_file.read()
        template_file.close()
        output_file = open(output_file_name, 'w')
        output_file.write(template.format(**kwargs))
        output_file.close()
        print(f'Sample page is created in {output_file_name}')

    except FileNotFoundError:
        print_error(f'Cannot open {template_file_name}')

    except KeyError as invalid_key:
        print_error(f'Please provide a value for {invalid_key}')


'''
function : load_keys
    loads keys from given template
@param 
    template_file_name : str    
@return List(str), None
'''
def load_keys(template_file_name):
    try:
        template_file = open(template_file_name, 'r')
        data = template_file.read()
        template_file.close()
        return findall(r'\{(.*)\}', data)

    except FileNotFoundError:
        print_error(f'Cannot open {template_file_name}')
        return []


'''
function : get_info
    read each key value from user
@param 
    keys : List(str )   
@return dict(str, str)
'''
def get_info(keys):
    print('Enter Required Info:')
    data = dict()
    for key in keys:
        data[key] = input(f'  - Enter {key}: ')
    return data


def main():
    print_banner()
    option = int(input("enter =>"))
    if option == 1:
        template_file_name = "MINIMAL_PERSONAL_DATA.html"
    elif option == 2:
        template_file_name = "SAMPLE_FORM.html"
    elif option == 3:
        template_file_name = "FRAME.html"
        print("\n\n *** Please enter your URLs in \"\" ***** \n\n")
    else:
        print("oops wrong option try again")
        exit()
    #template_file_name = input('Enter template file name(Eg: template.html): ')
    output_file_name = input('Enter output file name(Eg: output.html): ')
    keys = load_keys(template_file_name)
    data = get_info(keys)
    write_html(template_file_name, output_file_name, **data)
    can_edit = input(f'Open {output_file_name} in {DEFAULT_INLINE_EDITOR}? (y/n):')
    if can_edit.lower() == 'y':
        call(f'{DEFAULT_INLINE_EDITOR} {output_file_name}', shell=True)
    print('Thank You!')


if __name__ == '__main__':
    main()