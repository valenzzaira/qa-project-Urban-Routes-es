import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import unittest


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    set_phone_number = (By.CLASS_NAME, 'np-text')
    phone_code = (By.ID, 'phone')
    phone_number = (By.XPATH, '//*[@id="phone"]')
    button_next_xpath = (By.XPATH, '//button[text()="Siguiente"]')
    input_code = (By.ID, 'code') #confirmacion sms
    close_buton_in_code = (By. XPATH, '(//div[contains(@class,"number-picker open")]//div[contains(@class,"section active")]//button[contains(@class, "close-button")])[1]')
    confirm_button = (By.XPATH, '//button[text()="Confirmar"]')
    button_payment_method = (By.CLASS_NAME, 'pp-text')
    button_add_card = (By.CLASS_NAME, "pp-plus")
    input_credit_card_id = (By.ID,"number")
    input_card_cvv_xpath = (By.NAME,"code")
    submit_card_xpath = (By.XPATH, '//*[text()="Agregar"]')
    button_close_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    input_comment = (By.CSS_SELECTOR, "#comment")
    checkbox_bket_scrvs_xpath = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    checkbox_slide = (By.CLASS_NAME, "switch-input")
    ice_cream = (By.CLASS_NAME, "counter-plus")
    counter_value = (By.CLASS_NAME, 'counter-value')
    counter_ice_cream_2 = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    button_smart_order = (By.CLASS_NAME, "smart-button-main")
    order_header = (By.CLASS_NAME, 'order-header-title')
    burger_botton = (By.XPATH, "//img[@alt='burger']")
    modal_order = (By.CLASS_NAME, "order-details")
    de_recogida = (By.XPATH, "//div[normalize-space()='Lugar de recogida']")
    lu_destino = (By.XPATH, "//div[normalize-space()='Dirección de destino']")


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_call_taxi_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.call_taxi_button)
        )
        return self.driver.find_element(*self.call_taxi_button)

    def click_call_taxi_button(self):
        button = self.get_call_taxi_button()  # Retrieve the WebElement
        button.click()

    def get_comfort_mode(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort)
        )
        return self.driver.find_element(*self.comfort)

    def click_comfort_mode(self):
        button = self.get_comfort_mode()
        button.click()


    def get_phone_number_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.set_phone_number)
        )
        return self.driver.find_element(*self.set_phone_number)

    def click_phone_number_button(self):
        button = self.get_phone_number_button()
        button.click()

    def add_phone_number(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.phone_code).send_keys(data.phone_number)


    def input_phone_number(self):
        self.driver.implicitly_wait(10)
        self.click_phone_number_button()
        self.driver.implicitly_wait(10)
        self.add_phone_number()
        self.click_next_button()
        self.code_number()
        self.click_on_confirm_button()


    def get_next_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.button_next_xpath)
        )
        return self.driver.find_element(*self.button_next_xpath)

    def click_next_button(self):
        button = self.get_next_button()
        button.click()

    def code_number(self):
        self.driver.implicitly_wait(15)
        phone_code = retrieve_phone_code(driver=self.driver)
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.input_code).send_keys(phone_code)

    def get_confirm_info(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.confirm_button)
        )
        return self.driver.find_element(*self.confirm_button)

    def click_on_confirm_button(self):
        button = self.get_confirm_info()
        button.click()



    def get_phone(self):
        self.click_phone_number_button()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.phone_number))
        )
        return element.get_property('value')


    def get_payment_card(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.button_payment_method)
        )
        element = self.driver.find_element(*self.button_payment_method)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        return element


    def get_add_card(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.button_add_card)
        )
        return self.driver.find_element(*self.button_add_card)

    def click_add_card(self):
        button = self.get_add_card()
        button.click()

    def input_number(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.input_credit_card_id).send_keys(data.card_number)

    def get_card_input(self):
        return self.driver.find_element(*self.input_credit_card_id).get_property('value')

    def code_card_input(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.input_card_cvv_xpath).send_keys(data.card_code)

    def cvv_code(self):
        self.driver.implicitly_wait(15)
        self.code_card_input()

    def get_cvv_card(self):
        return self.driver.find_element(*self.input_card_cvv_xpath).get_property('value')

    def registered_card(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.submit_card_xpath).click()

    def close_button_payment(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.button_close_xpath)
        )
        self.driver.find_element(*self.button_close_xpath).click()

    def get_comment_input(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.input_comment)
        )
        return self.driver.find_element(*self.input_comment)

    def send_message_to_conductor(self):
        message = self.get_comment_input()
        message.send_keys(data.message_for_driver)

    def get_message(self):
        return self.driver.find_element(*self.input_comment).get_property('value')

    def get_blanket_scarfs_slide(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.checkbox_bket_scrvs_xpath)
        )
        element = self.driver.find_element(*self.checkbox_bket_scrvs_xpath) #added the * to unpack the locator
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element  # Devuelve el elemento

    def click_blanket_and_hndkrs(self):
        slide = self.get_blanket_scarfs_slide()
        slide.click()

    def get_blancket_hndrk_info(self):
        slider = self.driver.find_elements(*self.checkbox_slide)
        return slider[0].get_property('checked')

    def click_ice_cream(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.ice_cream).click()
        self.driver.find_element(*self.ice_cream).click()

    def get_ice_cream_counter(self):
        return self.driver.find_element(*self.counter_value).text

    def order_taxi(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.button_smart_order)
        )
        self.driver.find_element(*self.button_smart_order).click()

    def get_order_head(self):
        return self.driver.find_element(*self.order_header).text

    def click_burger(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.burger_botton)
        )
        self.driver.find_element(*self.burger_botton).click

    def get_order_info(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.order_header)
        )
        self.driver.find_element(*self.order_header).get_property('value')






class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    #1. Definir la ruta
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        #Verificacion de la direccion
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    #2.Seleccionar la  tarifa Comfort
    def test_select_comfort_rate(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi_button()
        routes_page.click_comfort_mode()

        #Verificacion de la tarifa
        assert routes_page.get_comfort_mode().text in "Comfort"

    #3. Rellenar el campo del telefono y recibir codigo
    def test_code_phone_number(self):
        self.test_select_comfort_rate()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_button()
        routes_page.add_phone_number()
        self.driver.implicitly_wait(50)
        routes_page.click_next_button()
        routes_page.code_number()
        routes_page.click_on_confirm_button()

        #Verificar numero de telefono
        phone_number = routes_page.get_phone()
        assert phone_number == data.phone_number


        #4.Agregar una tarjeta de crédito
    def test_payment_click(self):
        self.test_select_comfort_rate()
        routes_page = UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(50)
        routes_page.get_payment_card()
        routes_page.click_add_card()
        routes_page.input_number()
        routes_page.cvv_code()
        routes_page.registered_card()
        routes_page.close_button_payment()

        # Verificar que el número de tarjeta ingresado es el esperado
        card_number = routes_page.get_card_input()
        assert card_number == data.card_number, f"credit card esperada {data.card_number}, pero se tiene {card_number}"
        # Verificar que el código CVV ingresado es el esperado
        cvv_code = routes_page.get_cvv_card()
        assert cvv_code == data.card_code, f"CVV code esperado {data.card_code}, pero se tiene {cvv_code}"

        #5. Escribir mensaje al conductor
    def test_send_message(self):
        self.test_payment_click()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.send_message_to_conductor()
        # Verificar que el mensaje se haya ingresado correctamente
        message = routes_page.get_message()
        assert message == data.message_for_driver, f"Mensaje esperado {data.message_for_driver}, pero se tiene {message}"

        #6. Pedir una manta y pañuelos.
    def test_add_blanket_hndrsk(self):
        self.test_send_message()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_hndkrs()
        # Verificar que el switch este activado
        assert routes_page.get_blancket_hndrk_info() == True

        #7. Pedir 2 helados
    def test_add_two_ice(self):
        self.test_add_blanket_hndrsk()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_ice_cream()
        # Verificar que se hayan agregado los helados

        assert routes_page.get_ice_cream_counter() == '2'

        #8. Aparece el modal para buscar un taxi.
    def test_taxi_ordering(self):
        self.test_add_two_ice()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_taxi()

        #Verificar informacion de la ruta
        assert routes_page.get_order_head() in  "Buscar automóvil"

        #9. Esperar a que aparezca la información del conductor en el modal
    def test_order_details(self):
        self.test_taxi_ordering()
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(50)
        #Verificar el texto del header
        order_info = routes_page.get_order_info()
        if order_info is not None:
            assert 'El conductor llegará' in order_info, f"Se esperaba 'El conductor llegará', pero se tiene: {order_info}"
        else:
            self.fail("La información del pedido no se encontró.")





    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
