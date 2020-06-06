#nested disctionaries
movies= {
"Bollywood":{
    1990:"Yeh dillagi",
    1992:"Deewana",
    1996:"Rangeela"
},
"Sandalwood":{
    1990:"Ranadheera",
    1992:"Operation Antha",
    1997:"Mangalyamtanthunanena"
},
"Hollywood":{
    1990:"pulpfiction",
    1991:"speed",
    1997:"Basic Instinct"
}
}
print(movies)
# setdefault
x= movies.setdefault(1997,"diltoh pagal hai ")
print(x)












