from lista_de_compras import ShoppingList 

def test_add_and_remove_item():
    shopping = ShoppingList()
    shopping.add_item("Maçã", 1.50)
    assert "Maçã" in shopping.items
    assert shopping.items["Maçã"] == 1.50
    shopping.remove_item("Maçã")
    assert "Maçã" not in shopping.items

def test_show_items(capsys):
    shopping = ShoppingList()
    shopping.add_item("Pão", 3.75)
    shopping.show_items()
    captured = capsys.readouterr()
    assert "Pão: R$3.75" in captured.out

def test_calculate_total(capsys):
    shopping = ShoppingList()
    shopping.add_item("Banana", 2.00)
    shopping.add_item("Água", 1.00)
    shopping.calculate_total()
    captured = capsys.readouterr()
    assert "Total de gastos: R$3.00"  in captured.out

def test_empty_list(capsys):
    shopping = ShoppingList()
    shopping.show_items()
    captured = capsys.readouterr()
    assert "Sua lista de compras está vazia." in captured.out
