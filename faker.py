from faker import Faker
from blog.models import Blog
for i in range(1000):
    myfaker = Faker(seed=i)
    blog = Blog()
    blog.title = myfaker.name()
    blog.body = myfaker.text()
    blog.save()