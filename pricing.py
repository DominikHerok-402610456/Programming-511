# ==========================================
# PRICING.PY
# ==========================================

"""Pricing function for mall menu. Containing pricing for each mall type. This allows for easy modification of pricing."""
# ----------------------------------------------------------------------------------------------------------
def pricing(stored_mall_id,billable_hours):

    #Pricing Logic for MALL 01 - Gateway Theatre of Shopping - R15 - FLAT FEE
    if stored_mall_id == '01':
        fee = 15 #will be returned to mall_menu


    #Pricing Logic for MALL 02 - Pavilion Shopping Centre - R10 per hour or part there of. (round up to nearest hour)
    if stored_mall_id == '02':
        fee = billable_hours * 10

    # Pricing Logic for MALL 03 - La Lucia Mall - R12 per hour capped @ R60 per day
    if stored_mall_id == '03':
        fee = billable_hours * 12
        if fee > 60:
            fee = 60

    return fee
# ----------------------------------------------------------------------------------------------------------