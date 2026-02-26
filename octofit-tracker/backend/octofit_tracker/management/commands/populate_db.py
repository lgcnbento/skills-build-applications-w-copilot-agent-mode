from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write('Creating users...')
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2026-02-25')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2026-02-25')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2026-02-25')
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date='2026-02-25')

        self.stdout.write('Creating workouts...')
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Strength and flexibility', suggested_for='DC')

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write('Ensuring unique index on email...')
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('Database populated with superhero test data!'))
