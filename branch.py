import re
import subprocess
import os
import platform

def jira_ticket(input_str, ticket_prefix, ticket_code, ticket_type):
    formatted_text = input_str.lower()
    formatted_text = re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', formatted_text)
    formatted_text = re.sub(r'(?<=.)[^a-zA-Z0-9](?=.|$)', '-', formatted_text)
    formatted_text = re.sub(r"-+", '-', formatted_text)
    ticket_prefix = ticket_prefix.upper()
    ticket_text = f'{ticket_type.lower()}/{ticket_prefix}-{ticket_code}-{formatted_text}' # Modified here to use ticket_type variable

    return ticket_text

def clipboard_copy(text):
    try:
        if platform.system() == 'Windows': # Windows command to copy to clipboard
            command = 'echo | set /p nul=' + text.strip() + '| clip'
            os.system(command)
        if platform.system() == 'Darwin': # MacOS command to copy to clipboard, needs pbcopy installed using 'pip install pbcopy'
            subprocess.run(['pbcopy'], input=text, universal_newlines=True, check=True)
        print("Formatted text copied to clipboard.")
    except subprocess.CalledProcessError as e:
        print(f"Error copying to clipboard: {e}")

if __name__ == "__main__":
    ticket_type = input("Enter the ticket type (1: issue, 2: hotfix, 3: bugfix, 4: feature, 5: other) (default is 'issue', press Enter to use default): ") or '1'

    if ticket_type == '1':
        ticket_type = 'issue'
    elif ticket_type == '2':
        ticket_type = 'hotfix'
    elif ticket_type == '3':
        ticket_type = 'bugfix'
    elif ticket_type == '4':
        ticket_type = 'feature'
    elif ticket_type == '5':
        ticket_type = input("Enter the ticket type: ")

    ticket_prefix = input("Enter the ticket prefix (default is 'AC', press Enter to use default): ") or 'AC'
    ticket_code = input("Enter the ticket code: ")
    input_text = input("Enter the text to format: ")

    result_text = jira_ticket(input_text, ticket_prefix, ticket_code, ticket_type)
    clipboard_copy(result_text)

    print(result_text)
