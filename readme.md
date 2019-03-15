## Markovifying the Rijksacademie (Rijksify)

  
_Markov chain is a mathematical model which calculates the next step based on the one (or few) previous steps, but not uses the history of all previously taken steps to make the next move.  _A Markov chain is a stochastic process, but it differs from a general stochastic process in that a Markov chain must be "memory-less". That is, (the probability of) future actions are not dependent upon the steps that led up to the present state. This is called the Markov property. While the theory of Markov chains is important precisely because so many "everyday" processes satisfy the Markov property, there are many common examples of stochastic properties that do not satisfy the Markov property._  [source](https://brilliant.org/wiki/markov-chains/


While attending the Rijksacademie open day in 2018 I got very impressed with the caption texts of the exhibited artworks. The texts had somehow impersonal, uniform style, using a specific Art English which makes the text belong more to the space than to its content. I immediately knew I want to use some technological tool to try to emulate this writing. Then I have discovered [Markovify](https://github.com/jsvine/markovify), which is a Markov chain generator initially developed at BuzzFeed but later realised into the wild. Here is a  walkthrough of a process of using Markov chain generator to create captions for a fictional artwork, Rijksacademie-style



#### 1. Creating the corpus. 
  
Corpus is a large text file which will be used as a source for the script to generate new artwork captions. First goal is to get all the captions from the Rijksacdemie Open day website [https://www.rijksakademie.nl/NL/rijksakademieopen/](https://www.rijksakademie.nl/NL/rijksakademieopen/). This can be done manually, but I am going to scrape it, using [Parsehub](https://www.parsehub.com/) and [Beautifulsoup](https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe). First I am getting the list of all URL’s to the artists page using Parsehub (see artist-urls.csv for the outcome) and exporting it as CSV. Then I install Beautifulsoup. The list of urls is then used in a python script to scrape the part of each link which contains information about the artist. (See rijkssoup.py). I have troubles writing into a text file from the script, since the script keeps overriding the output after going through each link. The dumbest solution seems to be the easiest: I save my session as a text file.  These are the steps (for Mac):
1. Launch terminal
2. Change directory to the folder where the project is stored (cd + drag your folder into the terminal window)
3. Type ‘python rijkssoup.py’
4. Press enter
5. Press Command+S and save the session in your project folder 


#### 2. Editing the corpus

Now as I have my corpus, I am going to open it in Ulysses (any text editor of choice will do, Ulysses is my very favourite and if you are looking for software for writing I highly recommend it) and remove all information which is not an artwork caption (see all-captions.txt for an unedited file). After this is done, (see only-captions.txt for the file I am going to work with at this stage) few steps should be taken to remove any relations to an actual artwork.

1. Remove any indications of gender of the artist, using gender-neutral pronouns (they/their). This can be done with find & replace or manually. This step I think is better to do manually, since sometimes you have to edit they verb as you replace the pronoun (she does —\> they do)
2. Now the artist needs to have a name. My first version had a very funny name, which is rather disruptive if you want to preserve the seriousness of the whole thing. My artist (or a collective) will be called Acronym. I replace every artist name with ‘Acronym 01111010’, adding ‘01111010’ which is Z (first letter of my surname) in binary. 
3. Now the artwork needs the title. Evidence shows that an artwork benefits from an injection of a Russian poet. Since I also want this work to be an amalgam and kinda pop I will take an injection of Nabokov which was made into a recent Blade Runner movie, where a line from Pale Fire was injected into a test the main character was going through.   
	[https://www.reddit.com/r/MovieDetails/comments/a2evri/vladimir\_nabokovs\_pale\_fire\_is\_featured\_in\_both/](https://www.reddit.com/r/MovieDetails/comments/a2evri/vladimir_nabokovs_pale_fire_is_featured_in_both/)   
	[https://medium.com/@mariabustillos/blade-runner-2049-is-revealed-through-the-novel-pale-fire-dd9f04768439](https://medium.com/@mariabustillos/blade-runner-2049-is-revealed-through-the-novel-pale-fire-dd9f04768439)  
	I am very tempted to call ‘my' artwork Cells Interlinked, but I will have A Tall White Fountain as a title.
4. Now RijksakademieOPEN 2018 has to be replaced with ’this show’ and Rijksacademie has to be replaced with ‘residency’. 
5. Now more precise editing has to take place. The scraping picks up some sentences written in the first person, so, not to disrupt the tone, I will remove these parts. 
6. This is the last part I remove names and places, if the meaning of the sentence doesn’t get lost after me doing so, e.g. ‘They started this project after having a conversation with their grandmother’s cousin Agnes’ becomes ‘They started this project after having a conversation with their grandmother’s cousin’. 
7. Now the corpus is ready to be used. See corpus.txt for the edited text. Please note that this is a tiny text to work with, comparing to something like an entire novel.   
	  


#### 3.The script  


1. To get the right length of the output, I have to take a look at the unedited corpus (only-captions.txt) to see how many characters and sentences a caption has on average. The sentences in Art English are quite long, so I would have 5 sentences for one caption. Here is the script I will use.   

	import markovify
	
	with open("corpus.txt") as f:
	    text = f.read()

	text_model = markovify.Text(text, state_size=2)
	
	for i in range(5):

	    print (text_model.make_short_sentence(240))
	
  

Here are some examples of the texts generated by the script:  
  
	_The film starts with a single eye, and the fictions contained therein. Interested in botany, textiles, and the symbolism of flowers, Acronym 01111010 records their daily settings. This inspiration always happens in dialogue with their own private environment, Acronym01111010 shows the continued day-to-day effect of the marvelleous – whilst influenced by their photographs, installations, and films. These works are rooted in material that often originates from personal experiences involving a specific plot of land, in which Acronym 01111010 stages a performance about the excessive forces of motherhood, and the constructed. Acronym 01111010 introduces us to the tension between spirit and body, as well as in the lives of those who continue to build a new body of sculptural and text works exploring the limitations of language._

	_Thus, their practice revolves around an abusive, almost masochist, relationship in which elements of local history, such as form, dimension, and material qualities. An important reference point is a dreadful backing score and the visitor. Acronym 01111010’s work directly addresses the senses and the rigorous, the public and private, as well as anticipation. Acronym 01111010 explores how social constructs are based on mechanisms of control and instability, between natural cycles and clock time, between before and after. Acronym 01111010 years ago, form the basic material is nourishment sand, used on shorelines to combat the natural erosion of beaches._  
  
The texts are not great and the logic is clumsy, but my goal for now would be not the learn more python to create a perfect caption text but to rather see if something very simple can spit out the text which has the same tone and mood as the original. However, I am interested in learning how to perfect it, so if someone knowledgeable is reading this, I appreciate any tips, tutorials and advice.   

2. I want to save the text I generated into a .txt file, here’s the updated script:

	import markovify
	import sys
	import time
	
	
	timestr = time.strftime("%Y%m%d-%H%M%S")
	
	reload(sys)
	sys.setdefaultencoding('utf8')
	
	file = open( timestr +'.txt','w')
	with open("corpus.txt") as f:
	    text = f.read()
	

	text_model = markovify.Text(text, state_size=2)
	

	for i in range(5):
	    file.write(text_model.make_short_sentence(240))
	
  
Again, for beginners (like me), how to run a python script:
	1. Launch terminal
	2. Change directory to the folder where the project is stored (cd + drag your folder into the terminal window)
	3. Type Type ‘python rijksify.py’
	4. Press enter
	5. Watch your .txt file appear in the folder


#### 4. Run & enjoy  

First I wanted to develop this script into some sort of generator, but decided to leave it as a simple exercise: There is enough Art English generators online. I learned few interesting things and got even more interested in Python. Dear reader, I leave you with this:  
  
	_ An image of impotence. Acronym 01111010 developed a process that functions as a strong hint of longing – while walking among the nudes. Their grandmother’s collection of worn-out silk scarves, given to Acronym 01111010 revives and reconstructs memory through photographs and photos from the subject’s surroundings. Something, or rather the thing we’re talking about here is also a product of the war in the Antarctic ice. With the residency housed in a comfortable sofa in front of our reality, created from the subject’s surroundings._

  
  
  

  
  

