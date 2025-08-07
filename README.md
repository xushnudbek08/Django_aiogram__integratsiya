Bu loyiha organish uchun yani django bilan aiogramni Integratsiya qilish


Birinchi bolib virtual muhit ornating:
Termialga : python -m venv venv


Keyin esa django va aiogram kutubxonsini ornatish kerak
Termialga : pip install django 
Termialga : pip inastall aiogram

agar sizni devaysingiz mac yoki linux bolsa pip3 python3 qilib yozilib ishlanadi bazilarida yoiladi bazilada yzoilmaydi vindovda unday muammo bolmasligi mumkin

keyin django da project ochamiz 
Termialga : django-admin startproject core . #bu cor projectingiz yani praectingiz  nomi xoxlagnini qoshingizmi=umkin

keyin app ochamiz 
Termialga : python manage.py startapp main #men main dep yozdimbu apni nomi hohlagnigizni qoyishingiz mumkin


kein core settings ga app ni boglang qodda bor

keyin app ni ichida modelslarini kiritasiz 
 va soasiysi apni ichida management/commands/runbot.py bolishi kerka va uni ichida shu code bolis hsrt
 import asyncio
from django.core.management.base import BaseCommand
from bot.main import main


class Command(BaseCommand):
    help = 'Telegram botni ishga tushirish'

    def handle(self, *args, **kwargs):
        asyncio.run(main()



shu qod bolishi kerk va botga run bermoqchimisiz bunday run beriladi odi qilib run beraolmaysiz
Termialga : python manage.py runbot 
shunda keyin ishlaydi odi qilib run bera olmaysiz xato beradi




Russia

Чтобы изучить этот проект, а именно интеграцию aiogram с django,

Сначала настройте виртуальную среду:
В терминале: python -m venv venv

Затем необходимо установить библиотеки django и aiogram.
В терминале: pip install django
В терминале: pip install aiogram

Если у вас Mac или Linux, pip3 будет записан как python3 и запустится. На некоторых устройствах это будет работать, на некоторых — нет. В Windows это может быть не так уж и сложно.

Затем открываем проект в django.
В терминале: django-admin startproject core. #Это ваш основной проект, то есть имя вашего проекта. Можете ли вы добавить его?

Затем откройте приложение.
В терминале: python manage.py startapp main #Я написал main dep, вы можете добавить нужное имя этого приложения.

Затем подключите приложение к настройкам ядра, там есть код.

Затем введите модели в приложение.
И основной должна быть management/commands/runbot.py в приложении, и в ней должен быть этот код.
import asyncio
from django.core.management.base import BaseCommand
from bot.main import main

class Command(BaseCommand):
help = 'Запустить бота Telegram'

def handle(self, *args, **kwargs):
asyncio.run(main())

Этот код должен быть там, и вы хотите запустить бота. Он будет работать так, вы не сможете его запустить.
В терминале: python manage.py runbot
Тогда он будет работать, но вы не сможете его запустить, он выдаст ошибку.


engilish


To learn this project, namely Integrating aiogram with django

First, set up a virtual environment:
In the terminal: python -m venv venv

Then you need to install the django and aiogram libraries
In the terminal: pip install django
In the terminal: pip install aiogram

If your device is mac or linux, pip3 will be written as python3 and run, in some it will work, in some it will not work, in Windows it may not be such a problem

Then we open the project in django
In the terminal: django-admin startproject core . #this is your core project, that is, your project name, can you add it?

then open the app
In the terminal: python manage.py startapp main #I wrote main dep, you can add the name of this app you want

then connect the app to the core settings, there is a code

then you enter the models in the app
and the main one should be management/commands/runbot.py in the app and this code should be in it
import asyncio
from django.core.management.base import BaseCommand
from bot.main import main

class Command(BaseCommand):
help = 'Launch Telegram bot'

def handle(self, *args, **kwargs):
asyncio.run(main()

this code should be there and you want to run the bot, it will run like this, you can't run it
In the terminal: python manage.py runbot
then it will work, you can't run it, it will give an error
