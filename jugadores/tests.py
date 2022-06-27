from django.test import TestCase
import random
import string

KEY_LEN = 20
char_list = [random.choice((string.ascii_letters + string.digits)) for _ in range(KEY_LEN)]
mock_name = ''.join(char_list)
print(f'----------> Prueba con: {mock_name}')
