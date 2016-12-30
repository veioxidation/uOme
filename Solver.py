def SolveEntry(group, entry):
    unit_amount = entry.amount / len(set(entry.paid_for))
    for u_id in set(entry.paid_for):
        group.users[u_id].AddToTB(unit_amount)

    group.users[entry.payer].AddToRB(entry.amount)


