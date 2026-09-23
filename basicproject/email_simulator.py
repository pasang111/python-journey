import datetime


# Create an Email
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    # Mark the email as read
    def mark_as_read(self):
        self.read = True

    # Display the full email
    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    # Show email summary
    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


# Create a User
class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    # Send an email
    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # Check the inbox
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    # Read an email
    def read_email(self, index):
        self.inbox.read_email(index)

    # Delete an email
    def delete_email(self, index):
        self.inbox.delete_email(index)


# Manage the user's inbox
class Inbox:
    def __init__(self):
        self.emails = []

    # Receive an email
    def receive_email(self, email):
        self.emails.append(email)

    # List all emails
    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return

        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    # Read an email by number
    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        self.emails[actual_index].display_full_email()

    # Delete an email by number
    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        del self.emails[actual_index]
        print('Email deleted.\n')


# Run the email simulation
def main():
    # Create two users
    tory = User('Tory')
    ramy = User('Ramy')

    # Send emails
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')

    # Check, read, and delete Ramy's email
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)

    # Check Ramy's inbox again
    ramy.check_inbox()


if __name__ == '__main__':
    main()
