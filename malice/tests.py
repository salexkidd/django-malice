from django.test import TestCase, Client

try:
    from django.urls import reverse
except:
    from django.core.urlresolvers import reverse


class MaliceTest(TestCase):

    def setUp(self):
        self.client = Client()
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
