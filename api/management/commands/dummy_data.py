from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Task  # Ensure correct import path
from faker import Faker
import random
from datetime import datetime, timezone

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy task data'

    def handle(self, *args, **kwargs):
        # Create or get 4 users
        users = []
        for i in range(4):
            user, created = User.objects.get_or_create(
                username=f"user{i+1}",
                defaults={"email": fake.email()}
            )
            users.append(user)

        tasks = []
        for _ in range(50):  # Adjust the number as needed
            task = Task(
                user=random.choice(users),  # Assign task to a random user
                task_id=random.randint(1, 10000),  # Ensure task_id is unique
                name=fake.sentence(nb_words=3),
                description=fake.paragraph(),
                created_at=datetime.now(timezone.utc),  # Ensure timezone-aware datetime
                updated_at=datetime.now(timezone.utc),
                completed=random.choice([True, False])
            )
            tasks.append(task)

        Task.objects.bulk_create(tasks)  # Efficient bulk insertion

        self.stdout.write(self.style.SUCCESS('✅ 50 fake tasks created successfully with 4 users!'))
