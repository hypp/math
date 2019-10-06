

class Suitor(object):
    def __init__(self, id, rankings):
        self.id = id
        self.rankings = rankings
        self.current = 0

    def current_chosen(self):
        return self.rankings[self.current]

    def next(self):
        self.current += 1

    def __repr__(self):
        return "Suitor %s %s %s" % (self.id, self.rankings, self.current)

class Suited(object):
    def __init__(self, id, rankings):
        self.id = id
        self.rankings = rankings
        self.best_so_far = None
        self.current_set = set()

    def add_suitor(self, suitor):
        self.current_set.add(suitor)

    def check(self):
        # if no one proposed
        if len(self.current_set) == 0:
            return set()

        # Find the best match
        found = False
        for r in self.rankings:
            for s in self.current_set:
                if s.id == r:
                    self.best_so_far = s
                    found = True
                    break
            if found:
                break

        # Keep the rejected
        self.current_set.remove(self.best_so_far)
        rejected = self.current_set
        self.current_set = set()
        # Save the best so far
        self.current_set.add(self.best_so_far)
        # Return the rejected
        return rejected

    def __repr__(self):
        return "Suited %s %s %s %s" % (self.id, self.rankings, self.best_so_far, self.current_set)



def stable_marriage(suitor_list, suited_list):
    # suitor with no suited
    unassigned = set(suitor_list)

    # as long as there is at least one without a partner
    while len(unassigned) > 0:
        # Try to find a partner
        for s in unassigned:
            next_to_check = suited_list[s.current_chosen()]
            next_to_check.add_suitor(s)
        unassigned.clear()

        # Get chosen partners
        for s in suited_list:
            unassigned |= s.check()

        # Prepare to try next
        for s in unassigned:
            s.next()

    return dict([(s.best_so_far, s) for s in suited_list]) 

def test():
    suitor_list = [
        Suitor(0, [3,5,4,2,1,0]),
        Suitor(1, [2,3,1,0,4,5]),
        Suitor(2, [5,2,1,0,3,4]),
        Suitor(3, [0,1,2,3,4,5]),
        Suitor(4, [4,5,1,2,0,3]),
        Suitor(5, [0,1,2,3,4,5]),
    ]

    suited_list = [
        Suited(0, [3,5,4,2,1,0]),
        Suited(1, [2,3,1,0,4,5]),
        Suited(2, [5,2,1,0,3,4]),
        Suited(3, [0,1,2,3,4,5]),
        Suited(4, [4,5,1,2,0,3]),
        Suited(5, [0,1,2,3,4,5]),
    ]
    
    result = stable_marriage(suitor_list, suited_list)
    for k,v in result.items():
        print("k: %s v: %s" % (k,v))


if __name__ == "__main__":
    test()