'''
with function
'''
class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("In __exit__()")

with Sample() as s:
    a = s
    print(a)

print(s)
