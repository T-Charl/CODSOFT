import pytest
import calculator as cal


class Test_calculator:
    class Test_input:
        def test_non_digit_expression(self):
            assert cal.input_eval("Des") == False

        def test_non_string_expression(self):
            with pytest.raises(AttributeError):
                cal.input_eval(9 + 5)
            with pytest.raises(AttributeError):
                cal.input_eval([])

        def test_empty_expression(self):
            assert cal.input_eval("") == False

        def test_valid_expression(self):
            assert cal.input_eval("5/2") == True
            assert cal.input_eval("5*25") == True
            assert cal.input_eval("5+5-8-72") == True

        def test_invalid_expression_valid_characters(self):
            assert cal.input_eval("((5*2())/4)") == True

    class Test_math_evaluation:
        def test_math_eval_nameError(self):
            result = cal.arithmetic_eval("5+p")
            assert "Cannot evaluate expression" in result

        def test_valid_char_invalid_expression(self):
            result = cal.arithmetic_eval("5+5)")
            assert "Cannot evaluate expression" == result

        def test_ZeroDivisionError(self):
            result = cal.arithmetic_eval("(5+5)%0")
            assert "Cannot divide by zero" == result

        def test_valid_expressiom(self):
            result = cal.arithmetic_eval("(5+5)%2")
            assert 0 == result
            result = cal.arithmetic_eval("(5+5)%2*9")
            assert 0 == result
            result = cal.arithmetic_eval("(555+5)/2+5*9")
            assert 325 == result

if __name__ == "__main__":
    pytest.main()