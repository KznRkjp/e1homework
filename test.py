import pytest
from .game import main

def test_check():
    assert main.check('sss','s') == [0,1,2]
    assert main.check('sss','k') == []
    assert main.check('test','t') == [0,3]

def test_show_word():
    assert main.show_word('******',[0,5],'l') == 'l****l'
    assert main.show_word('012345',[3],'x') == '012x45'
    assert main.show_word('012345',[],'x') == '012345'

def test_check_input():
    assert main.check_input('k',[]) == True
    assert main.check_input('k',['k']) == False
    assert main.check_input('kk',[]) == False
