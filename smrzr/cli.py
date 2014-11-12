import argparse
from core import summarize_url, summarize_text

def cli():
    parser = argparse.ArgumentParser(
        description='Get summary and key points from text')
    parser.add_argument('-f', '--file')
    parser.add_argument('-t', '--text')
    parser.add_argument('-u', '--url')
    parser.add_argument('-l', '--lines', type=int)
    args = vars(parser.parse_args())
    num_sentences = 4 if not args['lines'] else args['lines']

    if args['file']:
        try:
            with open(args[file],'r') as f:
                text = f.read()
                print summarize_text(text)
        except:
            pass

    elif args['text']:
        print "\n".join(summarize_text(args['text']))

    elif args['url']:
        res = summarize_url(args['url'],num_sentences=num_sentences)
        print "Summary: ", res[0]
        print "\nKey Points\n==========\n*", "\n* ".join(res[1])