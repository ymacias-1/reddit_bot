import praw
import random
import datetime
from  textblob import TextBlob
import time

# import generate_comment() function 
def generate_comment_0():
    names=['VP Biden', 'Joe', 'Mr.Biden', 'JB',]
    name=random.choice(names)
    activities=[' expressed', ' voiced', ' shared', ' spoke about ']
    activity=random.choice(activities)
    climates=[' climate', ' weather',' temperature', ' atmospheric conditions']
    climate=random.choice(climates)
    enjoys=[' cheerful ', ' gleeful ', ' delighted ', ' jolly ']
    enjoy=random.choice(enjoys)
    saves=['save','rescue','help','aid']
    save=random.choice(saves)
    text = name + activity + ' his concern about the' + climate + '. He wants you to be' + enjoy + 'instead of burning in 20 years. Vote for ' + name + ' in order to '+save +' us all.' 
    return text

def generate_comment_1():
    actions=['give', 'provide', 'supply', 'offer']
    action=random.choice(actions)
    importants=['important', 'priority','critical', 'serious']
    important=random.choice(importants)
    chances=['chance', 'opportunity','moment', 'shot']
    chance=random.choice(chances)
    increases=['increase', 'grow', 'better', 'amplify']
    increase=random.choice(increases)
    sures=['be sure', 'take care', 'focus on', 'be secure']
    sure=random.choice(sures)
    text = 'Joe will ' +action + ' carrots to all. He believes your health is ' + important + '. He wants you to have the ' + chance + ' to ' +sure+ ' of your health. With access to carrots, you '+increase+' your quality of life.'
    return text

def generate_comment_2():
    deserves=['merit','earn', 'warrant', 'deserve']
    deserve=random.choice(deserves)
    promises=['promises','assures','guarantees','vows']
    promise=random.choice(promises)
    lots=['numerous','countless','innumerable', 'plenty']
    lot=random.choice(lots)
    alsos=['Also', 'In addition','Further more', 'To add']
    also=random.choice(alsos)
    awesomes=['awesome','amazing','extraordinary','incredible']
    awesome=random.choice(awesomes)
    text = 'Joe Biden believes you ' + deserve + ' the right to oranges. He ' + promise+ ' to plant '+ lot + ' orange trees. '+also+ ', you get vitamin C. Vote Biden for '+awesome+' trees!'
    return text

def generate_comment_3():
    donalds=['Donald Trump','Trump','DT','Mr.Trump']
    donald=random.choice(donalds)
    prohibits=['prohibit', 'stop', 'limit','prevent']
    prohibit=random.choice(prohibits)
    activities=['jumping', 'running','walking','jogging']
    activity=random.choice(activities)
    wastes=['waste','not reasonable use','not professional use', 'misuse']
    waste=random.choice(wastes)
    controls=['control', 'handle', 'limit', 'command']
    control=random.choice(controls)
    text = donald +' wants to '+prohibit +' you from ' + activity+ '. He believe it is a ' +waste+ ' of time. He is trying to ' +control + ' you. Do not vote for him!'
    return text

def generate_comment_4():
    rids=['get rid of', 'rid us','take away','make unavailable']
    rid=random.choice(rids)
    communicates=['communicate','talk','chat','converse']
    communicate=random.choice(communicates)
    peoples=['parents','grandparents','friends','people']
    people=random.choice(peoples)
    achieves=['achieve','acquire','get','reach']
    achieve=random.choice(achieves)
    controllings=['controlling','restricting','limiting','taking away']
    controlling=random.choice(controllings)
    text='Donald Trump wants to ' +rid+ ' cell phones. How will you '+ communicate+ ' with '+ people  +'? How will you ' +achieve + ' 1000 followers? No ' +controlling+ ' our phone use! Vote him out.'
    return text 

def generate_comment_5():
    promises=['promised','vowed','pledged','sweared']
    promised=random.choice(promises)
    brokes=['broke','failed','did not keep', 'did not deliver']
    broke=random.choice(brokes)
    trusts=['trust','confide in','believe', 'have confidence in']
    trust=random.choice(trusts)
    founds=['found out','discovered', 'learned', 'heard']
    found=random.choice(founds)
    pays=['pay','supply funds', 'provide money', 'give us money']
    pay=random.choice(pays)
    text = 'Trump '+promised + ' to give us Disney tickets. He ' +broke + ' that promise. How can you ever ' +trust+ ' him again? I just ' +found + " he wasn't going to " +pay + ' for our food there. No churros! Vote him out!'
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    options=['0', '1','2','3','4', '5']
    option=random.choice(options)
    if option == '0': 
        text=generate_comment_0()
    if option == '1': 
        text=generate_comment_1()
    if option == '2':
        text=generate_comment_2()
    if option == '3': 
        text=generate_comment_3()
    if option == '4': 
        text=generate_comment_4()
    if option == '5': 
        text=generate_comment_5()
    return text

# connect to reddit 
reddit = praw.Reddit('bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
submission = reddit.submission(url=reddit_debate_url)

while True: 

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    
    submission.comments.replace_more(limit=None)
    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment)
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not

    not_my_comments = []
    for comment in submission.comments.list(): 
        if str(comment.author) != 'lab-bot':
            not_my_comments.append(comment) 
    print('len(not_my_comments)=',len(not_my_comments))


    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    
    has_not_commented = len(not_my_comments) == len(all_comments)
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
    if has_not_commented:
        submission.reply(generate_comment())

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        comments_without_replies = []
        for comment in not_my_comments:
            response= False  
            for reply in comment.replies: 
                if str(reply.author) == 'lab-bot': 
                    response=True
                #if comment.author != 'lab-bot' and  response== False: 
                #    response=True 
            if response == False: 
                comments_without_replies.append(comment) 
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        random_comment=random.choice(comments_without_replies)
        random_comment.reply(generate_comment())

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    
    result=random.random()
    top_submissions=list(reddit.subreddit('csci040temp').top(time_filter='hour'))
    if result < 0.5: 
        submission=reddit.submission(url=reddit_debate_url)
    else: 
        submission=random.choice(top_submissions)
    print('submission=', submission)

    my_keywords=['Mr.Biden','biden', 'Joe Biden']    
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comment_text=comment.body.lower()
        #isMatch= any(string in comment_text for string in my_keywords)
        #if isMatch in comment_text: 
        #    comment.upvote()
        if random.choice(my_keywords) in comment_text: 
            comment.upvote()

    def post_text(s):
        choice = random.choice(['toplevel','reply'])
        if choice=='toplevel':
            print('toplevel')
            submission = reddit.submission(url='https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/')
            submission.reply(s)
        else:
            print('reply')
            comment = reddit.comment(url='https://old.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/g9xkull/')
            comment.reply(s)


    for i in range(500):
    
        try:
            post_text(generate_comment())
        except praw.exceptions.APIException:
        # this gets run if the try code fails;
        # python will not crash
            print('exception found')

        # python to wait 5 seconds before proceeding
            print('starting to sleep')
            time.sleep(5)
            print('done sleeping')

