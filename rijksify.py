import markovify
import sys
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

reload(sys)
sys.setdefaultencoding('utf8')
# Get raw text as string
file = open( timestr +'.txt','w')
with open("corpus.txt") as f:
    text = f.read()

# Build the model
text_model = markovify.Text(text, state_size=2)

# Print five randomly-generated sentences
for i in range(5):
    file.write(text_model.make_short_sentence(240))
