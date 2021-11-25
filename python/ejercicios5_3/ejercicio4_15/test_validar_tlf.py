from funciones import validar_tlf

def test_validar_tlf():
    assert validar_tlf("123456789") == True