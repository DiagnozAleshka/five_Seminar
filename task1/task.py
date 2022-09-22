# 38. Напишите программу, удаляющую из
# текста все слова содержащие "абв".

my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие абв("абв")'

def words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = words(my_text)
print(my_text)