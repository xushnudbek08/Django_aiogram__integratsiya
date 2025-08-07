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
