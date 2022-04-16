total_segs = int(input("Entre com o tempo para conversão: "))

horas = total_segs // 3600
dias = horas // 86400

segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

if (horas >= 24):

    dias = int(horas / 24)
    horas = int(horas % 24)

print(dias,"dia",horas,"horas",minutos,"minutos",segs_restantes_final,"segundos")
