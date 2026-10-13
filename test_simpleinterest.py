from simpleinterest import simpInt

def test_simpleint_pos():
    assert simpInt(20000,8,12) == 19200

def test_simpleint_zer():
    assert simpInt(10000,7,0) == 0    