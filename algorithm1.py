"""
// p1 and p2 are policy rules part of the high-level requirements given as input
if !topology(p1.src) _ !topology(p1.dst) then
	remove p1
end
if !topology(p2.src) _ !topology(p2.dst) then
	remove p2
end
if exactmatch(p1, p2) then
	if p1.action == p2.action then remove p2;
	else if p1.action == “allow" then remove p1;
	else remove p2;
end
else if inclusion(p1, p2) then
	if
	p1.action == p2.action ^ p3 s.t., inclusion(p3, p2)^inclusion(p1, p3)^p2.order > p3.order ^ p3.order > p1.order then remove p2;
	else
		p2.order > p1.order
	end
end
else if intersection(p1, p2) ^ p1.action != p2.action then
	if (p1.action = “allow") then p2.order > p1.order;
	else p1.order > p2.order;
end
"""

# p1 and p2 are policy rules part of the high-level requirements given as input
if not topology(p1.src) or not topology(p1.dst):
    p1 = None
if not topology(p2.src) or not topology(p2.dst):
    p2 = None
if exactmatch(p1, p2):
    if p1.action == p2.action:
        p2 = None
    elif p1.action == "allow":
        p1 = None
    else:
        p2 = None
elif inclusion(p1, p2):
    p3s = [p3 for p3 in policies if inclusion(p3, p2) and inclusion(p1, p3) and p2.order > p3.order and p3.order > p1.order]
    if p1.action == p2.action and len(p3s) > 0:
        p2 = None
    else:
        p2.order > p1.order
else:
    if intersection(p1, p2) and p1.action != p2.action:
        if p1.action == "allow":
            p2.order > p1.order
        else:
            p1.order > p2.order
