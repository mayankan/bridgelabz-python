from testing_programs import vending_machine as vm


def test_vending_machine():
    assert vm.vending_machine(1000) == "1000 X 1"
