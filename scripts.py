import random
from datacenter.models import Schoolkid, Teacher, Subject, Lesson, Mark, Chastisement, Commendation


def fix_marks(schoolkid):
    marks = [i for i in Mark.objects.filter(schoolkid=schoolkid,
                                            points__in=[2, 3])]
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(name, subject_title):
    try:
        child = Schoolkid.objects.get(full_name__contains=name)
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

    except Schoolkid.DoesNotExist:
        return f'Ученик с именем "{name}" не найден'
    except Schoolkid.MultipleObjectsReturned:
        return f'Найдено несколько учеников с именем "{name}"'
