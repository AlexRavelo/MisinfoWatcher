import basc_py4chan
from typing import List, Tuple
import random

def get_threads(board_name: str) -> Tuple[List[str], basc_py4chan.Board]:
    board = basc_py4chan.Board(board_name)
    return [str(id) for id in board.get_all_thread_ids()], board

def get_text_posts(thread_id: str, board: basc_py4chan.Board) -> List[str]:
    thread_posts = []
    thread = board.get_thread(thread_id)
    for post in thread.all_posts:
        thread_posts.append(post.text_comment)
    return thread_posts

# Test Example
# threads, board = get_threads('pol')
# print(get_text_posts(random.choice(threads), board))