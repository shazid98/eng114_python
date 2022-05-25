# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("File cannot be found")
#     print(errmsg)
#     raise

def open_and_print_file(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip("\n"))

    except:
        print("file cannot be found or directory is incorrect")
        raise

    finally:
        print("\nExecution complete")


def write_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item + "\n")
    except:
        print("file cannot be found or directory is incorrect")
        raise


write_to_file("order.txt", "Lasagna")
open_and_print_file("order.txt")

#         opened_file = open(file, "r")
#         file_line_list = opened_file.readlines()
#
#         for line in file_line_list:
#             print(line.rstrip("\n"))
#
#         opened_file.close()
#
#     except FileNotFoundError:
#         print("file cannot be found using details provided")
#         raise
#
#
# open_and_print_file("order.txt")

