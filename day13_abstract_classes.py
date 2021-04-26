#!/bin/python3
from abc import ABC, abstractmethod
class Book(ABC):
    def __init__(self,title,author):
        self.title=title
        self.author=author 

    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    
    def display(self):
        print("Title: " + title)
        print("Author: " + author)
        print("Price: " + str(price))
        
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()