import pytest
import calculator as cal

class Test_calculator():
    class Test_input():
        def test_non_digit_expression(self):
            assert cal.input_eval('Des') == False

        def test_non_string_expression(self):
            with pytest.raises(AttributeError):
                cal.input_eval(9+5)
            with pytest.raises(AttributeError):
                cal.input_eval([])
                
        def test_empty_expression(self):
            assert cal.input_eval('') == False

        def test_valid_expression(self):
            assert cal.input_eval('5/2') == True
            assert cal.input_eval('5*25') == True
            assert cal.input_eval('5+5-8-72') == True

        def test_invalid_expression_valid_characters(self):
            assert cal.input_eval('((5*2())/4)') == True

    class Test_math_evaluation():
        # def test_math_eval_nameError(self):
        #     with pytest.raises(NameError):
        #         cal.arithmetic_eval('5+p')
        ...