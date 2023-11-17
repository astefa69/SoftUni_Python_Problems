p_processor_usd = float(input())
p_video_usd = float(input())
p_ram_usd = float(input())
q_ram = int(input())
discount_percent = float(input())

usd = 1.57 #1 USD = 1.57 BGN

amount_bgn = p_processor_usd * (1 - discount_percent) * usd + p_video_usd * (1 - discount_percent) * usd + p_ram_usd * q_ram * usd

print(f"Money needed - {amount_bgn:.2f} leva.") #Total amount
