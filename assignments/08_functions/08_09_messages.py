def show_messages(messages):
    #This program is to show what is in the list of texts
    for message in messages:
        msg = f'{message.title()}'
        print(msg)

texts = ['hey','hi','bye']
show_messages(texts)