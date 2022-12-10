# Define the policy rule and configuration
p = "allow tcp from any to any"
configuration = "max"

# Define the paths and firewalls
paths = [
    ["fw1", "fw2", "fw3"],
    ["fw1", "fw4", "fw3"],
]
firewalls = {
    "fw1": {"rules": []},
    "fw2": {"rules": []},
    "fw3": {"rules": []},
    "fw4": {"rules": []},
}

# If the configuration is "max", add the rule to all firewalls in each path
if configuration == "max":
    for path in paths:
        if p.startswith("allow"):
            # Add the rule to all firewalls in the path
            for fw in path:
                firewalls[fw]["rules"].append(p)
        else:
            # Add the rule to the most upstream firewall in the path
            firewalls[path[0]]["rules"].append(p)

# If the configuration is "min", add the rule to all firewalls in the shortest path
if configuration == "min":
    # Find the shortest path
    path = min(paths, key=len)

    if p.startswith("allow"):
        # Add the rule to all firewalls in the path
        for fw in path:
            firewalls[fw]["rules"].append(p)
    else:
        # Add the rule to the most upstream firewall in the path
        firewalls[path[0]]["rules"].append(p)

# Print the rules for each firewall
for fw, data in firewalls.items():
    print(f"{fw}: {data['rules']}")
