"""
// p is a policy rule
if configuration == “max" then
	foreach path in paths(p.source, p.dest) do
		if p.action==“allow" then
			foreach f in firewall(path) // firewall(path) is the set of all the firewalls in path
			do
				f.rule.add(p)
			end
		end
		else most upstream(firewall(path)).rule.add(p) ;
	end
end
if configuration==“min" then
	path = routing(p.source, p.dest)
	if p.action==“allow" then
		foreach f in firewall(path) do
			f.rule.add(p)
		end
	end
	else most upstream(firewall(path)).rule.add(p) ;
end
"""

def get_firewall_rules(policy_rules, configuration):
	"""
	Given a list of policy rules and a configuration, returns a list of firewall rules.
	"""
	firewall_rules = []
	for p in policy_rules:
		if configuration == "max":
			for path in paths(p.source, p.dest):
				if p.action == "allow":
					for f in firewall(path):
						f.rule.add(p)
				else:
					most_upstream(firewall(path)).rule.add(p)
		elif configuration == "min":
			path = routing(p.source, p.dest)
			if p.action == "allow":
				for f in firewall(path):
					f.rule.add(p)
			else:
				most_upstream(firewall(path)).rule.add(p)
	return firewall_rules

def get_firewall_rules_from_file(filename, configuration):
	"""
	Given a filename and a configuration, returns a list of firewall rules.
	"""
	policy_rules = get_policy_rules_from_file(filename)
	return get_firewall_rules(policy_rules, configuration)

def get_firewall_rules_from_json(json_string, configuration):
	"""
	Given a json string and a configuration, returns a list of firewall rules.
	"""
	policy_rules = get_policy_rules_from_json(json_string)
	return get_firewall_rules(policy_rules, configuration)

def get_firewall_rules_from_json_file(filename, configuration):
	"""
	Given a filename and a configuration, returns a list of firewall rules.
	"""
	policy_rules = get_policy_rules_from_json_file(filename)
	return get_firewall_rules(policy_rules, configuration)



