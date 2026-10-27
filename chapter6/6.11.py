cities={
    'changsha':{
        "country":"china",
        "pro":"hunan",
        'fact':'hunandaxue'    
    },
    'xian':{
        "coutry":'china',
        "pro":"shanxi",
        'fact':'xjtu'    
    }
}
for city,city_information in cities.items():
    print(f"{city}'s information:")
    for a,b in city_information.items():
        print(f"{a}:{b}")


