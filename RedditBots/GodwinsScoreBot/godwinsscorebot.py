import praw

def main():
	botName = 'GodwinsScoreBot'
	botPass = 'RoboBrain98+'
	reddit = praw.Reddit(client_id = 'nzyGu6SsDkkKhA',
	                 client_secret = 'X_4bpxd1qv1G-40j-IWFXD4xT9k',
	                 username = botName,
	                 password = botPass,
	                 user_agent = botName)

	subreddit = 'all'

	for comment in reddit.subreddit(subreddit).stream.submissions():
		if comment.author.name != botName:
			processComment(comment)

def processComment(comment):
	for phrase in triggerPhrases:
	    if phrase in comment.body.lower():
	    	print(comment.body)
	    	numComments = comment.num_comments
	    	response = f"Congratulations! It only took this thread **{numComments}** comments to bring up something related to Hitler."
	    	comment.reply(response)
	    	break

triggerPhrases = ['adolph', 'hitler', 'nazi', 'reich']

if __name__ == '__main__':
	main()
