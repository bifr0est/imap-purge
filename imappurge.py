import imaplib
import getpass

def get_imap_connection():
    imap_server = input("Enter your IMAP server address: ")
    email = input("Enter your email address: ")
    password = getpass.getpass("Enter your email password: ")
    
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email, password)
    return mail

def list_folders(mail):
    status, folders = mail.list()
    
    if status == 'OK':
        print("\nAvailable folders:")
        for folder in folders:
            folder_name = folder.decode().split('"/"')[-1].strip('"')
            print(f"- {folder_name}")
    else:
        print("Failed to retrieve folder list.")

def cleanup_folder(mail, folder_name, subject_filter=None):
    status, messages = mail.select(folder_name)
    
    if status != 'OK':
        print(f"Error: Unable to open the folder '{folder_name}'. Please check if the folder name is correct.")
        return
    
    if subject_filter:
        _, msg_nums = mail.search(None, f'(SUBJECT "{subject_filter}")')
    else:
        _, msg_nums = mail.search(None, 'ALL')
    
    count = 0
    for num in msg_nums[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')
        count += 1
    
    mail.expunge()
    print(f"Total messages permanently deleted from {folder_name}: {count}")

# Main execution
try:
    mail = get_imap_connection()
    list_folders(mail)

    folder_to_clean = input("\nEnter the name of the folder you want to clean up: ")
    subject_filter = input("Enter a subject filter (or press Enter to delete all emails in the folder): ")

    if subject_filter:
        cleanup_folder(mail, folder_to_clean, subject_filter)
    else:
        cleanup_folder(mail, folder_to_clean)

except imaplib.IMAP4.error as e:
    print(f"An IMAP error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'mail' in locals():
        mail.logout()