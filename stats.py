from typing import TypedDict

class char_dict_list_type(TypedDict):
    char: str
    num: int

def get_num_words(text: str) -> int:
    return len(text.split())

def get_lowercased_characters(text: str) -> dict[str, int]:
    character_dict: dict[str, int] = {}
    text = text.lower()
    for char in text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sort_characters(char_dict: dict[str, int]) -> list[char_dict_list_type]:
    char_dict_list: list[char_dict_list_type] = []
    for k, v in char_dict.items():
        char_dict_list.append({"char": k, "num": v})

    char_dict_list.sort(key=lambda x: x["num"], reverse=True)
    return char_dict_list