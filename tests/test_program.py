import src.program as program



def test_main():
    """
    Test that the program has a main function.
    :return:
    """

    assert "main" in dir(program)