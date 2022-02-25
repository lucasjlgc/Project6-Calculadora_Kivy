from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.window import Window


#Configurar dimensões do APP
Window.size = (500,700)

#Designando Arquivo Kv
Builder.load_file("calculadora.kv")

class MyLayout(Widget):
    def Clear(self):
        self.ids.calc_input.text = "0"

    #Criando botões que irão agir quando pressionamos

    def button_press(self,button):
        #Criando uma variavel que esta dentro da variavel já
        prior = self.ids.calc_input.text

        #Determinar se zero esta no campo
        if prior =="0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            #Caso não exista zero, deixar o campo de texto como esta mais o botão pressionado
            self.ids.calc_input.text =f"{prior}{button}"

    #Criando uma função de adição
    def add(self):
        #Prior é igual ao campo de texto e o que contem nele
        prior = self.ids.calc_input.text

        #coloque um sinal de + no texto que já existe no campo.
        self.ids.calc_input.text = f"{prior}+"

    def multiply(self):
        #Prior é igual ao campo de texto e o que contem nele
        prior = self.ids.calc_input.text

        #coloque um sinal de X no texto que já existe no campo.
        self.ids.calc_input.text = f"{prior}*"

    def subtract(self):
        #Prior é igual ao campo de texto e o que contem nele
        prior = self.ids.calc_input.text

        #coloque um sinal de - no texto que já existe no campo.
        self.ids.calc_input.text = f"{prior}-"

    def divide(self):
        #Prior é igual ao campo de texto e o que contem nele
        prior = self.ids.calc_input.text

        #coloque um sinal de / no texto que já existe no campo.
        self.ids.calc_input.text = f"{prior}/"
    def equal(self):
        prior = self.ids.calc_input.text

        #Avalia a matematica na caixa de texto
        resposta = eval(prior)

        #Output da resposta
        self.ids.calc_input.text = str(resposta)


    """
    
    #CODIFICAÇÃO MANUAL DA FUNÇÃO EVAL
    Autor: João Lucas Gama do Couto.     
        #Adição
    
        if "+" in prior:
            num_list = prior.split("+")
            resposta = 0


            #Loop para nossa lista
            for number in num_list:
                resposta = resposta + int(number)

            self.ids.calc_input.text = f"{resposta}"

        #Multiply
        elif "x" in prior:
            num_list = prior.split("x")
            resposta = 1


            #Loop para nossa lista
            for number in num_list:
                resposta = resposta * int(number)

            self.ids.calc_input.text = f"{resposta}"

            # Divide
        elif "/" in prior:
            num_list = prior.split("/")
            resposta = eval(prior)

            # Loop para nossa lista
            for number in num_list:
                resposta =   int(number) / resposta

            self.ids.calc_input.text = f"{resposta}"

        elif "-" in prior:
            num_list = prior.split("-")
            resposta = 0

            # Loop para nossa lista
            for number in num_list:
                resposta = int(number) - resposta

            self.ids.calc_input.text = f"{resposta * -1}"

"""

class calculatorApp(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return MyLayout()

if __name__=="__main__":
    calculatorApp().run()