from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from school_users.models import Guest, Student, User
from programs.models import StudentApplications
from askuala.serializers import UserSerializer

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_guest_when_created(sender, **kwargs):
    if kwargs['created']:
        Guest.objects.create(user=kwargs['instance'])


@receiver(post_save, sender=StudentApplications)
def create_student_when_accepted(sender, **kwargs):
    if kwargs['instance'].accepted:
        user = User.objects.get(id=kwargs['instance'].user.id)
        user.user_type = 'student'
        user.save()
        Student.objects.create(user_id = kwargs['instance'].user.id,
                                enrolledProgram=kwargs['instance'].program,
                                batch=kwargs['instance'].batch,
                                enrolledDepartment=kwargs['instance'].department)
