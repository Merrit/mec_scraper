import datetime
import json

import tkinter
from tkinter import messagebox

from src.mec_product import MECProduct

date = str(datetime.date.today())


def read_urls() -> list[str]:
    __urls: list[str] = []
    file = open('urls.txt', 'r')
    for line in file:
        __urls.append(line.strip())
    file.close()
    return __urls


def read_result() -> dict:
    try:
        file = open('result.txt', 'r')
    except FileNotFoundError:
        return {}
    data = json.load(file)
    return data


def save_result(data: dict):
    file = open('result.txt', 'w')
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
