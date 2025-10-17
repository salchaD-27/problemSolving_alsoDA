import heapq
class DinnerPlates:
    def __init__(self, capacity):
        self.c = capacity
        self.q = [] # record the available stack, will use heap to quickly find the smallest available stack
        self.stacks = [] # record values of all stack of plates, its last nonempty stack are the rightmost position

    def push(self, val):
        # To push, we need to find the leftmost available position
        # first, let's remove any stacks on the left that are full
        # 1) self.q: if there is still available stack to insert plate
        # 2) self.q[0] < len(self.stacks): the leftmost available index self.q[0] is smaller than the current size of the stacks
        # 3) len(self.stacks[self.q[0]]) == self.c: the stack has reached full capacity
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            heapq.heappop(self.q) # we remove the filled stack from the queue of available stacks
        # now we reach the leftmost available stack to insert
        # if the q is empty, meaning there are no more available stacks
        if not self.q:
            heapq.heappush(self.q, len(self.stacks)) # open up a new stack to insert
        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.q[0] == len(self.stacks): self.stacks.append([])
        # append the value to the leftmost available stack
        self.stacks[self.q[0]].append(val)

    def pop(self):
        # To pop, we need to find the rightmost nonempty stack
        # 1) stacks is not empty (self.stacks) and
        # 2) the last stack is empty
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop() # we throw away the last empty stack, because we can't pop from it
        # now we reach the rightmost nonempty stack
        # we pop the plate from the last nonempty stack of self.stacks by using popAtStack function
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        # To pop from an stack of given index, we need to make sure that it is not empty
        # 1) the index for inserting is valid and，
        # 2) the stack of interest is not empty
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.q, index) # we add the index into the available stack
            return self.stacks[index].pop() # take the top plate, pop it and return its value
        return -1 # otherwise, return -1 because we can't pop any plate