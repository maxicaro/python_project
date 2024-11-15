def importe_total_carro(request):
    total = 0
    
    # Verifica si "carro" existe en la sesión antes de acceder a él
    if "carro" in request.session:
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"]) 
    
    return {"importe_total_carro": total}