#Programa Royal Sommelier - Sommelier virtual para o Mercado royal. Exercício final de Algoritmo na faculdade

from time import sleep
import os
print("*"*50) #Início da tela de Apresentação
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*14,"Royal Sommelier"," "*15,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"," "*46,"*")
sleep(0.2)
print("*"*50) #Fim da Tela de Apresentação
print("Conectando", end ="") #Início status de conexão
sleep(1)
print("  >", end=" ")
sleep(1)
print("  >", end=" ")
sleep (1)
print("  >")
sleep(1.6)#Fim status conexão

os.system('clear') #Limpar a tela do sistema
print('Bem Vindo ao Royal Sommelier! \n \n \n') #Boas vindas e identificação do cliente

print('Me chamo Charles e sou seu Royal Sommelier\n')
sleep(0.65)
print('Para o atendimento Royal que merece, preciso de algumas informações:\n')
sleep(0.65)
sex=0

while sex not in (1,2): #Verificação de validade da escolha
	sex = int(input('Como devo me dirigir?\n \n[1] Senhora \n[2] Cavalheiro\n'))
	#Condições para tratamento pessoal
	if sex == 1:
		trat="Senhora"
		nome=input('\nEncantado Senhora! E como se chama?:\n')
	elif sex == 2:
		trat="Senhor"
		nome=input('\nÉ um prazer, Cavalheiro! E como se chama?:\n')
	else:
		print(f'\nNão compreendi a opção, pode repetir?\n')

print(f'\nEntão {trat} {nome}, vamos falar sobre vinhos.\n')
tipo=0
#Escolha do tipo de vinho
while tipo not in (1,2,3):#Verificação de validade da escolha
	tipo=int(input('E qual o tipo que mais lhe agrada? \n[1] Tinto \n[2] Branco \n[3] Espumante\n '))
	if tipo not in (1,2,3):
		print(f'\nNão compreendi a opção, pode repetir?\n')
	else:
		print('Perfeitamente.\n')

print(f'Vamos aprofundar um pouco mais, {trat} {nome}?\n\n')
pais=0
uva=0
# Bloco de escolha do país e do tipo de uva
while pais not in (1,2,3,4,5,6):
	pais=int(input('De qual país gostaria que seu vinho viesse?\n[1] Argentina\n[2] Chile\n[3] Itália\n[4] Espanha\n[5] França\n[6] Portugal\n'))
	if pais == 1:
		pais1="Argentina"
		os.system('clear') #Limpar a tela do sistema
		print(f'Uma excelente escolha! Particularmente, seria a minha também!')
		if tipo == 1:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais1} nós temos vinhos das seguinte uvas: \n[1] Malbec\n[2] Syrah\n[3] Cabernet Sauvignon\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n \nALAMOS MALBEC 2018\n')
					print('Seguindo a tendência mundial de vinhos mais gastronômicos e menos alcóolicos, a partir da safra de 2016, o Alamos Malbec passou a ser talhado em um estilo mais elegante, e logo conquistou excelentes 91 pontos de James Suckling, que atribuiu a mesma nota às safras 2016 e 2017. Impressionado com a nova versão do vinho, o crítico elogiou o equilíbrio e a finesse do tinto, "uma das melhores compras de todo o mercado". É sem dúvida um dos eternos achados do Novo Mundo, um verdadeiro clássico argentino. Muito recomendado!\n')
					print('Harmoniza bem com carnes vermelhas e aves de sabor forte.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n DV Catena Syrah 2016\n')
					print('Elaborado com uvas de dois vinhedos excepcionais, plantados em altitudes distintas, este vinho da linha DV Catena, produzida para o mercado argentino, é o melhor Syrah do Catena Zapata. Rico e profundo, com ótima complexidade, mostra um bouquet complexo e convidativo, cheio de nuances\n')
					print('Harmoniza bem com carnes vermelhas, carnes de caça e queijos duros.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Animal Cabernet Sauvignon 2016\n')
					print('Elaborado por Ernesto Catena exclusivamente com uvas Cabernet Sauvignon de cultivo orgânico, o Animal é talhado para exaltar o caráter varietal da Cabernet, sendo apenas parcialmente maturado em barricas de carvalho. Rico, com notas de frutas maduras e um leve toque vegetal típico da casta, é um belo Cabernet, de impressionante relação qualidade/preço.\n')
					print('Harmoniza bem com carnes vermelhas, carnes de caça e queijos duros.')
		elif tipo == 2:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais1} nós temos vinhos das seguinte uvas: \n[1] Chardonnay\n[2] Sauvingnon Blanc\n[3] Torrontés\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n El Enemigo Chardonnay 2016\n')
					print('Assinado por Alejandro Vigil, um dos mais talentosos enólogos argentinos da atualidade, este vinho confere uma nova dimensão aos brancos de Mendoza. Uvas de Tupungato, cultivadas a 1500 metros de altitude, são fermentadas em barricas de carvalho francês, originando um branco intenso e cheio de caráter. No nariz, impõem-se notas de frutas cítricas e aromas minerais. No palato, é untuoso, com fruta madura e grande frescor. O El Enemigo Chardonnay é um branco sério e persistente. Um dos mais fantásticos brancos produzido na Argentina. A safra 2016 mereceu nada menos que 98 pontos de James Suckling: "Realmente maravilhoso!".\n')
					print('Harmoniza bem com saladas, frutos do mar, peixes e aves brancas.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Alamos Sauvignon Blanc 2018\n')
					print('Elaborado por Catena Zapata com uvas de vinhedos plantados em altitudes elevadas, este saboroso branco mostra agradáveis aromas de frutas cítricas e bastante frescor. Excelente relação qualidade/preço.\n')
					print('Harmoniza bem com peixes, crustáceos e queijo de cabra.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Alamos Torrontés 2018\n')
					print('Classificado com a nota mais alta já concedida a um Torrontés pela Wine Spectator nas safras de 2013, 2015 e 2016, o Alamos Torrontés é o melhor vinho elaborado com esta emblemática casta para a revista. Rico e aromático, com ótimo frescor e elegância, é elaborado com uvas de vinhedos plantados na região de Salta.\n')
					print('Harmoniza bem com frutos do mar, aperitivo, carnes brancas delicadas e queijos de cabra.')
		elif tipo == 3:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais1} nós temos vinhos das seguinte uvas: \n[1] Chardonnay\n[2] Chenin Blanc\n[3] Pinot Noir\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n COSECHA TARDIA\n')
					print('Um espumante doce e único, elaborado com uvas Chardonnay colhidas supermaduras, que lhe conferem um delicado sabor e doçura. O vinho perfeito para quem quer brindar à doçura da vida!\n')
					print('Harmoniza bem com canapés, especialmente de queijos azuis, sobremesas a base de frutas ou creme, como crème brûlée.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n ONE BOTTLE OF BUBBLES \n')
					print('Espumante de cor amarelo brilhante com borbulhas finas e intensas, no nariz apresenta notas frutadas como pêssego de damasco, flores brancas e um leve toque herbáceo. Em boca prevalece as notas frutadas com final fino e extrovertido.\n')
					print('Acompanha peixes e frutos do mar, pratos leves como saladas, ceviches e carpaccios, além de ser uma ótima bebida para desfrutar bem geladinha, sem acompanhamentos, em um belo dia de verão.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n PERDRIEL CHAMPENOISE\n')
					print('Um vinho de cor amarelo palha com pérlage muito atraente. No nariz apresenta notas cítricas, frutas como pêssego e notas de pão tostado, em boca tem boa cremosidade com um final longo e fresco.\n')
					print('Um vinho para combinar com camarões grelhados, lulas a dore, ostras ou mexilhões.')
	elif pais == 2:
		pais2="Chile"
		os.system('clear') #Limpar a tela do sistema
		print('Uma excelente escolha! Particularmente, seria a minha também!')
		if tipo == 1:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido no {pais2} nós temos vinhos das seguinte uvas: \n[1] Carmenère \n[2] Merlot\n[3] Pinot Noir\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n ANAKENA ONA ANDES\n')
					print('Cor vermelho rubi com halos violáceos. O nariz apresenta frutas negras como ameixa e cassis, chocolate amargo e especiarias. O paladar mostra taninos imponentes e macios, encorpado, final de boca longo e intenso. Certamente vai envelhecer com muita qualidade.\n')
					print('Harmonização: Grande companhia para bisteca bovina grelhada, lombo de porco assado, também queijos fortes como Grana Padano, Manchego e Cheddar')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n BIRDMAN MERLOT\n')
					print('Um vinho bem frutado, com notas marcantes de framboesa e amora, o Birdman Merlot tem uma textura macia e um final muito agradável.\n')
					print('Harmonização: Massas, pizzas e queijos cremosos leves. Também harmoniza com carnes vermelhas grelhadas ou assadas, gratinados e guisados.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n TAMA VINEYARD SELECTION PINOT NOIR 2015 \n')
					print('Vermelho-rubi. Apresenta aroma complexo com forte presença de morangos, cereja e cravo-da-índia, complementado por leve toque de folhas de chá. Em boca é delicado com final persistente.\n')
					print('Harmonização: Acompanha carnes brancas de sabor forte, aves de caça e risotos.')
		elif tipo == 2:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais2} nós temos vinhos das seguinte uvas: \n[1] Chardonnay\n[2] Sauvingnon Blanc\n[3] Semillon\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n \n TAMA VINEYARD SELECTION CHARDONNAY 2014\n')
					print('Amarelo-palha intenso. Apresenta notas de frutas tropicais e delicada lembrança da passagem por carvalho. Em boca é intenso e levemente cremoso.\n')
					print('Harmonização: Delicado e com médio corpo, este vinho acompanha perfeitamente carnes brancas em geral, massas com molhos à base de frutos do mar ou com leve cremosidade.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n HARAS DE PIRQUE ALBACLARA 2017\n')
					print('Amarelo-palha com nuances esverdeadas. O aroma revela delicada complexidade, com mix de frutas, mineral e uma pontinha de especiarias. Na boca é fresco e elegante, com toque floral e frutas cítricas e final de boca levemente mineral.\n')
					print('Harmonização: Acompanhamento perfeito para peixes, carnes brancas, queijos de massa mole.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Bodega Vieja\n')
					print('Vinho branco fresco e frutado, apresenta aromas de frutas tropicais e limão. Em boca, possui deliciosa textura e agradável acidez.  \n')
					print('Harmonização: Indicado para acompanhar peixes e mariscos, além de excelente como aperitivo.')
		elif tipo == 3:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais2} nós temos vinhos das seguinte uvas: \n[1] Chardonnay\n[2] Sauvignon Blanc\n[3] Pinot Noir\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Espace of Limarí Brut\n')
					print('Um toque leve, cítrico e refrescante tornam este espumante ideal para ser degustado em qualquer momento, harmonizado ou não.\n')
					print('Harmonização: Quiche de presunto cru com abacaxi, tomate recheado com atum, filé de peixe ao molho branco, risoto cremoso de camarão, coxinha de frango.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Amaral Brut\n')
					print('Com tom amarelo claro, com alguns reflexos esverdeados, apresenta aroma frutado com toque delicado de aromas florais. Já o paladar apresenta bolhas elegantes e paladar redondo, mas com grande frescura e acidez.\n')
					print('Harmonização:Carnes: Peixes e outros frutos do mar. Massas e molhos: Massas com molho pesto e branco. Risotos: Shimeji e Castanhas. Saladas diversas. Queijos: Gouda, Brie e Gruyère.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Casillero del Diablo Brut Reserva (2011)\n')
					print('Brilhante, com uma bela cor amarela pálida e borbulhas muito delicadas e pequenas. É possível sentir notoriamente a mineralidade. A acidez é maravilhosa e amigável, graças ao caráter que proporcionam as frutas, principalmente o limão e o marmelo. Alguns pequenos detalhes da levedura realçam a elegância \n')
					print('É ideal para acompanhar aperitivos compostos por peixes, mariscos ou crustáceos. A cozinha japonesa é a aliança perfeita, especialmente se apreciada condimentada com wasabi e shoyu.')
	elif pais == 3:
		pais3="Itália"
		os.system('clear') #Limpar a tela do sistema
		print('Uma excelente escolha! Particularmente, seria a minha também!')
		if tipo == 1:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais3} nós temos vinhos das seguinte uvas: \n[1] Sangiovese\n[2] Merlot\n[3] Cabernet Sauvignon\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n VILLA ANTINORI 2015 \n')
					print('Vermelho-rubi profundo. Aroma de frutas do bosque como mirtilo e amora, com leve toque de baunilha. Na boca apresenta bom corpo, taninos macios e notas de frutas do bosque maduras.\n')
					print('Harmonização: Acompanha perfeitamente os antipasti, as massas com molhos de tomate e os embutidos.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Castiglion Del Bosco Prima Pietra 2014\n')
					print('Aos olhos é vermelho em tom rubi, permeado pelo aroma com notas de frutas vermelhas, misturadas com notas levemente picantes. O paladar é complexo, bastante rico em taninos macios, espessos e aveludados.\n')
					print('Harmonização: Carnes: Filé Mignon e Maminha. Risotos: Tomate Seco, Marguerita e Caprese. Queijos: Gouda e Brie.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n BOTROSECCO 2016\n')
					print('Um vinho complexo, de personalidade. No nariz, apresenta notas balsâmicas e leve toque de baunilha, seguidos por notas de frutas vermelhas maduras. Em boca é sedoso, volumoso, bem estruturado e persistente\n')
					print('HarmonizaçãoUm vinho gastronômico, que pode ser servido acompanhando pratos de carne vermelha de sabor marcante, como cordeiro e outras carnes de caça. Além de queijos maduros em geral.')
		elif tipo == 2:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais3} nós temos vinhos das seguinte uvas: \n[1] Chardonnay\n[2] Roscetto\n[3] Pinot Grigio\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n FICHI D´INDIA BIANCO 2018\n')
					print('Cor amarela clara com tons esverdeados, no nariz notas frescas de flor de laranjeira, tomilho, rosa e lavanda. Na boca ele é fresco com notas mineral e frutado. Um ótimo equilíbrio e entre suavidade e frescor\n')
					print('HarmonizaçãoUm branco para acompanhar pratos a base de peixe frito, seja como empanado como aperitivo ou grelhado acompanhado de legumes na manteiga')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n FERENTANO 2015\n')
					print('Amarelo-palha intenso. Aromático, com notas de frutas brancas maduras, mescladas a leve toque herbáceo. Em boca é equilibrado e elegante.\n')
					print('HarmonizaçãoAcompanha pratos a base de frutos do mar e carnes brancas em geral, além de queijos de massa mole.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n SANTA CRISTINA PINOT GRIGIO 2016\n')
					print('Amarelo palha com reflexos esverdeados. Aroma frutado e intenso, com notas citricas, maçã verde e laranja. Em boca é fresco, agradavel, com bom equilibrio entre fruta e acidez.\n')
					print('HarmonizaçãoPode ser servido como aperitivo ou acompanhando pratos leves.')
		elif tipo == 3:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais3} nós temos vinhos das seguinte uvas: \n[1] Chardonnay\n[2] Pinot Nero\n[3] Pinot Noir\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n COSTARIPA BRUT\n')
					print('Amarelo-palha claro, com reflexos esverdeados, com espuma branca e perlage fino e persistente. Intenso aroma de fruta fresca, notas de maçã e leve toque de leveduras, sálvia e mel. Harmônico e de ótima complexidade, saboroso e persistente em sua tipicidade elegante.\n')
					print('Harmonização: Pode ser servido como aperitivo, acompanhando pratos de carnes brancas ou aves de caça, vitello tonnato.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n COSTARIPA BRUT ROSÉ\n')
					print('Vermelho-cereja claro, que com o tempo pode evoluir para um tom de salmão como a "casca da cebola". Espuma branca e perlage fino e persistente. No nariz apresenta intenso aroma de fruta madura com notas de groselha, leve toque de baunilha e floral. Na boca é elegante, harmônico, amplo e estruturado.\n')
					print('Harmonização: Ideal para beber mesmo sem acompanhamento. Um vinho versátil, que acompanha desde saladas e pratos mais leves até alguns mais estruturados, queijos, embutidos, etc..')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n MARCHESE ANTINORI CUVÉE ROYALE\n')
					print('Amarelo claro, com muita espuma, perlage delicada e duradoura. Aromas de pêssegos brancos, crostas de pão e fermento. Equilíbrio e vivacidade típicos de um Brut bem feito\n')
					print('Harmonização: Harmoniza perfeitamente com aperitivos, peixes, vegetais e carnes brancas, devido à sua fragrância frutada e floral.')
	elif pais == 4:
		pais4="Espanha"
		os.system('clear') #Limpar a tela do sistema
		print('Uma excelente escolha! Particularmente, seria a minha também!')
		if tipo == 1:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais4} nós temos vinhos das seguinte uvas: \n[1] Tempranillio\n[2] Petit Verdot\n[3] Garnacha \n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n MARQUES DE GRIÑON CRIANZA SELECCIÓN ESPECIAL 2014\n')
					print('Um vinho redondo, muito equilibrado, cor rubi intenso e muito saboroso. Apresenta notas de baunilha e especiarias doces, com um toque de frutas vermelhas\n')
					print('HarmonizaçãoAcompanha carnes de caça, assados, aves e queijos curados.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n MARQUES DE GRIÑON SVMMA VARIETALIS 2008\n')
					print('Vermelho-rubi com reflexos púrpura. Aroma intenso e marcante, com notas de frutas do bosque e toques de especiarias e minerais. Na boca é persistente, complexo, com boa estrutura. Taninos macios e doces.\n')
					print('HarmonizaçãoGrelhados, assados, bacalhau, aves de carne escura, massas com molhos densos e de tomate, queijos condimentados.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n REAL COMPAÑIA DE VINOS GARNACHA 2015\n')
					print('Um vinho de cor vívida e bastante escura. Aroma muito pronunciado de frutas vermelhas, ameixas e pêssego. Na boca lembra muito o nariz com uma acidez marcante que lhe confere muito frescor.\n')
					print('HarmonizaçãoAcompanha muito bem embutidos, pratos de carnes grelhadas e churrasco.')
		elif tipo == 2:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais4} nós temos vinhos das seguinte uvas: \n[1] Albariño\n[2] Verdejo \n[3] Viura\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n PAZO CILEIRO ALBARIÑO 2017\n')
					print('De cor amarelo dourado claro com reflexos esverdeados. No nariz se mostra limpo e equilibrado, com notas de frutas cítricas e frutas brancas de caroço como pêra e carambola, ao final se mostra muito aromático com nuances de flores brancas e levemente herbáceo. Em boca é um vinho fresco, redondo, elegante e persistente, completo e muito agradável\n')
					print('Harmonização: Acompanha pratos de peixes de carne branca, frutos do mar e crustáceos. Pode ser uma ótima combinação com espaguete ao vôngole, risoto de frutos do mar e queijos frescos.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n MARQUES DE GRIÑON VERDEJO RUEDA 2014\n')
					print('Cor amarelo claro com reflexos esverdeados. Aroma intenso e delicado, onde se conjugam frutas brancas como nêspera e flores brancas. Em boca é redondo, suave e untuoso, com um agradável amargor ao final que aporta grande persistência.\n')
					print('Harmonização: Para acompanhar aperitivos, mariscos, pescada azul e carnes brancas em geral.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n VIÑA MURIEL BLANCO RESERVA 2010\n')
					print('Viura é conhecida por ser complexa e aromática. No nariz apresenta frutas cítricas e flores brancas com especiarias finas e torradas do envelhecimento em carvalho. Na boca uma mistura de frescor e maciez, com um volume de boca especial e memorável.\n')
					print('Harmonização: Cai bem com saladas mais encorpadas, peixes e frutos do mar.')
		elif tipo == 3:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais4} nós temos vinhos das seguinte uvas: \n[1] Macabeo\n[2] Parellada\n[3] Xarello \n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Cava Codorníu Clasico Brut\n')
					print('Um dos rótulos mais tradicionais da Codorníu, é fresco e equilibrado, com notas delicadas de frutas tropicais. Um Espumante Cava perfeito para acompanhar os bons momentos da vida, em festas e celebrações.\n')
					print('Harmonização: Aprecie na companhia de aperitivos, como canapés, tortas salgadas, frutas secas e nozes.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Freixenet Cordón Negro \n')
					print('Lançado originalmente em 1974, Freixenet Cordón Negro é leve, apreciado por seu grande frescor e conhecido mundialmente por sua emblemática garrafa preta e dourada. Com aromas de frutas cítricas e acidez equilibrada.\n')
					print('Harmonização: Canapés variados, risoto de presunto cru, carpaccio, peixe grelhado com purê de batatas, bolinho de bacalhau, comida japonesa.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Freixenet Carta Nevada Demi Sec \n')
					print('A história da Freixenet começa na pequena cidade de Sant Sadurní d´Anoia. O Cava Freixenet Carta Nevada possui aromas que nos recordam maçã fresca e notas florais. Apresenta borbulhas finas, é levemente doce e refrescante.\n')
					print('Harmonização: Canapés à base de peixe, frutos do mar, ceviche de peixe branco, salmão assado e queijos de massa mole, salgadinhos de festa, sanduíches e tortas salgadas.')
	elif pais == 5:
		pais5="França"
		os.system('clear') #Limpar a tela do sistema
		print('Uma excelente escolha! Particularmente, seria a minha também!')
		if tipo == 1:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais5} nós temos vinhos das seguinte uvas: \n[1] Cabernet Franc\n[2] Merlot\n[3] Gamay \n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n MARQUIS DELATRE MÉDOC 2016\n')
					print('Cor vermelho rubi escuro com bordas violáceas, aromas que lembram frutas negras como cereja e ameixa, toques de baunilha e tostado. Em boca mostra taninos finos, textura macia e elegante. Fim de boca longo e frutado.\n')
					print('Harmonização: Experimente com carnes vermelhas carne de caça e queijos de massa dura.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n MARQUIS DELATRE BORDEAUX ROUGE 2017\n')
					print('Cor vermelho rubi escuro, aromas que lembram frutas vermelhas como cereja e amora, toques de tostado e pimenta negra. Taninos finos, textura macia e elegante. Fim de boca longo e frutado. \n')
					print('Harmonização: Excelente acompanhante para carnes assadas.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n BEAUJOLAIS 2016\n')
					print('Vermelho-cereja intenso. Aroma intenso e frutado, como cereja, groselha e leve toque de banana, complementados por notas florais, como violeta e peônia. A boca corresponde ao nariz. Equilibrado, com taninos discretos e macios, boa acidez e frescor.\n')
					print('Harmonização: Próprio para os dias quentes e pratos frescos e leves, acompanha bem inclusive sanduíches.')
		elif tipo == 2:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais5} nós temos vinhos das seguinte uvas: \n[1] Viogner\n[2] Sauvignon \n[3] Chardonnay\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n SAINT COSME COTES-DU-RHONE BLANC 2012\n')
					print('Um vinho que apresenta notas de frutas de caroço como pêssego maduro, manga, frutas tropicais como papaya e um leve toque de mel. Na boca ele tem médio corpo.\n')
					print('Harmonização: Ideal para acompanhar peixes brancos grelhados, quiche de alho poró, sushi, sashimi e queijos leves.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n LITTLE JAMES BASKET PRESS BLANC 2016\n')
					print('Um vinho que apresenta notas de damasco, marmelada e notas cítricas. Na boca ele é médio corpo, macio e com bom frescor.\n')
					print('Harmonização: Um vinho para ser bebido no dia a dia, para acompanhar peixes leves com sabores intensos')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n CORTON CHARLEMAGNE GRAND CRU 2015\n')
					print('Quando jovem ele é de cor pálida com nuances douradas, chegando a tons âmbar com a idade. No nariz ele mostra notas amanteigadas, frutas cítricas, maçã cozida, mel e especiarias. Na boca tem muita concentração, equilíbrio, frescor e complexidade.\n')
					print('Harmonização: Um vinho para acompanhar mariscos, crustáceos, lagosta, peixes e carnes brancas.')
		elif tipo == 3:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais5} nós temos vinhos das seguinte uvas: \n[1] Chardonnay\n[2] Pinot Noir\n[3] Castas Tradicionais \n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n CRÉMANT BRUT RÉSERVE\n')
					print('Amarelo-palha claro, com perlage fina e constante. Apresenta notas de frutas cítricas, com toque floral. Em boca é vivo e agradável, com final persistente.\n')
					print('Harmonização: Ideal para ser servido como aperitivo ou acompanhando pratos de pescados e frutos do mar.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n CRÉMANT BRUT ROSÉ\n')
					print('Um espumante com borbulhas finas e regulares, de cor rosa com tons salmão. No nariz ele possui frutas vermelhas (groselha e framboesa) e frutas cítricas, na boca ele é cheio, apresenta vivacidade e frescor.\n')
					print('Harmonização: Ideal para servir como aperitivo ou com sobremesa a base de frutas. Acompanha também a cozinha asiática.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n DELOZANNE BLANC DE BLANCS\n')
					print('Cor amarelo palha com reflexos verdeais, perlage persistente e fina. Aroma muito elegante e fresco que lembram casca de limão siciliano, frutas de polpa branca como maça verde, pera e pêssego, e um delicado floral. Em boca mostra um colchão de espuma cremoso e de bom volume. Novamente marcado pelo frescor e leveza com fim de boca longo\n')
					print('Harmonização: Excelente para acompanhar saladas leves, frango, pratos com peixes delicados.')
	elif pais == 6:
		pais6="Portugal"
		os.system('clear') #Limpar a tela do sistema
		print('Uma excelente escolha! Particularmente, seria a minha também!')
		if tipo == 1:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido em {pais6} nós temos vinhos das seguinte uvas: \n[1] Touringa Nacional\n[2] Tinta Roriz\n[3] Alfrocheiro \n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n FLOR DAS TECEDEIRAS 2017\n')
					print('Cor rubi intenso e aroma de frutos pretos do bosque. Na boca revela-se expressivo e volumoso, com taninos sólidos e muito encorpado, devido à sua componente floral dominante. Notas delicadas de baunilha e uma certa mineralidade.\n')
					print('Harmonização: Acompanha carnes assadas ou churrasco, bem como queijos e gastronomia associada à vida mais descontraída/jovem, como pizzas, batatas fritas, almôndegas e massas.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n MAGNUM VINES LILÁS 2014\n')
					print('Um vinho de aspecto límpido e com rubi. No nariz seus aromas são intensos, lembrando amoras, compotas e arbsutos silvestres. Na boca tem taninos suaves, um bom equilíbrio , muito frescor e longo final.\n')
					print('Harmonização: É um vinho muito versátil, pode ser bebido o ano todo e combina com uma enorme variedade de comida.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n JARDIM DA ESTRELA 2015\n')
					print('Vinho com aromas bem definidos de frutos silvestres e notas apimentadas. Na boca mostra juventude, é frutado com taninos redondos e bem integrados. Tem um final médio e suave.\n')
					print('Harmonização: Carnes vermelhas em geral, queijos maduros.')
		elif tipo == 2:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais6} nós temos vinhos das seguinte uvas: \n[1] Avesso\n[2] Bical\n[3] Malavasia-Fina\n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n COVELA EDIÇÃO NACIONAL AVESSO RESERVA 2017\n ')
					print('Cor amarelo palha com reflexos verdeais. Aroma muito elegante e refinado. Sobressai o seu lado floral delicado e os frutos arbóreos como a maçã, o pêssego e a nectarina. Subtilmente, podemos encontrar um lado tropical marcado pelo abacaxi e polpa de coco fresca. No paladar, ataque cremoso e acidez mineral. Aroma de boca persistente, intenso, revelando uma integração perfeita entre a barrica e o vinho. Final guloso que nos remete para uma segunda prova.\n')
					print('Harmonização: Um branco de excelente estrutura para acompanhar bacalhau grelhado, arenque com creme de leite, queijo canastra curado. Também pode ser uma ótima companhia para um pato no tucupi e moqueca capixaba.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n RIBEIRO SANTO PINHA 2016\n')
					print('Cor amarelo palha límpido e transparente. Apresenta aromas de frutos tropicais cítricos como abacaxi e maçã verde. Na boca tem uma acidez viva, bem equilibrada com final seco e longo.\n')
					print('HarmonizaçãoAcompanha pratos leves e delicados como lagosta, peixes e crustáceos e forma um belo casamento com risotos de limão siciliano e massas frescas.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n FLOR DE PENALVA 2015\n')
					print('Cor citrina, aroma frutado e típico do estilo tradicional dos brancos do Dão, que toda a gente da região gosta de beber em dias de festa.\n')
					print('Harmonização: Um vinho para acompanhar entradas, pratos a base de frutos do mar grelhados ou queijos frescos.')
		elif tipo == 3:
			while uva not in (1,2,3):
				uva=int(input(f'Produzido na {pais6} nós temos vinhos das seguinte uvas: \n[1] Maria Gomes\n[2] Pinot Noir\n[3] Baga \n'))
				if uva == 1:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Quinta do Boição Special Cuvée Extra Bruto Branco\n')
					print('Côr cítrica com laivos esverdeados. Boas notas cítricas, macãs ácidas, lima, casca de laranja, nuances florais e alguma mineralidade. Acidez viva, bolha fina, estruturado, alguma mousse, complexo e fruto bastante presente.\n')
					print('Harmonização: Um prato de marisco em cataplana de confeção lenta mas estruturado no tempero, vai bem com um espumante cítrico e de bolha fina.')
				elif uva == 2:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Quinta dos Abibes Sublime Brut Nature 2010\n')
					print('Amarelo palha com laivos esverdeados. Límpido. Apresenta notas tropicais, papaia, manga, extraordinária mineralidade, nuances cítricas, lima, maçãs verdes e bouquet bastante complexo. Bolha finíssima, crocante, acidez equilibrada, com muita alma, volumoso mas leve ao mesmo tempo, frutado e notas de toranja no fim.\n')
					print('Harmonização: Um espumante fresco, com acidez viva e vibrante, estruturado, vai bem com um prato de marisco temperado e que leva especiaria.')
				else:
					print(f'Muito bem {trat} {nome}, baseado no seu gosto, indico o vinho:\n\n Alvarinho QM Velha Reserva 2011\n')
					print('Amarelo cítrico ligeiramente dourado. Apresenta notas florais, tropicais, papaia, alguma baunilha e boa mineralidade. Bolha fina, alguma mousse na boca, estruturado e com algum toque sofisticado.\n')
					print('Harmonização: Um vinho espumante com esta acidez e alguma complexidade requer um prato especiado, simples mas com alguma estrutura.')
	else:
		print(f'\nNão compreendi a opção, pode repetir?\n')

#Despedida do cliente
sleep(10)
print(f'\n\n\n\nO Royal agradece pela preferência {trat} {nome}!\n')
print('\nEsperamos que o atendimento tenha sido dígno da Realeza, afinal, o cliente é nosso maior tesouro!\n')
print('Volte Sempre!')


print('<  <  <  Desconectado')
print('Fim da Execução')












