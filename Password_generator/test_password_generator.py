import pytest
import mock

# import mocker
import builtins
import password_generator as pg


class Test_password_generator:
    def test_password_length(self):
        with mock.patch.object(builtins, "input", lambda _: "15"):
            assert pg.get_password_length() == 15

        with mock.patch.object(builtins, "input", lambda _: "5"):
            assert pg.get_password_length() == 5

    def test_password_length_valueError(self, mocker):
        inputs = iter(["43", "five", "5"])

        mocker.patch.object(builtins, "input", side_effect=lambda _: str(next(inputs)))
        with pytest.raises(ValueError):
            assert pg.get_password_length()


if __name__ == "__main__":
    pytest.main()
