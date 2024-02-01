#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.play_even import play_even


def main():
    name = welcome_user()
    play_even(name)


if __name__ == '__main__':
    main()
