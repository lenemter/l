def describe_person(name, age=30):
    print(f"Человек {name} -- возраст: {age}")






























def determine_plural_form(n):
    if n % 10 == 1 and n % 100 != 11:
        return 0
    elif n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return 1
    return 2

def describe_person(name, age=30):
    age_words = ["год", "года", "лет"]
    plural_form = determine_plural_form(age)
    print(f"Человек по имени {name} прожил(а) уже {age} {age_words[plural_form]}")


# for i in range(1, 1000):
#     describe_person("...", i)
