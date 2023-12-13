class Menu:
    def __init__(self) -> None:
        pass
    
    # Gauna texto faila ir nurodym1 k1 skaityti
    def read_from_file(file_name: str, start_sign: str, end_sign: str) -> str:
        with open(file_name, "r", encoding="utf-8") as file:
            is_between_signs = False
            for line in file:
                if start_sign in line:
                    is_between_signs = True
                    continue
                elif end_sign in line:
                    is_between_signs = False
                    break

                if is_between_signs:
                    print(line.strip())
    
    # Sukuria kategorijos dictionary
    def prepare_category_dictionary() -> dict:
        pass

    # Sukuria maisto meniu sarasa
    def prepare_menu_dictionary() -> dict:
        pass