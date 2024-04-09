from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):

        student_list = [
            {'last_name': 'Ivanon', 'first_name': 'Ivan'},
            {'last_name': 'Petr', 'first_name': 'Petrov'},
            {'last_name': 'Semen', 'first_name': 'Semenov'},
            {'last_name': 'Klimenko', 'first_name': 'Danil'}
        ]

        # for student in student_list:
        #     Student.objects.create(**student)

        students_for_create = []
        for student in student_list:
            students_for_create.append(
                Student(**student)
            )

        Student.objects.bulk_create(students_for_create)
