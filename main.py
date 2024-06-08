from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from syllogism_checker.logic_checker import check_syllogism

class SyllogismCheckerApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        
        self.syllogism_input = TextInput(hint_text="Paste your syllogism here", size_hint=(1, 0.7))
        self.root.add_widget(self.syllogism_input)
        
        self.check_button = Button(text="Check logic", size_hint=(1, 0.1))
        self.check_button.bind(on_press=self.check_logic)
        self.root.add_widget(self.check_button)
        
        self.result_label = Label(size_hint=(1, 0.2))
        self.root.add_widget(self.result_label)
        
        return self.root

    def check_logic(self, instance):
        syllogism = self.syllogism_input.text
        errors = check_syllogism(syllogism)
        if errors:
            self.result_label.text = "Errors found:\n" + "\n".join(errors)
        else:
            self.result_label.text = "No errors found. The syllogism is valid."

if __name__ == '__main__':
    SyllogismCheckerApp().run()