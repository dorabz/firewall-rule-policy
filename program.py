# Define the policy rule and configuration
rule = "allow tcp from any to any"
config = "max"

# Define the source and destination
source = "10.0.0.1"
destination = "10.0.0.2"

# Define the firewalls and their paths
firewalls = {
    "fw1": ["10.0.0.1", "10.0.0.2"],
    "fw2": ["10.0.0.1", "10.0.0.3", "10.0.0.2"],
    "fw3": ["10.0.0.1", "10.0.0.4", "10.0.0.3", "10.0.0.2"],
    "fw4": ["10.0.0.1", "10.0.0.4", "10.0.0.2"],
}

# Find all paths between the source and destination
paths = []
for fw, path in firewalls.items():
    if source in path and destination in path:
        paths.append(path)

# If the configuration is "max", find all paths
if config == "max":
    print("All paths:")
    for path in paths:
        print(path)

# If the configuration is "min", find the shortest path
elif config == "min":
    shortest_path = min(paths, key=len)
    print("Shortest path:")
    print(shortest_path)

# If the action is "allow", add the rule to all firewalls in the path
if rule.startswith("allow"):
    print("Adding rule to all firewalls in the path:")
    for path in paths:
        for fw in path:
            print(fw, rule)

# If the action is "deny", add the rule to the most upstream firewall in the path
elif rule.startswith("deny"):
    print("Adding rule to the most upstream firewall in the path:")
    for path in paths:
        print(path[0], rule)
