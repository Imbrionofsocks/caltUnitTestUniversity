import unittest
from main import add, subtract, multiply, divide, power, sqrtl, factorial
from rich.console import Console
from rich.traceback import install

install()
console = Console()

class RichTestResult(unittest.TextTestResult):
    def addError(self, test, err):
        super().addError(test, err)
        description = test.shortDescription() or str(test)
        console.print(f"[red]ОШИБКА[/red] in [bold]{description}[/bold]", style="red")
        console.print_exception()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        description = test.shortDescription() or str(test)
        console.print(f"[yellow]СБОЙ[/yellow] in [bold]{description}[/bold]", style="yellow")
        console.print_exception()

    def addSuccess(self, test):
        super().addSuccess(test)
        description = test.shortDescription() or str(test)
        console.print(f"[green]УСПЕХ[/green]: [bold]{description}[/bold] пройдены успешно", style="green")


class RichTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        kwargs['resultclass'] = RichTestResult
        super().__init__(*args, **kwargs)

    def run(self, test):
        result = super().run(test)
        return result

class TestCalculatorFunctions(unittest.TestCase):
    def shortDescription(self):
        return getattr(self, 'description', None)
    def test_add(self):
        self.description = 'Тесты сложения'
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.description = 'Тесты вычитания'
        self.assertEqual(subtract(8, 5), 3)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.description = 'Тесты умножения'
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.description = 'Тесты деления'
        self.assertEqual(divide(15, 5), 3)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 3), 10 / 3)
        self.assertEqual(divide(0, 5), 0)

    def test_power(self):
        self.description = 'Тесты возведения в степень'
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(-2, 2), 4)

    def test_sqrtl(self):
        self.description = 'Тесты квадратного корня'
        self.assertEqual(sqrtl(9), 3)
        self.assertEqual(sqrtl(25), 5)
        self.assertEqual(sqrtl(0), 0)

    def test_factorial(self):
        self.description = 'Тесты факториала'
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative(self):
        self.description = 'Негативные тесты'
        self.assertEqual(add("Привет", "а я не число"), "Error: Значения должны быть числом")
        self.assertEqual(subtract("Привет", "а я не число"), "Error: Значения должны быть числом")
        self.assertEqual(multiply("Привет", "а я не число"), "Error: Значения должны быть числом")
        self.assertEqual(divide("Привет", "а я не число"), "Error: Значения должны быть числом")
        self.assertEqual(power("Привет", "а я не число"), "Error: Значения должны быть числом")
        self.assertEqual(factorial(-5), "Error: Значения должны быть положительным числом")
        self.assertEqual(sqrtl(-16), "Error: Значения должны быть положительным числом")
        self.assertEqual(factorial("я не число"), "Error: Значения должны быть числом")
        self.assertEqual(sqrtl("я не число"), "Error: Значения должны быть числом")
        self.assertEqual(divide(5,0),"Error: Деление на 0.")

if __name__ == '__main__':
    unittest.main(testRunner=RichTestRunner())
