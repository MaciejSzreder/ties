import unittest

import tempfile,os

import scripts.HTMLtoXML


class Test_HTMLtoXML_basic(unittest.TestCase):
	def test_singleTag(self):
		try:
			with tempfile.NamedTemporaryFile(delete=False) as file:
				file.write(b"<html></html>");
			xml=scripts.HTMLtoXML.read_html(file.name);
			root=xml.getroot();
			self.assertEqual(root.tag,"html");
		finally:
			os.remove(file.name);


if __name__ == '__main__':
    unittest.main()