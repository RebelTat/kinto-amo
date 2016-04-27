from kinto_amo.tests.support import AMOTestCase


class HelloViewTest(AMOTestCase):

    def test_capability_is_exposed(self):
        resp = self.app.get('/')
        capabilities = resp.json['capabilities']
        self.assertIn('amo', capabilities)

        expected = {'url': 'https://github.com/mozilla-services/kinto-amo/',
                    'description': 'An endpoint to generate v2 and v3 XML '
                    'blocklist export.'}
        self.assertEqual(expected, capabilities['amo'])
