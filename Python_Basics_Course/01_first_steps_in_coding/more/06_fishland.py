p_skumria = float(input())
p_caca = float(input())
q_palamud = float(input())
q_safrid = float(input())
q_midi = int(input())

p_palamud = 1.6 * p_skumria
p_safrid = 1.8 * p_caca
p_midi = 7.50


budget = p_palamud * q_palamud + p_safrid * q_safrid + p_midi * q_midi

print(f"{budget: .2f}")
