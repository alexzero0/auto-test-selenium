test-main:
	pytest -s -v --tb=line --language=en test_main_page.py

test-product:
	pytest -s -v --tb=line --language=en test_product_page.py

test-product-single:
	pytest -s -v --tb=line --language=en test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_main_page