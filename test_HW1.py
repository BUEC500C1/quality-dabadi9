import HW1

def test_convertions():
  assert HW1.arabic_to_roman(100) == "C"
  assert HW1.arabic_to_roman(3999) == "MMMCMXCIX"
  assert HW1.arabic_to_roman(893) == "DCCCXCIII"
  assert HW1.arabic_to_roman(12) == "XII"
  assert HW1.arabic_to_roman(1213) == "MCCXIII"
  assert HW1.arabic_to_roman(432) == "CDXXXII"
  assert HW1.arabic_to_roman(932) == "CMXXXII"
  assert HW1.arabic_to_roman(1001) == "MI"
  assert HW1.arabic_to_roman(384) == "CCCLXXXIV"

 
def test_errors():
  assert HW1.arabic_to_roman("100") == "ERROR"
  assert HW1.arabic_to_roman(100.123) == "ERROR"
  assert HW1.arabic_to_roman("test") == "ERROR"
  assert HW1.arabic_to_roman(100.00) == "ERROR"
