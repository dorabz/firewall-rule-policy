class PolicyRule:
    def __init__(self, src, dst, action, order):
        self.src = src
        self.dst = dst
        self.action = action
        self.order = order

class PolicyRules:
    def __init__(self, topology, policies):
        self.topology = topology
        self.policies = policies

    def filter_policies(self):
        for policy in self.policies:
            if not self.topology.contains(policy.src) or not self.topology.contains(policy.dst):
                policy = None

    def merge_policies(self):
        for i, policy1 in enumerate(self.policies):
            for j, policy2 in enumerate(self.policies):
                if i != j and policy1 is not None and policy2 is not None:
                    if exactmatch(policy1, policy2):
                        if policy1.action == policy2.action:
                            policy2 = None
                        elif policy1.action == "allow":
                            policy1 = None
                        else:
                            policy2 = None
                    elif inclusion(policy1, policy2):
                        p3s = [p3 for p3 in policies if inclusion(p3, policy2) and inclusion(policy1, p3) and policy2.order > p3.order and p3.order > policy1.order]
                        if policy1.action == policy2.action and len(p3s) > 0:
                           
