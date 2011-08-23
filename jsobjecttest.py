#!/usr/bin/env python

import jsobject
import unittest

class JSObject_Test(unittest.TestCase):
  def setUp(self):
    self.test_object = jsobject.JSObject({
      "name": "John Doe",
      "age": 20,
      "city": "Portland",
      "state": "Oregon"})

  def tearDown(self):
    pass

  def test_dotnotation(self):
    self.assertEqual(self.test_object.name, "John Doe")
    self.assertEqual(self.test_object.age, 20)
    self.assertEqual(self.test_object.city, "Portland")
    self.assertEqual(self.test_object.state, "Oregon")

  def test_bracketnotation(self):
    self.assertEqual(self.test_object['name'], "John Doe")
    self.assertEqual(self.test_object['age'], 20)
    self.assertEqual(self.test_object['city'], "Portland")
    self.assertEqual(self.test_object['state'], "Oregon")

  def test_assignment(self):
    self.test_object.name = "Jane Doe"
    self.assertEqual(self.test_object.name, "Jane Doe")
    self.test_object['age'] = 19
    self.assertEqual(self.test_object['age'], 19)

  def test_inspect(self):
    sample_data = {
      "name": "John Doe",
      "age": 20,
      "city": "Portland",
      "state": "Oregon"}
    for key in sample_data:
      self.assertEqual(self.test_object[key], sample_data[key])


if __name__ == '__main__':
  unittest.main()

