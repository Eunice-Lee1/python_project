import pytest
from .my_functions import Player
def test_player_set_name():
	p = Player()
	assert p.name == ''
	p.set_name('Daniel')
	assert p.name == 'Daniel'

def test_build_fire():
	p = Player()
	p.wood = 5
	p.build_fire() 
	assert p.fire == 2
	assert p.wood == 0

def test_eat_food():
	p = Player()
	p.food = 1
	p.eat_food()
	assert p.food == 0

def test_find_food():
	p = Player()
	p.knife_dur = 0
	p.find_food()
	assert p.food == 0

	p.knife_dur = 1
	p.find_food()
	assert p.food == 1

def test_find_wood():
	p = Player()
	p.knife_dur = 2 
	p.find_wood()
	assert p.wood == 0

	p.knife_dur = 3
	p.find_wood()
	assert p.wood == 5

def test_check_knife():
	p = Player()
	p.knife_dur = 5
	dmg = 5
	assert p.check_knife(dmg)

