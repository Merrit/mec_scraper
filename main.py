import datetime
import json
import os

import tkinter
from tkinter import messagebox

from src.mec_product import MECProduct

date = str(datetime.date.today())


# Get file path from the same dir as the running script.
def get_file_path(file_name) -> str:
    script_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_location = os.path.join(script_dir, file_name)
    return file_location


url_file_location = get_file_path('urls.txt')
result_file_location = get_file_path('result.txt')


def read_urls() -> list[str]:
    __urls: list[str] = []
    file = open(url_file_location, 'r')
    for line in file:
        __urls.append(line.strip())
    file.close()
    return __urls


def read_result() -> dict:
    try:
        file = open(result_file_location, 'r')
    except FileNotFoundError:
        return {}
    data = json.load(file)
    return data


def save_result(data: dict):
    file = open(result_file_location, 'w')
    json.dump(data, file)
    file.close()


def notify(prev_result: dict, current_result: dict):
    root = tkinter.Tk()
    root.withdraw()

    messagebox.showinfo("MEC Price Drop", f'''
    Previous
    Name: {prev_result['name']}
    Price: {prev_result['price']}
    Date: {prev_result['date']}
    
    Current
    Name: {current_result['name']}
    Price: {current_result['price']}
    Date: {current_result['date']}
    ''')


if __name__ == '__main__':
    previous_result = read_result()
    previous_result_exists = len(previous_result) > 0
    result = {}
    urls: list[str] = read_urls()
    for url in urls:
        product = MECProduct(url)
        result_dict = {
                'name': product.name,
                'price': product.price,
                'date': date,
            }
        result[result_dict['name']] = result_dict
        if previous_result_exists:
            previous_product = previous_result[product.name]
            if product.price < previous_product['price']:
                notify(previous_product, result_dict)
    save_result(result)
