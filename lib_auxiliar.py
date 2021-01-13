import re
import functools
import random

from datetime import date,datetime
import pytz  #Zonas horarias


#Funcion para devolver fecha y hora
#######################################
def get_date(format="%d/%m/%Y %H:%M:%S"):
  return datetime.now(pytz.timezone('Europe/Madrid')).strftime(format)


#Quitar tildes
#######################################
def quitar_tildes(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
     )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s



def gen_comment(name):
    
  return functools.reduce(lambda x,y : x+y , [ random.choice(COMENTARIOS[i]) for i in range(len(COMENTARIOS)) ] ).replace('~nombre~', name)



#Detecta nombres masculinos
def check_chico(name):
  for x in NOMBRES_MAS:
    if re.match(x, name, re.IGNORECASE ):
      return x
  return False


#Opciones para comentarios
COMENTARIOS=(
(
'Hola ~nombre~. ',
'Guau ~nombre~!!. ',
'Espectacular ~nombre~. ',
'Sensacional ~nombre~!!! ',
'Fantastica ~nombre~. ',
),
(
'Buena foto! ',
'Buenisima toma. ',
'Genial trabajo. ',
'Genial toma!! ',
),
(
'Me ha encantado. ',
'Me gusto!! ',
'Me encanto. ',
'Me ha gustado mucho. ',
),
(
'Una estrella para esta foto. ',
'Estrella que te envio. ',
'Te mando una estrella. ',
'Mereces una estrella. Ahi va.  ',
),
(
'Espero verte por',
'Te animo a que me visites',
'Que tal una visita por',
'No te pierdas',
),
(
  ' mi ficha. ',
  ' mi perfil. ' ,
  ' mis fotos. ',
),
(
 'Gracias!!!',
 'Muchas Gracias!',
 'Thanks',
)
)

#Nombres Masculinos
NOMBRES_MAS = (
"^Aar[óo]n[ \$]",
"^Abdal[áa][ \$]",
"^Abd[óo]n[ \$]",
"^Abdul[ \$]",
"^Abel[ \$]",
"^Abelardo[ \$]",
"^Abilio[ \$]",
"^Abner[ \$]",
"^Abraham[ \$]",
"^Absal[óo]n[ \$]",
"^Acacio[ \$]",
"^Accio[ \$]",
"^Adalberto[ \$]",
"^Ad[áa]n[ \$]",
"^Adelfo[ \$]",
"^Adelino[ \$]",
"^Adelio[ \$]",
"^Adolfo[ \$]",
"^Adona[íi][ \$]",
"^Adonis[ \$]",
"^Adri[áa]n[ \$]",
"^Adriano[ \$]",
"^Adulfo[ \$]",
"^Africano[ \$]",
"^Afrodisio[ \$]",
"^Agamen[óo]n[ \$]",
"^Agapito[ \$]",
"^Agesilao[ \$]",
"^Agripino[ \$]",
"^Agust[íi]n[ \$]",
"^Agust[íi]n[ \$]",
"^Ail[ée]n[ \$]",
"^Ailin[ \$]",
"^Aitor[ \$]",
"^Al[ \$]",
"^Aladino[ \$]",
"^Alain[ \$]",
"^Alan[ \$]",
"^Albano[ \$]",
"^Albert[ \$]",
"^Alberto[ \$]",
"^Albino[ \$]",
"^Alceo[ \$]",
"^Alcib[íi]ades[ \$]",
"^Alcides[ \$]",
"^Aldo[ \$]",
"^Ale[ \$]",
"^Alex[ \$]",
"^Alejandro[ \$]",
"^Alejo[ \$]",
"^Alfio[ \$]",
"^Alfonso[ \$]",
"^Alfredo[ \$]",
"^Al[íi][ \$]",
"^Almanzor[ \$]",
"^Alon[ \$]",
"^Alonso[ \$]",
"^[ÁA]lvaro[ \$]",
"^Alwyn[ \$]",
"^Amadeo[ \$]",
"^Amad[íi]s[ \$]",
"^Amado[ \$]",
"^Amador[ \$]",
"^Amalio[ \$]",
"^Amancio[ \$]",
"^Amando[ \$]",
"^Amaranto[ \$]",
"^Amaru[ \$]",
"^Ambrosio[ \$]",
"^Am[ée]rico[ \$]",
"^Am[íi]lcar[ \$]",
"^Amin[ \$]",
"^Anacleto[ \$]",
"^Anastasio[ \$]",
"^Andr[ée]s[ \$]",
"^Andrei[ \$]",
"^Angel[ \$]",
"^An[íi]bal[ \$]",
"^Aniceto[ \$]",
"^Anselmo[ \$]",
"^Ant[óo]n[ \$]",
"^Antonello[ \$]",
"^Antonino[ \$]",
"^Antonio[ \$]",
"^Ant[úu][ \$]",
"^Aparicio[ \$]",
"^Apolinario[ \$]",
"^Apolo[ \$]",
"^Apolonio[ \$]",
"^Aquiles[ \$]",
"^Aquilino[ \$]",
"^Arc[áa]ngel[ \$]",
"^Archibaldo[ \$]",
"^Argentino[ \$]",
"^Ariano[ \$]",
"^Ariel[ \$]",
"^Ar[íi]stides[ \$]",
"^Arist[óo]bulo[ \$]",
"^Arist[óo]teles[ \$]",
"^Armand[ \$]",
"^Armando[ \$]",
"^Arnaldo[ \$]",
"^Arni[ \$]",
"^Arnoldo[ \$]",
"^Arqu[íi]medes[ \$]",
"^Arsenio[ \$]",
"^Artemio[ \$]",
"^Arturo[ \$]",
"^Asdr[úu]bal[ \$]",
"^Aser[ \$]",
"^Asier[ \$]",
"^Astor[ \$]",
"^Atahualpa[ \$]",
"^Atanasio[ \$]",
"^Atila[ \$]",
"^Atilio[ \$]",
"^Auberto[ \$]",
"^Auca[ \$]",
"^Augusto[ \$]",
"^Aureliano[ \$]",
"^Aurelio[ \$]",
"^Avelino[ \$]",
"^Axel[ \$]",
"^Ayax[ \$]",
"^Ayel[ée]n[ \$]",
"^Aylwyn[ \$]",
"^Azar[íi]as[ \$]",
"^Azul[ \$]",
"^Baco[ \$]",
"^Balbino[ \$]",
"^Balbo[ \$]",
"^Balder[ \$]",
"^Baldomero[ \$]",
"^Balduino[ \$]",
"^Baldwin[ \$]",
"^Baltasar[ \$]",
"^Barry[ \$]",
"^Bartolo[ \$]",
"^Bartolom[ée][ \$]",
"^Baruc[ \$]",
"^Baruj[ \$]",
"^Basileo[ \$]",
"^Basilio[ \$]",
"^Baudilio[ \$]",
"^Bautista[ \$]",
"^Beda[ \$]",
"^Belarmino[ \$]",
"^Bel[ée]n[ \$]",
"^Belisario[ \$]",
"^Belmiro[ \$]",
"^Beltr[áa]n[ \$]",
"^Ben[ \$]",
"^Benedicto[ \$]",
"^Benicio[ \$]",
"^Benigno[ \$]",
"^Benildo[ \$]",
"^Benito[ \$]",
"^Benji[ \$]",
"^Benjam[íi]n[ \$]",
"^Berardo[ \$]",
"^Berengario[ \$]",
"^Bernab[ée][ \$]",
"^Bernardino[ \$]",
"^Bernardo[ \$]",
"^Bertoldo[ \$]",
"^Bertr[áa]n[ \$]",
"^Bienvenido[ \$]",
"^Blas[ \$]",
"^Boecio[ \$]",
"^Bogart[ \$]",
"^Bonifacio[ \$]",
"^Bono[ \$]",
"^Boris[ \$]",
"^Bowie[ \$]",
"^Brad[ \$]",
"^Brandon[ \$]",
"^Braulio[ \$]",
"^Brian[ \$]",
"^Brice[ \$]",
"^Bruce[ \$]",
"^Bruno[ \$]",
"^Buenaventura[ \$]",
"^Burt[ \$]",
"^Cacha[ \$]",
"^Cadme[ \$]",
"^Cadmo[ \$]",
"^Caetano[ \$]",
"^Caif[áa]s[ \$]",
"^Ca[íi]n[ \$]",
"^Caleb[ \$]",
"^Cal[íi]gula[ \$]",
"^Cal[íi]maco[ \$]",
"^Calisto[ \$]",
"^Calixto[ \$]",
"^Calqu[íi]n[ \$]",
"^Calvin[ \$]",
"^Camilo[ \$]",
"^Cana[áa]n[ \$]",
"^C[áa]ndido[ \$]",
"^Carlo[ \$]",
"^Carlomagno[ \$]",
"^Carlos[ \$]",
"^Carmelo[ \$]",
"^Casandro[ \$]",
"^Casiano[ \$]",
"^Casildo[ \$]",
"^Casimiro[ \$]",
"^Casio[ \$]",
"^Casiodoro[ \$]",
"^Casto[ \$]",
"^C[áa]stor[ \$]",
"^Cataldo[ \$]",
"^Cat[óo]n[ \$]",
"^Catriel[ \$]",
"^C[áa]tulo[ \$]",
"^Cayetano[ \$]",
"^Cecilio[ \$]",
"^Ceferino[ \$]",
"^Celedonio[ \$]",
"^Celestino[ \$]",
"^Celio[ \$]",
"^Celso[ \$]",
"^C[ée]sar [ \$]",
"^Cesario[ \$]",
"^Cicer[óo]n[ \$]",
"^Cid[ \$]",
"^Cielo[ \$]",
"^Cipriano[ \$]",
"^Ciriaco[ \$]",
"^Cirilo[ \$]",
"^Ciro[ \$]",
"^Claudiano[ \$]",
"^Claudio[ \$]",
"^Claus[ \$]",
"^Clemente[ \$]",
"^Clementino[ \$]",
"^Cleof[áa]s[ \$]",
"^Clodomiro[ \$]",
"^Clodoveo[ \$]",
"^Clorindo[ \$]",
"^Cochi[ \$]",
"^Coihue[ \$]",
"^Colombino[ \$]",
"^Concordio[ \$]",
"^Confucio[ \$]",
"^Cono[ \$]",
"^Conrado[ \$]",
"^Constancio[ \$]",
"^Constantino[ \$]",
"^Corel[ \$]",
"^Coriolano[ \$]",
"^Cornelio[ \$]",
"^Cosme[ \$]",
"^Coyan[ \$]",
"^Crescencio[ \$]",
"^Crisanto[ \$]",
"^Cris[óo]foro[ \$]",
"^Cris[óo]gono[ \$]",
"^Cris[óo]logo[ \$]",
"^Cris[óo]stomo[ \$]",
"^Crisp[íi]n[ \$]",
"^Cristi[áa]n[ \$]",
"^Cristiano[ \$]",
"^Crist[óo]bal[ \$]",
"^Christian[ \$]",
"^Cruz[ \$]",
"^Cunquen[ \$]",
"^Custodio[ \$]",
"^Cuyen[ \$]",
"^Dacio[ \$]",
"^Dadal[ \$]",
"^Dagoberto[ \$]",
"^Dalmacio[ \$]",
"^Dalmiro[ \$]",
"^D[áa]maso[ \$]",
"^Dami[áa]n[ \$]",
"^Damocles[ \$]",
"^Dan[ \$]",
"^Dani[ \$]",
"^Daniel[ \$]",
"^Danilo[ \$]",
"^Dante[ \$]",
"^Dardo[ \$]",
"^Dar[íi]o[ \$]",
"^David[ \$]",
"^Decio[ \$]",
"^D[ée]dalo[ \$]",
"^Delf[íi]n[ \$]",
"^Delfino[ \$]",
"^Demetrio[ \$]",
"^Demi[áa]n[ \$]",
"^Dem[óo]crito[ \$]",
"^Dem[óo]stenes[ \$]",
"^Denis[ \$]",
"^Desiderio[ \$]",
"^Dick[ \$]",
"^Didier[ \$]",
"^Diego[ \$]",
"^Dihue[ \$]",
"^Dimas[ \$]",
"^Dimitri[ \$]",
"^Dino[ \$]",
"^Dio[ \$]",
"^Di[óo]genes[ \$]",
"^Di[óo]medes[ \$]",
"^Di[óo]n[ \$]",
"^Dionel[ \$]",
"^Dionisio[ \$]",
"^Diosdado[ \$]",
"^Diuca[ \$]",
"^Doin[ \$]",
"^Domacal[ \$]",
"^Dom[ée]nico[ \$]",
"^Domiciano[ \$]",
"^Domicio[ \$]",
"^Domingo[ \$]",
"^Donaldo[ \$]",
"^Donato[ \$]",
"^Dorian[ \$]",
"^Doroteo[ \$]",
"^Dositeo[ \$]",
"^Douglas[ \$]",
"^Doyel[ \$]",
"^Duham[ \$]",
"^Duilio[ \$]",
"^Dulce[ \$]",
"^Dulcidio[ \$]",
"^Duncan[ \$]",
"^Dustin[ \$]",
"^Dylan[ \$]",
"^Eberardo[ \$]",
"^Ecio[ \$]",
"^Edelmar[ \$]",
"^Edelmiro[ \$]",
"^Ed[ée]n[ \$]",
"^Edgar[ \$]",
"^Edgardo[ \$]",
"^Edilio[ \$]",
"^Edipo[ \$]",
"^Edison [ \$]",
"^Edmundo[ \$]",
"^Eduardo[ \$]",
"^Efra[íi]n[ \$]",
"^Egidio[ \$]",
"^Egisto[ \$]",
"^Egoitz[ \$]",
"^Eimi[ \$]",
"^Einsam[ \$]",
"^Eladio[ \$]",
"^Elbio[ \$]",
"^Eleazar[ \$]",
"^Elenio[ \$]",
"^Eleodoro[ \$]",
"^Eleuterio[ \$]",
"^El[íi][ \$]",
"^Eli[áa]n[ \$]",
"^El[íi]as[ \$]",
"^Elicio[ \$]",
"^Eligio[ \$]",
"^Elio[ \$]",
"^Elisandro[ \$]",
"^Eliseo[ \$]",
"^Elmen[ \$]",
"^Elmer[ \$]",
"^Elmin[ \$]",
"^Eloy[ \$]",
"^Elpidio[ \$]",
"^Eluney[ \$]",
"^Elvio[ \$]",
"^Elvis [ \$]",
"^Emai[ \$]",
"^Emanuel [ \$]",
"^Emerio[ \$]",
"^Emerson [ \$]",
"^Emeterio[ \$]",
"^Emiliano[ \$]",
"^Emilio[ \$]",
"^Emir[ \$]",
"^Emmanuel[ \$]",
"^Eneas[ \$]",
"^Eniun[ \$]",
"^Enoch[ \$]",
"^Enrico[ \$]",
"^Enrique [ \$]",
"^Enzo [ \$]",
"^Epicuro[ \$]",
"^Epifanio[ \$]",
"^Epuchi[ \$]",
"^Epul[ée]n[ \$]",
"^Epumari[ \$]",
"^Erardo[ \$]",
"^Erasmo[ \$]",
"^Eric[ \$]",
"^Ermindo[ \$]",
"^Ernesto[ \$]",
"^Eros [ \$]",
"^Ervin[ \$]",
"^Erwin[ \$]",
"^Esa[úu][ \$]",
"^Esculapio[ \$]",
"^Esdras[ \$]",
"^Esopo[ \$]",
"^Espartaco[ \$]",
"^Estanislao[ \$]",
"^Esteban[ \$]",
"^Estefano[ \$]",
"^Eudoro[ \$]",
"^Eufemio[ \$]",
"^Eufrasio[ \$]",
"^Eugenio[ \$]",
"^Eulalio[ \$]",
"^Eulogio[ \$]",
"^Eusebio[ \$]",
"^Eustaquio[ \$]",
"^Evangelino[ \$]",
"^Evaristo[ \$]",
"^Evelio[ \$]",
"^Everardo[ \$]",
"^Exequiel[ \$]",
"^Ezequiel[ \$]",
"^Ezio[ \$]",
"^Ezra[ \$]",
"^Fabi[áa]n[ \$]",
"^Fabiano[ \$]",
"^Fabio[ \$]",
"^Fabricio[ \$]",
"^Facundo[ \$]",
"^Falco[ \$]",
"^Fantino[ \$]",
"^Fara[óo]n[ \$]",
"^Farid[ \$]",
"^Fausto[ \$]",
"^Favio[ \$]",
"^Federico[ \$]",
"^Fedor[ \$]",
"^Fedro[ \$]",
"^Feliciano[ \$]",
"^Felipe[ \$]",
"^F[ée]lix[ \$]",
"^Fer[ \$]",
"^Ferdinando[ \$]",
"^Ferm[íi]n[ \$]",
"^Fern[áa]n[ \$]",
"^Fernando[ \$]",
"^Fidel[ \$]",
"^Filadelfo[ \$]",
"^Fileas[ \$]",
"^Filem[óo]n[ \$]",
"^Filiberto[ \$]",
"^Fil[óo]n[ \$]",
"^Flaminio[ \$]",
"^Flaviano[ \$]",
"^Flavio[ \$]",
"^Floreal[ \$]",
"^Florencio[ \$]",
"^Florentino[ \$]",
"^Flori[áa]n [ \$]",
"^Floriano[ \$]",
"^Florindo[ \$]",
"^Florio[ \$]",
"^Floro[ \$]",
"^Fortunato[ \$]",
"^Fran[ \$]",
"^Fran[ \$]",
"^Francesc[ \$]",
"^Franco[ \$]",
"^Franz[ \$]",
"^Froil[áa]n[ \$]",
"^Fructuoso[ \$]",
"^Fulgencio[ \$]",
"^Fulvio[ \$]",
"^Gabino[ \$]",
"^Gabriel[ \$]",
"^Gadi[ \$]",
"^Gadiel[ \$]",
"^Gal[ \$]",
"^Gal[ \$]",
"^Galen[ \$]",
"^Galeno[ \$]",
"^Galileo[ \$]",
"^Galo[ \$]",
"^Gamal[ \$]",
"^Gamaliel[ \$]",
"^Gandolfo[ \$]",
"^Garc[íi]a[ \$]",
"^Gared[ \$]",
"^Garibaldi[ \$]",
"^Garibaldo[ \$]",
"^Gary[ \$]",
"^Gaspar[ \$]",
"^Gast[óo]n[ \$]",
"^Gaudencio[ \$]",
"^Gauderico[ \$]",
"^Gaudioso[ \$]",
"^Gavrie[ \$]",
"^Gavriel[ \$]",
"^Gede[óo]n[ \$]",
"^Gelasio[ \$]",
"^Gemelo[ \$]",
"^Geminiano[ \$]",
"^Gemino[ \$]",
"^Genaro[ \$]",
"^Genciano[ \$]",
"^Gene[ \$]",
"^Generoso[ \$]",
"^G[ée]nesis[ \$]",
"^Geoffrey[ \$]",
"^George[ \$]",
"^Georges[ \$]",
"^Geraldo[ \$]",
"^Gerardo[ \$]",
"^Gerem[íi]as[ \$]",
"^Germain[ \$]",
"^Germ[áa]n[ \$]",
"^Germ[áa]nico[ \$]",
"^Ger[óo]nimo[ \$]",
"^Gervasio[ \$]",
"^Gesualdo[ \$]",
"^Getulio[ \$]",
"^Gian[ \$]",
"^Giancarlo[ \$]",
"^Gianfranco[ \$]",
"^Gianluca[ \$]",
"^Gianni[ \$]",
"^Gil[ \$]",
"^Gilberto[ \$]",
"^Gildardo[ \$]",
"^Gildo[ \$]",
"^Gin[ée]s[ \$]",
"^Gino[ \$]",
"^Giordano[ \$]",
"^Giorgio[ \$]",
"^Giovanni[ \$]",
"^Gisberto[ \$]",
"^Giuliano[ \$]",
"^Giuseppe[ \$]",
"^Glauco[ \$]",
"^Glen[ \$]",
"^Glenn[ \$]",
"^Glicerio[ \$]",
"^Godofredo[ \$]",
"^Goliat[ \$]",
"^Gonzalo[ \$]",
"^Gordon[ \$]",
"^Gotardo[ \$]",
"^Graciano[ \$]",
"^Gregorio[ \$]",
"^Grimaldo[ \$]",
"^Gualberto[ \$]",
"^Gualdemar[ \$]",
"^Gualterio[ \$]",
"^Guarino[ \$]",
"^Guerrico[ \$]",
"^Guido[ \$]",
"^Guilherme[ \$]",
"^Guillermo[ \$]",
"^Gumersindo[ \$]",
"^Guntero[ \$]",
"^Gunther[ \$]",
"^Gus[ \$]",
"^Gustavo[ \$]",
"^Gutierre[ \$]",
"^Guy[ \$]",
"^Guzm[áa]n[ \$]",
"^Habib[ \$]",
"^Hadrian[ \$]",
"^Hadulfo[ \$]",
"^Haiko[ \$]",
"^Haman[ \$]",
"^Ham[íi]lcar[ \$]",
"^Hamlet[ \$]",
"^Han[íi]bal[ \$]",
"^Hans[ \$]",
"^Haroldo[ \$]",
"^Harvey[ \$]",
"^Hassan[ \$]",
"^Heber[ \$]",
"^Heberto[ \$]",
"^H[ée]ctor[ \$]",
"^Helio[ \$]",
"^Heliodoro[ \$]",
"^Heliog[áa]balo[ \$]",
"^Helvio[ \$]",
"^Her[áa]clito[ \$]",
"^Heraldo[ \$]",
"^H[ée]rcules[ \$]",
"^Heriberto[ \$]",
"^Herm[áa]n[ \$]",
"^Hermenegildo[ \$]",
"^Hermes[ \$]",
"^Herminio[ \$]",
"^Hern[áa]n[ \$]",
"^Hernando[ \$]",
"^Hernani[ \$]",
"^Her[óo]doto[ \$]",
"^Heros[ \$]",
"^Herv[ée][ \$]",
"^Higinio[ \$]",
"^Hilario[ \$]",
"^Hilari[óo]n[ \$]",
"^Hip[óo]lito[ \$]",
"^Hiram[ \$]",
"^Hiran[ \$]",
"^Homero[ \$]",
"^Honorato[ \$]",
"^Honorio[ \$]",
"^Horacio[ \$]",
"^Hortensio[ \$]",
"^Huaiquil[ \$]",
"^Huapi[ \$]",
"^Huara[ \$]",
"^Huayun[ \$]",
"^Huberto[ \$]",
"^Huechu[ \$]",
"^Hueco[ \$]",
"^Hueique[ \$]",
"^Huelten[ \$]",
"^Huenu[ \$]",
"^Huerquen[ \$]",
"^Hugo[ \$]",
"^Humberto[ \$]",
"^Iago[ \$]",
"^Ian[ \$]",
"^Ib[ée]rico[ \$]",
"^Ibero[ \$]",
"^Icaro[ \$]",
"^Ignacio[ \$]",
"^Igor[ \$]",
"^Iguen[ \$]",
"^Ihuen[ \$]",
"^Ildefonso[ \$]",
"^Imanol[ \$]",
"^Iñaki[ \$]",
"^Inal[ \$]",
"^Inalen[ \$]",
"^Inan[ \$]",
"^Inca[ \$]",
"^Incan[ \$]",
"^Indalecio[ \$]",
"^Iñigo[ \$]",
"^Inocencio[ \$]",
"^Inti[ \$]",
"^Ion[ \$]",
"^Ireneo[ \$]",
"^Irineo[ \$]",
"^Isaac[ \$]",
"^Isa[íi]as[ \$]",
"^Isidoro[ \$]",
"^Isidro[ \$]",
"^Ismael[ \$]",
"^Israel[ \$]",
"^Italo[ \$]",
"^Itziar[ \$]",
"^Iv[áa]n[ \$]",
"^Ivo[ \$]",
"^Jabel[ \$]",
"^Jacinto[ \$]",
"^Jacob[ \$]",
"^Jacobo[ \$]",
"^Jael[ \$]",
"^Jaime[ \$]",
"^Jair[ \$]",
"^Jairo[ \$]",
"^Jalil[ \$]",
"^Jhasmany[ \$]",
"^Jano[ \$]",
"^Jas[óo]n[ \$]",
"^Javier[ ]\$]",
"^Jenaro[ \$]",
"^Jenofonte[ \$]",
"^Jerem[íi]as[ \$]",
"^Jer[óo]nimo[ \$]",
"^Jes[úu]s[ \$]",
"^Joan[ \$]",
"^Joaqu[íi]n[ \$]",
"^Job[ \$]",
"^Joel[ \$]",
"^Jon[ \$]",
"^Jon[áa]s[ \$]",
"^Jonatan[ \$]",
"^Jonathan[ \$]",
"^Jord[áa]n[ \$]",
"^Jordi[ \$]",
"^Jorge[ \$]",
"^Jos[ée]",
"^Josemar[íi]a[ \$]",
"^Josu[ée][ \$]",
"^Juan[ \$]",
"^Juanjo[ \$]",
"^Juanjose[ \$]",
"^Juanma[ \$]",
"^Juli[áa]n[ \$]",
"^Julio [ \$]",
"^Justiniano[ \$]",
"^Justino[ \$]",
"^Justo[ \$]",
"^Juvenal[ \$]",
"^Juvencio[ \$]",
"^Kaiser[ \$]",
"^Kaled[ \$]",
"^Kalil[ \$]",
"^Kasuo[ \$]",
"^Keith[ \$]",
"^Kent[ \$]",
"^Kenzo[ \$]",
"^Kevin[ \$]",
"^Khalil[ \$]",
"^Kin[ \$]",
"^Kike[ \$]",
"^Kong[ \$]",
"^Laban[ \$]",
"^Ladislao[ \$]",
"^Laertes[ \$]",
"^Lahual[ \$]",
"^Lahuen[ \$]",
"^Lamberto[ \$]",
"^Lancelot[ \$]",
"^Landolfo[ \$]",
"^Lanfranco[ \$]",
"^Lanzarote[ \$]",
"^Laureano[ \$]",
"^Laurentino[ \$]",
"^Lauro[ \$]",
"^Lautaro[ \$]",
"^L[áa]zaro[ \$]",
"^Leal[ \$]",
"^Leandro[ \$]",
"^Lelio[ \$]",
"^Leo[ \$]",
"^Leocadio[ \$]",
"^Le[óo]n[ \$]",
"^Leonardo[ \$]",
"^Leoncio[ \$]",
"^Leonel[ \$]",
"^Le[óo]nidas[ \$]",
"^Leopoldo[ \$]",
"^Lev[íi][ \$]",
"^Liber[ \$]",
"^Liberal[ \$]",
"^Liberato[ \$]",
"^Liberio[ \$]",
"^Lican[ \$]",
"^Lien[ \$]",
"^Lighuen[ \$]",
"^Lihu[ée][ \$]",
"^Lil[ \$]",
"^Lilien[ \$]",
"^Lindor[ \$]",
"^Lino[ \$]",
"^Lionel[ \$]",
"^Lisandro[ \$]",
"^Lisardo[ \$]",
"^Lito[ \$]",
"^Liu[ \$]",
"^Livio[ \$]",
"^Llanca[ \$]",
"^Llanque[ \$]",
"^Llañu[ \$]",
"^Llechi[ \$]",
"^Llum[ \$]",
"^Lope[ \$]",
"^Lorenzo[ \$]",
"^Lot[ \$]",
"^Lotario[ \$]",
"^Loyola[ \$]",
"^Luca[ \$]",
"^Lucano[ \$]",
"^Lucas[ \$]",
"^Lucero[ \$]",
"^Luciano[ \$]",
"^Lucio[ \$]",
"^Lucrecio[ \$]",
"^Ludovico[ \$]",
"^Luis[ \$]",
"^Lupo[ \$]",
"^Lurencio[ \$]",
"^Lutero[ \$]",
"^Macabeo[ \$]",
"^Macario[ \$]",
"^Macedonio[ \$]",
"^Maciel[ \$]",
"^Maden[ \$]",
"^Madox[ \$]",
"^Maga[ \$]",
"^Mag[íi]n[ \$]",
"^Mahoma[ \$]",
"^Mainque[ \$]",
"^Mait[ée]n[ \$]",
"^Malaqu[íi]as[ \$]",
"^Malco[ \$]",
"^Malen[ \$]",
"^Mamerto[ \$]",
"^Mampu [ \$]",
"^Manas[ée]s[ \$]",
"^Mancio[ \$]",
"^Manfredo[ \$]",
"^Manel[ \$]",
"^Manlio[ \$]",
"^Manolo[ \$]",
"^Manque[ \$]",
"^Manrique[ \$]",
"^Manuel[ \$]",
"^Marc[ \$]",  
"^Marcelino[ \$]",
"^Marcelo[ \$]",
"^Marcial[ \$]",
"^Marciano[ \$]",
"^Marcio[ \$]",
"^Marco[ \$]",
"^Marcos[ \$]",
"^Mar[íi]a[ \$]",
"^Mariano[ \$]",
"^Mar[íi]n[ \$]",
"^Marino[ \$]",
"^Mario[ \$]",
"^Marlon[ \$]",
"^Marsilio[ \$]",
"^Mart[íi]n[ \$]",
"^Martiniano[ \$]",
"^Martino[ \$]",
"^Mateo[ \$]",
"^Mat[íi]as[ \$]",
"^Matusal[ée]n[ \$]",
"^Mauricio[ \$]",
"^Maurino[ \$]",
"^Mauro[ \$]",
"^Max[ \$]",
"^Maximiliano[ \$]",
"^M[áa]ximo[ \$]",
"^Medardo[ \$]",
"^Mederico[ \$]",
"^Melanio[ \$]",
"^Melchor[ \$]",
"^Mel[íi]n[ \$]",
"^Melito[ \$]",
"^Melit[óo]n[ \$]",
"^Melqu[íi]ades[ \$]",
"^Melquisedec[ \$]",
"^Melvin[ \$]",
"^Menajem[ \$]",
"^Menandro[ \$]",
"^Menelao[ \$]",
"^Menqui[ \$]",
"^Mentor[ \$]",
"^Mercurio[ \$]",
"^Meulen[ \$]",
"^Michay[ \$]",
"^Midas[ \$]",
"^Miguel[ \$]",
"^Mijael[ \$]",
"^Mikael[ \$]",
"^Mikel[ \$]",  
"^Milan[ \$]",
"^Miles[ \$]",
"^Milla[ \$]",
"^Mill[áa]n[ \$]",
"^Milton[ \$]",
"^Miquel[ \$]",
"^Misael[ \$]",
"^Moctezuma[ \$]",
"^Modesto[ \$]",
"^Mohamed[ \$]",
"^Mois[ée]s*[ \$]",
"^Montano[ \$]",
"^Monty[ \$]",
"^Moreno[ \$]",
"^Morenii*to[ \$]",
"^Moro[ \$]",
"^Munir[ \$]",
"^Mustaf[áa][ \$]",
"^Nabuconodosor[ \$]",
"^Nadir[ \$]",
"^Nahim[ \$]",
"^Nahuel[ \$]",
"^Nahum[ \$]",
"^Namuncur[áa][ \$]",
"^Napole[óo]n[ \$]",
"^Ñapu[ \$]",
"^Narciso[ \$]",
"^Natal[ \$]",
"^Natalio[ \$]",
"^Nat[áa]n[ \$]",
"^Natanael[ \$]",
"^Nazareno[ \$]",
"^Nazaret[ \$]",
"^Nazario[ \$]",
"^Necul[ \$]",
"^Neftal[íi][ \$]",
"^Nehem[íi]as[ \$]",
"^Nehuen[ \$]",
"^Nelson[ \$]",
"^Nemesio[ \$]",
"^Ne[óo]n[ \$]",
"^Nepomuceno[ \$]",
"^Neptuno[ \$]",
"^Nereo[ \$]",
"^Nerio[ \$]",
"^Ner[óo]n[ \$]",
"^N[ée]stor[ \$]",
"^Neyen[ \$]",
"^Nicandro[ \$]",
"^Nicanor[ \$]",
"^Nicasio[ \$]",
"^Nic[ée]foro[ \$]",
"^Niceto[ \$]",
"^Nicodemo[ \$]",
"^Nicol[áa]s[ \$]",
"^Nicomedes[ \$]",
"^Ñihue[ \$]",
"^Nil[ \$]",
"^Nilo[ \$]",
"^Ñire[ \$]",
"^No[ée][ \$]",
"^Noel[ \$]",
"^Nolasco[ \$]",
"^Nolberto[ \$]",
"^Norberto[ \$]",
"^Norman[ \$]",
"^Normando[ \$]",
"^Numa[ \$]",
"^Nuncio[ \$]",
"^Ñuque[ \$]",
"^Nuri[ \$]",
"^Nuriel[ \$]",
"^Obdulio[ \$]",
"^Obed[ \$]",
"^Ober[óo]n[ \$]",
"^Ocori[ \$]",
"^Octaviano[ \$]",
"^Octavio[ \$]",
"^Od[íi]n[ \$]",
"^Odiseo[ \$]",
"^Odo[ \$]",
"^Odorico[ \$]",
"^Ofir[ \$]",
"^Olaf[ \$]",
"^Olegario[ \$]",
"^Olindo[ \$]",
"^Oliverio[ \$]",
"^Omar[ \$]",
"^On[ée]simo[ \$]",
"^Onofre[ \$]",
"^Orangel[ \$]",
"^Orestes[ \$]",
"^Orfeo[ \$]",
"^Ori[óo]n[ \$]",
"^Orlando[ \$]",
"^Orosco[ \$]",
"^Orquen[ \$]",
"^Oscar[ \$]",
"^Oseas[ \$]",
"^Os[íi]as[ \$]",
"^Osiris[ \$]",
"^Osm[áa]n[ \$]",
"^Osmar[ \$]",
"^Osmundo[ \$]",
"^Osvaldo[ \$]",
"^Otelo[ \$]",
"^Otilio[ \$]",
"^Ot[óo]n[ \$]",
"^Otoniel[ \$]",
"^Ovidio[ \$]",
"^Owen[ \$]",
"^Oyan[ \$]",
"^Pablo[ \$]",
"^Paciano[ \$]",
"^Paciente[ \$]",
"^Pac[íi]fico[ \$]",
"^Paco[ \$]",
"^Pacomio[ \$]",
"^Pal[ \$]",
"^Palem[óo]n[ \$]",
"^Palmacio[ \$]",
"^Palmiro[ \$]",
"^Palomedes[ \$]",
"^Palqui[ \$]",
"^Pampa[ \$]",
"^Pancracio[ \$]",
"^P[áa]nfilo[ \$]",
"^Pangui[ \$]",
"^Pantale[óo]n[ \$]",
"^Paolo[ \$]",
"^Paris[ \$]",
"^Parisio[ \$]",
"^Parm[ée]nides[ \$]",
"^Parmenio[ \$]",
"^Pascal[ \$]",
"^Pascual[ \$]",
"^Pastor[ \$]",
"^Patricio[ \$]",
"^Patroclo[ \$]",
"^Paulino[ \$]",
"^Paulo[ \$]",
"^Pausidio[ \$]",
"^Paz[ \$]",
"^Pedro[ \$]",
"^Pegaso[ \$]",
"^Pehu[ée]n[ \$]",
"^Pelagio[ \$]",
"^Pelayo[ \$]",
"^Peleo[ \$]",
"^Pelquin[ \$]",
"^Pepe[ \$]",
"^Pep[ \$]",
"^Pepino[ \$]",
"^Percival[ \$]",
"^Peregrino[ \$]",
"^Perfecto[ \$]",
"^Pericles[ \$]",
"^Perpetuo[ \$]",
"^Perseo[ \$]",
"^Petrarca[ \$]",
"^Petronilo[ \$]",
"^Petronio[ \$]",
"^Pichi[ \$]",
"^Pilmaiqu[ée]n[ \$]",
"^P[íi]ndaro[ \$]",
"^P[íi]o[ \$]",
"^Pipino[ \$]",
"^Pirro[ \$]",
"^Pit[áa]goras[ \$]",
"^Pl[áa]cido[ \$]",
"^Plat[óo]n[ \$]",
"^Plauto[ \$]",
"^Plinio[ \$]",
"^Plutarco[ \$]",
"^Plut[óo]n[ \$]",
"^Polibio[ \$]",
"^Policarpo[ \$]",
"^Polidoro[ \$]",
"^Polifemo[ \$]",
"^Pompeo[ \$]",
"^Pompeyo[ \$]",
"^Poncio[ \$]",
"^Porcio[ \$]",
"^Porfirio[ \$]",
"^Porfirio[ \$]",
"^Poseid[óo]n[ \$]",
"^Pr[íi]amo[ \$]",
"^Prilidiano[ \$]",
"^Primitivo[ \$]",
"^Primo[ \$]",
"^Proclo[ \$]",
"^Procopio[ \$]",
"^Prometeo[ \$]",
"^Pr[óo]spero[ \$]",
"^Prudencio[ \$]",
"^Ptolomeo[ \$]",
"^Publio[ \$]",
"^Pulqui [ \$]",
"^Pusaki[ \$]",
"^Querub[íi]n[ \$]",
"^Quijote[ \$]",
"^Quill[ée]n[ \$]",
"^Quimey[ \$]",
"^Quintiliano[ \$]",
"^Quintilio[ \$]",
"^Quint[íi]n[ \$]",
"^Quinto[ \$]",
"^Quirino[ \$]",
"^Querub[íi]n[ \$]",
"^Quijote[ \$]",
"^Quill[ée]n[ \$]",
"^Quimey[ \$]",
"^Quique[ \$]",
"^Quintiliano[ \$]",
"^Quintilio[ \$]",
"^Quint[íi]n[ \$]",
"^Quinto[ \$]",
"^Quirino[ \$]",
"^Radam[ée]s[ \$]",
"^Rafa[ \$]",
"^Rafael[ \$]",
"^Raimondo[ \$]",
"^Raimundo[ \$]",
"^Rainero[ \$]",
"^Raiquen[ \$]",
"^Ramiro[ \$]",
"^Ram[óo]n[ \$]",
"^Rams[ée]s[ \$]",
"^Rancul[ \$]",
"^Randolfo[ \$]",
"^Ra[úu]l[ \$]",
"^Raulino[ \$]",
"^Ray[ \$]",
"^Ray[ée]n[ \$]",
"^Recaredo[ \$]",
"^Reginaldo[ \$]",
"^Regino[ \$]",
"^R[ée]gulo[ \$]",
"^Rehue[ \$]",
"^Reinaldo[ \$]",
"^Reinoldo[ \$]",
"^Relen[ \$]",
"^Remo[ \$]",
"^Renaldo[ \$]",
"^Ren[áa]n[ \$]",
"^Renato[ \$]",
"^Renzo[ \$]",
"^Restituto[ \$]",
"^Reynaldo[ \$]",
"^Ric*cardo[ \$]",
"^Rick[ \$]",
"^Rigoberto[ \$]",
"^Rinaldo[ \$]",
"^Robertino[ \$]",
"^Roberto[ \$]",
"^Robinson[ \$]",
"^Robustiano[ \$]",
"^Rod[ \$]",
"^Rodolfo[ \$]",
"^Roger[ \$]",
"^Rodrigo[ \$]",
"^Rogelio[ \$]",
"^Rolando[ \$]",
"^Rold[áa]n[ \$]",
"^Rom[áa]n[ \$]",
"^Romano[ \$]",
"^Romeo[ \$]",
"^Romildo[ \$]",
"^Romualdo[ \$]",
"^R[óo]mulo[ \$]",
"^Ronan[ \$]",
"^Roque[ \$]",
"^Rosario[ \$]",
"^Rosendo[ \$]",
"^Roy[ \$]",
"^Rub[ée]n[ \$]",
"^Rudy[ \$]",
"^Rufino[ \$]",
"^Rufo[ \$]",
"^Ruperto[ \$]",
"^Rutilio[ \$]",
"^Ruy[ \$]",
"^Ruyman[ \$]",
"^Ryan[ \$]",
"^Sabas[ \$]",
"^Sabino[ \$]",
"^Sacha[ \$]",
"^Sadoc[ \$]",
"^Salom[óo]n[ \$]",
"^Salustio[ \$]",
"^Salvador[ \$]",
"^Salviano[ \$]",
"^Salvino[ \$]",
"^Salvo[ \$]",
"^Samuel[ \$]",
"^Sancho[ \$]",
"^Sandalio[ \$]",
"^Sanders[ \$]",
"^Sandro[ \$]",
"^Sans[óo]n[ \$]",
"^Santiago[ \$]",
"^Santo[ \$]",
"^Santos[ \$]",
"^Saturnino[ \$]",
"^Saturno[ \$]",
"^Sa[úu]l[ \$]",
"^Saulo[ \$]",
"^Saunders[ \$]",
"^Saverio[ \$]",
"^Sayi[ \$]",
"^Sean[ \$]",
"^Sebasti[áa]n[ \$]",
"^Secundino[ \$]",
"^Segismundo[ \$]",
"^Segundo[ \$]",
"^Selim[ \$]",
"^Sempronio[ \$]",
"^S[ée]neca[ \$]",
"^Sen[ée]n[ \$]",
"^Septimio[ \$]",
"^S[ée]ptimo[ \$]",
"^Seraf[íi]n[ \$]",
"^Sergio[ \$]",
"^Servando[ \$]",
"^Servio[ \$]",
"^Severiano[ \$]",
"^Severino[ \$]",
"^Severo[ \$]",
"^Sidonio[ \$]",
"^Sigfrido[ \$]",
"^Silas[ \$]",
"^Sileno[ \$]",
"^Silvano[ \$]",
"^Silverio[ \$]",
"^Silvestre[ \$]",
"^Silvino[ \$]",
"^Silvio[ \$]",
"^Sime[óo]n[ \$]",
"^Sim[óo]n[ \$]",
"^Sim[óo]nides[ \$]",
"^Simplicio[ \$]",
"^Sinforiano[ \$]",
"^Sinforoso[ \$]",
"^Si[óo]n[ \$]",
"^Sirio[ \$]",
"^Sixto[ \$]",
"^S[óo]crates[ \$]",
"^S[óo]focles[ \$]",
"^Soi[ \$]",
"^Sol[ \$]",
"^Solano[ \$]",
"^Sol[óo]n[ \$]",
"^Sotero[ \$]",
"^Stanley[ \$]",
"^Stephan[ \$]",
"^Suyai[ \$]",
"^Tabar[ée][ \$]",
"^Taciano[ \$]",
"^Tacio[ \$]",
"^T[áa]cito[ \$]",
"^Tadeo[ \$]",
"^Tamaro[ \$]",
"^Tancredo[ \$]",
"^Tao[ \$]",
"^Tarquino[ \$]",
"^Tarsicio[ \$]",
"^Taurino[ \$]",
"^Tayil[ \$]",
"^Tel[ée]maco[ \$]",
"^Telmo[ \$]",
"^Tem[íi]stocles[ \$]",
"^Teo[ \$]",
"^Teobaldo[ \$]",
"^Teoberto[ \$]",
"^Te[óo]crito[ \$]",
"^Teodorico[ \$]",
"^Teodoro[ \$]",
"^Teodosio[ \$]",
"^Teofanes[ \$]",
"^Te[óo]filo[ \$]",
"^Teofrasto[ \$]",
"^Tercio[ \$]",
"^Terenciano[ \$]",
"^Terencio[ \$]",
"^Tertuliano[ \$]",
"^Teseo[ \$]",
"^Theo[ \$]",
"^Tiago[ \$]",
"^Tiberio[ \$]",
"^Tiburcio[ \$]",
"^Ticiano[ \$]",
"^Timoteo[ \$]",
"^Tirso[ \$]",
"^Tito[ \$]",
"^Tiziano[ \$]",
"^Tob[íi]as[ \$]",
"^Tolomeo[ \$]",
"^Tom[áa]s[ \$]",
"^Tommy[ \$]",
"^Ton[iy][ \$]",
"^Tom[ée][ \$]",
"^Toño[ \$]",
"^Toqui [ \$]",
"^Torcuato[ \$]",
"^Toribio[ \$]",
"^Traful[ \$]",
"^Tranquilino[ \$]",
"^Tr[áa]nsito[ \$]",
"^Trinidad[ \$]",
"^Trist[áa]n[ \$]",
"^Tubal[ \$]",
"^Tula[ \$]",
"^Tulio[ \$]",
"^T[úu]pac[ \$]",
"^Ubaldo[ \$]",
"^Udolfo[ \$]",
"^Ugolino[ \$]",
"^Ula[ \$]",
"^Uldarico[ \$]",
"^Ule[ \$]",
"^Ulfrido[ \$]",
"^Ulises[ \$]",
"^Ulrico[ \$]",
"^Unelen [ \$]",
"^Urbano[ \$]",
"^Uriel[ \$]",
"^Urso[ \$]",
"^Uziel[ \$]",
"^Valdemar[ \$]",
"^Valente[ \$]",
"^Valent[íi]n[ \$]",
"^Valentino[ \$]",
"^Valeriano[ \$]",
"^Valerio[ \$]",
"^Venancio[ \$]",
"^Venceslao[ \$]",
"^Ventura[ \$]",
"^Vasile[ \$]",
"^Vespasiano[ \$]",
"^Vicencio[ \$]",
"^Vicente[ \$]",
"^V[íi]ctor[ \$]",
"^Victoriano[ \$]",
"^Victorino[ \$]",
"^Victorio[ \$]",
"^Vinicio[ \$]",
"^Virgilio[ \$]",
"^Virginio[ \$]",
"^Visitaci[óo]n[ \$]",
"^Vital[ \$]",
"^Vito[ \$]",
"^Vitoldo[ \$]",
"^Viviano[ \$]",
"^Vladimir[ \$]",
"^Vladimiro[ \$]",
"^Vulpiano[ \$]",
"^Walberto[ \$]",
"^Waldemar[ \$]",
"^Waldo[ \$]",
"^Wally[ \$]",
"^Walter[ \$]",
"^Wara[ \$]",
"^Warren[ \$]",
"^Washington[ \$]",
"^Wayra[ \$]",
"^Wenceslao[ \$]",
"^Werner[ \$]",
"^Wilfredo[ \$]",
"^Wilfrido[ \$]",
"^Wilka[ \$]",
"^William[ \$]",
"^Wilson[ \$]",
"^Wiñay[ \$]",
"^Woody[ \$]",
"^Xavi [ \$]",
"^Xavier [ \$]",
"^X[óo]chtil[ \$]",
"^Yaco[ \$]",
"^Yago[ \$]",
"^Yaima[ \$]",
"^Yain[ \$]",
"^Yamil[ \$]",
"^Yaque[ \$]",
"^Yerimen[ \$]",
"^Yuksel[ \$]",
"^Yunca[ \$]",
"^Yune[ \$]",
"^Yung[ \$]",
"^Yvo[ \$]",
"^Zacar[íi]as[ \$]",
"^Zaqueo[ \$]",
"^Zelmar[ \$]",
"^Zenobio[ \$]",
"^Zen[óo]n[ \$]",
"^Zoilo[ \$]",
"^Z[óo]simo",
)


