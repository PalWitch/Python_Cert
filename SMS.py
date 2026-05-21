# Erstellt eine Liste mit den zu Zahlenden SMS's
def remove_free_sms(
    smss_per_month,
    free_sms_per_month):

    to_pay  = []
    for smss in smss_per_month:
        sms_to_pay = smss - free_sms_per_month
        if sms_to_pay > 0:
            to_pay.append(sms_to_pay)
    return to_pay


# Berechnet den Durchschnittspreis basierend auf dem
# Gesamtpreis und der Anzahl der Einträge auf denen
# sich dieser aufteilt.
def calc_average_price(price, number_of_entries):
    if number_of_entries == 0:
        return 0.0
    return price / number_of_entries

# Berechnet die Durchschnittlichen Kosten pro Monat
def calculate_average_cost_per_month(
    smss_per_month, 
    free_sms_per_month,
    cost_per_sms):

    to_pay = remove_free_sms(smss_per_month, free_sms_per_month)
    price = sum(to_pay) * cost_per_sms
    number_of_entries = len(to_pay)
    average_price = calc_average_price(price, number_of_entries)
    return average_price

smss = [23,9,11,23,10,12]

average_price_A = calculate_average_cost_per_month(smss, 10, 0.04)
average_price_B = calculate_average_cost_per_month(smss, 30, 0.06)