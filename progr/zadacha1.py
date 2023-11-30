#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'а', 'е',
              'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

    text = input("Введите предложение: ")

    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    print("Количество гласных в строке:", count)