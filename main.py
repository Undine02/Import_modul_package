from application.my_date import get_today
from application.salary import calculate_salary
from application.db.people import get_employees


def main():
    print(calculate_salary())
    print(get_employees())
    print(get_today())



if __name__ == '__main__':
    main()