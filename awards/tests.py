from django.test import TestCase

from .models import Profile, Projects

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.liz = Profile(id = 125, profile_pic = "",bio = "I love traveling", userId = 1)

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.liz,Profile))
    
    def test_initialization(self):
        self.assertEqual(self.liz.profile_pic,"")
        self.assertEqual(self.liz.bio, "I love traveling")
        self.assertEqual(self.liz.userId, 1)

    # Testing Save method
    def test_save(self):
        self.liz.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    # Testing Delete method
    def test_delete(self):
        self.liz.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Profile class test
        self.liz = Profile( bio = "I love traveling", userId = 1)

        # Project class Test
        self.project = Projects(title = "Life", project_image = " ",description="nature goodness",url = "", date = "10/2/2019", poster_id = 2)
        self.project.save_project()


    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Projects))

    # Testing Save method
    def test_save_method(self):
        self.project.save_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)

    # Testing Delete method
    def test_delete_method(self):
        self.project.delete_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects) == 0)


    # Testing getting project by id 
    def test_get_project(self):
        projects = Projects.get_project(self.project.id)
        self.assertTrue(projects == self.project)

class RateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='cecilia')
        self.post = Project.objects.create(id=1, title='test post', image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', details='desc',
                                        user=self.user, link='http://ur.coml')
        self.rating = Rate.objects.create(id=1, design=6, usability=7, creativity=9, content=9, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rate))

    def test_save_rating(self):
        self.rating.save_rate()
        rating = Rate.objects.all()
        self.assertTrue(len(rating) > 0)