# Email Cleanup Script

This Python script provides a simple way to clean up your email folders by deleting messages based on folder selection and optional subject filtering.
I originally was writing that because some funny person thought its funny to crack open an imap folder and send 20k Spam emails over it. 
The reason i wrote it was to delete the "Undeliverd Mail Returned to Sender" mails because the mail server was already on a blocklist.

It's not much but it's something 

## Features

- Connect to any IMAP server
- List available email folders
- Clean up a selected folder by deleting all messages or filtering by subject
- Secure password input (not displayed on screen)

## Requirements

- Python 3.x
- `imaplib` library (built-in)
- `getpass` library (built-in)

## Usage

1. Run the script:
   ```
   python email_cleanup.py
   ```

2. Follow the prompts:
   - Enter your IMAP server address
   - Enter your email address
   - Enter your email password (input will be hidden)
   - Select a folder to clean up
   - Optionally enter a subject filter

3. The script will delete the messages and display the number of deleted emails.

## Functions

- `get_imap_connection()`: Establishes a connection to the IMAP server
- `list_folders(mail)`: Lists all available folders in the email account
- `cleanup_folder(mail, folder_name, subject_filter=None)`: Deletes emails from the specified folder, optionally filtered by subject

## Security Note

This script requires your email password. Always ensure you're running the script in a secure environment and never share your password with others.

## Caution

This script permanently deletes emails. Use with caution and make sure you have backups of important emails before running the cleanup process.