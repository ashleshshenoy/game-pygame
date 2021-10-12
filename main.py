import pygame
import math
import random
from pygame import mixer
state='loaded'
HIGHEST_SCORE=[]
faded=True
ENTER_IMG=0

count=1
def game():
	#to save the highest  score :

	
	entry=True
	PLAY=True
	globals()['faded']=True
	pygame.init() # initialising the pygame module 
	screen=pygame.display.set_mode((1000,600)) # setting the game frame 
	clock=pygame.time.Clock()
	frames_per_second=60

	#adding the title and icon to the game window'

	mixer.music.load('assets/audio/background.mp3')
	mixer.music.play(-1)
	pygame.display.set_caption("DEAD POOL")
	some_img=pygame.image.load('assets/image/bullet.png')
	pygame.display.set_icon(some_img)



	#gunman charachter 
	char=pygame.image.load('assets/image/killer.png')
	charx=340
	chary=480
	char_changex=0
	char_changey=0

	def play(xcordinate,ycordinate):
		screen.blit(char,(xcordinate,ycordinate))


	#background image of the game 
	background=pygame.image.load('assets/image/background.jpg')
	background=pygame.transform.scale(background,(800,600))

	#creatong a target board 
	common_target=4
	target=[]
	targetx=[]
	targety=[]
	targetx_change=[]
	targety_change=[]
	''''while True :
		if len(targetx)==4:
			break
		x=random.randint(20,720)
		for j in targetx:
			if not ( targetx[j]==x+20 or targety_change==x-20):
				targetx.append(x)'''



	targetx.append(random.randint(20,200))
	targetx.append(random.randint(220,400))
	targetx.append(random.randint(420,580))
	targetx.append(random.randint(600,720))


	for i in range(common_target):
		target.append(pygame.image.load('assets/image/target.jpg'))
		targety.append(20)
		targety_change.append(10)
		targetx_change.append(3)
	def tar(x,y):
		for i  in range(common_target):
			screen.blit(target[i],(x,y))

	#creating an bullet for the character to shoot 
	#the character must shoot the bullet and it should apper from the  same cordirnates as of the character but underneath the character
	#the bullet than should follow its path straigh till the end of the frame 
	bullet=pygame.image.load('assets/image/bullet.png')
	bullety_change=6
	
	def fire(x,y):
		global state
		state='fired'
		screen.blit(bullet,(x,y))



	#scoring, survive time and score details ,stars
	survive_time=0
	score_value=0
	font_for_score=pygame.font.Font('assets/font/FreeSansBold.ttf',32)
	font_for_score_details=pygame.font.Font('assets/font/FreeSansBold.ttf',15)
	

	def point():
		line='-----------------------------------------------------------------------------------------------------------------------------------------------------------------'
		score=font_for_score.render('Score: {0}'.format(score_value),True,(255,255,255))
		scale1=font_for_score_details.render(line+'Excellent (5 points)',True,(0,225,0))
		scale2=font_for_score_details.render(line+'Good (3 points)' ,True,(255,255,0))
		scale3=font_for_score_details.render(line+'bad (1 point)',True,(255,255,255))
		scale4=font_for_score_details.render(line+'Game over ',True,(255,0,0))
		#survive_time=pygame.time.get_ticks()
		#survive_time=(survive_time-static_time)/1000
		#survive_time=math.trunc(survive_time)
		#survive_time=font_for_score_details.render('Time: {0}'.format(survive_time),True,(225,225,225))
		#screen.blit(survive_time,(805,450))
		screen.blit(score,(820,400))
		screen.blit(scale1,(0,0))
		screen.blit(scale2,(0,102))
		screen.blit(scale3,(0,152))
		screen.blit(scale4,(0,202))
	#checking if the bullet hit the target

	def  hit(targetx,bulletx,targety,bullety):
		boom_sound=mixer.Sound('assets/audio/boom.wav')

		distance=math.sqrt((math.pow((targetx+16)-bulletx,2))+(math.pow(targety-bullety,2)))
		if distance<38:
			boom_sound.play()
			return True
	


	""" creating an entrance with 3 buttons one for 'PLAY' , one for 'ABOUT' and the last one for 'EXIT'  
		The entrace will have ramdom circles flying in the  bakcground of black
		the screen of entrance will fade when the game is entered or when the entrance is called"""
	
	
	def entrance():
		entrance_text=pygame.font.Font('assets/font/FreeSansBold.ttf',30)
		entrance_text1=entrance_text.render("START",True,(225,225,225))
		entrance_text2=entrance_text.render("EXIT",True,(225,225,225))

		fadescreen=pygame.Surface((1000,600))
		
		entrance_image=pygame.image.load('assets/image/entrance.jpg')
		entrance_image=pygame.transform.scale(entrance_image,(1000,600))
		
		fadescreen.blit(entrance_image,(0,0))
		
		
		if faded:
			for alpha in range(0,60):
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						exit()	
				
				
				fadescreen.set_alpha(alpha)
				screen.blit(fadescreen,(0,0))
				pygame.time.delay(60)

				pygame.display.update()
				
			fadescreen.set_alpha(300)	
			pygame.draw.rect(screen,(0,150,0),(450,250,150,50))
			pygame.draw.rect(screen,(150,0,0),(450,350,150,50))
			screen.blit(entrance_text1,(475,255))
			screen.blit(entrance_text2,(490,355))
			pygame.display.update()
			globals()['faded']=False			
		
		pygame.display.flip()

		

	

	def star(x1,y1,x2,y2,x3,y3):
		star1=pygame.image.load('assets/image/star.png')
		star2=pygame.image.load('assets/image/star.png')
		star3=pygame.image.load('assets/image/star.png')
		hole1=pygame.image.load('assets/image/hole.png')
		hole2=pygame.image.load('assets/image/hole.png')
		hole3=pygame.image.load('assets/image/hole.png')
		if score_value<50:
			screen.blit(hole1,(x1,y1))
			screen.blit(hole2,(x2,y2))
			screen.blit(hole3,(x3,y3))
		if score_value>=50 and score_value<100:
			screen.blit(star1,(x1,y1))
			screen.blit(hole1,(x2,y2))
			screen.blit(hole2,(x3,y3))
		if score_value>=100 and score_value<150:
			screen.blit(star1,(x1,y1))
			screen.blit(star2,(x2,y2))
			screen.blit(hole2,(x3,y3))
		if score_value>=150:
			screen.blit(star1,(x1,y1))
			screen.blit(star2,(x2,y2))
			screen.blit(star3,(x3,y3))

	def bigstar(x1,y1,x2,y2,x3,y3):
		star1=pygame.image.load('assets/image/bighole.png')
		star2=pygame.image.load('assets/image/bighole.png')
		star3=pygame.image.load('assets/image/bighole.png')
		hole1=pygame.image.load('assets/image/bigstar.png')
		hole2=pygame.image.load('assets/image/bigstar.png')
		hole3=pygame.image.load('assets/image/bigstar.png')
		if score_value<50:
			screen.blit(hole1,(x1,y1))
			screen.blit(hole2,(x2,y2))
			screen.blit(hole3,(x3,y3))
		if score_value>=50 and score_value<100:
			screen.blit(star1,(x1,y1))
			screen.blit(hole1,(x2,y2))
			screen.blit(hole2,(x3,y3))
		if score_value>=100 and score_value<150:
			screen.blit(star1,(x1,y1))
			screen.blit(star2,(x2,y2))
			screen.blit(hole2,(x3,y3))
		if score_value>=150:
			screen.blit(star1,(x1,y1))
			screen.blit(star2,(x2,y2))
			screen.blit(star3,(x3,y3))




	def end():
		""""HIGHEST_TIME.append(SURVIVE)				#SCORES AND HIGHEST SCORE
		HIGH_TIMED=max(HIGHEST_TIME)"""
		HIGHEST_SCORE.append(score_value)
		HIGHEST_SCORED=max(HIGHEST_SCORE)
		
		img=pygame.image.load('assets/image/gameover.png')
		img=pygame.transform.scale(img,(1000,600))
		
		screen.blit(img,(0,0))
		final_text=pygame.font.Font('assets/font/FreeSansBold.ttf',25)
		final_text_other=pygame.font.Font('assets/font/FreeSansBold.ttf',20)
		final_text1=final_text_other.render(' Better luck next time press enter enter to go to the menu',True,(255,255,255))
		final_text2=final_text.render('You scored: {0}'.format(score_value),True,(225,225,255))
		#final_text3=final_text.render('You survived: {0} seconds'.format(SURVIVE),True,(225,225,255))
		#final_text4=final_text.render('Highest survive time: {0}'.format(HIGH_TIMED),True,(225,225,255))
		final_text5=final_text.render("Highest score: {0}".format(HIGHEST_SCORED),True,(225,225,255))
		screen.blit(final_text1,(250,400))
		screen.blit(final_text2,(600,500))
		#screen.blit(final_text3,(600,550))
		#screen.blit(final_text4,(200,550))
		screen.blit(final_text5,(200,500))
		bigstar(400,120,500,70,600,120)
		
		PLAY=False
	
	



	# for  creating the gaming loop 

	while  True:

		clock.tick(frames_per_second)
		
		while entry:
			button_press=mixer.Sound('assets/audio/pressedcon.wav')
			globals()['static_time']=pygame.time.get_ticks()
			mousex,mousey=pygame.mouse.get_pos()
			if (1,0,0)==pygame.mouse.get_pressed():
				if mousey>=250 and mousey<=300:
					if mousex>=450 and mousex<=600:	
						button_press.play()	
						entry=False	
			if (1,0,0)==pygame.mouse.get_pressed():
				if mousey>=350 and mousey<=400:
					if mousex>=450 and mousex<=600:		
						boom_sound.play()
						exit()

			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit()	
				
			
			
				
				
			entrance()
			pygame.display.update()
			
				
			pygame.display.flip()
		
		if PLAY:

			for event in pygame.event.get():
				if event.type==pygame.QUIT:  # end the loop if the event  is quit 
						exit()
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_LEFT:
						char_changex=-5
					if event.key==pygame.K_RIGHT:
						char_changex=5
							
					if event.key==pygame.K_UP:
						char_changey=-5
					if event.key==pygame.K_DOWN:
						char_changey=5
					if event.key==pygame.K_SPACE:
						if state=='loaded':
							bulletx=charx
							bullety=chary
							shoot_sound=mixer.Sound('assets/audio/gunshot.wav')
							shoot_sound.play()
							fire(bulletx,bullety)
				if event.type==pygame.KEYUP:
					if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT :
						char_changex=0
					if  event.key==pygame.K_UP or event.key==pygame.K_DOWN:
						char_changey=0



			
			screen.fill((0,0,0))
			
			#adding the green background to the game
			screen.blit(background,(0,0))



			#defines how the character  moves 
			charx=charx+char_changex
			chary=chary+char_changey
			play(charx,chary)


			#define the border to the game for the character 
			if charx>750:
				charx=21
			if charx<20:
				charx=749
			if chary>530:
				chary=529
			if chary<400:
				chary=401	
			
			#firing machanics and collison detection
			if state=='fired':
				bullety=bullety-bullety_change
				fire(bulletx,bullety)
				for i in  range(common_target):
					check=hit(targetx[i],bulletx,targety[i],bullety)
					if check:
						if targety[i]<50:
							score_value+=5
						if targety[i]>50 and targety[i]<=100:
							score_value+=3
						if targety[i]>=101 and targety[i]<=150:
							score_value+=5 
						globals()['state']='loaded'
						targetx[i]=random.randint(21,719)
						targety[i]=20
				if bullety<=20:
					globals()['state']='loaded'



			#displaying the target
			for i in range(common_target):
				targetx[i]=targetx[i]+targetx_change[i]
				tar(targetx[i],targety[i])	

			# giving motion to the target
			for i in range(common_target):
				if targetx[i]>=720:
					targety[i]+=targety_change[i]
					targetx_change[i]=-5
					
				if targetx[i]<=20:
					targety[i]+=targety_change[i]
					targetx_change[i]=5
			 
			

			

				
			#Displaying points and score details 
			point()
			star(820,330,880,330,940,330)
			#describes how the game is going to end

		if any([i >=151 for i in targety]):
				end()
				mixer.music.stop()
				end_sound=mixer.Sound('assets/audio/gameover.wav')
				end_sound.play()
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						game()

				
				



		
			
		
		pygame.display.update()

game()