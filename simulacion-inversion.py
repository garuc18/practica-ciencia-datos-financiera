def simular_inversion(capital_inicial, num_periodos, perfil_riesgo):
    if perfil_riesgo == "bajo":
        tasa_retorno = 0.05
    elif perfil_riesgo == "medio":
        tasa_retorno = 0.10
    elif perfil_riesgo == "alto":
        tasa_retorno = 0.15
    
    balance = capital_inicial
    
    print("Balance inicial:", balance)
    print("Tasa de retorno anual:", round(tasa_retorno * 100, 1))

    for periodo in range(1, num_periodos + 1):
        balance = balance * (1 + tasa_retorno)
        print("Periodo", periodo, "Balance:", round(balance, 2))

simular_inversion(10000, 5, "medio")
