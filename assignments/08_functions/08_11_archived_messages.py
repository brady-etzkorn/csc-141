def messages(texts,sent_messages):
    #This program moves messages between lists to shwo what was sent
    while texts:
        unsent_texts = texts.pop()
        print(f'Texts:{unsent_texts}')
        sent_messages.append(unsent_texts)

def show_text_messages(sent_message):
    print('\nThese messages were sent:')
    for sent_message in sent_messages:
        print(sent_message)

texts = ['hey','hi','bye']
sent_messages = []

messages(texts[:],sent_messages)
show_text_messages(sent_messages)

print(texts)
print(sent_messages)