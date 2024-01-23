# async_foaas

A simple Async Python library to [FOAAS].

* **Author**: [Alex Raskin]
* **Version**: 0.3.0
* **License**: [MIT]

## Documentation

### Installation

This package relies on [httpx], [async-property]  and should be installed with [pip]:

```python
pip install async-foaas
```

### Basic Usage

Fuck off:

```python
from async_foaas import Fuck
import asyncio

fuck = Fuck(secure=True)

async def main():
  fuck_off = await fuck.off(name='Tom', from_='Chris').text
  print(fuck_off)

asyncio.run(main())
```

Give me some fucking JSON:

```python
print(await fuck.that(from_='Chris').json)
{u'message': u'Fuck that.', u'subtitle': u'- Chris'}
```

Just get the fucking URL:

```python
print(fuck.everything(from_='Chris').url)
http://foaas.dev/everything/Chris
```

Give me some random fucking things:

```python
print(await fuck.random(from_='Chris').text)
Fuck you very much. - Chris

print(await fuck.random(from_='Chris').text)
Fuck my life. - Chris

print (await fuck.random(name='Tom', from_='Chris').text)
Fuck me gently with a chainsaw, Tom. Do I look like Mother Teresa? - Chris

print(await fuck.random(name='Tom', from_='Chris').text)
Fuck off, Tom. - Chris
```

### Supported Actions

* `fuck.awesome(from_)`
* `fuck.ballmer(name, company, from_)`
* `fuck.because(from_)`
* `fuck.bus(name, from_)`
* `fuck.bye(from_)`
* `fuck.caniuse(namer, from_)`
* `fuck.chainsaw(name, from_)`
* `fuck.cool(from_)`
* `fuck.diabetes(from_)`
* `fuck.donut(name, from_)`
* `fuck.everyone(from_)`
* `fuck.everything(from_)`
* `fuck.fascinating(from_)`
* `fuck.field(name, from_, reference)`
* `fuck.flying(from_)`
* `fuck.king(name, from_)`
* `fuck.life(from_)`
* `fuck.linus(name, from_)`
* `fuck.madison(name, from_)`
* `fuck.nugget(name, from_)`
* `fuck.off(name, from_)`
* `fuck.outside(name, from_)`
* `fuck.pink(from_)`
* `fuck.thanks(from_)`
* `fuck.that(from_)`
* `fuck.thing(thing, from_)`
* `fuck.this(from_)`
* `fuck.random(name, from_)`
* `fuck.shakespeare(name, from_)`
* `fuck.what(from_)`
* `fuck.xmas(name, from_)`
* `fuck.yoda(name, from_)`
* `fuck.you(name, from_)`

### tl;dr

```python
foaas.Fuck([secure=True]).<action>(**kwargs)[.<url|html|text|json>]
```

### Testing

```python
$ python tests.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.724s

OK
```

[FOAAS]: http://foaas.dev/
[Alex Raskin]: https://alexraskin.com
[MIT]: https://github.com/alexraskin/foaas-python/blob/master/LICENSE
[httpx]: https://www.python-httpx.org/
[async-property]: https://github.com/ryananguiano/async_property
[pip]: http://www.pip-installer.org/
