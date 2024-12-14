from django.contrib.auth.models import User

#FLAW-5
admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
beep = User.objects.create_user(username='beep', password='saysboop')
boop = User.objects.create_user(username='boop', password='saysbeep')

#FLAW-5
admin.save()
beep.save()
boop.save()