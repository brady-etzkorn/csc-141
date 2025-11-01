texts = ['hey','hi','bye']
sent_messages = []

while texts:
    unsent_texts = texts.pop()
    print(f'Texts:{unsent_texts}')
    sent_messages.append(unsent_texts)

print('\nThe following models have been printed:')
for sent_message in sent_messages:
    print(sent_message)