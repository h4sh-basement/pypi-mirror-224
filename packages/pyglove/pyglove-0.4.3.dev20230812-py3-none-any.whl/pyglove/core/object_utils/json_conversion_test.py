# Copyright 2022 The PyGlove Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for pyglove.object_utils.json_conversion."""

import abc
import typing
import unittest
from pyglove.core.object_utils import json_conversion
from pyglove.core.typing import inspect as pg_inspect


class X:
  """Classes with nested classes for testing purpose."""

  class Y:

    class Z:

      @classmethod
      def class_method(cls):
        return cls.__name__

      @staticmethod
      def static_method():
        return 1

      def instance_method(self):
        return str(self)


def bar():
  pass

T1 = typing.TypeVar('T1')
T2 = typing.TypeVar('T2')
T3 = typing.TypeVar('T3')
T4 = typing.TypeVar('T4')
T5 = typing.TypeVar('T5')


class G1(typing.Generic[T1]):
  pass


class G2(typing.Generic[T1, T2]):
  pass


class G3(typing.Generic[T1, T2, T3]):
  pass


class G4(typing.Generic[T1, T2, T3, T4]):
  pass


class G5(typing.Generic[T1, T2, T3, T4, T5]):
  pass


class JSONConvertibleTest(unittest.TestCase):
  """Tests for JSONConvertible type registry."""

  def test_registry(self):

    class A(json_conversion.JSONConvertible):

      @abc.abstractmethod
      def value(self):
        pass

    class B(A):

      def __init__(self, x):
        super().__init__()
        self.x = x

      def to_json(self):
        return A.to_json_dict({
            'x': self.x
        })

      def value(self):
        return self.x

    typename = lambda cls: f'{cls.__module__}.{cls.__qualname__}'

    # A is abstract.
    self.assertFalse(json_conversion.JSONConvertible.is_registered(typename(A)))
    self.assertTrue(json_conversion.JSONConvertible.is_registered(typename(B)))
    self.assertIs(
        json_conversion.JSONConvertible.class_from_typename(typename(B)), B)
    self.assertIn(
        (typename(B), B),
        list(json_conversion.JSONConvertible.registered_types()))

    class C(B):
      auto_register = False

    # Auto-register is off.
    self.assertFalse(json_conversion.JSONConvertible.is_registered(typename(C)))

    with self.assertRaisesRegex(
        KeyError, 'Type .* has already been registered with class .*'):
      json_conversion.JSONConvertible.register(typename(B), C)

    json_conversion.JSONConvertible.register(
        typename(B), C, override_existing=True)
    self.assertIn(
        (typename(B), C),
        list(json_conversion.JSONConvertible.registered_types()))

  def test_json_conversion(self):

    class T(json_conversion.JSONConvertible):

      def __init__(self, x):
        self.x = x

      def to_json(self):
        return T.to_json_dict(dict(x=self.x))

      def __eq__(self, other):
        return isinstance(other, T) and self.x == other.x

      def __ne__(self, other):
        return not self.__eq__(other)

    typename = lambda cls: f'{cls.__module__}.{cls.__qualname__}'
    json_value = json_conversion.to_json([(T(1), 2), {'y': T(3)}])
    self.assertEqual(json_value, [
        ['__tuple__', {'_type': typename(T), 'x': 1}, 2],
        {'y': {'_type': typename(T), 'x': 3}}
    ])
    self.assertEqual(json_conversion.from_json(json_value),
                     [(T(1), 2), {'y': T(3)}])

    # Test bad cases.
    with self.assertRaisesRegex(
        ValueError, 'Tuple should have at least one element besides .*'):
      json_conversion.from_json(['__tuple__'])

    with self.assertRaisesRegex(
        TypeError, 'Type name .* is not registered'):
      json_conversion.from_json({'_type': '__main__.ABC'})

  def assert_conversion_is(self, v):
    self.assertIs(json_conversion.from_json(json_conversion.to_json(v)), v)

  def assert_conversion_equal(self, v):
    self.assertEqual(json_conversion.from_json(json_conversion.to_json(v)), v)

  def test_json_conversion_for_types(self):
    # Built-in types.
    self.assert_conversion_is(int)
    self.assert_conversion_is(bool)
    self.assert_conversion_is(float)
    self.assert_conversion_is(str)
    self.assert_conversion_is(list)
    self.assert_conversion_equal(list[int])
    self.assert_conversion_is(tuple)
    self.assert_conversion_equal(tuple[int, int])
    self.assert_conversion_is(dict)
    self.assert_conversion_equal(dict[str, int])
    self.assert_conversion_is(Exception)
    self.assert_conversion_is(type(None))
    self.assert_conversion_is(...)
    self.assert_conversion_equal(typing.Callable[[int, int], None])
    self.assert_conversion_equal(typing.Callable[..., None])

    # User types.
    self.assert_conversion_is(X)
    self.assert_conversion_is(X.Y)
    self.assert_conversion_is(X.Y.Z)

    # Local type.
    class B:
      pass

    with self.assertRaisesRegex(
        ValueError, 'Cannot convert local class .* to JSON.'):
      json_conversion.to_json(B)

    # Generic types.
    self.assert_conversion_is(G1[int])
    self.assert_conversion_is(G2[int, int])
    self.assert_conversion_is(G3[int, int, int])
    self.assert_conversion_is(G4[int, int, int, int])
    with self.assertRaisesRegex(
        NotImplementedError,
        'Cannot convert generic type with more than 4 type arguments'):
      json_conversion.to_json(G5[int, int, int, int, int])

  def test_json_conversion_for_annotations(self):
    self.assert_conversion_is(typing.Any)
    self.assert_conversion_is(typing.List)
    self.assert_conversion_is(typing.List[typing.List[int]])
    self.assert_conversion_is(typing.Annotated[int, 'abc'])
    self.assert_conversion_is(typing.Dict[str, typing.Any])
    self.assert_conversion_is(typing.Union[int, str])
    self.assert_conversion_is(typing.Sequence[int])
    self.assert_conversion_is(typing.Set[int])
    self.assert_conversion_is(typing.FrozenSet[int])
    self.assert_conversion_is(typing.Mapping[int, str])
    self.assert_conversion_is(typing.MutableMapping[int, str])
    # Optional will be converted to Union[int, None]
    self.assert_conversion_equal(typing.Optional[int])

    with self.assertRaisesRegex(ValueError, 'Annotation cannot be converted'):
      json_conversion.to_json(typing.Literal)

  def test_json_conversion_for_functions(self):
    # Built-in functions.
    self.assert_conversion_is(print)
    self.assert_conversion_is(zip)
    self.assert_conversion_is(input)

    # User-defined functions.
    self.assert_conversion_is(bar)

    # Lambda function.
    s = lambda x, y=1: x + y
    s1 = json_conversion.from_json(json_conversion.to_json(s))
    self.assertTrue(pg_inspect.callable_eq(s1, s))
    self.assertEqual(s1(1), 2)
    self.assertEqual(s1(1, 2), 3)

    # Locally defined function.
    def baz(x, y=1):
      return x + y
    baz1 = json_conversion.from_json(json_conversion.to_json(baz))
    self.assertTrue(pg_inspect.callable_eq(baz1, baz))
    self.assertEqual(baz1(1), 2)
    self.assertEqual(baz1(1, 2), 3)

  def test_json_conversion_for_methods(self):
    # Test class-level method.
    f = json_conversion.from_json(json_conversion.to_json(X.Y.Z.class_method))
    self.assertEqual(f(), 'Z')

    # Test static method.
    self.assert_conversion_is(X.Y.Z.static_method)

    with self.assertRaisesRegex(
        ValueError, 'Cannot convert instance method .* to JSON.'):
      json_conversion.to_json(X.Y.Z().instance_method)


if __name__ == '__main__':
  unittest.main()
