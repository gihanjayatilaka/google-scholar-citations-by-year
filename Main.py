from scholarly import scholarly
import argparse
from time import sleep
import random


DELAY_TIME_SEC=1.0

def delay():
	sleep(random.uniform(1.0*DELAY_TIME_SEC, 2.0*DELAY_TIME_SEC))


def pub2String(publication,titleOnly=True):
	if titleOnly:
		return "=={}",format(publication['bib']['title'])
	else:
		ans=[]
		toAdd=['author','title','journal','publisher','pub_year']
		for t in toAdd:
			try:
				ans.append(publication['bib'][t])
			except:
				_=""
		ans=". ".join(ans)
		return ans

if __name__=="__main__":
	
	print("START")
	args=argparse.ArgumentParser()
	args.add_argument("--name",type=str,dest="name",default=None)
	args.add_argument("--year",type=int,dest="year",default=None)
	args.add_argument("--allDetails",type=bool,dest="allDetails",default=False)
	args.add_argument("--delaySec",type=float,dest="delaySec",default=1.0)

	args=args.parse_args()

	DELAY_TIME_SEC=args.delaySec
	
	authors=scholarly.search_author(args.name)
	author=next(authors)

	while True:
		print("------")
		print(author['name'], author['affiliation'])
		print("Is this the correct profile?")
		ans=input("Y or N?\n")
		if ans.strip()=="Y":
			break
		author=next(authors)

	author=scholarly.fill(author)


	print("*********************")
	print("Citations of {} ({}) 's publications for year {}".format(author['name'],author['affiliation'],args.year))


	pubIdx=1
	allPubsCitationIdx=1
	errors=[]

	for pub in author['publications']:
		# print(pub)
		delay()
		scholarly.fill(pub)
		# print(pub)
		try:
			thisPubCitationIdx=1
			print("{}\t {}\t {}.\t{}".format(pubIdx,"-","-",pub2String(pub,titleOnly=False)))
			delay()
			citations=scholarly.citedby(pub)
			for citation in citations:
				if citation['bib']['pub_year']==str(args.year):
					if args.allDetails==False:
						print("{}\t {}\t {}.\t{}".format(pubIdx,thisPubCitationIdx,allPubsCitationIdx,pub2String(citation)))
					else:
						print("{}\t {}\t {}.\t{}".format(pubIdx,thisPubCitationIdx,allPubsCitationIdx,pub2String(citation,titleOnly=False)))
					thisPubCitationIdx+=1
					allPubsCitationIdx+=1
		except:
				print("err")
				errors.append(pub['bib']['title'])

		pubIdx+=1


	if len(errors)>0:
		print("There were errors in {} publications.".format(len(errors)))
		print(errors)






	print("END of Program")



