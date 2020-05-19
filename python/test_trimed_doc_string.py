import textwrap


def trim_doc_string(text):
    return textwrap.dedent(text).strip()


def test_trim_doc_string():
    expected = """key1: value1
key2:
  key3: [1, 2, 3]"""

    text = """
    key1: value1
    key2:
      key3: [1, 2, 3]
    """

    assert trim_doc_string(text) == expected
