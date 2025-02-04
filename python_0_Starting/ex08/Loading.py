def ft_tqdm(lst: range) -> None:
    '''replicate real tqdm function'''
    total_len = len(lst)
    for i, item in enumerate(lst, 1):
        progress = i / total_len
        bar_length = 32
        filled_line = int(progress * bar_length)
        bar_line = '█' * filled_line + ' ' * (bar_length - filled_line)

        print(f'{int(progress * 100)}%|{bar_line}| {i}/{total_len}', end='\r')

        yield item
