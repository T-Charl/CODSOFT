import pytest
import mock
import builtins
import rock_paper_scissors as rsp

class Test_rock_paper_scissors:
    def test_user_win_outcomes(self):
        assert rsp.determine_winner("rock", "scissors") == "user"
        assert rsp.determine_winner("paper", "rock") == "user"
        assert rsp.determine_winner("scissors", "paper") == "user"


    def test_user_lose_outcomes(self):
        assert rsp.determine_winner("rock", "paper") == "comp"
        assert rsp.determine_winner("paper", "scissors") == "comp"
        assert rsp.determine_winner("scissors", "rock") == "comp"


    def test_draw_outcome(self):
        assert rsp.determine_winner("rock", "rock") == "both"
        assert rsp.determine_winner("paper", "paper") == "both"
        assert rsp.determine_winner("scissors", "scissors") == "both"


    def test_computer_choice(self):
        for i in range(100):
            choice = rsp.computer_choice()
            assert choice in ["rock", "paper", "scissors"]

    def test_user_choices(self):
        with mock.patch.object(builtins, 'input', lambda _: 'paper '):
            assert rsp.get_user_choice(0,0,0) == 'paper'

        with mock.patch.object(builtins, 'input', lambda _: 'p'):
            assert rsp.get_user_choice(0,0,0) == 'paper'

        with mock.patch.object(builtins, 'input', lambda _: 'r'):
            assert rsp.get_user_choice(0,0,0) == 'rock'
        
        with mock.patch.object(builtins, 'input', lambda _: ' rock'):
            assert rsp.get_user_choice(0,0,0) == 'rock'
        
        with mock.patch.object(builtins, 'input', lambda _: 's'):
            assert rsp.get_user_choice(0,0,0) == 'scissors'
        
        with mock.patch.object(builtins, 'input', lambda _: ' SciSsors '):
            assert rsp.get_user_choice(0,0,0) == 'scissors'
        
        # with mock.patch.object(builtins, 'input', lambda _: 'soap\p'):
        #     assert rsp.get_user_choice(0,0,0) == 'paper'
        
    
    def test_exit_1(self):
        with pytest.raises(SystemExit) as exit:
            with mock.patch.object(builtins, 'input', lambda _: ' exit'):
                rsp.get_user_choice(0,0,0)
                assert exit.value.code == 1
    

    def test_exit_2(self):
        with pytest.raises(SystemExit) as exit:
            with mock.patch.object(builtins, 'input', lambda _: ' Done '):
                rsp.get_user_choice(0,0,1)
                assert exit.value.code == 1

    def test_exit_3(self):
        with pytest.raises(SystemExit) as exit:
            with mock.patch.object(builtins, 'input', lambda _: '   qUiT  '):
                rsp.get_user_choice(5,10,8)
                assert exit.value.code == 1