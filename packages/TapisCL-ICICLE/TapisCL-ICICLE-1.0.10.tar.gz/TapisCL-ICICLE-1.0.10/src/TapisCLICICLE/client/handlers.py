from getpass import getpass
import os
import json
import pprint
import time

from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import word_completer, WordCompleter
from prompt_toolkit.shortcuts import checkboxlist_dialog
from prompt_toolkit import prompt

from blessed import Terminal


if __name__ != "__main__":
    from ..socketopts import schemas


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(f"{__file__}")))
saved_command = os.path.join(__location__, r'entered_command.json')


class Formatters:
    """
    Format received dictionaries in the client code
    """
    def print_response(self, input_data, depth: int=0):
        if isinstance(input_data, (list, set, tuple)):
            for data in input_data:
                if isinstance(data, (list, dict, set, tuple)):
                    print("\n")
                self.print_response(data, depth=depth+1)
        elif isinstance(input_data, dict):
            for name, data in input_data.items():
                if isinstance(data, (int, str)):
                    print(("  " * depth) + f"{name}: {data}")
                    continue
                print(("  " * depth) + f"{name}: ")
                self.print_response(data, depth=depth+1)
        elif isinstance(input_data, (int, str)):
            print(f"{depth * '  '}{input_data}")
        if depth == 0:
            print("\n")


class ParserTypeLenEnforcer:
    def __init__(self, name: str=str(), size: tuple=(0, 0), data_type: str='string', choices: list=list()):
        self.arg_name = name
        self.data_type = data_type
        self.lower_size_limit, self.upper_size_limit = size
        self.choices = choices

    def update_constraints(self, name=None, data_type=None, choices=None, size_limit=None, **kwargs):
        self.arg_name = name
        self.data_type = data_type
        self.choices = choices
        self.lower_size_limit, self.upper_size_limit = size_limit

    def __call__(self, data):
        if self.data_type:
            try:
                if self.data_type == 'string':
                    data = str(data)
                elif self.data_type == 'int':
                    data = int(data)
            except Exception as e:
                raise ValidationError(message=str(e) + self.data_type, cursor_position=0)
        if self.data_type == int:
            if not data >= self.lower_size_limit or not data < self.upper_size_limit:
                raise ValidationError(message=f"The input for the argument {self.arg_name} must be in the range ({self.lower_size_limit}, {self.upper_size_limit}). Got value {data}", cursor_position=0)
        elif self.data_type == str:
            if not len(data) >= self.lower_size_limit or not len(data) < self.upper_size_limit:
                raise ValidationError(message=f"The input length for the argument {self.arg_name} must be in the range ({self.lower_size_limit}, {self.upper_size_limit}). Got length {len(data)}", cursor_position=0)
        if self.choices and data not in self.choices:
            raise ValidationError(message=f"The input for the argument {self.arg_name} must be one of the following: {self.choices}", cursor_position=0)


class ResponseValidator(Validator):
    def __init__(self):
        super().__init__()
        self.enforcer = ParserTypeLenEnforcer()

    def validate(self, document):
        text = document.text
        self.enforcer(text)

        
class Handlers(Formatters):
    def __init__(self):
        self.validator = ResponseValidator()

    def __labelled_form(self, form_options, form_filled):
        labelled_dict = dict()
        for field_name, field_metadata in form_options.items():
            if field_metadata['required']:
                requirement_str = 'R'
            else:
                requirement_str = 'O'
            labelled_dict[f"({requirement_str}) {field_name}"] = form_filled[field_name]
        return json.dumps(labelled_dict, indent=3)


    def __expression_input(self) -> str: 
        """
        Input an expression as requested by the server for something like cypher queries
        """
        print("Enter 'exit' to submit") 
        expression = ''
        line = ''
        while line != 'exit': 
            line = str(input("> "))
            if line != 'exit':
                expression += line
        return expression
    
    def confirm_form_exit(self, message: str=None):
        print(message)
        while True:
            decision = str(input("(y/n)"))
            if decision == 'y':
                return True
            elif decision == 'n':
                return False
            else:
                print("Enter valid response")
        
    def confirmation_handler(self, argument: dict=None):
        print(argument['name'])
        if 'description' in argument and argument['description']:
            print(argument['description'])
        while True:
            decision = str(input("(y/n)"))
            if decision == 'y':
                return True
            elif decision == 'n':
                if not argument['required']:
                    return False
                raise KeyboardInterrupt('User negative reply on confirmation, cancelling')
            else:
                print("Enter valid response")
    
    def selection_list_handler(self, term: Terminal, attrs: dict):
        with term.fullscreen():
            results_array = checkboxlist_dialog(
                title="CheckboxList dialog",
                text="What would you like in your breakfast ?",
                values=[(True, field) for field in attrs['option_list']]
            ).run()
            results = dict(zip(attrs['option_list'], results_array))
            return results
        
    def input_dict_handler(self, term: Terminal, attrs: dict, default=None):
        mode = 'create'
        if not default:
            default = dict()
        answer = default
        default_name = attrs['data_type']['name']
        with term.fullscreen():
            print(f"You are now entering data for {attrs['name']}")
            while True:
                print(f"{term.clear}now editing the map: {attrs['name']}\nreserved names: create, delete, exit (enter these for special action)\nmode: {mode}")
                print(json.dumps(answer, indent=4))
                attrs['data_type']['name'] = default_name
                name = str(input(f"enter the name for the instance of your {attrs['data_type']['name']}: "))
                if name.lower() in ('delete', 'create'):
                    mode = name
                    continue
                if name.lower() == 'exit':
                    return answer
                if mode == 'create':
                    mode = 'create'
                    attrs['data_type']['name'] = name
                    if name in answer:
                        default_value = answer
                    else:
                        default_value = None
                    sub_answer = self.advanced_input_handler({name:attrs['data_type']}, term, default=default_value)
                    if sub_answer[name]:
                        answer.update(**sub_answer)
                elif mode == 'delete':
                    mode = 'delete'
                    try:
                        answer.pop(name)
                    except KeyError:
                        pass

    def input_list(self, term: Terminal, attrs: dict, default=None):
        if not default:
            default = list()
        answer = default
        with term.fullscreen():
            print(f"You are now entering data for {attrs['name']}")
            mode = 'modify'
            while True:
                sub_answer = None
                presentable_dict = {str(index+1):value for index, value in enumerate(answer)}
                print(rf"""{term.clear}now editing the list: {attrs['name']}
                      Enter exit to submit list, or new to create new list element.
                      Modes: to change mode, enter the mode you want to use. 
                        Delete: when you enter an index the index is deleted. 
                        Modify: when you enter an index you will re-enter the element to modify it
                      mode: {mode}""")
                print(json.dumps(presentable_dict, indent=4))
                decision = input("Enter 'new' or 'exit': ")
                if decision.lower() == 'exit':
                    return answer
                elif decision.lower() == 'new':
                    pass
                elif decision.lower() in ('modify', 'delete'):
                    mode = decision
                    continue
                elif decision.isdigit() and mode == 'delete':
                    try:
                        answer.pop(int(decision)-1)
                    except IndexError:
                        continue
                    continue
                elif decision.isdigit() and mode == 'modify':
                    try:
                        sub_answer = self.advanced_input_handler({f"{attrs['name']}_{str(decision)}":attrs['data_type']}, term, default={f"{attrs['name']}_{str(decision)}":answer[int(decision)-1]})
                        if sub_answer:
                            answer[int(decision)-1] = sub_answer[f"{attrs['name']}_{str(decision)}"]
                    except IndexError:
                        continue
                    continue
                else:
                    continue
                sub_answer = self.advanced_input_handler({f"{attrs['name']}_{str(len(answer)+1)}":attrs['data_type']}, term)
                index, value = list(sub_answer.items())[0]
                if value:
                    answer.append(value)

    def form_handler(self, term: Terminal, attrs: dict, form_name, default=None):
        form_options = attrs['arguments_list']
        completer = WordCompleter(list(form_options.keys()))
        if not default:
            form_input = dict()
            for name, command_metadata in form_options.items():
                if command_metadata['default_value']:
                    form_input[name] = command_metadata['default_value']
                    continue
                form_input[name] = ''
        else:
            form_input = {arg_name:arg_default_value for arg_name, arg_default_value in default.items() if arg_name in form_options}
        with term.fullscreen():
            while True:
                print(f"{term.clear}now editing the form: {form_name}")
                print(self.__labelled_form(form_options, form_input))
                field = prompt('Enter the field you want to modify. Enter exit to complete: ', completer=completer)
                if field.lower() == 'exit':
                    unfulfilled_requirements = []
                    for field_name, field_metadata in form_options.items():
                        if field_metadata['required'] and not form_input[field_name] and form_input[field_name] != False:
                            unfulfilled_requirements.append(field_name)
                    if unfulfilled_requirements:
                        decision = self.confirm_form_exit(f'The fields {unfulfilled_requirements} are required but did not receive any input. If you exit this form will not be submitted.\nSubmit form?')
                        if decision:
                            return None
                        else:
                            continue
                    return form_input
                elif field not in form_options:
                    continue
                result = self.advanced_input_handler({field:form_options[field]}, term, default=form_input)
                form_input[field] = result[field]
            
    def str_input(self, attrs):
        completer = None
        if 'choices' in attrs and attrs['choices']:
            completer = WordCompleter(attrs['choices'])
        answer = prompt(f"{attrs['name']}: ", validator=self.validator, wrap_lines=True, completer=completer)
        if attrs['data_type'] == 'str':
            answer = str(answer)
        elif attrs['data_type'] == 'int':
            answer = int(answer)
        elif attrs['data_type'] == 'bool':
            answer = bool(answer)
        return answer
    
    def advanced_input_handler(self, form_request: dict, term: Terminal, default=None):
        response = dict()
        for field, attrs in form_request.items():
            arg_type = attrs['arg_type']
            self.validator.enforcer.update_constraints(**attrs)
            if 'description' in attrs and attrs['description']:
                print(attrs['description'])
            if default and attrs['part_of']:
                default_selection = default[attrs['part_of']][field]
            elif default:
                default_selection = default[field]
            else:
                default_selection = None
            try:
                match arg_type:
                    case 'secure':
                        answer = prompt(f"{attrs['name']}: ", validator=self.validator, is_password=True)
                    case 'expression':
                        with term.fullscreen():
                            print(f"Enter expression input for the {attrs['name']} argument.")
                            answer = self.__expression_input()
                    case 'form':
                        answer = self.form_handler(term, attrs, field, default=default_selection)
                    case 'input_list':
                        answer = self.input_list(term, attrs, default=default_selection)
                    case 'input_dict':
                        answer = self.input_dict_handler(term, attrs, default=default_selection)
                    case 'str_input':
                        answer = self.str_input(attrs)
                    case 'standard':
                        answer = self.str_input(attrs)
                    case 'confirmation':
                        answer = self.confirmation_handler(attrs)
                    case 'silent':
                        continue
                    case _:
                        raise AttributeError(f"There is not argument type {arg_type}")
                response[field] = answer
            except KeyboardInterrupt:
                raise RuntimeError('Form cancelled, command execution stopped')
            except Exception as e:
                with open(saved_command, 'a') as f:
                    f.write(json.dumps(response))
                    print(f"Argument input failure, command data written to file {saved_command}")
                    raise e
        return response
    
    def universal_message_handler(self, message: schemas.BaseSchema, term: Terminal):
        self.print_response(message.message)
        if message.error:
            self.print_response(message.error)
        if message.request_content:
            try:
                default = message.existing_data
            except:
                default = None
            filled_form = self.advanced_input_handler(message.request_content, term, default=default)
            return filled_form
        return None
        
    def environment_cli_response_stream_handler(self, response):
        if response.schema_type == 'ResponseData' and response.exit_status: # if the command was a shutdown or exit, close the program
            self.print_response(response.response_message)
            os._exit(0)
        elif response.schema_type == 'ResponseData':
            if response.active_username:
                self.username = response.active_username
            if response.url:
                self.url = response.url
            self.print_response(response.response_message)