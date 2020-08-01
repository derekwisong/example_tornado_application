
class Interpreter(object):
    def evaluate(self, statement):
        return str(statement)

class CLI(object):
    def __init__(self, interpreter:Interpreter, prompt:str="> ", banner:str=None):
        """
        Create a CLI with a REPL.
        :param interpreter: The Interpreter that evaluate a statement
        """
        self.interpreter = interpreter
        self.prompt = prompt
        self.banner = banner
    
    def get_input(self):
        return input(self.prompt)
    
    def evaluate(self, statement):
        return self.interpreter.evaluate(statement)
    
    def display(self, result):
        print(result)

    def start(self):
        if self.banner:
            self.display(self.banner)

        try:
            while True:
                statement = self.get_input()
                result = self.evaluate(statement)
                self.display(result)
        except KeyboardInterrupt:
            pass



class PythonCLI(CLI):
    def __init__(self, prompt:str="> ", banner:str=None):
        super().__init__(Interpreter(), prompt=prompt, banner=banner)
    
    def evaluate(self, statement):
        """
        Evaluate the statement
        """

        try:
            return eval(statement)
        except Exception as e:
            return e


    def display(self, result):
        """
        Display the result of self.evaluate()
        """

        print(result)


def main():
    cli = PythonCLI(banner="PythonCLI: enter a python expression.")
    cli.start()

if __name__ == '__main__':
    main()