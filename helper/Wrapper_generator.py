import time

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

functions = [
    """from typing import List def has_close_elements(numbers: List[float], threshold: float) -> bool: \"\"\" Check if in given list of numbers, are any two numbers closer to each other than given threshold. >>> has_close_elements([1.0, 2.0, 3.0], 0.5) False >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) True\"\"\"""",
    """from typing import List def separate_paren_groups(paren_string: str) -> List[str]: \"\"\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to separate those group into separate strings and return the list of those. Separate groups are balanced (each open brace is properly closed) and not nested within each other Ignore any spaces in the input string.>>> separate_paren_groups('( ) (( )) (( )( ))')['()', '(())', '(()())']\"\"\"""",
    """def truncate_number(number: float) -> float: \"\"\" Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1). Return the decimal part of the number. >>> truncate_number(3.5) 0.5 \"\"\" """,
    """from typing import List def intersperse(numbers: List[int], delimeter: int) -> List[int]: \"\"\" Insert a number 'delimeter' between every two consecutive elements of input list `numbers' >>> intersperse([], 4) [] >>> intersperse([1, 2, 3], 4) [1, 4, 2, 4, 3] \"\"\" """,
    """from typing import List def parse_nested_parens(paren_string: str) -> List[int]: \"\"\" Input to this function is a string represented multiple groups for nested parentheses separated by spaces. For each of the group, output the deepest level of nesting of parentheses. E.g. (()()) has maximum two levels of nesting while ((())) has three. >>> parse_nested_parens('(()()) ((())) () ((())()())') [2, 3, 1, 3] \"\"\" """,
]


class Wrapper:
    def __init__(self, model_name: str, responds_length: int = 1000):
        self._length = responds_length
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        self.generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    def __call__(self, prompt) -> list:
        result = self.generator(
            prompt,
            max_length=self._length,
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            num_beams=5,
        )
        if "\n#" in result[0]["generated_text"]:
            self.__call__(prompt)
        else:
            return result


class Prompter:
    def __init__(self, prompts: list[str], runs: int = 10):
        self._runs = runs
        self._prompts = prompts
        self._wrapper = Wrapper("codellama/CodeLlama-7b-hf")

    def __call__(self):
        for eval, prompt in enumerate(self._prompts):
            for run in range(self._runs):
                start = time.time()

                run_todo = True
                while run_todo:
                    result = self._wrapper(prompt)

                    if result is not None:
                        run_todo = False

                with open(
                    f"runs/second/run_{run}_experiment_{eval}.txt", "w", newline=""
                ) as file:
                    for line in result:
                        file.write(f"{line}\n")

                end = time.time()
                diff = start - end
                with open(
                    "runs/times.txt", "a"
                ) as f:  # Use 'a' mode to append to the file
                    f.write(
                        f"run_{run}_experiment_{eval}.txt             time: {diff}\n"
                    )


if __name__ == "__main__":
    Prompter(functions)()
