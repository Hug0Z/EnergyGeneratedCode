import os
from importlib import import_module
from types import ModuleType

folder_path = "/home/hugo/TestingCode"

for benchmark in os.listdir(folder_path):
    print(f"\n--===={benchmark}====--")
    check_module_path = os.path.join(folder_path, benchmark, "check.py")
    if os.path.exists(check_module_path):
        check_module = import_module(f"TestingCode.{benchmark}.check")
        check_function = getattr(check_module, "check")
        for file in sorted(os.listdir(os.path.join(folder_path, benchmark))):
            if file.endswith(".py") and not file.startswith("check"):
                module_name = os.path.splitext(file)[0]
                generated_module = import_module(
                    f"TestingCode.{benchmark}.{module_name}"
                )
                if hasattr(generated_module, benchmark):
                    fun = getattr(generated_module, benchmark)
                    try:
                        try:
                            check_function(fun)
                        except IndexError as e:
                            print(
                                f"\033[1;31mFailure:\033[0m \033[1m{module_name} failed the checks. {e}\033[0m"
                            )
                        else:
                            print(
                                f"\033[1;32mSuccess:\033[0m \033[1m{module_name} passed the checks.\033[0m"
                            )
                    except AssertionError as e:
                        print(
                            f"\033[1;31mFailure:\033[0m \033[1m{module_name} failed the checks. {e}\033[0m"
                        )
