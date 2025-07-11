def format_cat(cat_list):
    my_string = ""
    for i in range(0, len(cat_list)):
        if (i != len(cat_list) - 1):
            my_string = my_string + str(cat_list[i]) + ", "
        elif (i == len(cat_list) - 1):
            my_string = my_string + "and " + str(cat_list[i]) + "."
    return my_string

cat_list = ["Hummle", "Buck", "Gon", "John", "Kiss"]
print(format_cat(cat_list))