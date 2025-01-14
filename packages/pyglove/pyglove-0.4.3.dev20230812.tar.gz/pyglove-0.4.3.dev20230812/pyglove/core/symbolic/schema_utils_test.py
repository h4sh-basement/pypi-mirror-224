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
"""Tests for pyglove.symbolize."""

import unittest

from pyglove.core import object_utils
from pyglove.core.symbolic import schema_utils


class SchemaDescriptionFromDocStrTest(unittest.TestCase):
  """Tests for `schema_description_from_docstr`."""

  def test_none_doc_str(self):
    self.assertIsNone(schema_utils.schema_description_from_docstr(None))

  def test_short_description_only(self):
    docstr = object_utils.DocStr.parse(
        """This is a function.""")
    self.assertEqual(
        schema_utils.schema_description_from_docstr(docstr),
        'This is a function.')
    self.assertEqual(
        schema_utils.schema_description_from_docstr(
            docstr, include_long_description=True),
        'This is a function.')

  def test_long_description_only(self):
    docstr = object_utils.DocStr.parse(
        """This is a function.
        
        This is the longer explanation of the function.
        
        """)
    self.assertEqual(
        schema_utils.schema_description_from_docstr(docstr),
        'This is a function.')
    self.assertEqual(
        schema_utils.schema_description_from_docstr(
            docstr, include_long_description=True),
        ('This is a function.\n\n'
         'This is the longer explanation of the function.'))


if __name__ == '__main__':
  unittest.main()
