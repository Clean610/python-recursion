def DeleteDuplicateString(s, part):
    if 1 <= len(s) <= 100 and 1 <= len(part) <= 100:
        reformat_string = s.replace(part, '')

        return print(f'{reformat_string}')
    else:
        return print(f'Invalid length of input.')


if __name__ == '__main__':
    DeleteDuplicateString("INPUT_TEXT", "INPUT_DATA_TO_SPLIT_OUT")


