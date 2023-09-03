import random
from datacenter.models import Schoolkid, Teacher, Subject, Lesson, Mark, Chastisement, Commendation


def get_child(name):
    try:
        child = Schoolkid.objects.get(full_name__contains=name)
        return child
    except Schoolkid.DoesNotExist:
        return f'Ученик с именем "{name}" не найден'
    except Schoolkid.MultipleObjectsReturned:
        return f'Найдено несколько учеников с именем "{name}"'


def fix_marks(name):
    child = get_child(name)
    try:
        Mark.objects.filter(schoolkid=child, points__in=[2, 3]).update(points=5)
    except ValueError:
        return child


def remove_chastisements(name):
    child = get_child(name)
    try:
        Chastisement.objects.filter(schoolkid=child).delete()
    except ValueError:
        return child


def create_commendation(name, subject_title):
    child = get_child(name)
    try:
        year_of_study = child.year_of_study
        group_letter = child.group_letter
        date_of_last_lesson = Lesson.objects.filter(year_of_study=year_of_study,
                                                    group_letter=group_letter,
                                                    subject__title=subject_title).order_by('-date').first().date

        subject = Subject.objects.get(title=subject_title,
                                      year_of_study=year_of_study)

        teacher = Lesson.objects.filter(year_of_study=year_of_study,
                                        group_letter=group_letter,
                                        subject__title=subject_title).order_by('-date').first().teacher

        with open('praise.txt', 'r') as file:
            phrases = file.readlines()
            random_phrase = random.choice(phrases).strip('\n')

        Commendation.objects.create(text=random_phrase,
                                    created=date_of_last_lesson,
                                    schoolkid=child,
                                    subject=subject,
                                    teacher=teacher)
    except AttributeError:
        return child
