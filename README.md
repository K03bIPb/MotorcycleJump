# Проектная работа по разработке кросплатформенных программных систем
Для переноса игры с basic был использован язык программирования python.
Для визуализации игры был использован игровой движок UnrealEngine 5.

## Реализация игры на python

### Запуск игры на windows
Проект был разработан в среде разработки PyCharm.
Запуск на windows производился через терминал в PyCharm.

 ![Win](https://github.com/K03bIPb/MotorcycleJump/blob/main/Windows.png)


### Запуск игры на linux
Запуск на linux был произведен с помощью онлайн компилятора "onlinegdb".
  
  ![lin](https://github.com/K03bIPb/MotorcycleJump/blob/main/Linux.png)
 
 ### Запуск игры на web
 На web код на python был перенесен с помощью "pyscript".
 
  ![web](https://github.com/K03bIPb/MotorcycleJump/blob/main/Web.png)
  
## Визуализация игры на движке Unreal engine 5

### Запуск визуализации на windows

Игра выгружается с движка и запускается через .exe файл.
Готовая игра не была выгружена на github в связи с большим весом файлов.

  ![ue5build](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Build.png)

На рисунках ниже продемонстрированы запуск и работа игры на windows.

Первый этап игры — выбор количество автобусов, через которые нужно прыгать

  ![busses1](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Busses1.png)
  ![busses2](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Busses2.png)
  ![busses3](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Busses3.png)

Второй этап игры — выбор угла рампы, на которой гонщик поднимется в воздух

  ![ramp1](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Ramp1.png)
  ![ramp2](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Ramp2.png)
  
  
Третий этап игры — выбор скорости гонщика, с которой тот начнет перепрыгивать автобусы

  ![rider1](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Rider1.png)
  ![rider2](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Rider2.png)

Далее идет процесс перепрыгивания. Успех или неудача зависят от трех предыдущих параметров — кол-во автобусов, угол рампы и скорость гонщика.

  ![jump](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Rider3.png)
  
В случае победы или поражения перед нами появится соответствующее окно, с последующим затемнением экрана и перезапуском уровня. 

![win](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Win.png)
![lose](https://github.com/K03bIPb/MotorcycleJump/blob/main/Unreal%20Engine%205/Gameplay/Lose.png)
