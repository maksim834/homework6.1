# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#immutable_var = 5, 6, 'c', 'D'
#print(immutable_var)
#print(type(immutable_var))
#immutable_var[0] = 7
#print(immutable_var)
mutable_list = [3, 4, 'a', 'B']
print(mutable_list)
print(type(mutable_list))
mutable_list[2] = 5
print(mutable_list)