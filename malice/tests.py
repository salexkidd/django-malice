from django.test import TestCase, Client, override_settings
from django.contrib.auth.models import User

try:
    from django.urls import reverse
except:
    from django.core.urlresolvers import reverse


class MaliceTestForAdmin(TestCase):
    """
    Request user is superuser.
    (User gets each error on malice view function)
    """
    def setUp(self):
        admin = User.objects.create_superuser('myuser', 'myemail@test.com', "test_password")
        self.client = Client()
        self.client.force_login(admin)
        super().setUp()

    def test_ok(self):
        res = self.client.get(reverse("malice:ok"))
        self.assertEqual(res.status_code, 200)

    def test_permission_denied(self):
        res = self.client.get(reverse("malice:permission-denied"))
        self.assertEqual(res.status_code, 403)

    def test_not_found(self):
        res = self.client.get(reverse("malice:not-found"))
        self.assertEqual(res.status_code, 404)

    def test_internal_server_error(self):
        with self.assertRaises(ValueError):
            self.client.get(reverse("malice:internal-server-error"))


@override_settings(MALICE_ADMIN_ONLY=False)
class MaliceTestForNonAdminUserWhenAdminOnlyIsFalse(MaliceTestForAdmin):
    """
    Request user is not superuser but, MALICE_ADMIN_ONLY is False.
    (User gets each error on malice view function)
    """
    def setUp(self):
        self.client = Client()
        super().setUp()


class MaliceTestForNonAdminUser(TestCase):
    """
    Request user is not superuser but, MALICE_ADMIN_ONLY is True.
    (User gets 404 status on all malice view function)
    """

    def setUp(self):
        self.client = Client()
        super().setUp()

    def test_ok(self):
        res = self.client.get(reverse("malice:ok"))
        self.assertEqual(res.status_code, 404)

    def test_permission_denied(self):
        res = self.client.get(reverse("malice:permission-denied"))
        self.assertEqual(res.status_code, 404)

    def test_not_found(self):
        res = self.client.get(reverse("malice:not-found"))
        self.assertEqual(res.status_code, 404)

    def test_internal_server_error(self):
        res = self.client.get(reverse("malice:internal-server-error"))
        self.assertEqual(res.status_code, 404)

