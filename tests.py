import unittest
import asyncio

from async_foaas import Fuck


class FuckingTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.fuck = Fuck()

    async def test_url(self):
        url = self.fuck.off(name="Alice", from_="Bob").url
        self.assertEqual("http://foaas.dev/off/Alice/Bob", url)

    async def test_url_secure(self):
        secure_fuck = Fuck(secure=True)
        url = secure_fuck.everything(from_="Bob", secure=True).url
        self.assertEqual("https://foaas.dev/everything/Bob", url)

    async def test_url_quoting(self):
        url = self.fuck.donut(name="Alice!", from_="Bobby McGee").url
        self.assertEqual("http://foaas.dev/donut/Alice%21/Bobby%20McGee", url)

    async def test_html(self):
        html = await self.fuck.thanks(from_="Bob").html
        self.assertIn("<h1>Fuck you very much.</h1>", html)
        self.assertIn("<em>- Bob</em>", html)

    async def test_json(self):
        json = await self.fuck.life(from_="Bob").json
        self.assertEqual({"message": "Fuck my life.", "subtitle": "- Bob"}, json)

    async def test_text(self):
        text = await self.fuck.thanks(from_="Bob").text
        self.assertEqual("Fuck you very much. - Bob", text)

    async def test_random(self):
        self.fuck.random(from_="Chris")
        self.fuck.random(name="Tom", from_="Chris")
        self.fuck.random(name="Alice", from_="Bob", company="Acme")
        self.fuck.random(name="Alice", from_="Bob", reference="Clara")


if __name__ == "__main__":
    unittest.main()
