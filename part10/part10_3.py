sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

# cap_count = 0
# for sentence in sentences:
#     cap_count += sentence.count('капитан')

print(sum(map(lambda sentence: sentence.count('капитан'), sentences)))
