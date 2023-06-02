#!/usr/bin/env python3

from cmd import Cmd
from collections import deque


class Node:
    pass


class TaskNode(Node):
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


class ForkNode(Node):

    def __init__(self, branch_labels):
        self.branches = None
        pass





class ThoughtStackCmd(Cmd):

    prompt = 'ts: '

    def __init__(self):
        super().__init__()
        self.root_stack: deque = deque()
        self.current_stack: deque = self.root_stack

    def do_quit(self, args):
        """quit ThoughtStack"""
        return True

    def do_print(self, args):
        """print the stack"""
        if not self.root_stack:
            print("You're stack is empty.  It's beer o'clock")
            return False

        print()
        last_node = self.root_stack[-1]
        for node in self.root_stack:
            root_prefix = '*' if node is last_node else ' '
            if isinstance(node, TaskNode):
                print(f"{root_prefix} -{node}")
                continue
            if isinstance(node, ForkNode):
                continue


        return False

    def do_add(self, label):
        """Add a task node onto the current stack"""
        self.current_stack.appendleft(
            TaskNode(label)
        )

    def do_remove(self, args):
        self.current_stack.popleft()

    def do_fork(self, branch_count):
        branch_count = int(branch_count)

        for i in range(branch_count):
            pass

        # fork_node = ForkNode()



def main():
    ThoughtStackCmd().cmdloop()


if __name__ == '__main__':
    main()
