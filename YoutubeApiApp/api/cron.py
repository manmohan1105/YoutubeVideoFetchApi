from .models import Category
import random
def my_scheduled_job():
  number=random.randint(0,100)
  Category.objects.create(category_name=number)
  