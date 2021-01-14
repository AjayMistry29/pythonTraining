def reverse(string):
    yield(string[::-1])

my_string = reverse("Consultadd Training")

for s in my_string:
    print(s)
    