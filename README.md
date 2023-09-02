# Скрипты для правок в базе данных
Данные скрипты написаны для [данного проекта](https://github.com/devmanorg/e-diary/tree/master) для изменений в базе 
данных. Подразумевается, что [данный проект](https://github.com/devmanorg/e-diary/tree/master) у вас скачан, настроен и 
выполнены миграции.  
## Установка:
```commandline
git clone https://github.com/Weffy61/e-diary-scripts.git
```
## Запуск скрипта:  
Передите в корневую директорию с проектом электронного школьного дневника. Запустите shell:
```commandline
python manage.py shell
```
Скопируйте код и вставьте из файла `scripts.py` и вставьте его в shell и выполните.  
### Краткое описание требований для запуска и возможностей:
- `fix_marks(schoolkid)` - для запуска требуется указать обьект класса `Schoolkid`. Данный скрипт исправляет все 2-ки и 
3-ки указанного ученика на 5-ки.
- `remove_chastisements` - для запуска требуется указать обьект класса `Schoolkid`. Данный скрипт удаляет все замечания 
от преподавателей у указанного ученика.
- `create_commendation(name, subject_title)` - для запуска требуется указать имя ученика(можно без отчества), а также 
название предмета. Данный скрипт добавляет похвалу от преподавателя за последний урок, у указанного ученика и предмета.