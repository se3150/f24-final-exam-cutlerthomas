import pytest
from unittest.mock import Mock
from brute import Brute

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def cracker():
    return Brute("TDD")

@pytest.fixture
def mock_randomGuess_correct(mocker):
    return mocker.patch.object(Brute, 'randomGuess', return_value="TDD")

@pytest.fixture
def mock_randomGuess_incorrect(mocker):
    return mocker.patch.object(Brute, 'randomGuess', return_value="LLLL")

@pytest.fixture
def mock_hash(mocker):
    return mocker.patch.object(Brute, 'hash', return_value="hash")

def describe_Brute():

    def describe_bruteOnce():
        
        def it_returns_true_when_attempt_is_correct(cracker):
            target = cracker
            assert target.bruteOnce("TDD") == True

        def it_returns_false_when_attempt_is_wrong(cracker):
            target = cracker
            assert target.bruteOnce("LLLLLLLLL") == False

        def it_returns_false_when_there_is_extra_whitespace(cracker):
            target = cracker
            assert target.bruteOnce(" TDD ") == False

        def it_returns_false_when_caps_are_wrong(cracker):
            target = cracker
            assert target.bruteOnce("tdd") == False

    def describe_bruteMany():
        
        def it_calls_randomGuess_once_when_correct(cracker, mock_randomGuess_correct):
            target = cracker
            target.bruteMany()
            mock_randomGuess_correct.assert_called_once()

        def it_calls_randomGuess_multiple_when_wrong(cracker, mock_randomGuess_incorrect):
            target = cracker
            target.bruteMany(limit=1000)
            mock_randomGuess_incorrect.assert_called_with()

        def it_calls_hash_to_check_guess(cracker, mock_hash):
            target = cracker
            target.bruteMany(limit=1000)
            mock_hash.assert_called()

        def it_passes_correct_value_to_hash(cracker, mock_randomGuess_correct, mock_hash):
            target = cracker
            target.bruteMany(limit=1000)
            mock_hash.asset_called_with("TDD")
