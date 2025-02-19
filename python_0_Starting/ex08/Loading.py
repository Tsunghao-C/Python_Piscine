import shutil
import time


def format_time(seconds):
    """Format time into tqdm time format"""
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    '''replicate real tqdm function'''
    total_len = len(lst)
    start_time = time.time()

    terminal_width = shutil.get_terminal_size().columns -  30
    progress_bar_width = terminal_width - 10
    for i, item in enumerate(lst, start=1):
        progress = int(i / total_len * progress_bar_width)
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time
        eta = (total_len - i) / speed

        elapsed_format = format_time(elapsed_time)
        eta_format = format_time(eta)
        # :<{progress_bar_width} means left-aligns to keep bar size consistent
        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        # // is floor division, it rounds down to the nearest whole number
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total_len}"
        time_info = f"[{elapsed_format}<{eta_format}, {speed:.2f}it/s]"

        print(f"\r{progress_info} {time_info}", end="", flush=True)

        yield item


def main():
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()
