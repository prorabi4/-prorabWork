# 2. �� ������������� ���������� ����� (text18-31.txt) ������� �� ����� ��� ����������, ���������� ��������,
#������������� � ������ ����. ������������ ����� ����, � ������� ��������� ������ ���������� �����.
with open('text18-31.txt', 'r') as file:
    content = file.read()
    letter_count = sum(c.isalpha() for c in content)

print("���������� �����:")
print(content)
print(f"���������� ����: {letter_count}")
shortest_line = min(content.splitlines(), key=len)
with open('new_file.txt', 'w') as new_file:
    new_file.write(shortest_line)
